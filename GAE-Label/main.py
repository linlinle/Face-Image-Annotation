"""主函数"""
import logging
import time
import os
import pandas as pd
import argparse
from attributeDetection import baiduAPIDetection


def main(Data_path, output_path, urllibWay,process_range):
    """

    :param Data_path: 照片的存储路径
    :return: txt文件：照片文件名-年龄-美貌-表情-性别
    """
    logging.basicConfig(level=logging.ERROR,  # 控制台打印的日志级别
                        filename=output_path,
                        filemode='w',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                        # a是追加模式，默认如果不写的话，就是追加模式
                        format=
                        '%(message)s'
                        # 日志格式
                        )

    imagesFileList= os.listdir(Data_path)
    #pdInit = pd.DataFrame(columns=['file_name','age','beauty','expression','gender'])
    if '.DS_Store' in imagesFileList:
        imagesFileList.remove('.DS_Store')

    for jpg in imagesFileList[process_range[0]:process_range[1]]:
        singleImage = os.path.join(Data_path, jpg)
        resultDict = baiduAPIDetection(singleImage, urllibWay)

        # 请求qps过于频繁
        while resultDict['error_code'] == 18:
            time.sleep(1)
            resultDict = baiduAPIDetection(singleImage, urllibWay)
        # 不是人脸照片
        if resultDict['error_code']  == 222202:
            os.remove(singleImage)
            continue

        # 正常通过，注意这里只能使用if，不可使用elif
        if resultDict['error_code'] == 0:
            faceAttributeList = resultDict['result']['face_list'][0]
            logList = [jpg,
                       str(faceAttributeList['age']),
                       faceAttributeList['gender']['type'],
                       faceAttributeList['expression']['type']]
            logstr = ' '.join(logList)
            logging.error(logstr)
            print(logstr)
            # signleRow = pd.Series([jpg,
            #                        faceAttributeList['age'],
            #                        faceAttributeList['beauty'],
            #                        faceAttributeList['expression']['type'],
            #                        faceAttributeList['gender']['type']],
            #                       index=['file_name', 'age', 'beauty', 'expression', 'gender'])
            #pdInit = pdInit.append(signleRow, ignore_index=True)

       # print(jpg, resultDict['error_code'])

    #pdInit.to_csv(output_path,sep=' ', header=True, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputDir",type=str,default="/Users/androiduser/Desktop/Data/Manual-Label/test1",
                        help="输入照片文件夹")
    parser.add_argument("--outputDir",type=str,default="/Users/androiduser/Desktop/Data/Manual-Label/result.log",
                        help="输出文本地址")
    parser.add_argument("--urllibWay",type=int,default=3,help="从(0 = urllib ，3 = urllib3)中选择一个请求模块")
    parser.add_argument("--process_range",type=str,required=True,help="分批处理照片的范围")
    arg = parser.parse_args()
    rangeList = [int(x) for x in arg.process_range.split('-')]
    main(arg.inputDir, arg.outputDir, arg.urllibWay,rangeList)