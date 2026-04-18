import cv2
import numpy as np
import matplotlib.pyplot as plt

tv=cv2.imread("news.jpg",cv2.IMREAD_COLOR_RGB)
chebu=cv2.imread("cheburashka.jpg",cv2.IMREAD_COLOR_RGB)

rows,cols,_=chebu.shape
pts1=np.array([[0,0],[cols,0],[cols,rows],[0,rows]],dtype="f4")
pts2=np.array([17,24],[430,56],[430,267],[41,294],dtype="f4")
m=cv2.getPerspectiveTransform(pts1,pts2)
print(m)
transormed=cv2.warpPerspective(chebu,m,tv.shape[1],tv.shape[0])
gray=cv2.cvtColor(transormed,cv2.COLOR_RGB2GRAY)
ret,mask=cv2.threshold(gray,1,255,cv2.THRESH_BINARY)
bg=cv2.bitwise_and(tv,tv,mask=cv2.bitwise_not(mask))
fg=cv2.bitwise_and(transormed,transormed,mask=mask)
result=cv2.add(bg,fg)
plt.imshow(result)
plt.show()