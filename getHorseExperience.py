# -*- coding: utf-8 -*-
import csv
import urllib2
from bs4 import BeautifulSoup
import sys
import serchHorse
import codecs
import unicodecsv as csv

def main():
    serchedUrl = serchHorse.serch()
    html = urllib2.urlopen(serchedUrl)
    soup = BeautifulSoup(html, 'html.parser')
    
    try:
        table = soup.findAll('table',{'class':'db_h_race_results'})[0]
        rows = table.findAll('tr')
        csvFile = open('raceInfo.csv', 'w')
        writer = csv.writer(csvFile)
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
        finally:
            csvFile.close()
                
    except:
        print 'non race experience'
        urlArray = [serchedUrl]
        nonTableFile = open('nonRaceInfo.csv', 'w')
        nonTableWriter = csv.writer(nonTableFile)
        nonTableWriter.writerow(urlArray)
        nonTableFile.close()

if __name__ == '__main__':
    main()


    
