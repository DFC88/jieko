import requests
import json
from datetime import datetime, timedelta
#定义时间
from Akjdsdl import dkjds
from Axz import order_id
import Fkjsh


#跨境电商-付款信息
url = "http://testapi.globalston.com/trade/cb-purchaseOrder/pay"
token = dkjds()
# 设置请求头，将 token 添加到 Authorization 字段中
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": f"Bearer {token}"
}
# 设置请求体
data = {
    "id": order_id,
    "real_rate": "2.0000",
    "real_price_total": "10",
    "bank_name":"银行名称",
    "bank_card_no":"银行账号1",
    "buyer_company_id":13,
    "out_trade_no":"12",
    "invoice_no":"付款发票号",
    "oa_no":"OA审批号",
    "pay_time":"2023-11-12",
    "real_purchase_time":"2023-11-04",
    "pay_image": [
        {
            "name": "1683339965297.jpg",
            "url": "http://ruston-test.oss-cn-shenzhen.aliyuncs.com/1683339965297.jpg",
            "uid": 1684488932671,
            "status": "success"
        }
    ],
    "goods_price_list": [
        {
            "id": 2254,  # 商品id
            "goods_id": 668320,  # 商品id
            "goods_code": "202310310903",  # 商品sku
            "goods_model": "10-31p",  # 商品型号
            "ean": "",  # EAN
            "goods_name": "绿色",  # 商品中文名称
            "brand": "baodong",  # 品牌
            "is_battery": 0,  # 是否带电 0否
            "units": "PCS",  # 单位
            "plan_price": 10,  # 计划采购价
            "apply_price":"",  # 申报价格
            "USDPrice": "20",  # 申报价格USD
            "real_price": 1,  # 实际采购价
            "USDRealPrice": "2",  # 实际采购价USD
            "num": 10,  # 数量
            "plan_price_total": "88.40",  # 计划采购总价
            "real_price_total": "88.50"  # 实际采购总价
        },
    ]
}
# 发起服务商接单请求
try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()  # 检查响应状态，如果出现错误状态码，则会抛出HTTPError异常
    response_json = response.json()  # 将响应内容解析为JSON格式
    print(response_json)  # 打印响应内容

except requests.exceptions.HTTPError as error:
    # 如果请求失败，则会捕获HTTPError异常，并打印错误代码和错误信息
    print(f"付款信息请求失败，错误代码：{error.response.status_code}，错误信息：{error.response.json()}")
