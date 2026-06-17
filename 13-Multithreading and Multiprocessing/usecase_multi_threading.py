'''
Real-world Example: Multithreading for I/O-bound tasks
Scenario: Web Scraping
Web scrapping often involves making multiple HTTP requests to fetch data from various web pages. This is an I/O-bound task, as the program spends a lot of time waiting for responses from the server. Using multithreading can help improve the performance of web scraping by allowing multiple requests to be made concurrently.

'''
'''

https://python.longchain.com/v0.2/docs/introduction/

https://python.longchain.com/v0.2/docs/concepts/

https://python.longchain.com/v0.2/docs/tutorials/
'''

import threading
import requests
import time
from bs4 import BeautifulSoup

urls=[
    'https://python.longchain.com/v0.2/docs/introduction/',

'https://python.longchain.com/v0.2/docs/concepts/',

'https://python.longchain.com/v0.2/docs/tutorials/'
]

def fetch_content(url):
    response=requests.get(url)
    if response.status_code==200:
        soup=BeautifulSoup(response.content, 'html.parser')
        title=soup.title.string
        print(f"Title of {url}: {title}")
    else:
        print(f"Failed to fetch {url}")

threads=[]
for url in urls:
    thread=threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web  pages have been fetched.")        