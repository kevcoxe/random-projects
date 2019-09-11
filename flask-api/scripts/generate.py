import os
import math
import time
import uuid
import urllib2

from threading import Thread
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True


FACE_URL = 'https://thispersondoesnotexist.com/image'
USER_AGENT = 'Some bot: https://www.256kilobytes.com/content/show/4903/'


def get_face(file_location, thumbnail=False):
    print('Generating face...')

    if os.path.exists(file_location):
        os.remove(file_location)

    REQUEST_HEADER = 'https://www.256kilobytes.com/content/show/4903/{}'.format(str(uuid.uuid1()))

    req = urllib2.Request(FACE_URL)
    req.add_header('Referer', REQUEST_HEADER)
    req.add_header('User-Agent', USER_AGENT)

    resp = urllib2.urlopen(req)
    content = resp.read()

    print('Saving face to {}'.format(file_location))
    f = open(file_location, "a")
    f.write(content)

    im = Image.open(file_location)
    im.save(file_location, "PNG")

    if thumbnail:
        print('Converting to thumbnail')
        # Scale the image and make a copy of it as a thumbnail
        file, ext = os.path.splitext(file_location)
        im = Image.open(file_location)
        im.thumbnail([256, 256])
        im.save(file_location, "PNG")

    print('Face saved')


if __name__ == '__main__':

    threads = []
    total_number_of_faces = 10

    for i in range(total_number_of_faces):
        name_of_file = str(uuid.uuid1())
        src = 'static/images/{}.jpg'.format(name_of_file)
        t = Thread(target=get_face, kwargs=dict(file_location=src, thumbnail=True))
        threads.append(t)

    for t in threads:
        t.start()
        time.sleep(2)

    for t in threads:
        t.join()

    # get_face('../static/images/my_face.jpg', thumbnail=True)
