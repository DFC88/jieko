import requests
import json
#定义时间
from Akjdsdl import dkjds
from Axz import order_id
import Eswsh


#跨境电商-确认收货信息
url = "http://testapi.globalston.com/trade/cb-purchaseOrder/receive"
token = dkjds()
# 设置请求头，将 token 添加到 Authorization 字段中
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": f"Bearer {token}"
}
# 设置请求体
data = {
    "id": order_id,
    "receive_file": [
        {
            "name": "1683342704135 (1)(1).jpg",
            "url": "http://ruston-test.oss-cn-shenzhen.aliyuncs.com/1683342704135%20(1)(1).jpg",
            "uid": 1684483954279,
            "status": "success"
        }
    ],
    "purchase_order_file": [
        {
            "name": "1683342704135 (1)(1).jpg",
            "url": "http://ruston-test.oss-cn-shenzhen.aliyuncs.com/1683342704135%20(1)(1).jpg",
            "uid": 1684483960111,
            "status": "success"
        }
    ],
    "receive_time": "2023-11-01",
    "real_rate": "7.1796",
    "goods_list": [
        {
            "goods_id": 668320,
            "goods_code": "202310310903",
            "remark": "",
            "receive_num": 10
        },
    ],
    "goods_price_list": [
        {
            "id": 2249,
            "goods_id": 668320,
            "real_price": "10.000"
        },
    ]
}
# 发起服务商接单请求
try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    response_json = response.json()
    print(response_json)

except requests.exceptions.HTTPError as error:
    print(f"跨境电商入库请求失败，错误代码：{error.response.status_code}，错误信息：{error.response.json()}")
