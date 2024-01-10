import requests
import json

#订单中自增箱标号-你好
# 定义存储全局变量的文件路径
counter_file = "acounter.txt"
def generate_incremental_string():
    # 读取全局变量的值
    counter = read_counter()
    # 进行自增操作
    counter += 1
    # 将新的全局变量的值写入文件
    write_counter(counter)
    # 使用字符串格式化来生成自增的字符串，例如 'D001', 'D002', ...
    return f'C{counter:03d}'

def read_counter():
    try:
        with open(counter_file, "r") as file:
            counter = int(file.read())
    except FileNotFoundError:
        # 如果文件不存在，则初始化为0
        counter = 0
    return counter
def write_counter(counter):
    with open(counter_file, "w") as file:
        file.write(str(counter))  # 将计数器的值转换为字符串并写入文件

def goods_data1():
    goods_data1 = {
        "goods_code":"202305091437",
        "goods_id":2564,
        "num":10
    }
    return goods_data1

def goods_data2():
    goods_data2 = {
        "goods_code":"202305091440",
        "goods_id":2565,
        "num":10
    }
    return goods_data2

def goods_data4():
    goods_data4 = {
        "goods_code":"202310310903",
        "goods_id":668320,
        "num":10,
    }
    return goods_data4