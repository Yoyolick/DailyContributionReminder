from selenium import webdriver

def checkIfContributed():
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    path = "chromedriver.exe"
    driver = webdriver.Chrome(path, options=op)
    driver.get('https://github.com/Yoyolick')
    #the newest day has the date as data-date in rect so get that