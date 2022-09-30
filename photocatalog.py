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
    """处理图片，对图片按时间进行归类分组"""
    src_root_dir = r'D:\Fanchaoqun\20220816\333'
    des_root_dir = r'D:\Temp'

    for roots, dirs, filenames in os.walk(src_root_dir):
        for file_list in filenames:
            # 处理手机图片中IMG_YYYYMMDD_HHMISS.jpg命名结构的文件
            if file_list.startswith('IMG') and file_list.endswith('jpg'):
                des_dir_date = re.search(r'\d{8}', file_list).group()
                des_dir_date_year = des_dir_date[0:4]
                des_dir_date_month = des_dir_date[4:6]
                src_file = os.path.join(roots, file_list)
                des_dir = os.path.join(des_root_dir, des_dir_date_year, des_dir_date_month, des_dir_date)
                if os.path.exists(des_dir):
                    shutil.copy(src_file, des_dir)
                else:
                    os.makedirs(des_dir)
                    shutil.copy(src_file, des_dir)


process_photo()
