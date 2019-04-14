from selenium import webdriver

driver=webdriver.Chrome()
open1=driver.get("http://www.baidu.com")
kw=driver.find_element_by_xpath("//*[@id='kw']").send_keys("自动化测试")
searchs=driver.find_element_by_xpath("//*[@id='su']").click()