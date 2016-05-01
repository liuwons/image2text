#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PIL import Image

# Convert pixel values to chars.
def image_to_text(pixels, width, height):
    color = "MNHQ$OC?7>!:-;. "
    string = ""
    for h in xrange(height):
        for w in xrange(width):
            rgb = pixels[w, h]
            string += color[int(sum(rgb) / 3.0 / 256.0 * 16)]
        string += "\n"
    return string

# Load image from file and resize it.
def load_and_resize_image(imgname, width, height):
    img = Image.open(imgname)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    w, h = img.size
    rw = width * 1.0 / w
    rh = height * 1.0 / h
    r = rw if rw < rh else rh
    rw = int(r * w)
    rh = int(r * h)
    img = img.resize((rw, rh), Image.ANTIALIAS)
    return img

# Convert image file to plain ascii text.
def image_file_to_text(img_file_path, dst_width, dst_height):
    img = load_and_resize_image(img_file_path, dst_width, dst_height)
    pixels = img.load()
    width, height = img.size
    string = image_to_text(pixels, width, height)
    return string


if __name__ == '__main__':
    imgname = sys.argv[1] # Image file path
    w = int(sys.argv[2]) # width
    h = int(sys.argv[3]) # height
    print image_file_to_text(imgname, w, h)
