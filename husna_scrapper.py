import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin


# Get Document's links from the page
def get_links(url):
    response = requests.get(url)

    if response.status_code == 200:
        # continue with parsing the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []
        for link in soup.find_all('a'):
            links.append(link.get('href'))
        return links
    else:
        # handle the error
        print('Error code: ', response.status_code)

# Get Document from links 
def get_document(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    document = soup.find_all('p')

    document_data = {
        "url": url,
        "document": []
    }

    for item in document:
        document_data["document"].append(str(item))

    with open('document.json', 'a', encoding='utf-8') as f:
        json.dump(document_data, f, ensure_ascii=False, indent=4)

    return document_data

# Get the links
links = get_links('https://husna.fm/%D9%85%D9%82%D8%A7%D9%84%D8%A7%D8%AA')

# Loop over the links and get the documents
for link in links:
    if link is not None:
        if link.startswith('http'):
            document = get_document(link)
        else:
            absolute_url = urljoin('https://husna.fm/', link)
            document = get_document(absolute_url)
    else:
        print('Link is None')
