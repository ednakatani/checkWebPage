import time
import requests
from bs4 import BeautifulSoup
import hashlib

ALERTZY_KEY = ""
              
PAGE = "https://www.jovemdionisio.com.br/shows"
 
 
def get_hash():

    response = requests.get(PAGE)
    soup = BeautifulSoup(response.text, 'html.parser')
    soup = soup.find("div", {"class": "ticket_content"})
    
    divs = soup.select('div')


    for x in divs[1:]:
        if 'CURITIBA' in str(x) and 'AGOSTO' in str(x):            
            return hashlib.md5(str(x).encode('utf-8')).hexdigest()
    
    return False

initial_hash = False

print("running")

while True:
    
    curr_hash = get_hash()
    if initial_hash != curr_hash:
        print('changed!')
        requests.post('https://alertzy.app/send?accountKey={}&title=Ingresso%20Jovem%20Dionisio&message=Altera%C3%A7%C3%A3o%20no%20site'.format(ALERTZY_KEY))
        initial_hash = curr_hash
        
    time.sleep(15)



