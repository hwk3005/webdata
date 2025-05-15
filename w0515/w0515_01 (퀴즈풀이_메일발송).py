### 퀴즈 ###
# news.csv
# # 신문사 기사
# 국민일보,이재명 운동화, 프리미엄 붙어 가격 10배 껑충
# 파이낸셜뉴스, 머리에 다닥다닥 빨간 물집 생기더니..20대 男 머리 뭉텅이로 빠...

# 파일첨부 메일로 발송
# 제목: 네이버 랭킹뉴스 보냄.
# 내용: 네이버 12개 랭킹 1위 뉴스
# 보내는주소: onulee@naver.com

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

## 메일 발송 관련 추가
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


#######################  퀴즈  풀이  #######################

## csv파일 생성
f = open('w0515/news.csv','w',encoding='utf-8-sig',newline='')  # 추가 (풀이) / newline='' : 엔터키 2번 안들어감
writer = csv.writer(f)

title = ['언론사','기사제목']
writer.writerow(title)  # csv 리스트 저장


### 1. 네이버 접속
url = "https://news.naver.com/main/ranking/popularDay.naver"
browser.get(url)

##########################


## html 파싱
soup = BeautifulSoup(browser.page_source,"lxml")

## 언론사별 랭킹뉴스 전체
data = soup.find("div",{"class":'rankingnews_box_wrap'})
## 랭킹뉴스 리스트 - 12개
rNews = data.find_all("div",{"class":'rankingnews_box'})

## 12번 반복해서 가져옴.
for r in rNews:
    ## 언론사이름
    newsName = r.find("strong",{"class":"rankingnews_name"}).get_text()
    print(newsName)
    ## 기사제목
    newsContent = r.find("a",{"class":"list_title"}).get_text().strip()
    print(newsContent)
    writer.writerow([newsName,newsContent])

## 파일생성완료
f.close()

# 파일생성동안 잠시 대기
time.sleep(2)



### 메일발송 ###
## 중요부분
recvMail = "hwk3005@naver.com"  # 받는사람 주소
password = "UTS3MV6H12JZ"  ## 네이버 로그인 비밀번호를 입력해도 되지만, 파일이 노출위험 있기 때문


### 파일첨부 부분
## MIME 객체화
msg = MIMEMultipart('alternative')
# 내용부분  / img(이미지주소 다 적어야 함)
text = """<h2>네이버 12개 랭킹 1위 뉴스</h2>
<img src='https://mail.naver.com/read/image/original/?mimeSN=1747271414.137749.152.14080&offset=1759&size=4808542&u=hwk3005&cid=e6d3b782bdd9cc65693e2c75e6f3137@cweb014.nm&contentType=image/jpeg&filename=1747271408835.jpeg&org=1'>
"""
part2 = MIMEText(text,"html")
msg.attach(part2)
msg['From'] = "hwk3005@naver.com"
msg['To'] = recvMail
msg['Subject'] = "네이버 랭킹뉴스 보냄."

## 파일첨부
part = MIMEBase('application',"octet-stream")
## 파일읽어오기
with open('w0515/news.csv',"rb") as f:
    # part담기
    part.set_payload(f.read())

# 파일 첨부할 수 있는 형태로 인코딩
encoders.encode_base64(part)
## header 정보 - 파일이름 변경
part.add_header('Content-Disposition','attachment',filename='news.csv')
msg.attach(part)


## 메일발송 부분
s = smtplib.SMTP("smtp.naver.com",587)
s.starttls()
s.login("hwk3005",password)  # 아이디,패스워드
### 보내는 주소가 네이버메일이 아니면 에러처리
recvMails = ['hwk3005@naver.com']
s.sendmail("hwk3005@naver.com",recvMail,msg.as_string())  # 보내는사람, 받는사람
s.quit()

print("메일발송 완료")



input("프로그램 종료(엔터키 입력)")