import requests
from bs4 import BeautifulSoup
import csv

with open("w0509/게시판3.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")

# html태그 출력 soup.title
print(soup.title)
print(soup.title.get_text())
# 속성 출력 soup.a['href']
print(soup.a['href'])
# find(),find_all()
# print(soup.find("thead")) 
data = soup.find("thead") 
ths = data.find_all("th")
print("th개수 : ",len(ths)) 
    
# for i in range(len(ths)-1):
#     print(ths[i])    

# 파일저장
fileName = "board.csv"
ff = open("w0509/"+fileName,"w",encoding="utf-8-sig",newline="")
# with open("w0509/"+fileName,"w",encoding="utf-8-sig",newline="") as ff:
    
writer = csv.writer(ff)

txt = "번호,제목,작성자,작성일,조회수\n";

######## 1.
# 상단제목 파일에 저장
topTitle = []
for i,th in enumerate(ths):
    if i<5: 
        print(th.get_text(),end="\t")
        topTitle.append(th.get_text())
writer.writerow(topTitle)  # 리스트타입만 입력가능
print()    

# ###### 2
# data2 = soup.find("tbody")
# trs = data2.find_all("tr")
# # print("tr개수 : ",len(trs))
# for tr in trs:
#     tds = tr.find_all("td")
#     if len(tds)<=1: continue
#     bodyData = [] # 게시글 부분 데이터저장
#     for i,td in enumerate(tds):
#         if i<5: 
#             print(td.get_text(),end="\t")
#             bodyData.append(td.get_text())
#     writer.writerow(bodyData)  # 파일에 게시글1개를 저장
#     print()  
ff.close()    
print("파일 저장완료!!")      
    
