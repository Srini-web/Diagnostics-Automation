#Magician
import math
import csv

dType.SetPTPJointParams(api,200,200,200,200,200,200,200,200,0)
dType.SetPTPCoordinateParams(api,200,200,200,200,0)
dType.SetPTPJumpParams(api, 10, 200,0)
dType.SetPTPCommonParams(api, 100, 100,0)

pos = dType.GetPose(api)
print(pos[0],pos[1],pos[2],pos[3])

with open('values.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     
     writer.writerow(["R","C","X","Y","Z","R"])
     writer.writerow(['A',pos[0],pos[1],pos[2],pos[3]])
     #writer.writerow([2, "Gary Oak", "Mathematics"])
     #writer.writerow([3, "Brock Lesner", "Physics"])
     
with open('values.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} ,{row[1]} ,{row[2]},{row[3]},{row[4]}')
            line_count += 1
    print(f'Processed {line_count} lines.')