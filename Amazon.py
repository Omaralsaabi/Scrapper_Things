import requests

url = "https://www.amazon.com/gp/goldbox?ref_=nav_cs_gb"

payload = {}
headers = {
  'Cookie': 'i18n-prefs=USD; session-id=139-3290723-7243519; session-id-time=2082787201l; sp-cdn="L5Z9:JO"'
}

response = requests.request("GET", url, headers=headers, data=payload).text


# Get Item's links from the page

from bs4 import BeautifulSoup

soup=BeautifulSoup(response, features="html.parser")

links = soup.find_all("a", {"class":"a-link-normal DealLink-module__dealLink_3v4tPYOP4qJj9bdiy0xAT"})

print (links)