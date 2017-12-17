# -*- coding: utf-8 -*-
import csv
import urllib2
from bs4 import BeautifulSoup
import sys
import serchHorse
import codecs
import unicodecsv as csv
import getHorseInfomation
import os
from collections import OrderedDict

def createLearnData(horseName):
    for name in horseName:
        serchedUrl = serchHorse.serch(name)
        html = urllib2.urlopen(serchedUrl)
        soup = BeautifulSoup(html, 'html.parser')
        if os.path.exists('learnData') == False:
            os.mkdir('learnData')
        if os.path.exists('nonExperience') == False:
            os.mkdir('nonExperience')
        
        try:
            table = soup.findAll('table',{'class':'db_h_race_results'})[0]
            rows = table.findAll('tr')
            filename = 'learnData/' + name + '.csv'
            print filename
            csvFile = open(filename, 'w')
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
            urlArray = [serchedUrl, name]
            filename = 'nonExperience/' + name + '.csv'
            print filename
            nonTableFile = open(filename, 'w')
            nonTableWriter = csv.writer(nonTableFile)
            nonTableWriter.writerow(urlArray)
            nonTableFile.close()
    

def main(key, value):
    horseName = getHorseInfomation.getName(key, value)
    createLearnData(horseName)

if __name__ == '__main__':
    horse_info_map = OrderedDict()
    horse_info_map = {
        "horseInfo/00.csv":"http://www.jbis.or.jp/syllabary/horse_index_00.html",
        "horseInfo/01.csv":"http://www.jbis.or.jp/syllabary/horse_index_01.html",
        "horseInfo/02.csv":"http://www.jbis.or.jp/syllabary/horse_index_02.html",
        "horseInfo/03.csv":"http://www.jbis.or.jp/syllabary/horse_index_03.html",
        "horseInfo/04.csv":"http://www.jbis.or.jp/syllabary/horse_index_04.html",
        "horseInfo/10.csv":"http://www.jbis.or.jp/syllabary/horse_index_10.html",
        "horseInfo/11.csv":"http://www.jbis.or.jp/syllabary/horse_index_11.html",
        "horseInfo/12.csv":"http://www.jbis.or.jp/syllabary/horse_index_12.html",
        "horseInfo/13.csv":"http://www.jbis.or.jp/syllabary/horse_index_13.html",
        "horseInfo/14.csv":"http://www.jbis.or.jp/syllabary/horse_index_14.html",
        "horseInfo/20.csv":"http://www.jbis.or.jp/syllabary/horse_index_20.html",
        "horseInfo/21.csv":"http://www.jbis.or.jp/syllabary/horse_index_21.html",
        "horseInfo/22.csv":"http://www.jbis.or.jp/syllabary/horse_index_22.html",
        "horseInfo/23.csv":"http://www.jbis.or.jp/syllabary/horse_index_23.html",
        "horseInfo/24.csv":"http://www.jbis.or.jp/syllabary/horse_index_24.html",
        "horseInfo/30.csv":"http://www.jbis.or.jp/syllabary/horse_index_30.html",
        "horseInfo/31.csv":"http://www.jbis.or.jp/syllabary/horse_index_31.html",
        "horseInfo/32.csv":"http://www.jbis.or.jp/syllabary/horse_index_32.html",
        "horseInfo/33.csv":"http://www.jbis.or.jp/syllabary/horse_index_33.html",
        "horseInfo/34.csv":"http://www.jbis.or.jp/syllabary/horse_index_34.html",
        "horseInfo/40.csv":"http://www.jbis.or.jp/syllabary/horse_index_40.html",
        "horseInfo/41.csv":"http://www.jbis.or.jp/syllabary/horse_index_41.html",
        "horseInfo/42.csv":"http://www.jbis.or.jp/syllabary/horse_index_42.html",
        "horseInfo/43.csv":"http://www.jbis.or.jp/syllabary/horse_index_43.html",
        "horseInfo/44.csv":"http://www.jbis.or.jp/syllabary/horse_index_44.html",
        "horseInfo/50.csv":"http://www.jbis.or.jp/syllabary/horse_index_50.html",
        "horseInfo/51.csv":"http://www.jbis.or.jp/syllabary/horse_index_51.html",
        "horseInfo/52.csv":"http://www.jbis.or.jp/syllabary/horse_index_52.html",
        "horseInfo/53.csv":"http://www.jbis.or.jp/syllabary/horse_index_53.html",
        "horseInfo/54.csv":"http://www.jbis.or.jp/syllabary/horse_index_54.html",
        "horseInfo/60.csv":"http://www.jbis.or.jp/syllabary/horse_index_60.html",
        "horseInfo/61.csv":"http://www.jbis.or.jp/syllabary/horse_index_61.html",
        "horseInfo/62.csv":"http://www.jbis.or.jp/syllabary/horse_index_62.html",
        "horseInfo/63.csv":"http://www.jbis.or.jp/syllabary/horse_index_63.html",
        "horseInfo/64.csv":"http://www.jbis.or.jp/syllabary/horse_index_64.html",
        "horseInfo/70.csv":"http://www.jbis.or.jp/syllabary/horse_index_70.html",
        "horseInfo/72.csv":"http://www.jbis.or.jp/syllabary/horse_index_72.html",
        "horseInfo/74.csv":"http://www.jbis.or.jp/syllabary/horse_index_74.html",
        "horseInfo/80.csv":"http://www.jbis.or.jp/syllabary/horse_index_80.html",
        "horseInfo/81.csv":"http://www.jbis.or.jp/syllabary/horse_index_81.html",
        "horseInfo/82.csv":"http://www.jbis.or.jp/syllabary/horse_index_82.html",
        "horseInfo/83.csv":"http://www.jbis.or.jp/syllabary/horse_index_83.html",
        "horseInfo/84.csv":"http://www.jbis.or.jp/syllabary/horse_index_84.html",
        "horseInfo/90.csv":"http://www.jbis.or.jp/syllabary/horse_index_90.html",
    }

    for key, value in horse_info_map.items():
        main(key, value)


    
