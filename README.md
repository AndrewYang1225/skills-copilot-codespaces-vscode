台灣股票資料抓取工具


核心理念：
本專案旨在為投資者與資料分析愛好者提供一個簡單、自動化的工具，用於抓取台灣證券交易所的股票歷史資料，並將其轉換為易於分析的 CSV 格式。透過 twstock 與 pandas 的結合，幫助使用者快速獲取結構化資料，為投資決策或學術研究提供基礎數據支持。這個 side project 的目標是降低資料收集的門檻，讓任何人都能輕鬆開始股票資料分析。



專案 Demo

目前專案為命令列工具，未來計劃推出視覺化展示頁面（例如 Flask 或 Streamlit 打造的網頁儀表板）。
Demo 連結：(待補充，未來可提供展示網頁或 Jupyter Notebook 的視覺化圖表連結)
範例展示：





透過腳本生成的 CSV 檔案可直接用於繪製價格走勢圖或計算技術指標。



未來將支援線上查看股票資料的互動式圖表（例如 K 線圖）。



主要功能





自動化資料抓取：從台灣證券交易所獲取指定股票的歷史交易資料（開盤價、最高價、最低價、收盤價、成交量等）。



靈活的日期範圍：支援自定義起始日期（例如 2020 年 5 月）至當前日期的資料抓取。



結構化輸出：將資料轉換為 pandas DataFrame，並儲存為標準 CSV 檔案，方便後續分析。



易於擴展：可輕鬆修改股票代碼或新增分析功能（例如計算移動平均線或繪製圖表）。



輕量高效：僅依賴 twstock 和 pandas，適合個人電腦或伺服器運行。



前置條件





Python 版本：3.6 或以上



所需套件：





twstock：用於抓取台灣股票資料



pandas：用於資料處理與儲存

安裝依賴套件：

pip install twstock pandas



使用指南

1. 複製專案

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. 建立資料目錄

腳本會將 CSV 檔案儲存至 ./data/ 目錄，請確保該目錄存在：

mkdir data

3. 執行腳本

腳本預設抓取股票代碼 '0050'（元大台灣50 ETF）自 2020 年 5 月起的歷史資料：

python stock_fetcher.py

執行後，資料將儲存為 ./data/0050.csv。

4. 自訂設置





更改股票代碼：編輯 stock_fetcher.py，修改 target_stock = '0050' 為其他股票代碼（例如 '2330' 代表台積電）。



調整日期範圍：修改 stock.fetch_from(2020, 5) 中的年份和月份。



進階分析：可將 CSV 檔案導入 Jupyter Notebook 或其他工具，進行視覺化或技術分析。

範例程式碼

以下是 stock_fetcher.py 的核心內容：

import twstock
import pandas as pd

# 設定股票代碼
target_stock = '0050'
stock = twstock.Stock(target_stock)

# 抓取 2020/05 至今的資料
target_price = stock.fetch_from(2020, 5)

# 定義資料表欄位
name_attribute = ['Date', 'Capacity', 'Turnover', 'Open', 'High', 'Low', 'Close', 'Change', 'Transaction']

# 轉換為 DataFrame
df = pd.DataFrame(columns=name_attribute, data=target_price)

# 儲存為 CSV
filename = f'./data/{target_stock}.csv'
df.to_csv(filename)



資料目錄：請確認 ./data/ 目錄存在，否則可能出現 FileNotFoundError。



網路連線：twstock 依賴外部資料來源（如 Yahoo Finance），請確保網路暢通。



欄位名稱：已修正 Transcation 為 Transaction，確保與 twstock 資料格式一致。



錯誤處理：若抓取資料失敗，可檢查網路或資料來源狀態，或聯繫維護者。



未來計劃





視覺化儀表板：開發網頁介面（使用 Flask 或 Streamlit），支援即時資料展示與 K 線圖。



進階分析功能：新增技術指標計算（如移動平均線、RSI）與圖表繪製。



批次抓取：支援多檔股票的同時抓取與比較。



雲端部署：將工具部署至雲端，方便遠端存取。



問題與貢獻





問題回報：若遇到執行錯誤或有功能建議，請開啟 GitHub Issue。



貢獻程式碼：歡迎提交 Pull Request，新增功能或優化程式碼。



聯繫方式：請透過 GitHub 聯繫維護者。



授權

本專案採用 MIT 授權，歡迎自由使用、修改與分享。
