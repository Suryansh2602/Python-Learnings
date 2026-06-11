import requests
from datetime import datetime, timedelta
from datetime import datetime

today = datetime.now()
week_ago = today - timedelta(days=7)


start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")


url = f"https://api.open-meteo.com/v1/forecast?latitude=22.7008&longitude=-75.8774&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
response = requests.get(url)
data = response.json()
print(data)