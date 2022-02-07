###direnum.py <target IP>### 
###Future: use arg wordlist###

import requests 
import sys 
from multiprocessing.dummy import Pool as ThreadPool


sub_list = open("wordlist.txt").read() 
directories = sub_list.splitlines()

# make pool of workers
pool = ThreadPool(10)
#results = pool.map(my_function, my_array)

def my_function
    for dir in directories:
        dir_enum = f"http://{sys.argv[1]}/{dir}.html" 
        r = requests.get(dir_enum)
        if r.status_code==404: 
            pass
        else:
            print("Valid directory:" ,dir_enum)

results = pool.map(my_function, sub_list)

# close the pool and wait for work to finish
pool.close()
pool.join()