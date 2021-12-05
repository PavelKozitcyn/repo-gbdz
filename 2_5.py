price = [57.8, 46.51, 9, 7, 45.52, 56.90, 89.33, 343, 31.09, 21.54]
print(id(price))
for ind in price:
    ind = str(ind)
    cost = ind.ljust(5, '0')
    if '.' in cost:
        print(f'{cost[0:2]} руб. {cost[3:5]} коп.', end=', ')
    else:
        print(f'{cost[0:2]} руб. {cost[2:4]} коп.', end=', ')

price.sort()
print(f'ID{id(price)} "\n" {price}')
price_new = sorted(price, reverse=True)
print(price_new)
print(f'Самые дорогие товары{price_new[0:5]}')
