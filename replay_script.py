from selenium import webdriver
import time
browser=webdriver.Firefox()
oldsite=0;
newsite=0;
text_file = open("Output.txt", "w")
text_file.close()
while True:
    newsite=browser.current_url
    if(newsite!=oldsite):
        text_file=open("Output.txt", "a")
        text_file.write(newsite+"\n")
        oldsite=newsite
        text_file.close()
    time.sleep(1)