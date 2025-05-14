# Beautiful 데이터 가져옴.
# selenium 틀 가져옴.

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import random

## 웹스크래핑 - Beautiful
with open("w0514/ya1.html","r",encoding="utf-8") as f:
    soup = BeautifulSoup(f,"lxml")

# 검색된 리스트 전체
data = soup.find("div",{"class":"mb-[calc(76px+env(safe-area-inset-bottom))]"})
# 검색된 호텔정보 100개
a_list = data.find_all("a")
print("검색개수: ",len(a_list))


### 반복 출력
for i,a in enumerate(a_list):
    # 평점 4.1 미만 제외, 평가수 500 미만 제외
    # 2.평점출력 - 평점이 있을때/없을때
    rank = a.find("span",{"class":"typography-body-14-bold"})
    rank = rank.get_text().strip()  # 후기
    # 후기글자가 아닌지 확인
    if rank not in "후기": rank = float(rank)
    else: rank = 0
    # 3.평가수 출력 2,167
    rating = a.find("span",{"class":"typography-body-14-bold"}).next_sibling.next_sibling
    rating = rating.get_text().strip()
    rating = int(rating[1:-1].replace(",",""))  # 앞뒤글자제거 [1:-1] (833)
    if rank < 4.1 or rating < 500:
        continue
    print(i+1,end="\t")
       
    
    # 1.제목 출력
    title = a.find("p",{"class":"mb-4"})
    title = title.get_text().strip() 
    print(title,end="\t")

    # 2.평점출력 - 평점이 있을때/없을때
    print(rank,end="\t")

    # 3.평가수 출력 2,167
    print(rating,end="\t")

    # 4.가격 출력
    price = a.find("span",{"class":"shrink-0"})
    if price != None:
        price = price.get_text().strip().replace(",","")
        price = int(price)
        print(price)
    else:
        print("가격없음")
    print("-"*50)


# print(soup.prettify())

    
