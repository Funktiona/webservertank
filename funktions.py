import time
import urllib
import cv2
import thread


class tank_connections():
    def __init__(self):
        self.tanks = []

    def on_new_client(self, client_socket):
        client_socket.listen(5)
        while True:
            c, addr = client_socket.accept()
            thread.start_new_thread(self.connect_tanks, (c, addr))

    def connect_tanks(self, c, addr):
        """
        Waits for tanks to connect and add them to a list.

        :param s: socket
        :return: list of dictionaris with tank id, ip and connection
        """

        # time_out = int(time.time())
        # this should run in a thread, so it's always running and returning the tanks list
        while True:
            data = c.recv(1000)
            data = data.decode()
            print(data)
            self.tanks.append({
                'id': None,
                'adress': addr[0],
                'connection': c,
                'timer': int(time.time())
            })
        c.close() # is this actually needed?

    def fire(self, aim_pos, id):
        """
        Changes the value of key '32'(space) in input dictionary if the tank has "reloaded".
        :param dict: the input dictionary with keys for all the keypresses
        :param aim_pos:
        :param id: Id of the
        :return:
        """

	if int(time.time()) - self.tanks[id]['timer'] > 1:
		self.tanks[id]['timer'] = self.save_snapshot(id, aim_pos)
		return True
	else:
		return False


    def give_id(self):
        for counter, tank in enumerate(self.tanks):
            print(counter)
            tank['id'] = int(counter)
        # return self.tanks

# TODO Fix this function
    def save_snapshot(self, id, aim_pos=None):
        """
        Saves the current time and a snapshot from the tanks url using uv4l.
        Then crops the image.
        :param tank: dictionary with tank data
        :param aim_pos: list with x and y coordinates
        :return: integer timer
        """

        now = int(time.time())
        tank_path = 'shots/tank' + id + '/tank_' + id + '_'
        img_path = 'shots_cropped' + id + '/tank_' + id + '_'

        urllib.urlretrieve('http://' + self.tanks[id]['adress'] + ':8080/stream/snapshot.jpeg?delay_s=0',
                           tank_path + str(now) + '.jpg')
        img = cv2.imread(tank_path + str(now) + '.jpg')
        cropped_img = img[aim_pos[1] - 80:-480 + aim_pos[1] + 80, aim_pos[0] - 80:- aim_pos[0] + 80]
        cv2.imwrite(img_path + str(now) + '.jpg', cropped_img)

        return now
