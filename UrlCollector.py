# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unicodecsv as csv
from time import sleep
import codecs
import os

class UrlCollector:

    def collect(self):
         csv_file_name = []
         csv_file_name.append('HorseName/00.csv')
         csv_file_name.append('HorseName/01.csv')
         csv_file_name.append('HorseName/02.csv')
         csv_file_name.append('HorseName/03.csv')
         csv_file_name.append('HorseName/04.csv')
         csv_file_name.append('HorseName/10.csv')
         csv_file_name.append('HorseName/11.csv')
         csv_file_name.append('HorseName/12.csv')
         csv_file_name.append('HorseName/13.csv')
         csv_file_name.append('HorseName/14.csv')
         csv_file_name.append('HorseName/20.csv')
         csv_file_name.append('HorseName/21.csv')
         csv_file_name.append('HorseName/22.csv')
         csv_file_name.append('HorseName/23.csv')
         csv_file_name.append('HorseName/24.csv')
         csv_file_name.append('HorseName/30.csv')
         csv_file_name.append('HorseName/31.csv')
         csv_file_name.append('HorseName/32.csv')
         csv_file_name.append('HorseName/33.csv')
         csv_file_name.append('HorseName/34.csv')
         csv_file_name.append('HorseName/40.csv')
         csv_file_name.append('HorseName/41.csv')
         csv_file_name.append('HorseName/42.csv')
         csv_file_name.append('HorseName/43.csv')
         csv_file_name.append('HorseName/44.csv')
         csv_file_name.append('HorseName/50.csv')
         csv_file_name.append('HorseName/51.csv')
         csv_file_name.append('HorseName/52.csv')
         csv_file_name.append('HorseName/53.csv')
         csv_file_name.append('HorseName/54.csv')
         csv_file_name.append('HorseName/60.csv')
         csv_file_name.append('HorseName/61.csv')
         csv_file_name.append('HorseName/62.csv')
         csv_file_name.append('HorseName/63.csv')
         csv_file_name.append('HorseName/64.csv')
         csv_file_name.append('HorseName/70.csv')
         csv_file_name.append('HorseName/72.csv')
         csv_file_name.append('HorseName/74.csv')
         csv_file_name.append('HorseName/80.csv')
         csv_file_name.append('HorseName/81.csv')
         csv_file_name.append('HorseName/82.csv')
         csv_file_name.append('HorseName/83.csv')
         csv_file_name.append('HorseName/84.csv')
         csv_file_name.append('HorseName/90.csv')

         successful_csv = []
         failed_csv = []

         for index in range(len(csv_file_name)):
             csv_file = codecs.open(csv_file_name[index], 'r', 'utf-8')
             reader = csv.reader(csv_file)
             for row in csv_file:
                 if row != '\r\n':
                     cells = row.split(',')
                     browser = webdriver.Chrome('./../chromedriver')
                     browser.get('http://db.netkeiba.com/?pid=horse_top')
                     sleep(5.0)
                     search_input = browser.find_element_by_css_selector('.field')
                     search_input.send_keys(cells[0])
                     search_input.submit()
                     if browser.current_url == 'http://db.netkeiba.com/':
                         race_table = []
                         table = browser.find_element_by_class_name('race_table_01')
                         trs = table.find_elements(By.TAG_NAME, 'tr')
                         for tr_index in range(0, len(trs)):
                             tds_table = []
                             tds = trs[tr_index].find_elements(By.TAG_NAME, 'td')
                             count = 0
                             for td_index in range(0, len(tds)):
                                 if ((count == 1) or (count == 6) or (count == 7)):
                                     tds_table.append(tds[td_index].text)
                                 count = count + 1
                             race_table.append(tds_table)
                         for row in race_table:
                             names = ','.join(row)
                             names = names.split(',')
                             if names[0] != '':
                                 if cells[0] == names[0]:
                                     if (cells[1] == names[1]) or (cells[2] == names[2]):
                                         browser.find_element_by_link_text(cells[0]).click()
                                         sleep(5.0)
                                         successful_csv.append(browser.current_url)
                                         print str(successful_csv).decode('string-escape')
                                 else:
                                     failed_csv.append(cells[0])
                                     print str(failed_csv).decode('string-escape')
                                     break
                     else:
                         successful_csv.append(browser.current_url)
                         print str(successful_csv).decode('string-escape')
                     sleep(5.0)
                     browser.close()
         csv_file.close()

if __name__ == '__main__':
    collector = UrlCollector()
    collector.collect()
