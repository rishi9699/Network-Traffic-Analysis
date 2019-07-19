from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json   # module to parse JSON to dictionary

caps = DesiredCapabilities.CHROME
caps['loggingPrefs'] = {'performance': 'ALL'}

options = webdriver.ChromeOptions()
options.add_experimental_option('w3c', False)

driver = webdriver.Chrome(desired_capabilities=caps, options=options)

driver.get('http://www.gmail.com')

logs=driver.get_log('performance')
logreqs = [item for item in logs if 'Network.requestWillBeSent' in str(item)]

file=open(file='get_logs.txt', mode='w')


for i in logreqs:
    tmp=json.loads(i['message'])
    if (tmp['message']['params']['request']['method']=='GET'):
        file.write('GET ' + tmp['message']['params']['request']['url']+' HTTP/1.1\n' )
        file.write('HOST: '+tmp['message']['params']['documentURL']+'\n')
        file.write('HEADERS: '+str(tmp['message']['params']['request']['headers'])+'\n\n')
        

        
file.close()
driver.quit()