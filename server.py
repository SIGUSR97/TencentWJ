from glob import glob

from bs4 import BeautifulSoup
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.remote_connection import LOGGER, logging
from webdriver_manager.chrome import ChromeDriverManager

LOGGER.setLevel(logging.FATAL)

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(),
                          chrome_options=options)

app = FastAPI()

# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
# ]
origins = '*'

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/img/{img_name}")
def get_img(img_name: str):
    files = glob(f"./src/assets/{img_name}.*")
    if files:
        path, *_ = files
        return FileResponse(path)
    else:
        pass


@app.get("/usercount")
def get_user_count():
    driver.get('https://wj.qq.com/')

    html = driver.page_source
    soup = BeautifulSoup(html, features="html.parser")

    return {"count": int(soup.find(class_='user_count').get_text().replace(',', ''))}
