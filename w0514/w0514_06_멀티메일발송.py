import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

## 중요부분
recvMail = "hwk3005@naver.com"  # 받는사람 주소
password = "UTS3MV6H12JZ"  ## 네이버 로그인 비밀번호를 입력해도 되지만, 파일이 노출위험 있기 때문


### 파일첨부 부분
## MIME 객체화
msg = MIMEMultipart('alternative')
# 내용부분
text = "이메일 글자 발송"
part2 = MIMEText(text)
msg.attach(part2)
msg['From'] = "hwk3005@naver.com"
msg['To'] = recvMail
msg['Subject'] = "시가총액 250개 주식정보를 보냅니다."

## 파일첨부
part = MIMEBase('application',"octet-stream")
## 파일읽어오기
with open('w0514/stock.csv',"rb") as f:
    # part담기
    part.set_payload(f.read())

# 파일 첨부할 수 있는 형태로 인코딩
encoders.encode_base64(part)
## header 정보
part.add_header('Content-Disposition','attachment',filename='stock.csv')
msg.attach(part)


## 메일발송 부분
s = smtplib.SMTP("smtp.naver.com",587)
s.starttls()
s.login("hwk3005",password)  # 아이디,패스워드
### 보내는 주소가 네이버메일이 아니면 에러처리
recvMails = ['hwk3005@naver.com','sky777369@gmail.com']
for recvMail in  recvMails:
    s.sendmail("hwk3005@naver.com",recvMail,msg.as_string())  # 보내는사람, 받는사람
s.quit()

print("메일발송 완료")