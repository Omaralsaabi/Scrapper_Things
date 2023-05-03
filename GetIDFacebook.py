import requests
from bs4 import BeautifulSoup

username = 'sprf1lyzgh'
password = 'Y0xnnKy6ete47AxmnG'

proxy = f'http://{username}:{password}@gate.smartproxy.com:7000'
print ("----------------------")
print (proxy)
print ("----------------------")

def get_id(url):

    url = url

    payload = {}
    headers = {
    'authority': 'www.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'datr=dE1SZDlHC8pPBaEFsWq8AW1f; wd=839x952',
    'sec-ch-ua': '"Chromium";v="112", "Brave";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }



    response = requests.request("GET", url, headers=headers, data=payload).text

    if '/profile/' in response:
        print ('User ID: ', response.split("/profile/")[1].split('\"')[0])
    else:
        print("Not Found Without Proxy")
        try:
            response = requests.request("GET", url, headers=headers, data=payload, proxies={'http': proxy, 'https': proxy}).text
            print ('User ID: ', response.split("/profile/")[1].split('\"')[0])
        except:
            print ("Not Found")

    return response



url = "https://www.facebook.com/anna.brunello.12"

get_id(url)



















#     soup=BeautifulSoup(response,features="html.parser")

    
#     id = soup.find("a", {"class": "x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x87ps6o x1lku1pv x1a2a7pz x1lliihq x1vrad04 x1n2onr6 xh8yej3"})['href'].split('fb://profile/')[0]
#     print('User ID: ', id)
  
#     return id