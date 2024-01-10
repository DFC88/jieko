import requests
import json
from datetime import datetime, timedelta
#定义时间
from Akjdsdl import yy,yu
from Axz import order_id
import Bshone


#跨境电商-运营审核2
url = "http://testapi.globalston.com/trade/cb-purchaseOrder/operationCheck"
token = yu()
# 设置请求头，将 token 添加到 Authorization 字段中
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": f"Bearer {token}"
}
# 设置请求体
data = {
    "id": order_id,  # 使用上一步新增跨境单的返回结果中提取的订单ID
    "is_pass": 1,   # 通过
}
# 发起服务商接单请求
try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    response_json = response.json()
    print(response_json)

except requests.exceptions.HTTPError as error:
    print(f"服务商发票审核请求失败，错误代码：{error.response.status_code}，错误信息：{error.response.json()}")
