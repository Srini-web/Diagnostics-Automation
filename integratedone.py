#Magician
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
dist_btw_slots=21
op=[227, -104, 130]
dp1=[147, 138, 130]
dp2=[104 , -197, 130]
ox = op[0]
oy = op[1]
oz = op[2]
dx = dp1[0]
dy = dp1[1]
dz = dp1[2]
def moved(sour,dest,tn):
	
	r1=sour[0]
	c1=sour[1]
	r2=dest[0]
	c2=dest[1]
	dType.SetPTPCmd(api, 2, (ox+(r1*dist_btw_slots)), (oy+(c1*dist_btw_slots)), 130, rHead, 1)
	dType.SetPTPCmd(api, 2,  (ox+(r1*dist_btw_slots)), (oy+(c1*dist_btw_slots)), 25, rHead, 1)
	dType.SetEndEffectorSuctionCup(api, 1,  1, isQueued=1)
	dType.SetPTPCmd(api, 2,  (ox+(r1*dist_btw_slots)), (oy+(c1*dist_btw_slots)), 130, rHead, 1)
	dType.SetPTPCmd(api, 2,  (ox+(0*dist_btw_slots)), (oy+(11*dist_btw_slots)), 130, rHead, 1)
	dType.SetPTPCmd(api, 2,  (dx+(r2*dist_btw_slots)), (dy+(c2*dist_btw_slots)), 130, rHead, 1)
	dType.SetPTPCmd(api, 2, (dx+(r2*dist_btw_slots)), (dy+(c2*dist_btw_slots)), 25, rHead, 1)
	dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)
	dType.SetPTPCmd(api, 2,  (dx+(r2*dist_btw_slots)), (dy+(c2*dist_btw_slots)), 130, rHead, 1)
	dType.SetPTPCmd(api, 2,  (ox+(0*dist_btw_slots)), (oy+(6*dist_btw_slots)), 130, rHead, 1)

#126 140
#(x+(r1*dist_btw_slots)), (y+(c1*dist_btw_slots))
#80 -197
file1 = open("C:/DobotStudio/myfile.txt","r")
L=file1.readline()
for i in range(4):
     for j in range(12):
		if(L[c]=='1'):
			moved([i,j],[i,j],1)

#moved([0,1],[0,1],1)
#moved([1,0],[1,0])
#moved([1,1],[1,1])
#moved([2,0],[2,0])
#moved([2,1],[2,1])