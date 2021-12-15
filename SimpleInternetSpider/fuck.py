from selenium import webdriver



"""
browser = webdriver.Edge()

#browser.get('http://cscore.buaa.edu.cn/#/problem?ProblemId=730&PieId=712')
browser.get('http://cscore.buaa.edu.cn/')
input_first = browser.find_element_by_name('login')
input_second = browser.find_element_by_name('password')
print(input_first, input_second)
input_first.send_keys('20376203')
input_second.send_keys('Fychen@0907')
button_login = browser.find_element_by_xpath('//*[@id="login"]/div/main/div/div[1]/div/div/div/div[3]/button')
button_login.click()
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.baidu.com')
browser.get('http://cscore.buaa.edu.cn/#/problem?ProblemId=730&PieId=712')
text = browser.find_element_by_class_name('markdown-body')
print(text)
#browser.close()
"""
browser = webdriver.Edge()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://python.org')