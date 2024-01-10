import requests
import json
from Akjdsdl import dkjds
from abl import generate_incremental_string,goods_data1,goods_data2,goods_data4
#新增pick订单
# 调用登录接口获取 token
token = dkjds()
# 设置下单接口的 URL
url = "http://testapi.globalston.com/trade/cb-pick-up-order/add"

# 设置请求头，将 token 添加到 Authorization 字段中
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": f"Bearer {token}"
}
# 设置请求体
data = {
  "is_draft": 0, #是否草稿：1=是，0否
  "currency_id": 5,   #币种
  "shop_id": 6,    #店铺id  10发财科技，6店铺1
  "warehouse_id": 26,  # 仓库id 5仓库名称  26深圳仓  25香港仓
  "shop_code": "8889",   #店铺编码
  "pick_up_no": generate_incremental_string(),   #  pickup号
  "operate_fee":"10",
  "box_num": "12",      #箱数
  "order_goods": [
    goods_data4()
  ],
  "pick_up_time": "2023-11-08",  #	pickup日期
  "volume": "10"    #体积/m³
}
# 发起下单请求
try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    print(response.json())
except requests.exceptions.HTTPError as error:
    print(f"新增跨境采购单请求失败，错误代码：{error.response.status_code}，错误信息：{error.response.json()}")

# 调用查询订单接口，根据订单下单时间查询订单 id
query_url = "http://testapi.globalston.com/trade/cb-pick-up-order/list"
data = {
    "limit": 10,
    "page": 1,
}
try:
    response = requests.post(query_url, headers=headers, json=data)  # Use json parameter instead of manually converting to JSON
    response.raise_for_status()
    result = response.json()
    print(result)
except requests.exceptions.HTTPError as error:
    print(f"查询订单请求失败，错误代码：{error.response.status_code}，错误信息：{error.response.json()}")

order_id = None

if result["code"] == 200 and "data" in result:
    order_data = result["data"].get("data", [])
    if order_data:
        order_id = order_data[0].get("id")
        print(f"查询到订单ID为: {order_id}")
    else:
        print("没有查询到订单")
