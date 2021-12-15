from sys import argv

with open('bakery.csv', 'a', encoding='utf-8') as sum_sale_append:
    with open('bakery.csv', 'r', encoding='utf-8') as sum_sale_read:
        if str(argv[1:]).strip("[']").replace(".", "").isdigit():
            if '.' in str(argv[1:]).strip("[']") and len(str(argv[1:]).strip("[']")) == 6:
                print(str(argv[1:]).strip("[']"), file=sum_sale_append)
            else:
                print('Вводим сумму продаж булочной:')
        else:
            print(sum_sale_read.read())
