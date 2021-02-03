import os
import glob
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter



thumb_width = 256



def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))

for i in range(1, 2375):


    my_file = Path('trainB/old'+str(i)+'.jpg')
    my_file2 = Path('trainB/old'+str(i)+'.jpeg')
    if my_file.is_file():
    # file exists
        im = Image.open('trainB/old'+str(i)+'.jpg')
        im_thumb = crop_max_square(im).resize((thumb_width, thumb_width), Image.LANCZOS)
        im_thumb.save('trainB/old'+str(i)+'.jpg', quality=95)
    elif my_file2.is_file():
        im = Image.open('trainB/old'+str(i)+'.jpeg')
        im_thumb = crop_max_square(im).resize((thumb_width, thumb_width), Image.LANCZOS)
        im_thumb.save('trainB/old'+str(i)+'.jpg', quality=95)
    else:
        im = Image.open('trainB/old'+str(i)+'.png')
        im_thumb = crop_max_square(im).resize((thumb_width, thumb_width), Image.LANCZOS)
        im_thumb.save('trainB/old'+str(i)+'.png', quality=95)
