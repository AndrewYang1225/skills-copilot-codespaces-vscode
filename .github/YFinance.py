import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# 定義函數來下載並返回股票資料的 DataFrame
def get_stock_data(stock_code):
    try:
        # 計算日期範圍：預設為最近 6 個月
        end_date = datetime.today()
        start_date = end_date - timedelta(days=180)

        # 使用 yfinance 下載股票歷史資料
        stock = yf.Ticker(stock_code)
        df = stock.history(start=start_date, end=end_date)

        # 檢查資料是否為空
        if df.empty:
            print(f"錯誤：無法取得 {stock_code} 的資料，請檢查股票代碼是否正確。")
            return None

        # 確保資料欄位正確
        required_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
        if not all(col in df.columns for col in required_columns):
            print(f"錯誤：資料格式不正確，缺少必要欄位。")
            return None

        # 格式化 DataFrame：重置索引以將日期作為欄位
        df = df.reset_index()
        df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')  # 將日期格式化為字符串
        df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]  # 選擇所需欄位

        return df

    except Exception as e:
        print(f"發生錯誤：{str(e)}")
        return None

# 主程式
if __name__ == "__main__":
    # 獲取使用者輸入的股票代碼
    stock_code = input("請輸入股票代碼（例如 2330.TW）：").strip()

    # 調用函數獲取資料
    stock_data = get_stock_data(stock_code)

    # 顯示結果
    if stock_data is not None:
        print(f"\n{stock_code} 的歷史資料：")
        print(stock_data)
    else:
        print("無法顯示資料，請檢查錯誤訊息。")
