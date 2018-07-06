
MAX_age = 100
MIN_age = 1
gender_range = ['f','m']
mood_range = ['angry','sad','neutral','happy','surprise']


def is_right_age(input_age, min_age, max_age):

    if input_age<min_age or input_age>max_age:
        new_age = input('wrong input please input right number: ')
        age = is_right_age(int(new_age), min_age, max_age)
    return input_age



def check_label(input_list):

    if input_list[0] not in gender_range or int(input_list[1]) < MIN_age or int(input_list[1]) > MAX_age or input_list[2] not in mood_range :
        new_input = input('Error!   输入正确的3个标签属性(性别 年龄 心情)!!: ')
        input_list = new_input.split(sep=' ')
    #     return False
    # if int(input_list[1])<MIN_age or int(input_list[1])>MAX_age:
    #     print('输入正确的年龄！！')
    #     return False
    # if input_list[2] not in mood_range:
    #     print('输入正确的心情！！')
        input_list = check_label(input_list)
    return input_list