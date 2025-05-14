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
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 브라우저 실행
browser = webdriver.Chrome(options=options)
browser.maximize_window() # 창 최대화

# 1. 호텔/리조트 클릭
# 2. 지역선택 > 제주 > 서귀포시/모슬포 클릭
# 3. 6/7 ~ 6/8 적용하기 버튼 클릭
# 4. 스크롤 내리기
# 5. 호텔, 호텔이름, 평점, 후기개수, 가격

#-------------------------------------

url = "https://nol.yanolja.com/"
browser.get(url)

# 1. 호텔/리조트 클릭
time.sleep(1)
browser.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/button').click()
time.sleep(1)
browser.find_element(By.XPATH,'/html/body/div[9]/div/div/aside/div/div[1]/div[2]/div[1]/button[1]').click()
time.sleep(1)
# 2. 지역선택 > 제주 > 서귀포시/모슬포 클릭
# 지역선택
browser.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/button/span').click()
time.sleep(2)
# 제주선택
browser.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div/div/div[1]/button[3]').click()
time.sleep(1)
# 서귀포시/모슬포 선택
browser.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div/div/div[2]/div[1]/a[2]').click()
time.sleep(1)

# 3. 6/7 ~ 6/8 적용하기 버튼 클릭
browser.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/header/div[2]/div/button[1]').click()
time.sleep(1)
# 6/7일 선택
browser.find_element(By.XPATH,'//*[@id="day-picker-2025-06"]/div[2]/div[1]/div[7]/button').click()
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="day-picker-2025-06"]/div[2]/div[2]/div[1]/button').click()
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="pc-dialog-sheet"]/div/div/div[3]/button').click()
time.sleep(1)

### 로딩시간 대기
# 검색버튼 클릭후 화면이 나타날때까지 대기하고 길게는 10초 대기
# WebDriverWait(browser,10).until(EC.presence_of_all_elements_located(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[1]'))
time.sleep(5)


### 스크롤 내리기
# 현재 사이트 높이를 가져오는 자바스크립트
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 실행
while True:
    # 현재 브라우저에서 0에서 현재 높이까지 스크롤 내리기
    # 자바스크립트 실행
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    # 변동된 현재 문서 높이을 가져오기
    curr_height = browser.execute_script("return document.body.scrollHeight")
    # 스크롤 높이가 변동이 없을시
    if curr_height == prev_height: break 
    prev_height = curr_height # 현재 높이를 다시 입력해서 스크롤 내리기 재실행

print("스크롤 내리기 종료")



input("프로그램 종료(엔터키입력)")