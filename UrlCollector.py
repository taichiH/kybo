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
         csv_file_name.append('00.csv')
         csv_file_name.append('01.csv')
         csv_file_name.append('02.csv')
         csv_file_name.append('03.csv')
         csv_file_name.append('04.csv')
         csv_file_name.append('10.csv')
         csv_file_name.append('11.csv')
         csv_file_name.append('12.csv')
         csv_file_name.append('13.csv')
         csv_file_name.append('14.csv')
         csv_file_name.append('20.csv')
         csv_file_name.append('21.csv')
         csv_file_name.append('22.csv')
         csv_file_name.append('23.csv')
         csv_file_name.append('24.csv')
         csv_file_name.append('30.csv')
         csv_file_name.append('31.csv')
         csv_file_name.append('32.csv')
         csv_file_name.append('33.csv')
         csv_file_name.append('34.csv')
         csv_file_name.append('40.csv')
         csv_file_name.append('41.csv')
         csv_file_name.append('42.csv')
         csv_file_name.append('43.csv')
         csv_file_name.append('44.csv')
         csv_file_name.append('50.csv')
         csv_file_name.append('51.csv')
         csv_file_name.append('52.csv')
         csv_file_name.append('53.csv')
         csv_file_name.append('54.csv')
         csv_file_name.append('60.csv')
         csv_file_name.append('61.csv')
         csv_file_name.append('62.csv')
         csv_file_name.append('63.csv')
         csv_file_name.append('64.csv')
         csv_file_name.append('70.csv')
         csv_file_name.append('72.csv')
         csv_file_name.append('74.csv')
         csv_file_name.append('80.csv')
         csv_file_name.append('81.csv')
         csv_file_name.append('82.csv')
         csv_file_name.append('83.csv')
         csv_file_name.append('84.csv')
         csv_file_name.append('90.csv')

         if os.path.exists('HorseUrl') == False:
             os.mkdir('HorseUrl')
         if os.path.exists('HorseUrl/Successful') == False:
             os.mkdir('HorseUrl/Successful')
         if os.path.exists('HorseUrl/Failed') == False:
             os.mkdir('HorseUrl/Failed')

         for index in range(len(csv_file_name)):
             csv_file = codecs.open('HorseName/' + csv_file_name[index], 'r', 'utf-8')
             reader = csv.reader(csv_file)

             successful_csv_file = open('HorseUrl/Successful/' + csv_file_name[index], 'w')
             successful_writer = csv.writer(successful_csv_file)

             failed_csv_file = open('HorseUrl/Failed/' + csv_file_name[index], 'w')
             failed_writer = csv.writer(failed_csv_file)

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
                                         temp = []
                                         temp.append(cells[0])
                                         temp.append(browser.current_url)
                                         successful_writer.writerow(temp)
                                 else:
                                     temp = []
                                     temp.append(cells[0])
                                     failed_writer.writerow(temp)
                                     break
                     else:
                         temp = []
                         temp.append(cells[0])
                         temp.append(browser.current_url)
                         successful_writer.writerow(temp)
                     sleep(5.0)
                     browser.close()

         csv_file.close()
         successful_csv_file.close()
         failed_csv_file.close()

if __name__ == '__main__':
    collector = UrlCollector()
    collector.collect()
