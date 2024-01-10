import requests
import json
from datetime import datetime, timedelta
#定义时间
from Akjdsdl import dkjds,yu,yy,sw,dfctestsys
#调用请求、赋值格式、定义时间、调用baidu里的ddscm\dfc
from abl import auditor_ids,goods_data,goods_data2
# 新增供货单
# 调用登录接口获取 token
token = dkjds()
# 设置下单接口的 URL
url = "http://testapi.globalston.com/trade/cb-purchaseOrder/add"
# 设置请求头，将 token 添加到 Authorization 字段中
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": f"Bearer {token}"
}

# 设置请求体
data = {
    "is_draft": 0,    #是否草稿 1是 0否
    "auditor_ids": auditor_ids(),    #审核运营人员
    "seller": "跨境采购卖方",      #卖方公司名称
    "contract_area": "1",   #采购地 1中国 2香港  3澳门
    "contract_area_text":"中国",
    "code":"000888",
    "contract_id": 29,     #合同id
    "warehouse_id": 26,     #仓库id
    "currency_id": 1,     #	币种id
    "tax_rate":13,   #税率
    "real_purchase_time": "2023-11-02",  # 实际采购日期
    "real_pay_time":"2023-11-14",  #实际付款日期
    "plan_rate": "7.1797",  # 计划采购价汇率
    "real_rate": "7.1796",  # 实际采购价汇率
    "payment_terms": 1,   #支付条款1预付2账期
    "payment_terms_text": "prepayment",
    "payment_days": 0,
    "days":"0",
    "phone": "15522336644",    #联系人电话
    "linkman": "fafa",     #联系人姓名
    "goods_list": [      #商品集

            goods_data(),

    ]
}
# 发起下单请求
try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    print(response.json())
except requests.exceptions.HTTPError as error:
    print(f"新增跨境采购单请求失败，错误代码：{error.response.status_code}，错误信息：{error.response.json()}")

# 调用查询订单接口，根据订单下单时间查询订单 id
query_url = "http://testapi.globalston.com/trade/cb-purchaseOrder/list"
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
if result["code"] == 200 and "data" in result:
    order_data = result["data"].get("data", [])
    if order_data:
        order_no = order_data[0].get("order_no")
        print(f"查询到订单号为: {order_no}")
    else:
        print("没有查询到订单")
else:
    print("查询订单失败")