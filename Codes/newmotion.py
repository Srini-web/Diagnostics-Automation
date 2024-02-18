#Magician
import math
import numpy as np

dType.SetPTPJointParams(api,200,200,200,200,200,200,200,200,0)
dType.SetPTPCoordinateParams(api,200,200,200,200,0)
dType.SetPTPJumpParams(api, 10, 200,0)
dType.SetPTPCommonParams(api, 100, 100,0)
v1=[164.07073974609375 ,-43.66489028930664 ,-14.902947425842285]
v2=[148.17532348632812 ,54.97605514526367 ,20.355876922607422]
v = [1, 2, 3]
a = np.zeros((48, 5))
a[0] = [1, 1, -80.82039642333984, -240.76593017578125, -114.85740661621094]
a[7] = [1, 7, 43.354217529296875, -239.26097106933594, -86.03093719482422]

def givpos(r, c):
    global v
    if r == 1:
        os = 0
    elif r == 2:
        os = 12
    elif r == 3:
        os = 24
    else:
        os = 36

    for i in range(12):
        if a[i + os][1] == (c - 1):
            v[0] = a[i + os][2]
            v[1] = a[i + os][3]
            v[2] = a[i + os][4]
            break

givpos(1, 2)
print(v)
v1=v
givpos(1,8)
v2=v



def move(v1,v2):
	dType.SetPTPCmd(api, 2, 153.8434600830078 ,14.184000015258789 ,130.0 ,5.267641067504883 , 1)
	dType.SetPTPCmd(api, 2, v1[0], v1[1], 130.0, v1[2], 1)
	dType.SetEndEffectorSuctionCup(api, 1,  1, isQueued=1)
	dType.SetPTPCmd(api, 2, v1[0], v1[1], 24.5125, v1[2], 1)
	dType.SetPTPCmd(api, 2, v1[0], v1[1], 130.0, v1[2], 1)
	dType.SetPTPCmd(api, 2, v2[0], v2[1], 130.0, v2[2], 1)
	dType.SetPTPCmd(api, 2, v2[0], v2[1], 26.0125, v2[2], 1)
	dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)
	dType.SetPTPCmd(api, 2,  v2[0], v2[1], 60.0125, v2[2], 1)



move(v1,v2)

