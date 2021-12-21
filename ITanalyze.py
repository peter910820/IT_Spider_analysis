import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://ithelp.ithome.com.tw/questions",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    })

soup = BeautifulSoup(response.text, "html.parser")
data = soup.select("div.qa-list__info a")
data2 = soup.select("span.qa-condition__count")
data3 = soup.select("h3.qa-list__title a")

db = {"Like":[],"answer":[],"Browse":[],"Data":[],"title":[]}
for f in data3:
    db["title"].append(f.text)
for d in range(0,len(data2),3):
    db["Like"].append(data2[d].text)
for d in range(1,len(data2),3):
    db["answer"].append(data2[d].text)
for d in range(2,len(data2),3):
    db["Browse"].append(data2[d].text)
for i in range(0,len(data),2):
    db["Data"].append(data[i].text)
    
df = pd.DataFrame(db)
print(df)