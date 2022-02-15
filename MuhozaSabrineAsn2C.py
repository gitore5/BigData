#Sabrine Muhoza
#Assignment 2A
#October 6, 2021
#Part C

#exchange rate today is 1 dollars for 0.87 euro and 6.45 yuan
print('Welcome to the 3-currency calculator!')
money = float(input('Please enter the From amount: '))
currency = input('Please enter the From currency (USD, EUR, RMB): ')
convert = input('Please enter the To currency (USD, EUR, RMB): ')

usd_to_eur = money/1.16
eur_to_usd = money*1.16
usd_to_rmb = money*6.45
rmb_to_usd = money/6.45
eur_to_rmb = money*7.45
rmb_to_eur = money/7.45

if currency.upper() == "USD" and convert.upper() == "EUR":
    print(f'USD {money} equals EUR {usd_to_eur:.2f}')
elif currency.upper() == "USD" and convert.upper() == "RMB":
    print(f'USD {money} equals RMB {usd_to_rmb:.2f}')
elif currency.upper() == "EUR" and convert.upper() == "USD":
    print(f'EUR {money} equals USD {eur_to_usd:.2f}')
elif currency.upper() == "EUR" and convert.upper() == "RMB":
    print(f'EUR {money} equals RMB {eur_to_rmb:.2f}')
elif currency.upper() == "RMB" and convert.upper() == "USD":
    print(f'RMB {money} equals USD {rmb_to_usd:.2f}')
elif currency.upper() == "RMB" and convert.upper() == "EUR":
    print(f'RMB {money} equals EUR {rmb_to_eur:.2f}')
else:
    print('Please input a valid currency.')




