import os
import time
import urllib3
from PIL import Image
from PIL import ImageFile


resize = True
http = urllib3.PoolManager()
ImageFile.LOAD_TRUNCATED_IMAGES = True
target_directory = "./images/"
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

url = "https://thispersondoesnotexist.com/image"
user_agent = "Python script"
http_referer = "https://ya.com"

for x in range(0, 400):
    req = http.request('GET', url)
    content = req.data

    file_name = target_directory + 'image-' + str(x).zfill(5) + '.jpg'
    print("Writing to {}...".format(file_name))
    f = open(file_name, "wb")
    f.write(content)

    if resize:
        file, ext = os.path.splitext(file_name)
        im = Image.open(file_name)
        im.thumbnail([500, 500])
        thumb = file + "_resized.jpg"
        print("Resizing the file to {}...".format(thumb))
        im.save(thumb, "JPEG")

    # Wait five seconds between requests
    time.sleep(5)
    print("...")
