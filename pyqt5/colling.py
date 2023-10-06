import requests
from bs4 import BeautifulSoup as bs

'''req = requests.get("http://192.168.61.137/")
req_txt = req.text
    print(req_txt)'''

while(True): #실시간 통신
    req = requests.get("http://192.168.61.137/")
    req_txt = req.text
    #print(req_txt)
    text = req_txt.split()
    cnt = len(text)
    for i in range(cnt):
        globals()['Var_{}'.format(i)] = text[i]
    #i번째 인덱스 문자 = Var_{i} 변수로 대입
    print(Var_19)
    print(type(Var_19))