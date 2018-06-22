import time
import socket
import urllib
import cv2

def connect_tanks(s):
	s.listen(5)
	
	#Old tank
	tank_1_c = None
	tank_1_addr = None

	#New tank
	tank_2_c = None
	tank_2_addr = None


	while 1:
		temp_c, temp_addr = s.accept()
		data=temp_c.recv(1000)
		data = data.decode()

		if data == '1':
			print('tank 1 connected')
			tank_1_c = temp_c
			tank_1_addr = temp_addr
			print tank_1_addr

		if data == '2':
			print('tank 2 connected')
			tank_2_c = temp_c
			tank_2_addr = temp_addr


		if(tank_1_c):

			print 'Both tanks are connected'	
					
			#return tank_1_c, tank_1_addr, tank_2_c, tank_2_addr
			return tank_1_c, tank_1_addr

def shoot(tank=None, aim_pos=None):

	if tank == 1:
		now = int(time.time())
		urllib.urlretrieve('http://192.168.1.247:8080/stream/snapshot.jpeg?delay_s=0', 'shots/tank1/tank_1_' + str(now) +'.jpg' )

		img=cv2.imread('shots/tank1/tank_1_'+ str(now) + '.jpg')

		cropped_img = img[aim_pos[1] - 80:-480 + aim_pos[1] + 80, aim_pos[0] - 80:- aim_pos[0] + 80]
		cv2.imwrite('shots_cropped/tank1/tank_1_' + str(now) + '.jpg', cropped_img)


	if tank == 2:
		now = int(time.time())
		urllib.urlretrieve('http://192.168.1.236:8080/stream/snapshot.jpeg?delay_s=0', 'shots/tank2/tank_2_' + str(int(time.time)) +'.jpg' )
		
		img=cv2.imread('shots/tank2/tank_2_'+ str(now) + '.jpg')

		cropped_img = img[aim_pos[1] - 80:-480 + aim_pos[1] + 80, aim_pos[0] - 80:- aim_pos[0] + 80]
		cv2.imwrite('shots_cropped/tank2/tank_2_' + str(now) + '.jpg', cropped_img)

