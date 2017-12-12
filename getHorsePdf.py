# -*- coding: utf-8 -*-

import requests
import time

from BeautifulSoup import BeautifulSoup

BASE_URL = u"http://www.jra.go.jp/datafile/resist/"
EXTENSION = u"pdf"

urls = [
  u"http://www.jra.go.jp/datafile/resist/index.html",
]

for url in urls:
  download_urls = []
  r = requests.get(url)
  soup = BeautifulSoup(r.content)
  links = soup.findAll('a')
  for link in links:
    href = link.get('href')
    if href and EXTENSION in href:
      download_urls.append(href)
  for download_url in download_urls[:11]:
    time.sleep(1)
    file_name = download_url.split("/")[-1]
    if BASE_URL in download_url:
      r = requests.get(download_url)
    else:
      r = requests.get(BASE_URL + download_url)
    if r.status_code == 200:
      f = open(file_name, 'w')
      f.write(r.content)
      f.close()
