from selenium import webdriver
import time

driver=webdriver.Chrome()

driver.get('http://www.youtube.com')
time.sleep(3)

si=driver.find_elements_by_xpath('//*[@aria-label="Sign in"]')
si[0].click()
time.sleep(3)

(driver.find_element_by_class_name('whsOnd.zHQkBf')).send_keys('testsnetwork13@gmail.com')
(driver.find_element_by_class_name('RveJvd.snByac')).click()
time.sleep(3)

(driver.find_element_by_class_name('whsOnd.zHQkBf')).send_keys('iitbombay13')
(driver.find_element_by_class_name('RveJvd.snByac')).click()
time.sleep(3)

a=driver.find_element_by_id('search')
a.click()
a.send_keys('Interstellar Soundtrack\n') #search parameter
time.sleep(3)

driver.find_element_by_class_name('yt-simple-endpoint.style-scope.ytd-video-renderer').click()
time.sleep(10)   #playback time

driver.get('http://www.youtube.com')
time.sleep(3)

driver.find_element_by_xpath('//*[@id="img"]').click()
time.sleep(2)
driver.find_elements_by_xpath("//*[@class='style-scope ytd-compact-link-renderer' and contains(text(), 'Sign out')]")[0].click()
time.sleep(2)

driver.quit()