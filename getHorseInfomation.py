# -*- coding: utf-8 -*-
import csv
import urllib2
from bs4 import BeautifulSoup
import sys
import codecs
import unicodecsv as csv
import os

def getName(path, url):
    serchedUrl = url
    print serchedUrl
    html = urllib2.urlopen(serchedUrl)
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.findAll('table',{'class':'tbl-data-02'})[0]
    rows = table.findAll('tr')
    if os.path.exists('horseInfo') == False:
      os.mkdir('horseInfo')
    csvFile = open(path, 'w')
    writer = csv.writer(csvFile)
    horseName = []

    try:
        for row in rows:
            csvRow = []
            for cell in row.findAll(['td', 'th']):
                if '\n' in cell.get_text():
                    tmpText = cell.get_text()
                    updatedText = tmpText.replace('\n', '')
                    csvRow.append(updatedText)
                else:
                    csvRow.append(cell.get_text())
            writer.writerow(csvRow)
            horseName.append(csvRow[0])

    finally:
        csvFile.close()
        return horseName
    
