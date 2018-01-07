# -*- coding: utf-8 -*-
from time import sleep
from bs4 import BeautifulSoup
from collections import OrderedDict
import unicodecsv as csv
import urllib2
import os

class HorseNameCollector:

    def collect(self):
        horse_name_map = OrderedDict()
        horse_name_map['HorseName/00.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_00.html'
        horse_name_map['HorseName/01.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_01.html'
        horse_name_map['HorseName/02.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_02.html'
        horse_name_map['HorseName/03.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_03.html'
        horse_name_map['HorseName/04.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_04.html'
        horse_name_map['HorseName/10.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_10.html'
        horse_name_map['HorseName/11.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_11.html'
        horse_name_map['HorseName/12.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_12.html'
        horse_name_map['HorseName/13.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_13.html'
        horse_name_map['HorseName/14.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_14.html'
        horse_name_map['HorseName/20.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_20.html'
        horse_name_map['HorseName/21.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_21.html'
        horse_name_map['HorseName/22.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_22.html'
        horse_name_map['HorseName/23.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_23.html'
        horse_name_map['HorseName/24.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_24.html'
        horse_name_map['HorseName/30.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_30.html'
        horse_name_map['HorseName/31.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_31.html'
        horse_name_map['HorseName/32.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_32.html'
        horse_name_map['HorseName/33.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_33.html'
        horse_name_map['HorseName/34.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_34.html'
        horse_name_map['HorseName/40.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_40.html'
        horse_name_map['HorseName/41.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_41.html'
        horse_name_map['HorseName/42.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_42.html'
        horse_name_map['HorseName/43.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_43.html'
        horse_name_map['HorseName/44.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_44.html'
        horse_name_map['HorseName/50.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_50.html'
        horse_name_map['HorseName/51.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_51.html'
        horse_name_map['HorseName/52.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_52.html'
        horse_name_map['HorseName/53.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_53.html'
        horse_name_map['HorseName/54.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_54.html'
        horse_name_map['HorseName/60.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_60.html'
        horse_name_map['HorseName/61.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_61.html'
        horse_name_map['HorseName/62.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_62.html'
        horse_name_map['HorseName/63.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_63.html'
        horse_name_map['HorseName/64.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_64.html'
        horse_name_map['HorseName/70.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_70.html'
        horse_name_map['HorseName/72.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_72.html'
        horse_name_map['HorseName/74.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_74.html'
        horse_name_map['HorseName/80.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_80.html'
        horse_name_map['HorseName/81.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_81.html'
        horse_name_map['HorseName/82.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_82.html'
        horse_name_map['HorseName/83.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_83.html'
        horse_name_map['HorseName/84.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_84.html'
        horse_name_map['HorseName/90.csv'] = 'http://www.jbis.or.jp/syllabary/horse_index_90.html'

        if os.path.exists('HorseName') == False:
            os.mkdir('HorseName')

        for key, value in horse_name_map.iteritems():
            html = urllib2.urlopen(value)
            soup = BeautifulSoup(html, 'html.parser')
            table = soup.findAll('table',{'class':'tbl-data-02'})[0]
            rows = table.findAll('tr')
            csv_file = open(key, 'w')
            writer = csv.writer(csv_file)

            for row in rows:
                tbl_data = []
                cell_count = 0
                for cell in row.findAll(['td', 'th']):
                    if ((cell_count == 0) or (cell_count == 4) or (cell_count == 5)):
                        if cell.get_text() != u'馬名' and cell.get_text() != u'馬齢' and cell.get_text() != u'性' and cell.get_text() != u'父馬' and cell.get_text() != u'母馬' and cell.get_text() != u'レース名':
                            tbl_data.append(cell.get_text())
                    cell_count = cell_count + 1
                writer.writerow(tbl_data)
            csv_file.close()
            print key, value
            sleep(5.0)

if __name__ == '__main__':
    collector = HorseNameCollector()
    collector.collect()
