# coding:utf-8
from PIL import Image

im = Image.open('hctf.png')
# print im.format, im.size, im.mode
pix = im.load()
# qr数据位于alpha 第0位
width = im.size[0]
height = im.size[1]
bin_str = ''
for i in xrange(width):
    for j in xrange(height):
        alpha = pix[i, j][3]
        # print '{0:07b}'.format(alpha)[7]
        bin_str += str('{0:07b}'.format(alpha)[7])
# print bin_str
# print len(bin_str) / 1280
pic_width = 1280
pic_height = 1024
pic_img = Image.new("RGB", (pic_width, pic_height))
k = 0
for i in xrange(pic_width):
    for j in xrange(pic_height):
        if bin_str[k] == '1':
            pic_img.putpixel([i, j], (0, 0, 0))
        else:
            pic_img.putpixel([i, j], (255, 255, 255))
        k = k + 1

pic_img.show()
pic_img.save('flag.png')
