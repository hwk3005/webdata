#### 네이버 항공권
# 김포, 제주 5/31 ~ 6/1 ->
# 출발 비행기표 금액 110,000원 이상 제외
# 김포출발시간 5/31 17:00 이후 제외
from datetime import datetime
standard_time = datetime(2025,5,31,17,00,00)
now_time = datetime(2025,5,31,15,00,00)

print(standard_time)
print(now_time)
print(standard_time>now_time)


# 참고 -----------------  w0513_06_네이버항공권.py  ------------------

import requests  # Python에서 HTTP 요청을 보내고 외부 라이브러리인 requests 모듈을 불러와 응답을 쉽게 처리가능
from bs4 import BeautifulSoup  # HTML/XML 파싱 도구 BeautifulSoup 클래스만 불러오기
from selenium import webdriver  # 웹 브라우저 자동 제어 기능 불러오기
from selenium.webdriver.common.keys import Keys  # 키보드 입력 제어를 위한 Keys 클래스 불러오기
from selenium.webdriver.common.by import By  # 	웹 요소를 어떻게 찾을지 지정하기 위한 클래스 불러오기
# ㄴ 사용예시: find_element(By.ID, "id값") 등
from selenium.webdriver.chrome.service import Service  # ChromeDriver 실행을 위한 서비스 설정 객체 불러오기
from selenium.webdriver.chrome.options import Options  # Chrome 실행 시 추가 설정을 적용하기 위한 클래스
# ㄴ 사용목적: headless 실행, 창 크기 설정, 시크릿 모드 등
from selenium.webdriver.support.ui import WebDriverWait  # 명시적 대기를 위한 클래스 불러오기
# ㄴ 사용목적: 요소가 나타날 때까지 기다려서 오류 방지
from selenium.webdriver.support import expected_conditions as EC  # expected_conditions 모듈을 EC로 불러옴
# ㄴ 사용용도: WebDriverWait()과 함께 조건 검사에 사용

import csv  # csv모듈 불러옴 (csv파일읽기/쓰기 등)
import time  # time모듈 불러옴 (지연, 현재 시간, 시간 측정)
import random  # random모듈 불러옴


# 크롬 옵션 설정 - 셀레니움 접근 제한: 보안접근 해제
options = Options()
options.add_argument("--disable-blink-features-AutomationControlled")  # 자동화 숨김 위한 설정
options.add_argument("start-maximized")  # 브라우저 창 최대화
options.add_argument("user-agent=Mozilla/5.0 ")
