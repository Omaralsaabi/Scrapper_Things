import json
import requests
from bs4 import BeautifulSoup







def google_get_price(product_name, num_pages=1):
    # Read the rates from the json file
    with open('rates.json') as f:
        RATES = json.load(f)

    # Convert the amount to USD
    def converter(amount, currency):
        print(amount, "     ", currency)
        if currency:
            rate = RATES[currency]
            return amount * rate
        else:return amount
        
    # Setup the scrapper 
    results = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    SEARCH_ENGINE_BASE_URL = 'https://www.google.com/search?q={}&hl=en&start={}'

    # Loop through the pages
    for i in range(num_pages):
        start_index = i * 10
        url = SEARCH_ENGINE_BASE_URL.format(product_name, start_index)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        for result in soup.find_all('div', {'class': 'g'}):
            try:
                url = result.find('a')['href']
                name_element = result.find('h3')
                name_site = result.find('span', {'class': 'VuuXrf'})
                if name_element != None:
                    name = name_element.text
                else:
                    continue
                if name_site != None:
                    name_site = name_site.text
                else:
                    continue
                element = result.find('div', class_='fG8Fp uo4vr')
                if element != None and element.text != '':
                    for span_element in element.find_all('span'):
                        if span_element and not span_element.has_attr('aria-label') and 'In stock' not in span_element.text and 'reviews' not in span_element.text and 'review' not in span_element.text and 'Review' not in span_element.text and 'Rating' not in span_element.text and 'stars' not in span_element.text and 'votes' not in span_element.text and 'Out of stock' not in span_element.text and 'Starting from' not in span_element.text:
                            price_text = span_element.get_text()
                            print('price_text: ', price_text)
                            if price_text != "":
                                if ' to ' in price_text:
                                    # Range of price
                                    price_range = price_text.split(' to ')
                                    chosen = price_range[0] 
                                    if '$' in chosen:
                                        chosen1 = chosen.split('$')
                                        chosen1.append('USD')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '£' in chosen:
                                        chosen1 = chosen.split('£')
                                        chosen1.append('GBP')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '€' in chosen:
                                        chosen1 = chosen.split('€')
                                        chosen1.append('EUR')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₹' in chosen:
                                        chosen1 = chosen.split('₹')
                                        chosen1.append('INR')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '¥' in chosen:
                                        chosen1 = chosen.split('¥')
                                        chosen1.append('JPY')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₩' in chosen:
                                        chosen1 = chosen.split('₩')
                                        chosen1.append('KRW')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'Lek' in chosen:
                                        chosen1 = chosen.split('Lek')
                                        chosen1.append('Lek')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '؋' in chosen:
                                        chosen1 = chosen.split('؋')
                                        chosen1.append('AFN')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'ƒ' in chosen:
                                        chosen1 = chosen.split('ƒ')
                                        chosen1.append('AWG')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₼' in chosen:
                                        chosen1 = chosen.split('₼')
                                        chosen1.append('AZN')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'Br' in chosen:
                                        chosen1 = chosen.split('Br')
                                        chosen1.append('BYN')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'BZ$' in chosen:
                                        chosen1 = chosen.split('BZ$')
                                        chosen1.append('BZD')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '$b' in chosen:
                                        chosen1 = chosen.split('$b')
                                        chosen1.append('BOB')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'KM' in chosen:
                                        chosen1 = chosen.split('KM')
                                        chosen1.append('BAM')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'P' in chosen:
                                        chosen1 = chosen.split('P')
                                        chosen1.append('BWP')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'R$' in chosen:
                                        chosen1 = chosen.split('R$')
                                        chosen1.append('BRL')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'лв' in chosen:
                                        chosen1 = chosen.split('лв')
                                        chosen1.append('BGN')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '៛' in chosen:
                                        chosen1 = chosen.split('៛')
                                        chosen1.append('KHR')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '¥' in chosen:
                                        chosen1 = chosen.split('¥') 
                                        chosen1.append('CNY')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₡' in chosen:
                                        chosen1 = chosen.split('₡')
                                        chosen1.append('CRC')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'kn' in chosen:
                                        chosen1 = chosen.split('kn')
                                        chosen1.append('HRK')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₱' in chosen:
                                        chosen1 = chosen.split('₱')
                                        chosen1.append('PHP')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'Kč' in chosen:
                                        chosen1 = chosen.split('Kč')
                                        chosen1.append('CZK')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'kr' in chosen:
                                        chosen1 = chosen.split('kr')
                                        chosen1.append('DKK')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'RD$' in chosen:
                                        chosen1 = chosen.split('RD$')
                                        chosen1.append('DOP')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '¢' in chosen:
                                        chosen1 = chosen.split('¢')
                                        chosen1.append('GHS')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'Q' in chosen:
                                        chosen1 = chosen.split('Q')
                                        chosen1.append('GTQ')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'L' in chosen:
                                        chosen1 = chosen.split('L')
                                        chosen1.append('HNL')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'Ft' in chosen:
                                        chosen1 = chosen.split('Ft')
                                        chosen1.append('HUF')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'Rp' in chosen:
                                        chosen1 = chosen.split('Rp')
                                        chosen1.append('IDR')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '﷼' in chosen:
                                        chosen1 = chosen.split('﷼')
                                        chosen1.append('IRR')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₪' in chosen:
                                        chosen1 = chosen.split('₪')
                                        chosen1.append('ILS')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'J$' in chosen:
                                        chosen1 = chosen.split('J$')
                                        chosen1.append('JMD')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₭' in chosen:
                                        chosen1 = chosen.split('₭')
                                        chosen1.append('LAK')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'ден' in chosen:
                                        chosen1 = chosen.split('ден')
                                        chosen1.append('MKD')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'RM' in chosen:
                                        chosen1 = chosen.split('RM')
                                        chosen1.append('MYR')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₨' in chosen:
                                        chosen1 = chosen.split('₨')
                                        chosen1.append('MUR')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₮' in chosen:
                                        chosen1 = chosen.split('₮')
                                        chosen1.append('MNT')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'MT' in chosen:
                                        chosen1 = chosen.split('MT')
                                        chosen1.append('MZN')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'C$' in chosen:
                                        chosen1 = chosen.split('C$')
                                        chosen1.append('NIO')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₦' in chosen:
                                        chosen1 = chosen.split('₦')
                                        chosen1.append('NGN')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'kr' in chosen:
                                        chosen1 = chosen.split('kr')
                                        chosen1.append('NOK')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'S/.' in chosen:
                                        chosen1 = chosen.split('S/.')
                                        chosen1.append('PEN')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'zł' in chosen:
                                        chosen1 = chosen.split('zł')
                                        chosen1.append('PLN')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'lei' in chosen:
                                        chosen1 = chosen.split('lei')
                                        chosen1.append('RON')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₽' in chosen:
                                        chosen1 = chosen.split('₽')
                                        chosen1.append('RUB')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'Дин' in chosen:
                                        chosen1 = chosen.split('Дин')
                                        chosen1.append('RSD')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'NT$' in chosen:
                                        chosen1 = chosen.split('NT$')
                                        chosen1.append('TWD')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '฿' in chosen:
                                        chosen1 = chosen.split('฿')
                                        chosen1.append('THB')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'TT$' in chosen:
                                        chosen1 = chosen.split('TT$')
                                        chosen1.append('TTD')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₴' in chosen:
                                        chosen1 = chosen.split('₴')
                                        chosen1.append('UAH')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '$U' in chosen:
                                        chosen1 = chosen.split('$U')
                                        chosen1.append('UYU')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'Bs' in chosen:
                                        chosen1 = chosen.split('Bs')
                                        chosen1.append('VEF')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₫' in chosen:
                                        chosen1 = chosen.split('₫')
                                        chosen1.append('VND')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'FCFA' in chosen:
                                        chosen1 = chosen.split('FCFA')  
                                        chosen1.append('XAF')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'CFA' in chosen:
                                        chosen1 = chosen.split('CFA')
                                        chosen1.append('XOF')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    else:
                                        chosen1 = chosen.split(' ')
                                        chosen1 = chosen1[0].replace('\xa0', ' ')
                                        chosen1 = chosen1.split(' ')
                                        if len(chosen1) == 2:
                                            currency = chosen1[0]
                                            price = chosen1[1]
                                        else:
                                            price = chosen1[0]
                                else:
                                    # Single price
                                    if '$' in price_text:
                                        chosen1 = price_text.split('$')
                                        chosen1.append('USD')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '£' in price_text:
                                        chosen1 = price_text.split('£')
                                        chosen1.append('GBP')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '€' in price_text:
                                        chosen1 = price_text.split('€')
                                        chosen1.append('EUR')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₹' in price_text:
                                        chosen1 = price_text.split('₹')
                                        chosen1.append('INR')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '¥' in price_text:
                                        chosen1 = price_text.split('¥')
                                        chosen1.append('JPY')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'Lek' in price_text:
                                        chosen1 = price_text.split('Lek')
                                        chosen1.append('Lek')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '؋' in price_text:
                                        chosen1 = price_text.split('؋')
                                        chosen1.append('AFN')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'ƒ' in price_text:
                                        chosen1 = price_text.split('ƒ')
                                        chosen1.append('AWG')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₼' in price_text:
                                        chosen1 = price_text.split('₼')
                                        chosen1.append('AZN')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'Br' in price_text:
                                        chosen1 = price_text.split('Br')
                                        chosen1.append('BYN')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'BZ$' in price_text:
                                        chosen1 = price_text.split('BZ$')
                                        chosen1.append('BZD')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '$b' in price_text:
                                        chosen1 = price_text.split('$b')
                                        chosen1.append('BOB')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'KM' in price_text:
                                        chosen1 = price_text.split('KM')
                                        chosen1.append('BAM')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'P' in price_text:
                                        chosen1 = price_text.split('P')
                                        chosen1.append('BWP')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'R$' in price_text:
                                        chosen1 = price_text.split('R$')
                                        chosen1.append('BRL')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'лв' in price_text:
                                        chosen1 = price_text.split('лв')
                                        chosen1.append('BGN')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '៛' in price_text:
                                        chosen1 = price_text.split('៛')
                                        chosen1.append('KHR')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '¥' in price_text:
                                        chosen1 = price_text.split('¥') 
                                        chosen1.append('CNY')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₡' in price_text:
                                        chosen1 = price_text.split('₡')
                                        chosen1.append('CRC')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'kn' in price_text:
                                        chosen1 = price_text.split('kn')
                                        chosen1.append('HRK')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₱' in price_text:
                                        chosen1 = price_text.split('₱')
                                        chosen1.append('PHP')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'Kč' in price_text:
                                        chosen1 = price_text.split('Kč')
                                        chosen1.append('CZK')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'kr' in price_text:
                                        chosen1 = price_text.split('kr')
                                        chosen1.append('DKK')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'RD$' in price_text:
                                        chosen1 = price_text.split('RD$')
                                        chosen1.append('DOP')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '¢' in price_text:
                                        chosen1 = price_text.split('¢')
                                        chosen1.append('GHS')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'Q' in price_text:
                                        chosen1 = price_text.split('Q')
                                        chosen1.append('GTQ')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'L' in price_text:
                                        chosen1 = price_text.split('L')
                                        chosen1.append('HNL')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'Ft' in price_text:
                                        chosen1 = price_text.split('Ft')
                                        chosen1.append('HUF')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'Rp' in price_text:
                                        chosen1 = price_text.split('Rp')
                                        chosen1.append('IDR')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '﷼' in price_text:
                                        chosen1 = price_text.split('﷼')
                                        chosen1.append('IRR')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₪' in price_text:
                                        chosen1 = price_text.split('₪')
                                        chosen1.append('ILS')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'J$' in price_text:
                                        chosen1 = price_text.split('J$')
                                        chosen1.append('JMD')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₭' in price_text:
                                        chosen1 = price_text.split('₭')
                                        chosen1.append('LAK')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'ден' in price_text:
                                        chosen1 = price_text.split('ден')
                                        chosen1.append('MKD')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'RM' in price_text:
                                        chosen1 = price_text.split('RM')
                                        chosen1.append('MYR')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₨' in price_text:
                                        chosen1 = price_text.split('₨')
                                        chosen1.append('MUR')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₮' in price_text:
                                        chosen1 = price_text.split('₮')
                                        chosen1.append('MNT')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'MT' in price_text:
                                        chosen1 = price_text.split('MT')
                                        chosen1.append('MZN')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'C$' in price_text:
                                        chosen1 = price_text.split('C$')
                                        chosen1.append('NIO')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₦' in price_text:
                                        chosen1 = price_text.split('₦')
                                        chosen1.append('NGN')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'kr' in price_text:
                                        chosen1 = price_text.split('kr')
                                        chosen1.append('NOK')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'S/.' in price_text:
                                        chosen1 = price_text.split('S/.')
                                        chosen1.append('PEN')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'zł' in price_text:
                                        chosen1 = price_text.split('zł')
                                        chosen1.append('PLN')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'lei' in price_text:
                                        chosen1 = price_text.split('lei')
                                        chosen1.append('RON')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₽' in price_text:
                                        chosen1 = price_text.split('₽')
                                        chosen1.append('RUB')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'Дин' in price_text:
                                        chosen1 = price_text.split('Дин')
                                        chosen1.append('RSD')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'NT$' in price_text:
                                        chosen1 = price_text.split('NT$')
                                        chosen1.append('TWD')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '฿' in price_text:
                                        chosen1 = price_text.split('฿')
                                        chosen1.append('THB')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'TT$' in price_text:
                                        chosen1 = price_text.split('TT$')
                                        chosen1.append('TTD')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₴' in price_text:
                                        chosen1 = price_text.split('₴')
                                        chosen1.append('UAH')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '$U' in price_text:
                                        chosen1 = price_text.split('$U')
                                        chosen1.append('UYU')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'Bs' in price_text:
                                        chosen1 = price_text.split('Bs')
                                        chosen1.append('VEF')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif '₫' in price_text:
                                        chosen1 = price_text.split('₫')
                                        chosen1.append('VND')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'FCFA' in price_text:
                                        chosen1 = price_text.split('FCFA')  
                                        chosen1.append('XAF')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    elif 'CFA' in price_text:
                                        chosen1 = price_text.split('CFA')
                                        chosen1.append('XOF')
                                        currency = chosen1[2]
                                        price = chosen1[1]
                                    else:
                                        chosy = price_text.split(' ')
                                        chosy1 = chosy[0].replace('\xa0', ' ')
                                        chosy2 = chosy1.split(' ')
                                        if len(chosy2) == 2:
                                            currency = chosy2[0]
                                            price = chosy2[1]
                                        else:
                                            price = chosy2[0]
                            else:
                                # No price information
                                price, currency = None, None
                else:
                    # No price information
                    price, currency = None, None

                if currency != "USD":
                    price = converter(price,currency)
                    currency = "USD"
                results.append({'URL': url, 'Name': name, 'Price': price, 'Currency': currency, 'Name_Site': name_site})
            except TypeError:
                pass
        return results  
    

google_get_price('iphone 14', 20)