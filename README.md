股票資料下載器

一個簡單的 Python 腳本，使用 yfinance 下載股票歷史資料並以 pandas DataFrame 格式呈現。

功能





輸入股票代碼（例如 2330.TW，台積電）。



從 Yahoo Finance 下載股票歷史資料（預設：最近 6 個月）。



以乾淨的 pandas.DataFrame 格式顯示資料，包含欄位：Date（日期）、Open（開盤價）、High（最高價）、Low（最低價）、Close（收盤價）、Volume（成交量）。



基本的錯誤處理，應對無效股票代碼或網路問題。

前置條件





Python 3.6 或更高版本



所需庫：yfinance、pandas

安裝





克隆此儲存庫：

git clone https://github.com/your-username/stock-data-downloader.git
cd stock-data-downloader



安裝所需庫：

pip install yfinance pandas

使用方法





運行腳本：

python stock_data_dataframe.py



按提示輸入股票代碼（例如 2330.TW）。



在終端機中查看以 DataFrame 格式顯示的股票歷史資料。

範例輸出

請輸入股票代碼（例如 2330.TW）：2330.TW

2330.TW 的歷史資料：
          Date        Open        High         Low       Close    Volume
0   2024-04-18  830.000000  836.000000  820.000000  820.000000  45678912
1   2024-04-19  815.000000  818.000000  805.000000  810.000000  38765432
...

注意事項





確保網路連線穩定以存取 Yahoo Finance API。



必須使用有效的股票代碼（例如 .TW 表示台灣市場）。



Yahoo Finance 的免費 API 可能有請求頻率限制。

貢獻

歡迎提交問題或拉取請求來改進此腳本！

授權

本專案採用 MIT 授權。
