#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import Queue
import threading
import codecs, sys, os, nltk, time
from collections import Counter
from pyPdf import PdfFileWriter, PdfFileReader

txtfile = "schlag.txt"
f = codecs.open(txtfile, encoding='utf-8')
schlaglist = [x.strip().lower() for x in f]

# Queue instances
queue = Queue.Queue()
out_queue = Queue.Queue()

exitFlag = 0

class ThreadPdfReader(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        print "Starting" + self.name
        pdfReader(self.name, self.queue)
        print "Exiting" + self.name

def pdfReader(name, q):
    while not exitFlag:
        queueLock.acquire()
        # queue is list of files but could be changed to be a list of pdf objects..hmm.
        if not queue.empty():
            # get the filename to open
            pdfFile = q.get()
            print "%s processing %s" % (name, pdfFile)
            try:
                content = ""
                pdf = PdfFileReader(file(pdfFile, "rb")) 
                if pdf.isEncrypted:
                    print "%s is encrypted!" % pdfFile
                    continue
                else:
                    # get all pages and put them in a string
                    for i in range(0, pdf.getNumPages()):
                        content += pdf.getPage(i).extractText().lower() + " \n"
                    content = u" ".join(content.replace(u"\xa0", u" ").strip().split())
                    print repr(content)
                    out_queue.put(content)
            except ValueError as d:
                print d.args
            except Exception as e:
                print e.args
            queueLock.release()
        else:
            queueLock.release()
        time.sleep(1)


start = time.time()
threads = []
queueLock = threading.Lock()

def main():
    # spawn a pool of thread
    for i in range(8): #len(os.listdir(sys.argv[1]))):
        t = ThreadPdfReader(queue)
        #t.setDaemon(True)
        t.start()
        threads.append(t)
    # give it data! 
    queueLock.acquire()
    for k in os.listdir(sys.argv[1]):
        # put the filenames in the queue
        queue.put(sys.argv[1] + k)
    queueLock.release()
    
    # wait for everything to be processed
    while not queue.empty():
        pass

    exitFlag = 1
    
    for e in threads:
        e.join()

main()
for i in range(os.listdir(sys.argv[1])):
    pageString = out_queue.get()
    print pageString
    '''
    for pageString in i: #.split():
        if word in schlaglist:
            cnt[word] += 1
    '''
# print it out!
#print cnt.most_common(20)
print "%.3f" % (time.time() - start)
