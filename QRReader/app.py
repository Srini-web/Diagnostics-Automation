from server import *
from time import sleep

"""
Response format:
{
    status: "SUCCESS/FAILURE",
    message: "",
    data: {}
}
The response is an object so all the members can be accessed using dot operators.
The data member contains a dictionary. For instance, the data member can look like:
{
    "name": "Ishaan",
    "barcodeId": "R92323-22",
    "testList": ["Test1", "Test2", "Test3"]
}

"R9098940-05", "R9099403-81", "R9099002-01", "R9099281-80"
"""


def getManySamples():
    #sampleIds = ["R9009262-141", "R9098940-05", "R9099403-81", "R9099002-01", "R9099281-80", "R9099259-04", "R9099282-20"]
    sampleIds = ["R9098940-05", "R9099403-81", "R9099002-01", "R9099281-80", "R9099259-04", "R9099282-20"] 
    #sampleIds = ["R9098940-05"]
    for sampleId in sampleIds:
        res = getSampleData(sampleId, 1)
        print(res.status, res.message)
        print(res.data)
        #update_res = updateSample(sampleId)
        #print(update_res.status, update_res.data)

        

getManySamples()