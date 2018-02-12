# -*- coding: utf-8 -*-

import os
import sys
import urllib2
import codecs
from time import sleep
import unicodecsv as csv
from bs4 import BeautifulSoup
from collections import OrderedDict

class ExperienceCollector:

    def collect(self):
         assert os.path.exists('HorseUrl'), "HorseUrl does not exist."

         csv_file_name = []
         # csv_file_name.append('00.csv')
         csv_file_name.append('01.csv')
         # csv_file_name.append('02.csv')
         # csv_file_name.append('03.csv')
         # csv_file_name.append('04.csv')
         # csv_file_name.append('10.csv')
         # csv_file_name.append('11.csv')
         # csv_file_name.append('12.csv')
         # csv_file_name.append('13.csv')
         # csv_file_name.append('14.csv')
         # csv_file_name.append('20.csv')
         # csv_file_name.append('21.csv')
         # csv_file_name.append('22.csv')
         # csv_file_name.append('23.csv')
         # csv_file_name.append('24.csv')
         # csv_file_name.append('30.csv')
         # csv_file_name.append('31.csv')
         # csv_file_name.append('32.csv')
         # csv_file_name.append('33.csv')
         # csv_file_name.append('34.csv')
         # csv_file_name.append('40.csv')
         # csv_file_name.append('41.csv')
         # csv_file_name.append('42.csv')
         # csv_file_name.append('43.csv')
         # csv_file_name.append('44.csv')
         # csv_file_name.append('50.csv')
         # csv_file_name.append('51.csv')
         # csv_file_name.append('52.csv')
         # csv_file_name.append('53.csv')
         # csv_file_name.append('54.csv')
         # csv_file_name.append('60.csv')
         # csv_file_name.append('61.csv')
         # csv_file_name.append('62.csv')
         # csv_file_name.append('63.csv')
         # csv_file_name.append('64.csv')
         # csv_file_name.append('70.csv')
         # csv_file_name.append('72.csv')
         # csv_file_name.append('74.csv')
         # csv_file_name.append('80.csv')
         # csv_file_name.append('81.csv')
         # csv_file_name.append('82.csv')
         # csv_file_name.append('83.csv')
         # csv_file_name.append('84.csv')
         # csv_file_name.append('90.csv')

         for index in range(len(csv_file_name)):
             csv_file = codecs.open('HorseUrl/Successful/' + csv_file_name[index], 'r', 'utf-8')
             reader = csv.reader(csv_file)

             if os.path.exists('HorseExperience') == False:
                 os.mkdir('HorseExperience')
             experience_csv_file = open('HorseExperience/' + csv_file_name[index], 'w')
             writer = csv.writer(experience_csv_file)

             for row in csv_file:
                 name = row.split(",")[0]
                 url = row.split(",")[1]
                 sleep(1.0)
                 html = urllib2.urlopen(url)
                 soup = BeautifulSoup(html, 'html.parser')
                 try:
                     table = soup.find('table',{'class':'db_h_race_results'})
                     rows = table.find_all('tr')
                     for row in rows:
                         csv_row = []
                         for cell in row.findAll(['td', 'th']):
                             if '\n' in cell.get_text():
                                 text = cell.get_text().replace('\n', '')
                                 csv_row.append(text)
                             else:
                                 csv_row.append(cell.get_text())
                         writer.writerow(csv_row)
                 except:
                     print name,url
                     pass
             csv_file.close()
             experience_csv_file.close()

if __name__ == '__main__':
    collector = ExperienceCollector()
    collector.collect()
