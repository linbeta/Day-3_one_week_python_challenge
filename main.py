import requests
import os
from datetime import datetime as dt

# 基本資訊：API endpoint, api headers, api keys, 台北市的city id等
API_KEY = os.environ['api_key']
ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
PARAMS = {
    "id": "1668341",
    "appid": API_KEY
}

response = requests.get(ENDPOINT, params=PARAMS)
response.raise_for_status()

raw_data = response.json()

forecast_date = raw_data["list"]
sorted_data = sorted(forecast_date, key=lambda item: item['main']['temp_max'])
# 輸出未來五天最高溫時段將出現在何時、幾度，原始溫度單位為K，先轉為攝氏溫度(至小數點後第二位數)：
max_temp = round((sorted_data[-1]['main']['temp_max'] - 273.15), 2)
# "dt_txt"欄位中的時間格式為UTC time zone，使用"dt"裡的timestamp才是根據時區timezone調整的台北時間
max_temp_time_local = dt.fromtimestamp(sorted_data[-1]['dt'])
print(f"未來5日最高溫將出現在台北時間：{max_temp_time_local}，預測氣溫為{max_temp}°C")
