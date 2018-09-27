import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("not_frontal.jpg")
r_sz=cv2.resize(img,(int(img.shape[1]/4),int(img.shape[1]/4)))
gray_img=cv2.cvtColor(r_sz,cv2.COLOR_BGR2GRAY)


faces=face_cascade.detectMultiScale(gray_img,
scaleFactor=1.1,minNeighbors=5)

for x,y,w,h in faces:
    r_sz=cv2.rectangle(r_sz,(x,y),(x+w,y+h),(0,255,0),2)

print(type(faces))
print(faces)

cv2.imshow("Gray",r_sz)
cv2.waitKey(0)
cv2.destroyAllWindows()
