#Magician
import math
import numpy as np

dType.SetPTPJointParams(api,200,200,200,200,200,200,200,200,0)
dType.SetPTPCoordinateParams(api,200,200,200,200,0)
dType.SetPTPJumpParams(api, 10, 200,0)
dType.SetPTPCommonParams(api, 100, 100,0)



def move(v1[],v2[]):
	dType.SetPTPCmd(api, 2, v1[0], v1[1], 130.0, v1[2], 1)
	dType.SetEndEffectorSuctionCup(api, 1,  1, isQueued=1)
  dType.SetPTPCmd(api, 2, v1[0], v1[1], 24.5125, v1[2], 1)
  dType.SetPTPCmd(api, 2, v1[0], v1[1], 130.0, v1[2], 1)
  dType.SetPTPCmd(api, 2, v2[0], v2[1], 130.0, v2[2], 1)
  dType.SetPTPCmd(api, 2, v2[0], v2[1], 26.0125, v2[2], 1)
  dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)
  dType.SetPTPCmd(api, 2,  v2[0], v2[1], 60.0125, v2[2], 1)

v1=[-44.62016296386719 -121.29320526123047 -110.51469421386719]
v2=[51.1119384765625 -116.33891296386719 -66.59998321533203]
move(v1,v2)

