#! python3
# download all Xkcd comics using multiple threads

import requests, os, bs4, threading

url = 'https://xkcd.com'
os.makedirs('./docs/xkcd', exist_ok=True)  # folder to store comics

def downloadXkcd(startComic, endComic):

    for urlNumber in range(startComic, endComic):
        # download page
        print(f"Downloading page {url}/{urlNumber}..")
        res = requests.get(f"{url}/{urlNumber}")
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
    # prevLink = soup.select('a[rel="prev"]')[0]
    # url = 'https://xkcd.com' + prevLink.get('href')

### create and start thread objects
downloadThreads = []   # list of all thread objects
for i in range(0, 140, 10):   # loops 14 times, creates 14 threads
    start = i
    end = i + 9
    if start == 0:
        start = 1  # there is no comic 0, so set it to 1
    downloadThread = threading.Thread(target=downloadXkcd, args=(start,end))
    downloadThreads.append(downloadThread)
    downloadThread.start()

### wait for all threads to end
for downloadThread in downloadThreads:
    downloadThread.join()

print('Done')

