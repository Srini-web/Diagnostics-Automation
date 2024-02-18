import requests
import json
from time import localtime, strftime

# from .failsafe import helloworld

# TODO: Create a seperate config file or ENV file to store the apiKey.
# TODO: Add failsafe to store samples 

API_KEY = '691038ED-6C2C-499A-BE9E-F8EE5807AFD0'


# Create a custom response by specifiying a status code,
# the data to be passed and a custom message of choice.
class Response:
    def __init__(self, status, message, data = {}):
        self.status = status
        self.message = message
        self.data = data



def debugResponse(mode, data):
    if mode:
        print(data.status, ": ", data.message)
        print(data.data)



# Returns the LOCAL date and time in the following format:
# "YEAR-MONTH-DAY HOURS:MINUTES" The formatting can be changed
# below. For reference to the codes, visit: https://strftime.org/
def getDateAndTime():
    # If you wish to convert the time format from
    # LOCAL time to UTC time, replace localtime() with gmtime().
    current_time = strftime("%Y-%m-%d %H:%M", localtime())
    return current_time




# The JSON data recieved from the API contains a lot of data.
# This function just extracts only some of the data required
# and also converts the data from JSON to a dictionary.
def extractDataFromJSON(samples_list, sampleId, returnId):

    # requested_sample holds a single document of the ID that is requested by filtering out
    # the other documents which dont have the same barcode ID as the one that is passed.
    requested_sample = [sample for sample in samples_list if sample["BarcodeId"] == sampleId][0]
    
    # testList = []
    # for test in requested_sample["TestList"]:
    #     testList.append(test["TestId"])

    response_obj = {}

    if returnId == 1:
        response_obj["title"] = requested_sample["Title"]
        response_obj["name"] = requested_sample["Name"]
        response_obj["age"] = requested_sample["Age"]
        response_obj["ageUnits"] = requested_sample["AgeUnit"]
        response_obj["sex"] = requested_sample["Sex"]
    elif returnId == 2:
        response_obj["labId"] = requested_sample["LabId"]
        response_obj["barcodeId"] = requested_sample["BarcodeId"]
        response_obj["batchNo"] = requested_sample["Batch no"]
        response_obj["totalSamples"] = requested_sample["Total Sample in Batch"]
        response_obj["sampleCollectionDateTime"] = requested_sample["Sample Collection date and Time"]
        response_obj["registrationDateTime"] = requested_sample["Registration Date and Time"]
        response_obj["batchCreatedBy"] = requested_sample["Batch Created by"]
        response_obj["batchCreatedDateTime"] = requested_sample["Batch Created date and Time"]
        response_obj["sourceSiteId"] = requested_sample["Source of the Site ID"]
    elif returnId == 3:
        response_obj["barcodeId"] = requested_sample["BarcodeId"]
        response_obj["labId"] = requested_sample["LabId"]
        response_obj["testList"] = requested_sample["TestList"]
    else:
        response_obj = requested_sample


    return response_obj



# 1 - Patient Data
# 2 - Sample Details
# 3 - List of tests
# 4 - All details
# Send a request to the LIS to fetch the details of the sample.
def getSampleData(sampleId, returnId, debug = False):
    # The API requires a body to passed while making the request
    # containing the ID, apiKey and BatchNo (optional). 

    document_body = {
        'SampleId': sampleId,
        'BatchNo': '',
        'apikey': API_KEY
    }
    # The response data acquires a list of many samples of various barcode ID's
    # A simple filtering script is run to get the document belonging to the
    # barcode ID that is passed.
    try:
        response = requests.post("https://reports.anandlab.com/listest/samplesorter.asmx/GetSampleDetails", json=document_body)
    except requests.exceptions.ConnectionError:
        return Response("FAILURE", "Connection Error - Unable to fetch sample data")

    response_json_data = json.loads(json.dumps(response.json()))

    if response_json_data["StatusCode"] == 1:
        requested_sample = extractDataFromJSON(response_json_data["Data"], sampleId, returnId)
        debugResponse(debug, Response("SUCCESS", "Sample fetched successfully", requested_sample))
        return Response("SUCCESS", "Sample fetched successfully", requested_sample)
    else:
        debugResponse(debug, Response("FAILURE", "Unable to find sample of ID: " + sampleId))
        return Response("FAILURE", "Unable to find sample of ID: " + sampleId)





# Sends an update request to the LIS to inform the LIS of the sample
# updated successfully.
def updateSample(sampleId, batch_number = "", debug = False):
    
    document_body = {
        "SampleId": sampleId,
        "BatchNo": batch_number,
        "ReceiveDate": getDateAndTime(),
        "apikey": API_KEY
    }

    try:
        response = requests.post("https://reports.anandlab.com/listest/samplesorter.asmx/UpdateSampleReciveStatus", json=document_body)
    except requests.exceptions.ConnectionError:
        return Response("FAILURE", "Connection Error - Unable to update sample")
    
    response_obj = json.loads(json.dumps(response.json()))
    # The database responds with a JSON object with 2 values,
    # { StatusCode, StatusMessage }. Returns a success response
    # if the status code is 1. Returns a generalized failure response
    # if the status code is anything other than 1.

    if response_obj["StatusCode"] == 1:
        debugResponse(debug, Response("SUCCESS", "Sample updated successfully", response_obj))
        return Response("SUCCESS", "Sample updated successfully", response_obj)

    else:
        debugResponse(debug, Response("FAILURE", "Failed to update sample", response_obj))        
        return Response("FAILURE", "Failed to update sample", response_obj)
