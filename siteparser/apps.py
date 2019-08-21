from django.apps import AppConfig


class SiteparserConfig(AppConfig):
    name = 'siteparser'




import time
import threading
from django.apps import apps

print(apps)

def f(string):
    while True:
        print(string)
        time.sleep(2)

f_thr1 = threading.Thread(target=f, args=({'123'}))
f_thr1.daemon = True
#f_thr2 = threading.Thread(target=f, args=({'abc'}))
#f_thr2.daemon = True

f_thr1.start()
#time.sleep(0.5)
#f_thr2.start()