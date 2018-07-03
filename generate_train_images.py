#!/usr/bin/env python
import cv2
import numpy as np
from glob import glob


image_origin_dir = './images/origin'
image_resized_dir = './images/resized'
image_mono_dir = './images/mono'
image_train_dir = './images/pix2pix_format'


def _resize(filename) -> None:
    origin = cv2.imread('%s/%s' % (image_origin_dir, filename,))
    resized = cv2.resize(origin, None, fx=0.2, fy=0.2)
    cv2.imwrite('%s/%s' % (image_resized_dir, filename,), resized)


def _merge_image(filename) -> None:
    """
    A is Grayscale
    B is Colorful
    +---+   +---+    +------+
    | A | + | B | -> | A  B |
    +---+   +---+    +------+
    """
    origin = cv2.imread('%s/%s' % (image_resized_dir, filename,))
    mono = cv2.imread('%s/%s' % (image_mono_dir, filename,))
    new_canvas = cv2.hconcat([mono, origin])
    cv2.imwrite('%s/%s' % (image_train_dir, filename,), new_canvas)


def main():
    files = glob('%s/*.jpg' % (image_origin_dir,))
    for image_path in files:
        # origin to resized
        _resize(image_path)
        filename = image_path.split('/')[-1]
        # Create Grayscale Image
        img = cv2.imread('%s/%s' % (image_resized_dir, filename,))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('%s/%s' % (image_mono_dir, filename,), gray)
        # 
        _merge_image(filename)


if __name__ == "__main__":
    main()
