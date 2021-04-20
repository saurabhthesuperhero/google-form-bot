from selenium import webdriver
import time
option = webdriver.ChromeOptions()
option.add_argument("-incognito")
#option.add_argument("--headless")
#option.add_argument("disable-gpu")
import random
browser = webdriver.Chrome(executable_path='E:/Programs/driver/chromedriver.exe', options=option)
browser.get("https://forms.gle/bBjUoYjwRj4vczGt7")

name = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
radiobuttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
# checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
# submitbutton = browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")

print(name)
print("#######")
print(radiobuttons)
name[0].send_keys("Shahrukh Khan")

 # radiobuttons[2].click()
# for i in radiobuttons:
# 	i.click()
# 	time.sleep(1)
q1=['//*[@id="i9"]/div[3]/div','//*[@id="i12"]/div[3]/div','//*[@id="i15"]/div[3]/div','//*[@id="i18"]/div[3]/div']
q2=['//*[@id="i25"]/div[3]/div','//*[@id="i28"]/div[3]/div','//*[@id="i31"]/div[3]/div']
q3=['//*[@id="i51"]/div[3]/div','//*[@id="i54"]/div[3]/div','//*[@id="i57"]/div[3]/div']
q4=['//*[@id="i64"]/div[3]/div','//*[@id="i67"]/div[3]/div','//*[@id="i70"]/div[3]/div']
q5=['//*[@id="i77"]/div[3]/div','//*[@id="i80"]/div[3]/div']
q6=['//*[@id="i87"]/div[3]/div','//*[@id="i87"]/div[3]/div','//*[@id="i93"]/div[3]/div']
q7=['//*[@id="i100"]/div[3]/div','//*[@id="i103"]/div[3]/div','//*[@id="i106"]/div[3]/div']
q8=['//*[@id="i113"]/div[3]/div','//*[@id="i116"]/div[3]/div','//*[@id="i119"]/div[3]/div','//*[@id="i122"]/div[3]/div','//*[@id="i125"]/div[3]/div']
q9=['//*[@id="i132"]/div[3]/div','//*[@id="i135"]/div[3]/div','//*[@id="i138"]/div[3]/div']
q10=['//*[@id="i145"]/div[3]/div','//*[@id="i148"]/div[3]/div','//*[@id="i151"]/div[3]/div']


ls=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
# browser.find_element_by_xpath("//*[@id='i9']/div[3]/div").click()
# browser.find_element_by_xpath("//*[@id='i25']/div[3]/div").click()
# browser.find_element_by_xpath('//*[@id="i38"]/div[3]/div').click()
# browser.find_element_by_xpath('//*[@id="i41"]/div[3]/div').click()
for q in ls:
	for i in q:
		browser.find_element_by_xpath(i).click()
# checkboxes[1].click()
# checkboxes[3].click()

# submitbutton[0].click()