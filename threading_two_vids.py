from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json   # module to parse JSON to dictionary
import time
from threading import Thread

caps = DesiredCapabilities.CHROME
caps['loggingPrefs'] = {'performance': 'ALL'}

options = webdriver.ChromeOptions()
options.add_experimental_option('w3c', False)

def downloader1(vid_link1):
    driver1 = webdriver.Chrome(desired_capabilities=caps, options=options)
    print("\nDownloader started1")
    driver1.get(vid_link1)
    time.sleep(1)
    tl=((driver1.find_element_by_class_name('ytp-time-duration')).get_attribute('innerText')).split(':')
    time.sleep(int(tl[0])*60 + int(tl[1]))
    print("Download complete1")
    logs=driver1.get_log('performance')
    driver1.quit()
    logreqs = [item for item in logs if 'Network.requestWillBeSent' in str(item)]

    file_http=open(file='HTTPlogs1.txt', mode='w')

    for i in logreqs:
        tmp=json.loads(i['message'])
        if (tmp['message']['params']['request']['method']=='GET'):
            if (not tmp['message']['params']['request']['url'].startswith('https')):
                file_http.write('GET ' + tmp['message']['params']['request']['url']+' HTTP/1.1\n' )
            else:
                file_http.write(tmp['message']['params']['request']['url']+'\n')
            file_http.write('HOST: '+tmp['message']['params']['documentURL']+'\n\n')
            
    file_http.close()
    

    
def downloader2(vid_link2):
    driver2 = webdriver.Chrome(desired_capabilities=caps, options=options)
    print ("\nDownloader started2")
    driver2.get(vid_link2)
    time.sleep(2)
    tl=((driver2.find_element_by_class_name('vjs-duration-display')).get_attribute('innerText')).split(':')
    time.sleep(int(tl[0])*60 + int(tl[1]))
    print("Download complete2")
    logs=driver2.get_log('performance')
    driver2.quit()
    logreqs = [item for item in logs if 'Network.requestWillBeSent' in str(item)]

    file_http=open(file='HTTPlogs2.txt', mode='w')

    for i in logreqs:
        tmp=json.loads(i['message'])
        if (tmp['message']['params']['request']['method']=='GET'):
            if (not tmp['message']['params']['request']['url'].startswith('https')):
                file_http.write('GET ' + tmp['message']['params']['request']['url']+' HTTP/1.1\n' )
            else:
                file_http.write(tmp['message']['params']['request']['url']+'\n')
            file_http.write('HOST: '+tmp['message']['params']['documentURL']+'\n\n')
            
    file_http.close()
    
    
if __name__ == '__main__':
    print("Enter Video link1")
    vid_link1=str(input())
    print("Enter Video link2")
    vid_link2=str(input())
    t1=Thread(target = downloader1, args=(vid_link1, ))
    t2=Thread(target = downloader2, args=(vid_link2, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()