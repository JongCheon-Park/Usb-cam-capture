import cv2
import os

# you can modify the usb_cam numbering here
cap = cv2.VideoCapture(0)

# set up the frame width*height for example : 640x480, 1080x720, 1440x1080
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if cap.isOpened() :
	print("width : {}, height : {}".format(cap.get(3), cap.get(4)))

file_name = input('Enter the your image name : ')
save_num = 1
if os.path.isdir(file_name)==False:
	os.mkdir(file_name)
	print('Make the \'{}\' folder sucessfully'.format(file_name))
else :
	print('\'{}\' name folder is already existed'.format(file_name))

while True:
	ret, frame = cap.read()
	
	if ret:
		cv2.imshow('video', frame)
		Key = cv2.waitKey(1) & 0xFF
		if Key == ord('s') :
			save_file_name = ("./%s/%s_%d.png" %(file_name, file_name, save_num))
			cv2.imwrite(save_file_name, frame)
			print("./%s/%s_%d.png is saved" %(file_name, file_name, save_num))			
			save_num = save_num + 1
		elif Key == ord('q') :
			print('Exit')
			break
	else :
		print('error')

cap.release()
cv2.destroyAllWindows()
