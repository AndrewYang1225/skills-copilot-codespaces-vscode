需求分析
輸入：使用者輸入股票代碼（例如 2330.TW）。
功能：
使用 yfinance 下載指定股票的歷史資料（預設為最近 6 個月的日線資料）。
繪製 K 棒圖，顯示開盤價、收盤價、最高價、最低價。
輸出：顯示 K 棒圖。
環境：需要安裝 yfinance 和 mplfinance 庫。
錯誤處理：確保輸入的股票代碼有效，並處理可能的網路或資料錯誤。
程式碼與解釋
stock_k_chart.py
python
行內顯示
程式碼逐部分解釋
1. 匯入必要的庫
python

複製
import yfinance as yf
import mplfinance as mpf
from datetime import datetime, timedelta
import pandas as pd
yfinance：用於從 Yahoo Finance 下載股票資料。
mplfinance：專為金融資料視覺化設計的庫，用於繪製 K 棒圖。
datetime, timedelta：用於計算日期範圍（例如最近 6 個月）。
pandas：用於處理股票資料（yfinance 返回的資料是 pandas.DataFrame 格式）。
2. 定義主函數 plot_stock_k_chart
python

複製
def plot_stock_k_chart(stock_code):
這是一個封裝函數，接受股票代碼作為參數，負責下載資料並繪製 K 棒圖。
使用函數封裝使程式碼模組化，方便重複使用或修改。
3. 設定日期範圍
python

複製
end_date = datetime.today()
start_date = end_date - timedelta(days=180)
end_date：當前日期，作為資料的下載終點。
start_date：從當前日期減去 180 天（約 6 個月），作為資料的起點。
修改建議：你可以調整 days=180 來改變時間範圍，例如改為 days=30（1 個月）或 days=365（1 年）。
4. 下載股票資料
python

複製
stock = yf.Ticker(stock_code)
df = stock.history(start=start_date, end=end_date)
yf.Ticker(stock_code)：創建一個股票物件，代表指定的股票（例如 2330.TW）。
stock.history：下載指定時間範圍的歷史資料，返回一個 pandas.DataFrame，包含 Open（開盤價）、High（最高價）、Low（最低價）、Close（收盤價）、Volume（成交量）等欄位。
資料結構：df 的索引是日期，欄位包括價格和成交量。
5. 檢查資料有效性
python

複製
if df.empty:
    print(f"錯誤：無法取得 {stock_code} 的資料，請檢查股票代碼是否正確。")
    return
required_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
if not all(col in df.columns for col in required_columns):
    print(f"錯誤：資料格式不正確，缺少必要欄位。")
    return
檢查空資料：如果 df.empty 為 True，表示沒有下載到資料（可能是股票代碼錯誤或網路問題）。
檢查欄位：確保資料包含繪製 K 棒圖所需的欄位（Open, High, Low, Close, Volume）。
錯誤處理：如果資料無效，程式會打印錯誤訊息並退出函數。
修改建議：你可以添加更具體的錯誤提示，例如檢查網路連線狀態。
6. 格式化日期索引
python

複製
df.index = pd.to_datetime(df.index)
mplfinance 要求：K 棒圖的索引必須是 datetime 格式。
yfinance 的索引：通常已經是 datetime，但這裡顯式轉換以確保相容性。
7. 設定 K 棒圖樣式
python

複製
mpf_style = mpf.make_mpf_style(base_mpf_style='yahoo', rc={'font.size': 12})
mpf.make_mpf_style：自訂 K 棒圖的樣式，基於 Yahoo Finance 的預設風格。
rc={'font.size': 12}：設定圖表的字體大小為 12。
修改建議：你可以嘗試其他風格（如 'classic'、'nightclouds'）或調整字體大小、顏色等。
8. 繪製 K 棒圖
python

複製
mpf.plot(
    df,
    type='candle',  # K 棒圖類型
    title=f'{stock_code} K Chart',
    style=mpf_style,
    volume=True,    # 顯示成交量
    ylabel='Price',
    ylabel_lower='Volume',
    figsize=(12, 8)
)
df：傳入股票資料。
type='candle'：指定繪製 K 棒圖（每個 K 棒顯示開盤、收盤、最高、最低價）。
title：圖表標題，顯示股票代碼。
style：應用自訂的圖表樣式。
volume=True：在圖表下方顯示成交量柱狀圖。
ylabel, ylabel_lower：設定價格和成交量的 Y 軸標籤。
figsize=(12, 8)：設定圖表尺寸（寬 12 英寸，高 8 英寸）。
修改建議：
改變 type 為 'ohlc' 以繪製 OHLC 圖（另一種 K 線表示方式）。
調整 figsize 來改變圖表大小。
添加技術指標（如移動平均線）：使用 mpf.plot 的 addplot 參數（需要額外計算）。
9. 錯誤處理
python

複製
except Exception as e:
    print(f"發生錯誤：{str(e)}")
捕捉異常：處理可能的錯誤（例如網路問題、無效股票代碼）。
打印錯誤：向使用者顯示錯誤訊息，便於除錯。
修改建議：可以記錄錯誤到日誌檔案，或提供更具體的錯誤處理邏輯。
10. 主程式
python

複製
if __name__ == "__main__":
    stock_code = input("請輸入股票代碼（例如 2330.TW）：").strip()
    plot_stock_k_chart(stock_code)
if __name__ == "__main__"：確保程式碼僅在直接運行時執行（而非作為模組導入）。
input：提示使用者輸入股票代碼，.strip() 移除輸入中的多餘空格。
調用函數：將輸入的股票代碼傳遞給 plot_stock_k_chart 函數。
修改建議：可以添加輸入驗證（例如檢查股票代碼格式是否包含 .TW）。
安裝需求
在運行程式之前，需安裝以下 Python 庫：

bash

複製
pip install yfinance mplfinance pandas
yfinance：用於下載股票資料。
mplfinance：用於繪製 K 棒圖。
pandas：通常由 yfinance 和 mplfinance 自動安裝，用於資料處理。
使用方式
儲存程式碼為 stock_k_chart.py。
確保已安裝所需的庫。
運行程式：
bash

複製
python stock_k_chart.py
輸入股票代碼（例如 2330.TW），程式會下載資料並顯示 K 棒圖。
可能的修改建議
自訂時間範圍：
修改 timedelta(days=180) 來改變資料範圍。
讓使用者輸入開始和結束日期：
python

複製
start_date = input("請輸入開始日期（YYYY-MM-DD）：")
end_date = input("請輸入結束日期（YYYY-MM-DD）：")
df = stock.history(start=start_date, end=end_date)
添加技術指標：
計算並顯示移動平均線（MA）：
python

複製
df['MA20'] = df['Close'].rolling(window=20).mean()
ap = mpf.make_addplot(df['MA20'], color='blue')
mpf.plot(df, type='candle', addplot=ap, ...)
儲存圖表：
將 K 棒圖儲存為圖片：
python

複製
mpf.plot(..., savefig='k_chart.png')
支援多個股票：
允許輸入多個股票代碼，繪製比較圖表。
改變圖表風格：
嘗試不同的 mpf_style，如 'binance' 或 'blueskies'。
