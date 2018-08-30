import json
import logging

logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='new.log',
                    filemode='w',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(message)s'
                    #日志格式
                    )

with open("/Users/androiduser/Desktop/log.txt") as f:
    for line in f.readlines():
        image_name = line.split()[0]
        if len(line.split(".jpg ")) <2:
            continue
        result_dict = line.split(".jpg ")[1]
        dic = eval(result_dict)
        if dic["error_code"] == 0:
            age = dic["result"]["face_list"][0]["age"]
            gender = dic["result"]["face_list"][0]["gender"]['type']
            expression = dic["result"]["face_list"][0]["expression"]['type']
            logging.info(image_name+' '+str(age)+' '+gender+' '+expression)
        if dic["error_code"] == 18 or dic["error_code"] == 222202:
            continue
