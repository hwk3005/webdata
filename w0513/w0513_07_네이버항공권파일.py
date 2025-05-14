import requests
from bs4 import BeautifulSoup

# 파일 불러오기
with open("w0513/fly1.html","r",encoding="utf-8") as f:
    soup = BeautifulSoup(f,"lxml")

## 비행정보 모두 가져오기
datas = soup.find_all("div",{"class":"domestic_Flight__8bR_b"})
print(len(datas)) #287
datas_list = []   # List정렬
for data in datas:
    ## 항공사이름
    airline = data.find("b",{"class":"airline_name__0Tw5w"}).get_text().strip()
    print(airline)
    times = data.find_all("b",{"class":"route_time__xWu7a"})
    ## 출발시간
    startTime = times[0].get_text().strip()
    print(startTime)
    ## 도착시간
    endTime = times[1].get_text().strip()
    print(endTime)
    ## 가격 - 천단위제거
    price = data.find("i",{"class":"domestic_num__ShOub"}).get_text().strip().replace(",","")
    price = int(price)
    print(price)
    print('-'*50)
    datas_list.append( [airline,startTime,endTime,price] )

### 최저가 LIST정렬
dd_list = sorted(datas_list,key = lambda x:x[3]) # 순차정렬
# dd_list = sorted(d_list,key = lambda x:x[3], reverse=True ) # 역순정렬
print(dd_list)    
    
    
    
    