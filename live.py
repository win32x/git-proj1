import requests
from pprint import pprint as p

# https://yobit.net/api/3/depth/esp_eth

a = lambda x: sum(float(i[1]) for i in requests.get('https://api.livecoin.net/exchange/order_book?currencyPair={}'.format(x)).json()['asks'])
y = (input('введите необходимую крипту\n')).upper()
x = y+'/USD'
orders = requests.get('https://api.livecoin.net/exchange/order_book?currencyPair={}'.format(x)).json()
p(x)
print(orders['asks'][0][0])
print(orders['bids'][0][0])

prices = {}
for c in ['ETH', 'BTC']:
    x = '{}/USD'.format(c)
    orders = requests.get('https://api.livecoin.net/exchange/order_book?currencyPair={}'.format(x)).json()
    # print(x)
    prices[c + 'a'] = float(orders['asks'][0][0])
    prices[c + 'b'] = float(orders['bids'][0][0])
    # print(orders['asks'][0][0])
    # print(orders['bids'][0][0])


    x = y+'/{}'.format(c)
    orders = requests.get('https://api.livecoin.net/exchange/order_book?currencyPair={}'.format(x)).json()
    print(x)
    print(round(float(orders['asks'][0][0]) * prices[c + 'a'], 5), orders['asks'][0][1])
    print(round(float(orders['bids'][0][0]) * prices[c + 'b'], 5))

for c in ['RUR']:
    x = 'USD/{}'.format(c)
    orders = requests.get('https://api.livecoin.net/exchange/order_book?currencyPair={}'.format(x)).json()
    # print(x)
    prices[c + 'a'] = float(orders['asks'][0][0])
    prices[c + 'b'] = float(orders['bids'][0][0])
    # print(orders['asks'][0][0])
    # print(orders['bids'][0][0])


    x = y+'/{}'.format(c)
    orders = requests.get('https://api.livecoin.net/exchange/order_book?currencyPair={}'.format(x)).json()
    print(x)
    print(round(float(orders['asks'][0][0]) / prices[c + 'a'], 5), orders['asks'][0][1])
    print(round(float(orders['bids'][0][0]) / prices[c + 'b'], 5))