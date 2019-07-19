from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities.CHROME
caps['loggingPrefs'] = {'performance': 'ALL'}

options = webdriver.ChromeOptions()
options.add_experimental_option('w3c', False)

driver = webdriver.Chrome(desired_capabilities=caps, options=options)

driver.get('http://www.google.com')

logs=driver.get_log('performance')
logreqs = [item for item in logs if 'Network.requestWillBeSent' in str(item)]

file=open(file='logs1.txt', mode='w')


for e in logreqs:
    file.write(str(e))
    file.write('\n\n')

    
file.close()
driver.quit()