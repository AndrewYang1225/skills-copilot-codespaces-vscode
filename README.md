台灣股票資料抓取工具

本專案提供一個 Python 腳本，使用 twstock 套件從台灣證券交易所抓取指定股票的歷史交易資料，將其轉換為 pandas DataFrame 格式，並儲存為 CSV 檔案。

功能





抓取指定股票的每日交易資料（如開盤價、最高價、最低價、收盤價、成交量等）。



支援從指定日期（例如 2016 年 8 月）至今的資料抓取。



將資料儲存為結構化的 CSV 檔案，方便後續分析。



使用 pandas 進行高效資料處理，搭配 twstock 確保資料抓取的可靠性。

前置條件





Python 3.6 或以上版本



所需的 Python 套件：





twstock



pandas

使用 pip 安裝依賴套件：

pip install twstock pandas

使用方法





複製專案：

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name



確保資料目錄存在： 腳本會將 CSV 檔案儲存至 ./data/ 目錄。請手動建立該目錄，或確保腳本有權限自動建立：

mkdir data



執行腳本： 腳本預設抓取股票代碼 '00620'（台灣高股息 ETF）自 2016 年 8 月起的資料。執行方法：

python stock_fetcher.py

這將在 ./data/ 目錄中生成名為 0050.csv 的檔案。



自訂腳本：





修改股票代碼：將 target_stock = '00620' 更改為其他有效的台灣股票代碼（例如 '2330' 代表台積電）。



調整開始日期：修改 stock.fetch_from(2016, /8) 為您想要的年份和月份。

程式碼說明

主腳本（stock_fetcher.py）執行以下步驟：





導入 twstock 和 pandas 套件。



定義目標股票代碼（例如 '0050'）。



使用 twstock.Stock.fetch_from() 抓取歷史股票資料。



將資料轉換為 pandas DataFrame，包含欄位：Date、Capacity、Turnover、Open、High、Low、Close、Change、Transaction。



將 DataFrame 儲存為 CSV 檔案至 ./data/ 目錄。

範例輸出

生成的 CSV 檔案（./data/00620.csv）格式如下：

Date,Capacity,Turnover,Open,High,Low,Close,Change,Transaction
2020-05-01,12345678,987654321,100.5,102.0,99.8,101.2,0.7,1234
...

注意事項





目錄設定：請確保 ./data/ 目錄存在，否則可能出現 FileNotFoundError。



資料來源：twstock 套件依賴外部資料來源（如 Yahoo Finance）。網路問題或資料來源不可用可能導致錯誤。



欄位名稱：腳本中的 Transaction 欄位已修正可能的拼寫錯誤（避免使用 Transcation）。

問題與支援





除錯：若遇到執行錯誤（如目錄問題或資料抓取失敗），請提供具體錯誤訊息以便協助。



進階功能：若需新增功能（如繪製股票價格圖表或計算技術指標），可進一步提供相關程式碼。



資料驗證：可協助檢查 CSV 檔案內容或進行更深入的資料分析。

如有任何問題或需要進一步協助，請開啟 issue 或聯繫維護者！

授權

本專案採用 MIT 授權，歡迎自由使用與修改。
