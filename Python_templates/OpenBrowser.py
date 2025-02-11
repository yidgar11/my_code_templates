#python_apache.pyfrom subprocess import Popen
import webbrowser
import sys
import time
import threading


sites=['http://ynet.co.il','http://mako.co.il']


def check():
    for url in sites:


        if sys.platform == 'darwin':    # in case of OS X
            p=Popen(['open', url])
            time.sleep(5)
            p.kill()


            #Popen(['open', 'chrome' , url], shell=True)
        else:
            webbrowser.get('chrome %s').open_new_tab(url)

        if sys.platform == 'darwin':    # in case of OS X
            print
        else:
            webbrowser.get('chrome %s').open_new_tab(url)


class FuncThread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        self._is_running = True
        threading.Thread.__init__(self)

    def run(self):
        if (self._is_running):
            self._target(*self._args)

    #def stop(self):
    #    self._is_running = False

def openSite(url):
    if sys.platform == 'darwin':    # in case of OS X
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        webbrowser.get(chrome_path).open(url , new=1)

    else:
        webbrowser.get('chrome %s').open_new_tab(url)


for url in sites:
    t1 = FuncThread(openSite, url)
    t1.start()
    t1.join()
    time.sleep(1)




