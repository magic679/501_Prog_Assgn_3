__author__ = 'schang'

from pylab import *
from skimage import img_as_float

def main():
    img = imread("someimage.png")
    img = img_as_float(img)
    w, h = img.shape[:2]
    R = img[:,:,0]
    G = img[:,:,1]
    B = img[:,:,2]
    figure()
    gray()
    subplot(1,4,1); imshow(img); title("RGB")
    subplot(1,4,2); imshow(R); title("Red")
    subplot(1,4,3); imshow(G); title("Green")
    subplot(1,4,4); imshow(B); title("Blue")
    show()
    pass

if __name__ == '__main__':
    main()