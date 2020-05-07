import requests
from datetime import datetime as dt
from bs4 import BeautifulSoup
from selenium import webdriver

today = dt.now().date()
driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
driver.get('https://github.com/login')
delay = 3
driver.implicitly_wait(delay)

#github 계정으로 연결
driver.find_element_by_name('login').send_keys('github_id@xxx.com')
driver.find_element_by_name('password').send_keys('xxxxxx')
driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]').click()

#내가 commit comment 가져올 대상 레파지토리의 브랜치 주소
driver.get('https://github.com/my_github_nickname/my_repository/commits/branch_name')
driver.implicitly_wait(delay)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

result = soup.findAll('li', {'class': 'commit'})
print(len(result))
for comment in result:
    titleParent = comment.find('p', {'class': 'commit-title'})
    title = titleParent.find('a')['aria-label']
    authorParent = comment.find('div', {'class': 'f6 text-gray min-width-0'})
    author = authorParent.find('a')['aria-label']
    datetime = authorParent.find('relative-time')['datetime']
    #내 커밋 닉네임으로만 커밋한 코멘트만 출력
    if ('chakangost' in author):
        if (str(today) in datetime[:11]):
            print('- ' + title)