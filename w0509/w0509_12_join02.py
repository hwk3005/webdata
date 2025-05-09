import requests
from bs4 import BeautifulSoup
import csv       # csv파일 저장

with open('w0509/join02_info_input.html','r',encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")
    
### 파일저장
ff = open("w0509/input.csv","w",encoding="utf-8-sig",newline="")
writer = csv.writer(ff)    
data = soup.find_all("fieldset")
print("fieldset 개수 : ",len(data))

fileName = []
for d in data:
    dts = d.find_all("dt")
    for dt in dts:
        print(dt.get_text().strip(), end=" ")  # 공백제거 strip()
        fileName.append(dt.get_text().strip())
writer.writerow(fileName)

ff.close()
print("파일저장 완료")        
