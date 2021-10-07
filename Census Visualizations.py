import requests
import pandas as pd

url = "https://api.census.gov/data/2018/abscs?get=NAME,GEO_ID,NAICS2017_LABEL,SEX,ETH_GROUP,RACE_GROUP,VET_GROUP,FIRMPDEMP&for=state:*&NAICS2017=00&key=55e66c014b79233a93d62e4de48c6b4cbae8d3fc"
#querystring = {}

response = requests.request("GET", url)

dataJson = response.json()
df = pd.DataFrame(dataJson)
print(df.head(5))