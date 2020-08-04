## chapter 12 - web scraping

import webbrowser
webbrowser.open('https://inventwithpython.com/')


### downloading webpage with requests
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.status_code == requests.codes.ok  # check status of request
len(res.text)  # character length
print(res.text[:250])


### checking for errors
res = requests.get('https://inventwithpython.com/page-does-not-exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))


## writing to file
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
f = open("../docs/RJ.txt", "wb")
for chunk in res.iter_content(100000):
    f.write(chunk)

f.close()


### beautiful soup
import requests, bs4
res = requests.get('https://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
type(noStarchSoup)

## loading file from harddisk
exampleFile = open('../docs/webscraping/example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
type(exampleSoup)

## finding elements
exampleFile = open('../docs/webscraping/example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')
type(elems)
len(elems)
type(elems[0])
str(elems[0])
elems[0].getText()
elems[0].attrs


## retrieving elements from p tag
pElems = exampleSoup.select('p')
str(pElems[0])
pElems[0].getText()
str(pElems[1])
pElems[1].getText()
str(pElems[2])
pElems[2].getText()


## get method
sElems = exampleSoup.select('span')[0]
str(sElems)
sElems.get('id')
sElems.get('nonexistent_addr') == None  # this doesnt exist
sElems.attrs


### Testing selenium
from selenium import webdriver
browser = webdriver.Firefox()
type(browser)
browser.get('https://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name(' cover-thumb')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')

## clicking the page
linkElem = browser.find_element_by_link_text('Read Online for Free')
type(linkElem)
linkElem.click()


## filling out and submitting forms
# not tried this - refer to site

## sending special keys (eg. keyboard arrow keys)
# not tried this - refer to site

## clicking browser buttons
# eg. browser.forward(), browser.refresh(), browser.quit()

