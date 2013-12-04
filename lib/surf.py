#coding:GB2312
__author__ = 'LuoCheng'
import httplib2
import socks
import Queue
import threading
import urlparse
import os
from time import strftime, ctime
from HTMLParser import HTMLParser

LINESEP = os.linesep

class Html(HTMLParser):
    def handle_data(self, data):
        self.text = data

class Surf():
    def __init__(self, fpath, proxy, user, pwd):
        self.urlpath = fpath
        self.user = user
        self.pwd = pwd
        self.proxy = proxy
        self.logs = {'success':[], 'failed':[]}
        self.url_queue = Queue.Queue()
        self.total_url = None
        self.threads = []
        self.fname = 'WTestPlatform.exe-' + strftime('%Y-%m-%d-%H-%M-%S.log')
        self._getUrl()

    def _getUrl(self):
        with open(self.urlpath) as f:
            for line in f.xreadlines():
                self.url_queue.put(line)
        self.total_url = self.url_queue.qsize()


    def _parseResponse(self,response):
        #the response has already satisfied the format like this:
        #source ip$source port$destination ip$destination port$time$url
        h = Html()
        h.feed(response)
        info = h.text.replace('$', '\t')
        return info

    def Requester(self):
        h = httplib2.Http(proxy_info = httplib2.ProxyInfo(socks.PROXY_TYPE_SOCKS5, self.proxy, 1080, proxy_user=self.user, proxy_pass=self.pwd))
        while not self.url_queue.empty():
            url = self.url_queue.get().strip()
            try:
                r, c = h.request(url)
            except Exception as e:
                self.logs['failed'].append(url+LINESEP)
                continue
            else:
                if r.status == 200:
                    u = urlparse.urlparse(url)
                    if u.hostname == '119.254.227.45':
                        info = self._parseResponse(c.decode('utf-8').encode('GBK'))
                        if c.find('$') != -1:
                            self.logs['success'].append(info+LINESEP)
                        else:
                            self.logs['failed'].append('%s(%s)%s'%(url, info, LINESEP))
                    else:
                        self.logs['success'].append(url+LINESEP)
                else:
                    self.logs['failed'].append(url+LINESEP)
            finally:
                self.url_queue.task_done()


    def _generateLogFile(self):
        with open(self.fname, 'w') as f:
            f.write('源IP\t源端口\t目的IP\t目的端口\t访问时间\t访问URL%s'%LINESEP)

    def start(self):
        self._generateLogFile()
        for i in xrange(25):
            t = threading.Thread(target=self.Requester)
            t.daemon = True
            self.threads.append(t)
            t.start()
        self.url_queue.join()
        with open(self.fname, 'a') as f:
            f.write('\r\nSuccess: %d\r\n'%len(self.logs['success']))
            f.writelines(self.logs['success'])
            f.write('\r\nFailed: %d\r\n'%len(self.logs['failed']))
            f.writelines(self.logs['failed'])
            f.write('\r\nsurfing finished, %s\r\n'%ctime())

if __name__ == '__main__':
    pass