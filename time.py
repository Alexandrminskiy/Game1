from datetime import datetime
from threading import Timer
import os
clear = lambda: os.system('cls')

def TaskManager():
    clear()
    print(datetime.now().strftime("%H:%M:%S"))
    t = Timer( 1, TaskManager )
    t.start()


TaskManager()
