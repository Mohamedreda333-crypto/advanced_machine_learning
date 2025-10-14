from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import csv

user_input = 'smart watch'
url = f'https://www.noon.com/egypt-en/search/?q={user_input}'
product_details = []

def noon (link):
    try:
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service)
        browser.get(link)
        time.sleep(5)
        
        product_list = browser.find_elements('class name','PBoxLinkHandler_linkWrapper__8FlHB')
        for product in product_list:
            html_code = product.get_attribute('outerHTML')
            soup = BeautifulSoup(html_code,'html.parser')
            try:
                product_name = soup.find('h2',{'class':'ProductDetailsSection_title__JorAV'}).text.strip() or soup.find('h2',{'data-qa':'plp-product-box-name'}).text.strip()
            except:
                product_name = 'No product found'
            
            try:
                product_price = soup.find('strong',{'class':'Price_amount__2sXa7'}).text.strip() 
            except:
                product_price = 'No price found'
                
            try:
                product_discount = soup.find('span',{'class':'PriceDiscount_discount__1ViHb PriceDiscount_pBox__eWMKb'}).text.strip()
            except:
                product_discount = 'This product is not have any discount'
            try:
                product_rate = soup.find('div',{'class':'RatingPreviewStar_textCtr__sfsJG'}).text.strip()
            except:
                product_rate = 'This product is not have any rate'
            try:
                product_link = soup.find('a').get('href')
            except:
                product_link = 'No product link'
            product_details.append({
                'product_name':product_name,
                'product_price': product_price,
                'product_discount': product_discount,
                'product_rate' : product_rate,
                'product_link':product_link                
            })
                
                         
    except Exception as e:
        print(f"Something with wrong with noon ==> {e}")    
            
def printing_file():
    path = 'E:/noon.csv' 
    keys = product_details[0].keys()
    with open (path, 'w' , newline='',encoding='UTF-8') as output_file:
        dict_writer = csv.DictWriter(output_file , keys)
        dict_writer.writeheader()
        dict_writer.writerows(product_details) 
    print('file created successfully')             
             
    
noon(url)
printing_file()
