#Magician
import math


dType.SetPTPJointParams(api,200,200,200,200,200,200,200,200,0)
dType.SetPTPCoordinateParams(api,200,200,200,200,0)
dType.SetPTPJumpParams(api, 10, 200,0)
dType.SetPTPCommonParams(api, 100, 100,0)
moveX=0;moveY=0;moveZ=10;moveFlag=-1
pos = dType.GetPose(api)
x = pos[0]
y = pos[1]
z = pos[2]
rHead = pos[3]

def move(v1[],v2[]):
	dType.SetPTPCmd(api, 2, v1[0], v1[1], 130.0, v1[2], 1)
	dType.SetEndEffectorSuctionCup(api, 1,  1, isQueued=1)
  dType.SetPTPCmd(api, 2, v1[0], v1[1], 24.5125, v1[2], 1)
  dType.SetPTPCmd(api, 2, v1[0], v1[1], 130.0, v1[2], 1)
  dType.SetPTPCmd(api, 2, v2[0], v2[1], 130.0, v2[2], 1)
  dType.SetPTPCmd(api, 2, v2[0], v2[1], 26.0125, v2[2], 1)
  dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)
  dType.SetPTPCmd(api, 2,  v2[0], v2[1], 60.0125, v2[2], 1)

dType.SetPTPCmd(api, 2, 190, -22, 43, rHead, 1)

for c in range(0,3):
	for r in range(0,11):
		
dType.SetPTPCmd(api, 2, 225, -105, 130, rHead, 1)


dType.SetPTPCmd(api, 2, 225+21, -105, 130, rHead, 1)

#orginpos x225 y-105
#homepos x190 y-22 z43