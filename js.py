import json

data = '''
{
    "market": {
        "fruits": [
            {
                "name": "Apple",
                "variety": "Red Delicious",
                "price_per_kg": 4.99,
                "quantity": 100
            },
            {
                "name": "Banana",
                "variety": "Cavendish",
                "price_per_kg": 2.99,
                "quantity": 150
            },
            {
                "name": "Orange",
                "variety": "Valencia",
                "price_per_kg": 3.49,
                "quantity": 80
            }
        ],
        "vegetables": [
            {
                "name": "Tomato",
                "variety": "Beefsteak",
                "price_per_kg": 3.99,
                "quantity": 120
            },
            {
                "name": "Cucumber",
                "variety": "English",
                "price_per_kg": 2.49,
                "quantity": 90
            },
            {
                "name": "Carrot",
                "variety": "Nantes",
                "price_per_kg": 1.99,
                "quantity": 110
            }
        ]
    }
}
'''

# 解析JSON数据
market_data = json.loads(data)

# 获取所有水果的名称
fruit_names = [fruit['name'] for fruit in market_data['market']['fruits']]
print("所有水果的名称：", fruit_names)

# 获取每公斤价格大于3的蔬菜
expensive_vegetables = [veg for veg in market_data['market']['vegetables'] if veg['price_per_kg'] > 3]
print("每公斤价格大于3的蔬菜：", expensive_vegetables)

# 获取所有农产品的总数量
total_quantity = sum(item['quantity'] for item in market_data['market']['fruits'] + market_data['market']['vegetables'])
print("所有农产品的总数量：", total_quantity)