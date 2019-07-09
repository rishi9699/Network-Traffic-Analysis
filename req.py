from selenium import webdriver
import logging
import requests
dr=webdriver.Firefox()
logging.basicConfig(filename="newfile.log", format='%(asctime)s %(message)s', filemode='w')
logger=logging.getLogger()
url='http://www.fb.com'  #set url
dr.get(url)
logger.setLevel(logging.DEBUG)
requests.get(url)
