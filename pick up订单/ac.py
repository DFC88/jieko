import requests
import json
#订单中的箱标号
# 定义存储全局变量的文件路径
counter_file = "acounter.txt"
def box_number():
    # 读取全局变量的值
    counter = read_counter()
    # 将新的全局变量的值写入文件
    write_counter(counter)
    # 使用字符串格式化来生成自增的字符串，例如 'D001', 'D002', ...
    return f'F{counter:03d}'

def read_counter():
    try:
        with open(counter_file, "r") as file:    # r 表示读取模式   打开counter文件并读取
            counter = int(file.read())      #存储的是一个整数值
    except FileNotFoundError:
        # 如果文件不存在，则初始化为0
        counter = 0
    return counter
def write_counter(counter):
    with open(counter_file, "w") as file:      #  w 表示写入模式
        file.write(str(counter))  # 将计数器的值转换为字符串并写入文件