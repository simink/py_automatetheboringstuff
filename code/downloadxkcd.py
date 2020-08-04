#! python3
# download all Xkcd comics

import requests, os, bs4

url = 'https://xkcd.com'
os.makedirs('./docs/xkcd', exist_ok=True)  # folder to store comics
while not url.endswith('2339/'):  # downloaded till this number

    # download page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # find url of image
    comicE = soup.select('#comic img')
    if comicE == []:
        print("Couldn't find image")
    else:
        comicURL = 'https:' + comicE[0].get('src')
    
    # download image
    print('Downloading image %s' % (comicURL))
    res = requests.get(comicURL)
    res.raise_for_status

    # save image
    imageFile = open(os.path.join('./docs/xkcd', os.path.basename(comicURL)), 'wb')  # change folder
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # get prev button url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done')

