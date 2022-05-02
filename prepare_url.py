import os
import copy
import random
import numpy as np
# import csv

# root = 'https://raw.githubusercontent.com/ooorin/image-AMT/main/Oracle-Data-Masked-Ex0.9/'
# root = 'https://somnushk.s3.ap-southeast-1.amazonaws.com/Oracle-Data-Masked-Ex0.9/'
# root = 'https://somnushk.s3.ap-southeast-1.amazonaws.com/Oracle-Data-GIF-Green-Ex0.9/'
root = 'https://somnushk.s3.ap-southeast-1.amazonaws.com/Oracle-Data-AVI-Ex0.9/'

# sub = 'A-train-ImageNet-mobilenet_v2'
# name = 'iou-0.33-603-n03538406_17786-0.jpg'
# url = root + ('%s/same/%s' % (sub, name))


# path_dir = 'Oracle-Data-Masked-Ex0.9'
path_dir = 'Oracle-Data-AVI-Ex0.9'
num_each_case = 50

url_list = []
sub_list = sorted(os.listdir(path_dir))
for sub in sub_list:
    name_list = sorted(os.listdir('%s/%s/same/' % (path_dir, sub)))
    random.shuffle(name_list)
    for name in name_list[:num_each_case]:
        url = root + ('%s/same/%s' % (sub, name))
        url_list.append(url)

random.shuffle(url_list)
url_list1 = copy.deepcopy(url_list)
random.shuffle(url_list)
url_list2 = copy.deepcopy(url_list)
# random.shuffle(url_list)
# url_list3 = copy.deepcopy(url_list)

print(url_list1[0])
print(url_list2[0])
# print(url_list3[0])

unit = 250

# total_url_list = url_list1 + url_list2 + url_list3
total_url_list = url_list1 + url_list2
for i in range(10):
    url_list = total_url_list[i*unit: (i+1)*unit]
    with open('avi_url_list_%d.csv' % i, 'w') as f:
        f.write('image_url\n')
        for url in url_list:
            f.write('%s\n' % url)