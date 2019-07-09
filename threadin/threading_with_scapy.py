import threading
from threading import Thread
import time
from scapy.all import sniff

check = threading.Event()
var=0

def downloader(vid_link):
    global check
    print ("\nDownloader started")
    for i in range(5):  #representing download time
        time.sleep(1)
    print("Download complete")
    check.set()
    

def sniffer(check):
    global var
    print("Sniffing started \n")
    var=sniff(stop_filter=lambda x: check.is_set())
    print("Sniffing Complete \n")

if __name__ == '__main__':
    print("Enter Video link")
    vid_link=str(input())
    t1=Thread(target = downloader, args=(vid_link, ))
    t2=Thread(target = sniffer, args=(check, ))
    t1.start()
    t2.start()
    t2.join()
    print(var.summary())