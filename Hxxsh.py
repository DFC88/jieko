import requests
import json
from datetime import datetime, timedelta
#定义时间
from Akjdsdl import dfctestsys
from Axz import order_no
import Gkjfk
# 调用登录接口获取 token
token = dfctestsys()
# 调用查询订单接口，根据订单下单时间查询订单 id
query_url = "http://testapi.globalston.com/admin/order-offline-pay/list"
# 设置请求头，将 token 添加到 Authorization 字段中
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": f"Bearer {token}"
}
#查询请求
data = {
    "limit": 10,
    "page": 1,
    "order_no": order_no,
    "id":None
}
try:
    response = requests.post(query_url, headers=headers, json=data)  # Use json parameter instead of manually converting to JSON
    response.raise_for_status()
    result = response.json()
    print(result)
except requests.exceptions.HTTPError as error:
    print(f"查询订单请求失败，错误代码：{error.response.status_code}，错误信息：{error.response.json()}")

order_id_1 = None

if result["code"] == 200 and "data" in result:
    order_list = result["data"].get("list", [])
    if order_list:
        order_id_1 = order_list[0].get("id")
        print(f"查询到订单ID为: {order_id_1}")
    else:
        print("没有查询到订单")
else:
    print("查询订单失败")

#线下汇款-核验
url = "http://testapi.globalston.com/admin/order-offline-pay/verify"
token = dfctestsys()
# 设置请求头，将 token 添加到 Authorization 字段中
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": f"Bearer {token}"
}

# 设置请求体
data = {
    "id": order_id_1,  # 使用上一步新增供货单的返回结果中提取的订单ID
    "status": 1,   # 通过
}
# 发起服务商接单请求
try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()  # 检查响应状态，如果出现错误状态码，则会抛出HTTPError异常
    response_json = response.json()  # 将响应内容解析为JSON格式
    print(response_json)  # 打印响应内容

except requests.exceptions.HTTPError as error:
    # 如果请求失败，则会捕获HTTPError异常，并打印错误代码和错误信息
    print(f"线下汇款请求失败，错误代码：{error.response.status_code}，错误信息：{error.response.json()}")
