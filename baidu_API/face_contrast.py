from getRequest import access_token
import urllib,base64,json
import os
import logging
import argparse



def face_contrast_api(file_path_1, file_path_2):
    url='https://aip.baidubce.com/rest/2.0/face/v3/match?access_token='+access_token
    with open(file_path_1,'rb') as f1:
        img1 = base64.b64encode(f1.read())

    with open(file_path_2,'rb') as f2:
        img2 = base64.b64encode(f2.read())


    params = [{"image":str(img1,'utf-8'),"image_type":'BASE64'},{"image":str(img2,'utf-8'),"image_type":'BASE64'}]
    params = json.dumps(params).encode('utf-8')
    request = urllib.request.Request(url=url, data=params)
    request.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(request)
    result = eval(response.read())
    return result


def main(inputDir,PairTxtDir, outputDir):
    logging.basicConfig(level=logging.ERROR,  # 控制台打印的日志级别
                         filename=outputDir,
                         filemode='w',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                         # a是追加模式，默认如果不写的话，就是追加模式
                         format=
                         '%(message)s'
                         # 日志格式
                         )


    with open(PairTxtDir) as f:
        allPairs = f.readlines()
    for onePair in allPairs[1:]:# 第一行有个10 300的数据
        onePair = onePair.split()
        if len(onePair) == 3:   #同一个用户
            personImg_1 ,personImg_2= onePair[0],onePair[0]
            indexImg_1, indexImg_2 = int(onePair[1]), int(onePair[2])
        else:
            personImg_1, personImg_2 = onePair[0], onePair[2]
            indexImg_1, indexImg_2 = int(onePair[1]), int(onePair[3])

        faceImgPath_1 = os.path.join(inputDir,
                                     "{}/{}_00{}{}.jpg".format(personImg_1,personImg_1,indexImg_1//10,indexImg_1%10))

        faceImgPath_2 = os.path.join(inputDir,
                                     "{}/{}_00{}{}.jpg".format(personImg_2,personImg_2,indexImg_2//10,indexImg_2%10))
        try:
            result_dict = face_contrast_api(faceImgPath_1,faceImgPath_2)
        except :
            continue
        logstr = ' '.join(onePair) +" {}".format(result_dict["result"]["score"])
        logging.error(logstr)
        print(logstr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputDir", type=str, default="/Users/androiduser/Desktop/Data/LFW/lfw",
                        help="输入照片文件夹")
    parser.add_argument("--PairTxtDir",type=str,default="/Users/androiduser/Desktop/Data/LFW/pairs.txt",
                        help="输入照片文件夹")
    parser.add_argument("--outputDir",type=str,default="/Users/androiduser/Desktop/pythonTestFramework/lfw_112x96/lfw/baiduAPIscore.log",
                        help="输出文本地址")
    arg = parser.parse_args()
    main(arg.inputDir,arg.PairTxtDir, arg.outputDir)