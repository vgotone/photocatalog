# -*- coding: utf-8 -*-
"""
@AUTHOR: fanchaoqun
@E_MAIL: vgotone@gmail.com 
@TIME: 2022/9/29 10:23
"""
import os
import os.path
import re
import shutil


def process_photo():
    """处理图片，对图片按时间进行归河分组"""
    src_dir = 'D:\\Fanchaoqun\\20220816\\333\\'
    des_dir = 'D:\\Temp\\'
    print(os.path.dirname(src_dir))
    print(os.path.dirname(des_dir))

    # def get_file_list():
    file_lists = os.listdir(src_dir)
    for file_list in file_lists:
        if file_list.startswith('IMG') and file_list.endswith('jpg'):
            # print(file_list)
            des_dir_date = re.search('\d{8}', file_list).group()
            des_dir_date_year = des_dir_date[0:3]
            des_dir_date_month = des_dir_date[4:5]
            print(des_dir_date)
            if os.path.exists(os.path.join(des_dir, des_dir_date)):
                shutil.copy(os.path.join(src_dir, file_list), os.path.join(des_dir, des_dir_date))
            else:
                os.mkdir(os.path.join(des_dir, des_dir_date))
                shutil.copy(os.path.join(src_dir, file_list), os.path.join(des_dir, des_dir_date))

            # des_dir_date = file_list[4:12]
            # print(des_dir_date)


process_photo()
