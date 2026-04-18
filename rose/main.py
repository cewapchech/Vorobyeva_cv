import cv2

mush=cv2.imread("mushroom.jpg",cv2.IMREAD_UNCHANGED)

logo=cv2.imread("cvlogo.png",cv2.IMREAD_UNCHANGED)[:,:,:-1]

logo = cv2.resize(logo,(logo.shape[1]//2,logo.shape[0]//2))

roi=mush[:logo.shape[0],:logo.shape[1]]
logo_gray=cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)

ret,mask=cv2.threshold(logo_gray,1,255,cv2.THRESH_BINARY)

bg=cv2.bitwise_and(roi,roi,mask=cv2.bitwise_not(mask))

fg=cv2.bitwise_and(logo,logo,mask=mask)
cimbined=cv2.add(bg,fg)

cv2.namedWindow("Result",cv2.WINDOW_NORMAL)
cv2.imshow("Result",mush)
cv2.waitKey(0)
cv2.destroyAllWindows()
