#Magician
import math
import numpy as np

pos = dType.GetPose(api)
ans=np.arctan([pos[1]/pos[0]])
print((180*ans/math.pi)-180)
print(ans)