import requests
# 쿠팡 접근해서 res.text출력하시오.
# url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
# url = 'https://www.daum.net/'
# url = 'https://www.melon.com/'
url = 'https://www.google.com/'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
# user-agent : python-requests/2.32.3
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료
print(res.text)
with open("w0509/test.html","w",encoding="utf8") as f:
    f.write(res.text)
print("[ 프로그램 종료 ]")


# if res.status_code == 200:
#     print(res.text)
# else:
#     print("프로그램 종료")    