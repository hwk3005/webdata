import smtplib
from email.mime.text import MIMEText


# 중요정보
recvEmail = "hwk3005@naver.com"
password = "UTS3MV6H12JZ"  ## 네이버 로그인 비밀번호를 입력해도 되지만, 파일이 노출위험 있기 때문
text = "날씨정보 오늘날씨:맑음, 내일날씨:흐리고 비"

msg = MIMEText(text)
msg['Subject'] = "웹스크래핑 이메일 보내기"
## 네이버주소메일이 아니면 에러
msg['From'] = "hwk3005@naver.com"  # 보내는주소
msg['To'] = recvEmail  # 받는주소

s = smtplib.SMTP("smtp.naver.com",587)
s.starttls()
s.login("hwk3005",password)  # 아이디,패스워드
### 보내는 주소가 네이버메일이 아니면 에러처리
s.sendmail("hwk3005@naver.com",recvEmail,msg.as_string())  # 보내는사람, 받는사람
s.quit()

print("메일발송 완료")