from selenium import webdriver
import time
option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_argument("--headless")
from getindianname import *

# option.add_argument("disable-gpu")
import random
def runBot(num):
	for i in range(num):
		browser = webdriver.Chrome(executable_path='E:/Programs/driver/chromedriver.exe', options=option)
		browser.get("https://forms.gle/bBjUoYjwRj4vczGt7")

		name = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
		submit=browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
		name[0].send_keys(randname())

		q1=['//*[@id="i158"]/div[3]/div','//*[@id="i161"]/div[3]/div']
		q2=['//*[@id="i168"]/div[3]/div','//*[@id="i171"]/div[3]/div']
		q3=['//*[@id="i178"]/div[3]/div','//*[@id="i181"]/div[3]/div']
		q4=['//*[@id="i188"]/div[3]/div','//*[@id="i188"]/div[3]/div','//*[@id="i194"]/div[3]/div']
		q5=['//*[@id="i201"]/div[3]/div','//*[@id="i204"]/div[3]/div']
		q6=['//*[@id="i214"]/div[3]/div','//*[@id="i217"]/div[3]/div']
		q7=['//*[@id="i224"]/div[3]/div','//*[@id="i227"]/div[3]/div','//*[@id="i230"]/div[3]/div']
		q8=['//*[@id="i237"]/div[3]/div','//*[@id="i240"]/div[3]/div']
		q9=['//*[@id="i247"]/div[3]/div','//*[@id="i250"]/div[3]/div','//*[@id="i253"]/div[3]/div','//*[@id="i256"]/div[3]/div']
		q10=['//*[@id="i263"]/div[3]/div','//*[@id="i266"]/div[3]/div']
		q11=['//*[@id="i273"]/div[3]/div','//*[@id="i276"]/div[3]/div','//*[@id="i279"]/div[3]/div']
		q12=['//*[@id="i286"]/div[3]/div','//*[@id="i289"]/div[3]/div']

		ls=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12]
		time.sleep(0.99)

		for q in ls:
			browser.find_element_by_xpath(random.choice(q)).click()
			time.sleep(0.2)
		submit.click()
runBot(150)