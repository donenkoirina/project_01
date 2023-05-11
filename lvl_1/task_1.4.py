# Задача 1.4.

# Есть словарь кодов товаров titles

titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}

# Товары находятся на складе и сохранены в виде словаря списков словарей,
# которые отражают количество товаров в магазине по каждому коду.

store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}

# Рассчитайте на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара в магазине в формате:
# "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"

# Пример: "Кроссовки тип 3 (Adidas) - 31 шт, стоимость 50747 руб"


titles = { 'Кроссовки тип 3 (Adidas)': '100000110', 'Мячик тип 2 (Adidas)': '100000146', 'Кепка тип 1 (Adidas)': '100000149', 'Ремень тип 2 (Nike)': '100000194', 'Футболка тип 1 (Adidas)': '100000224', 'Шапка тип 5 (Puma)': '100000280',}

store = {
    titles['Кроссовки тип 3 (Adidas)']: [{'quantity': 2, 'price': 100}, {'quantity': 1, 'price': 200}],
    titles['Мячик тип 2 (Adidas)']: [{'quantity': 3, 'price': 50}],
    titles['Кепка тип 1 (Adidas)']: [{'quantity': 1, 'price': 500}, {'quantity': 2, 'price': 300}],
    titles['Ремень тип 2 (Nike)']: [{'quantity': 4, 'price': 150}],
    titles['Футболка тип 1 (Adidas)']: [{'quantity': 2, 'price': 400}],
    titles['Шапка тип 5 (Puma)']: [{'quantity': 1, 'price': 800}]
}

totals = {}
for title_code, items in store.items():
    title = [key for key, value in titles.items() if value == title_code][0]
    quantity = sum(item['quantity'] for item in items)
    cost = sum(item['quantity'] * item['price'] for item in items)
    totals[title] = {'quantity': quantity, 'cost': cost}

for title, total in totals.items():
    print(f"{title} - {total['quantity']} шт, стоимость {total['cost']} руб")
