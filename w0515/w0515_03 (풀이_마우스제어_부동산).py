### 마우스 제어

# requests
# find, find_all
# soup = Beautiful(res.text,"lxml")

# selenium
# find_element(By.XPATH)
# soup = Beautiful(browser.page_source,"lxml")




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
import pyautogui  # 마우스 제어

## 메일 관련 import
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# 크롬 옵션 설정 - 셀레니움 접근 제한 : 보안접근 해제
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 브라우저 실행
browser = webdriver.Chrome(options=options)
browser.maximize_window() # 창 최대화

###############################
### 1. 링크 접속
url = "https://new.land.naver.com/complexes/102737?ms=37.5373434,127.0100999,17&a=APT:PRE:ABYG:JGC&e=RETAIL"
browser.get(url)

time.sleep(1)
pre_height = browser.execute_script("return articleListArea.scrollHeight")
print("처음 화면 높이: ",pre_height)
### 자바스크립트의 스크롤 내리기를 사용해서 진행
# browser.execute_script("window.scroll(0,aticleListArea.scrollHeight)")
pyautogui.moveTo(50,700)
time.sleep(2)
while True:
    pyautogui.scroll(-pre_height)  # 마우스 휠로 스크롤 내리기
    time.sleep(2)
    # 변화된 현재 높이
    curr_height = browser.execute_script("return articleListArea.scrollHeight")
    print("변화된 현재 높이: ",curr_height)
    # 높이의 변동이 없으면
    if curr_height == pre_height:
        break
    pre_height = curr_height

soup = BeautifulSoup(browser.page_source,"lxml")
## items 메인정보
data = soup.find("div",{"id":"articleListArea"})
## items 리스트 가져오기
items = data.find_all("div",{"class":"item"})


### Q. 30억이하 전세만 출력하시오.

for item in items:
    # 타입 - 매매,전세,월세
    price = item.find("div",{"class":"price_line"})
    price_type = price.find("span",{"class":"type"}).get_text().strip()
    ### 전세가 아니면 skip
    if price_type not in "전세": continue
    # 가격 - 109억, 109 -> int타입으로 변경
    ## 가격 17억 9,000, 109억, 55억
    price_line = price.find("span",{"class":"price"}).get_text().strip()
    p_line = price_line.split("억")  # '10억 9,000 -> ['10','9000']
    price_line = int(p_line[0])
    # 30억초과는 제외
    if price_line > 30 : continue
    # 상단타이틀
    title = item.find("div",{"class":"item_title"})
    item_title = title.find("span",{"class":"text"}).get_text().strip()
    print(item_title)
    # 타입 - 매매,전세,월세
    print(price_type)
    # 가격 - 109억, 109 -> int타입으로 변경
    print(price_line)
    # 스펙내용
    area = item.find("div",{"class":"info_area"})
    area_spec = area.find("span",{"class":"spec"}).get_text().strip()
    print(area_spec)
    print("-"*30)
    
input("프로그램 종료(엔터키)")

