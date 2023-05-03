import requests
from bs4 import BeautifulSoup

username = 'sprf1lyzgh'
password = 'Y0xnnKy6ete47AxmnG'

proxy = f'http://{username}:{password}@gate.smartproxy.com:7000'
print ("----------------------")
print (proxy)
print ("----------------------")


def get_id(usr_url):

  url = "https://lookup-id.com/"

  usr_url = usr_url

  # payload = 'fburl=https%3A%2F%2Fwww.facebook.com%2Fbudran.nasher&check=Lookup'
  payload = f'fburl={usr_url}&check=Lookup'
  headers = {
    'authority': 'lookup-id.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://lookup-id.com',
    'referer': 'https://lookup-id.com/',
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

  response = requests.request("POST", url, headers=headers, data=payload, proxies={'http': proxy, 'https': proxy}).text

  soup=BeautifulSoup(response,features="html.parser")

  try:
    id = soup.find("span", {"id": "code"}).text
    print('User ID: ',id)
  except:
    print('User ID: Not Found')
    id = 'Not Found'

  return id

usr_url = "https://www.facebook.com/people/Natasha-Queen/pfbid02HPviQyGB6YtjTDeg5Rfvs336Me5jaKnwaWCrzhwmCLb6VkY3qa2E83VvahhtGAWTl/"

get_id(usr_url)