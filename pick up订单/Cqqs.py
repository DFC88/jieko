import requests
import json
from Akjdsdl import dkjds
from abl import goods_data1,goods_data4
from Bxzdd import order_id
import Bxzdd

#pick订单-去签收
# 调用登录接口获取 token
token = dkjds()
# 设置下单接口的 URL
url = "http://testapi.globalston.com/trade/cb-pick-up-order/operate-receive"

# 设置请求头，将 token 添加到 Authorization 字段中
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": f"Bearer {token}"
}
# 设置请求体
data = {
    "id":order_id,
    "receive_time": "2023-11-30",
    "receive_file": [
        {
            "name": "1683339965297.jpg",
            "url": "http://ruston-test.oss-cn-shenzhen.aliyuncs.com/1683339965297.jpg",
            "uid": 1684488932671,
            "status": "success"
        }
    ],
    "receive_goods":[
        {
            "goods_code": "202310310903",
            "goods_id": 668320,
            "num": 10,
            "receive_num":10  #签收数量


        },
    ]
}
# 发起下单请求
try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    print(response.json())
except requests.exceptions.HTTPError as error:
    print(f"新增跨境采购单请求失败，错误代码：{error.response.status_code}，错误信息：{error.response.json()}")
