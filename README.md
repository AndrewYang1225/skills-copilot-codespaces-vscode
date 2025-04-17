有任何問題歡迎透過 Gitter.im 詢問。

YFinance 台灣股市股票價格擷取
擷取台灣證券交易所之股價資料 重新製作 toomore/grs 之功能

資料來源:

Yahoo股市 (YFinance)

Documentation
yfinance：用於從 Yahoo Finance 下載股票資料。
mplfinance：專為金融資料視覺化設計的庫，用於繪製 K 棒圖。
datetime, timedelta：用於計算日期範圍（例如最近 6 個月）。
pandas：用於處理股票資料（yfinance 返回的資料是 pandas.DataFrame 格式）。

$ python -m pip install --user twstock
By Source

$ git clone https://github.com/mlouielu/twstock
$ cd twstock
$ pipenv install
By Source & install

$ git clone https://github.com/mlouielu/twstock
$ cd twstock
$ python -m pip install --user flit
$ flit install
CLI Tools
$ twstock -b 2330 6223

By CLI
$ twstock -U
Start to update codes
Done!
By Python
>>> import twstock
>>> twstock.__update_codes()
Quick Start
分析計算

from twstock import Stock

stock = Stock('2330')                             # 擷取台積電股價
ma_p = stock.moving_average(stock.price, 5)       # 計算五日均價
ma_c = stock.moving_average(stock.capacity, 5)    # 計算五日均量
ma_p_cont = stock.continuous(ma_p)                # 計算五日均價持續天數
ma_br = stock.ma_bias_ratio(5, 10)                # 計算五日、十日乖離值
擷取自 2024 年 3 月至今之資料

stock = Stock('2330')
stock.fetch_from(2024, 3)
基本資料之使用

>>> stock = Stock('2330')
>>> stock.price
[203.5, 203.0, 205.0, 205.0, 205.5, 207.0, 207.0, 203.0, 207.0, 209.0, 209.0, 212.0, 210.5, 211.5, 213.0, 212.0, 207.5, 208.0, 207.0, 208.0, 211.5, 213.0, 216.5, 215.5, 218.0, 217.0, 215.0, 211.5, 208.5, 210.0, 208.5]
>>> stock.capacity
[22490217, 17163108, 17419705, 23028298, 18307715, 26088748, 32976727, 67935145, 29623649, 23265323, 1535230, 22545164, 15382025, 34729326, 21654488, 35190159, 63111746, 49983303, 39083899, 19486457, 32856536, 17489571, 28784100, 45384482, 26094649, 39686091, 60140797, 44504785, 52273921, 27049234, 31709978]
>>> stock.data[0]

# 單一 Proxy
>>> from twstock.proxy import SingleProxyProvider
>>> spr = SingleProxyProvider({'http': 'http://localhost:8080'})
>>> twstock.proxy.configure_proxy_provider(spr)

# 多個 Proxy
>>> from twstock.proxy import RoundRobinProxiesProvider
>>> proxies = [{'http': 'http://localhost:5000'}, {'http': 'http://localhost:5001'}]
>>> rrpr = RoundRobinProxiesProvider(proxies)
>>> twstock.proxy.configure_proxy_provider(rrpr)

# 變更 Proxy 表
>>> another_proxies = [{'http': 'http://localhost:8000'}, {'https': 'https://localhost:8001'}]
>>> rrpr.proxies = another_proxies
四大買賣點分析
from twstock import Stock
from twstock import BestFourPoint

stock = Stock('2330')
bfp = BestFourPoint(stock)

bfp.best_four_point_to_buy()    # 判斷是否為四大買點
bfp.best_four_point_to_sell()   # 判斷是否為四大賣點
bfp.best_four_point()           # 綜合判斷
即時股票資訊查詢
import twstock

twstock.realtime.get('2330')    # 擷取當前台積電股票資訊
twstock.realtime.get(['2330', '2337', '2409'])  # 擷取當前三檔資訊
使用範例
YFinance
