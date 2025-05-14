import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import time

# 크롬 옵션 설정
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 브라우저 실행
broswer = webdriver.Chrome(options=options)

# 페이지 접속
url = "https://www.melon.com/chart/index.htm"
broswer.get(url)
time.sleep(3)  # 페이지 로딩 대기

soup = BeautifulSoup(broswer.page_source,"lxml")
 
data = soup.find("tbody")
trs = data.find_all("tr") 

### 파일 저장
ff = open("w0512/melon1.csv","w",encoding="utf-8-sig",newline="")
writer = csv.writer(ff) 
title = ["순위","곡제목","가수","좋아요"]
writer.writerow(title)


### 1-100위 까지 순위 저장
for tr in trs:
    
    tds = tr.find_all("td")
    #### 순위
    rank = tds[1].find("span",{"class":"rank"}).get_text()
    print(rank)    
    #### 곡제목
    song = tds[5].find("div",{"class":"rank01"}).a.get_text()
    print(song) # 곡제목
    #### 가수
    singer = tds[5].find("div",{"class":"rank02"}).a.get_text()
    print(singer) # 가수
    #### 좋아요
    cnt = tds[7].find("span",{"class":"cnt"}).get_text().strip()[3:].strip()
    ### 천단위표시제거, int타입으로 변경
    cnt = int(cnt.replace(",",""))
    print(cnt)                                                # 좋아요
    print(tds[3].img["src"])                                  # 이미지링크
    print("-"*30)
    ## 곡정보 파일 저장
    writer.writerow([rank,song,singer,cnt])
    

    ### 이미지 저장
    imgUrl = tds[3].img["src"]
    img_res = requests.get(imgUrl)
    with open(f"w0512/images/melon_chart{rank}.jpg","wb") as f:
        f.write(img_res.content)
        

### csv파일 저장
ff.close()
print("프로그램 종료")        




 