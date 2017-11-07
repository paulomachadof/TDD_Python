from selenium import webdriver

browser = webdriver.Firefox(executable_path='/home/paulo/Downloads/geckodriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
