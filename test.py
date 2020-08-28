from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(),
                          chrome_options=options)
driver.get('https://wj.qq.com/')

html = driver.page_source
soup = BeautifulSoup(html, features="html.parser")

# print("usercount: ", int(soup.find(class_='user_count').get_text().replace(',', '')))
print(soup.select(".template > img"))
for tag in soup.select("img.thumbnail"): 
    print(tag.attrs)
