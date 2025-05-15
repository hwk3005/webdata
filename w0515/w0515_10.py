# https://www.yeogi.com/

# 여기어때<br>
# 오사카<br>
# 9.24<br>
# 9.27 검색<br>

# 금액 220,000원 이하<br>
# 평점 8.0 이상<br>
# 평가수 5000명 이상<br>

# 출력하시오.<br>

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

# 크롬 옵션 설정 - 셀레니움 접근 제한 : 보안접근 해제
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")  # 브라우저 창 최대화
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")  # 사용자 에이전트 변경
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 브라우저 실행
browser = webdriver.Chrome(options=options)
browser.maximize_window() # 창 최대화

### 1. 여기어때 접속
url = "https://www.yeogi.com/"
browser.get(url)

# 1. 여행지 검색 - 오사카
time.sleep(2)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/main/section[1]/div/div/div[2]/form/div[1]/div[1]/div/label/div/div[2]/input')
elem.click()
# 오사카 검색 입력
elem.send_keys("오사카")
time.sleep(1)
# 오사카 선택
browser.find_element(By.XPATH,'//*[@id="__next"]/main/section[1]/div/div/div[2]/form/div[1]/div[2]/ul/li/div[2]/div/span').click()

# 2. 날짜 선택 - 9.24 ~ 9.27
time.sleep(1)
# 오른쪽 이동 (9월로)
browser.find_element(By.XPATH,'//*[@id="__next"]/main/section[1]/div/div/div[2]/form/div[2]/div[2]/div/div[1]/div[1]/button[2]').click()
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="__next"]/main/section[1]/div/div/div[2]/form/div[2]/div[2]/div/div[1]/div[1]/button[2]').click()
time.sleep(1)
# 출발날짜 선택
browser.find_element(By.XPATH,'//*[@id="__next"]/main/section[1]/div/div/div[2]/form/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/ul[2]/li[25]/button').click()
time.sleep(1)
# 도착날짜 선택
browser.find_element(By.XPATH,'//*[@id="__next"]/main/section[1]/div/div/div[2]/form/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/ul[2]/li[28]/button').click()
time.sleep(1)

# 3. 검색버튼 클릭
browser.find_element(By.XPATH,'//*[@id="__next"]/main/section[1]/div/div/div[2]/form/div[4]/button').click()
time.sleep(1)

# 4. 스크롤 내리기
# 현재 사이트 높이를 가져오는 자바스크립트
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 실행
while True:
    # 현재 브라우저에서 0에서 현재 높이까지 스크롤 내리기
    # 자바스크립트 실행
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    # 변동된 현재 문서 높이을 가져오기
    curr_height = browser.execute_script("return document.body.scrollHeight")
    # 스크롤 높이가 변동이 없을시
    if curr_height == prev_height: break 
    prev_height = curr_height # 현재 높이를 다시 입력해서 스크롤 내리기 재실행


### 1페이지

# html 파싱
soup = BeautifulSoup(browser.page_source,"lxml")

## 비행정보 모두 가져오기
data = soup.find("div",{"class":"css-1poun1e"})
a_list = data.find_all("a",{"class":"gc-thumbnail-type-seller-card css-wels0m"})


# 호텔명 평점 평가수 금액 이미지링크

for a in a_list:
    ## 항공사 이름
    title = a.find("h3").get_text()
    ## 평점
    rate = a.find("div",{"class":"css-19f645y"}).find("span",{"class":"css-9ml4lz"}).get_text()
    ## 평가수
    rating = a.find("div",{"class":"css-1ar2n2o"}).find("span",{"class":"css-oj6onp"}).get_text().strip()[:-4]
    ## 금액
    price = a.find("span",{"class":"css-5r5920"}).get_text()
    
    if int(price.replace(",",""))>220000 or int(rating.replace(",",""))<5000 or float(rate)<8.0:
        continue
    
    print(title,rate,rating,price)
    

# ### 최저가 LIST정렬
# dd_list = sorted(datas_list,key = lambda x:x[3]) # 순차정렬
# # dd_list = sorted(d_list,key = lambda x:x[3], reverse=True ) # 역순정렬
# print(dd_list)    



    
## 2페이지 이동
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/section/div[2]/div[2]/div/div/button[2]').click()
time.sleep(1)

# 4. 스크롤 내리기
# 현재 사이트 높이를 가져오는 자바스크립트
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 실행
while True:
    # 현재 브라우저에서 0에서 현재 높이까지 스크롤 내리기
    # 자바스크립트 실행
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    # 변동된 현재 문서 높이을 가져오기
    curr_height = browser.execute_script("return document.body.scrollHeight")
    # 스크롤 높이가 변동이 없을시
    if curr_height == prev_height: break 
    prev_height = curr_height # 현재 높이를 다시 입력해서 스크롤 내리기 재실행
    



### 2페이지

# html 파싱
soup = BeautifulSoup(browser.page_source,"lxml")

## 비행정보 모두 가져오기
data = soup.find("div",{"class":"css-1poun1e"})
a_list = data.find_all("a",{"class":"gc-thumbnail-type-seller-card css-wels0m"})


# 호텔명 평점 평가수 금액 이미지링크

for a in a_list:
    ## 항공사 이름
    title = a.find("h3").get_text()
    ## 평점
    rate = a.find("div",{"class":"css-19f645y"}).find("span",{"class":"css-9ml4lz"}).get_text()
    ## 평가수
    rating = a.find("div",{"class":"css-1ar2n2o"}).find("span",{"class":"css-oj6onp"}).get_text().strip()[:-4]
    ## 금액
    price = a.find("span",{"class":"css-5r5920"}).get_text()
    
    if int(price.replace(",",""))>220000 or int(rating.replace(",",""))<5000 or float(rate)<8.0:
        continue
    
    print(title,rate,rating,price)
    

# ### 최저가 LIST정렬
# dd_list = sorted(datas_list,key = lambda x:x[3]) # 순차정렬
# # dd_list = sorted(d_list,key = lambda x:x[3], reverse=True ) # 역순정렬
# print(dd_list)    

