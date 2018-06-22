import time
import urllib
import cv2


def connect_tanks(s):
    """
    Waits for tanks to connect and add them to a list.

    :param s: socket
    :return: list of dictionaris with tank id, ip and connection
    """

    s.listen(5)
    tanks = []

    while 1:
        temp_c, temp_addr = s.accept()
        data = temp_c.recv(1000)
        data = data.decode()

        tanks.append({
            'id': data,
            'adress': temp_addr,
            'connection': temp_c,
            'timer': int(time.time())
        })

        if len(tanks) == 2:
            return tanks

def shoot(tank=None, aim_pos=None):
    """
    Saves the current tim and a snapshot from the tanks url using uv4l.
    Then crops the image.
    :param tank: dictionary with tank data
    :param aim_pos: list with x and y coordinates
    :return: integer timer
    """

    now = int(time.time())
    tank_path = 'shots/tank' + tank['id'] + '/tank_' + tank['id'] + '_'
    img_path = 'shots_cropped' + tank['id'] + '/tank_' + tank['id'] + '_'

    urllib.urlretrieve('http://' + tank['adress'] + ':8080/stream/snapshot.jpeg?delay_s=0',
                       tank_path + str(now) + '.jpg')
    img = cv2.imread(tank_path + str(now) + '.jpg')
    cropped_img = img[aim_pos[1] - 80:-480 + aim_pos[1] + 80, aim_pos[0] - 80:- aim_pos[0] + 80]
    cv2.imwrite(img_path + str(now) + '.jpg', cropped_img)

    return now