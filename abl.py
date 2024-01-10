import requests
import json

#跨境电商采购单流程

# 定义跨境运营审核人员为变量
def auditor_ids():
    return "847,849"
# 跨境订单id
def get_ddid():
    return 347
#跨境订单商品
def goods_data():
        goods_data = {
            "id": 668320,
            "goods_id": 668320,
            "goods_code": "202310310903",
            "goods_model": "10-31p",
            "ean": "",
            "goods_name": "绿色",
            "brand": "你好吗",
            "is_battery": 0,
            "num": 10,  # 数量
            "plan_price": "10",  # 计划采购价
            "plan_price_total": "100",  # 计划采购总价
            "plan_price_usd": 1.392,  # 计划采购价（USD）
            "price_without_tax": "8.85",  # 计划不含税采购价
            "price_without_tax_usd": "1.23",
            "real_price": "10",
            "real_price_total": "100",
            "real_price_without_tax": "8.85",
            "real_price_without_tax_usd": "1.23",
            "total_real_price_without_tax_usd": "88.50",
            "units": "PCS"

        }
        return goods_data

#跨境订单商品
def goods_data2():
        goods_data2 = {
            "id": 2565,
            "goods_id": 2565,
            "goods_code": "202305091440",
            "goods_model": "op-5",
            "ean": "88899",
            "goods_name": "吸冰拿铁",
            "brand": "baodong",
            "is_battery": 0,
            "num": 10,     #数量
            "plan_price": "10",  #计划采购价
            "plan_price_total": "100",   #计划采购总价
            "plan_price_usd": 1.392,    #计划采购价（USD）
            "price_without_tax": "8.85",   #计划不含税采购价
            "price_without_tax_usd": "1.23",
            "real_price": "10",
            "real_price_total": "100",
            "real_price_without_tax": "8.85",
            "real_price_without_tax_usd": "1.23",
            "total_real_price_without_tax_usd": "88.50",
            "units": "PCS"
        }
        return goods_data2
