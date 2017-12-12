import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import serchHorse

url = 'http://db.netkeiba.com/horse/2012102013/'
serchUrl = serchHorse.serch()
html = urlopen(serchUrl)
soup = BeautifulSoup(html, 'html.parser')

table = soup.findAll('table',{'class':'db_h_race_results'})[0]
rows = table.findAll('tr')

csvFile = open('raceInformation.csv', 'wt', newline = '', encoding = 'utf-8')
writer = csv.writer(csvFile)

hoge = 3
if (hoge == 3):
    print(hoge)

try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            if '\n' in cell.get_text():
                tmp_txt = cell.get_text()
                updated_txt = tmp_txt.replace('\n', '')
                csvRow.append(updated_txt)
            else:
                csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()



    
