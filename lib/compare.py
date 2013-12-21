__author__ = 'LuoCheng'

import os

LINESEP = os.linesep

class Compare(object):
    def __init__(self, surf_url_path, log_url_path):
        with open(surf_url_path, 'r') as f:
            self.url_surf = map(lambda x: x.strip(), f.xreadlines())
        with open(log_url_path, 'r') as f:
            self.url_log = map(lambda x: x.strip(), f.readlines())
        self.url_success = []
        self.same_num = 0

    def do_compare(self):
        for url in self.url_surf:
            if url in self.url_log:
                self.url_log.remove(url)
                self.url_success.append(url)
        self.same_num = len(self.url_success)

    def __str__(self):
        return "Same Url Number: %d\r\n%s"%(self.same_num, LINESEP.join(self.url_success))

if __name__ == '__main__':
    c = Compare('1.log', '2.log')
    c.do_compare()
    print c
    with open('result.log', 'w') as f:
        f.write(str(c))


