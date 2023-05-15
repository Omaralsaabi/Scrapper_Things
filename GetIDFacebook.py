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
    soup=BeautifulSoup(response, features="html.parser")

    if '/profile/' in response:
        User_ID =  response.split("/profile/")[1].split('\"')[0]
        print ('User ID: ', User_ID)
    elif 'entity_id' in response:
        User_ID =  response.split("entity_id")[1].split('"')[2]
        print ('User ID: ', User_ID)
    else:
        print("Not Found Without Proxy")
        try:
            response = requests.request("GET", url, headers=headers, data=payload, proxies={'http': proxy, 'https': proxy}).text
            if '/profile/' in response:
                User_ID =  response.split("/profile/")[1].split('\"')[0]
                print ('User ID: ', User_ID)
            elif 'entity_id' in response:
                User_ID =  response.split("entity_id")[1].split('"')[2]
                print ('User ID: ', User_ID)
        except:
            print ("Not Found")
    


    try: 
        profile_name = soup.find("h1", {"class":"x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz"}).text
        print ("Profile Name: ", profile_name)
    except:
        profile_name = "Not Found"
        print ("Profile Name Not Found")

    with open("profile_info.txt", "a") as f:
        f.write("Profile Name: " + profile_name + "\n")
        f.write("User ID: " + User_ID + "\n")

    return response



url = "https://www.facebook.com/ahmad.boos.1675?comment_id=Y29tbWVudDo1ODY3MTAwMDM1MTM3NThfNDcwMDE3NDMxOTc1NTIz&__cft__[0]=AZV3DTdtygmVHQRBENHGzXya8ixcvp0XpXRpbRsswDRgRcDZsMXuTMHYw8dspFqDhHqHo0ZncR95KQR1NsET8r-DXvrlri9tbdAhX3RFH17b2Vu2N8CiZxHGlmECoFbux5UTihzW6kW11sb-MiuKnsfslVCyR0gQKUCCGuCV4vg008O_hCdtF7uU7BgN-6WZRQffF8SDHX5Gig0ppbl3TRAF&__tn__=R]-R"

get_id(url)



















#     soup=BeautifulSoup(response,features="html.parser")

    
#     id = soup.find("a", {"class": "x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x87ps6o x1lku1pv x1a2a7pz x1lliihq x1vrad04 x1n2onr6 xh8yej3"})['href'].split('fb://profile/')[0]
#     print('User ID: ', id)
  
#     return id