'''
批量下载豆瓣首页的图片
采用伪装浏览器的方式爬取豆瓣网站首页的图片，保存到指定路径文件夹下
'''

# 导入所需的库
import pandas as pd
import urllib.request, time, pickle,json, os

# 定义文件保存路径



def saveFile(folder, name):
    # 如果新的文件夹
    if not os.path.exists(folder):
        os.mkdir(folder)

    save_path = os.path.join(folder,name)

    # 设置每个图片的路径
    return save_path

def main():

    file_path = '/Users/androiduser/Desktop/Data/Manual-Label/images.csv'
    targetPath = "/Users/androiduser/Desktop/Data/Manual-Label/paqu"
    os.chdir(targetPath)
    image_url = pd.read_csv(file_path, names=['folder', 'url'])
    for row  in image_url.itertuples(index=False):
        folder = row[0]
        link = row[1]
        name = link.split('/')[-1]
        if os.path.exists(os.path.join(folder,name)):
            print(name+ "has existed")
            continue
        urllib.request.urlretrieve(link, saveFile(folder,name))
        print(name + " --> "+ folder)
        time.sleep(0.3)


def get_structure(dir_path):
    structure = {}
    folder_list = os.listdir(dir_path)
    if '.DS_Store' in folder_list:
        folder_list.remove('.DS_Store')
    for folder in folder_list:
        structure[folder] = os.listdir(os.path.join(dir_path,folder))


    # with open('structure.json','a') as fj:
    #     json.dump(structure,fj)

    return structure


if __name__ == "__main__":
   # main()
    get_structure('/Users/androiduser/Desktop/Data/Manual-Label/paqu_test')