# -*- coding: utf-8 -*-
import codecs
import unicodecsv as csv
import copy
import os
import re

class ExperienceParser:
    def parse(self):
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

        for index in range(len(csv_file_name)):
            csv_cols_count = codecs.open('HorseExperienceTwo/' + csv_file_name[index], 'r', 'utf-8')
            csv_cols = sum(1 for row in csv_cols_count)
            csv_cols_count.close()
            csv_file = codecs.open('HorseExperienceTwo/' + csv_file_name[index], 'r', 'utf-8')
            reader = csv.reader(csv_file)
            if os.path.exists('HorseExperienceThree') == False:
                os.mkdir('HorseExperienceThree')
            csv_write_file = codecs.open('HorseExperienceThree/' + csv_file_name[index], 'w')
            writer = csv.writer(csv_write_file)
            
            winning_percentage_map = {}
            past_name = ''
            victory_count = 0
            count = 0
            experience = []
            index = 0
            
            for row in csv_file:
                if len(row.split(',')) == 14:
                    experience.append(row)
                    current_name = row.split(',')[0]
                    if past_name != current_name or csv_cols - 1 == index:
                        if index != 0:
                            winning_percentage = victory_count / float(count)
                            winning_percentage_map.update({past_name: winning_percentage})
                            count = 0
                            victory_count = 0
                            past_name = current_name
                    if re.search('1', row.split(',')[13]) != None:
                        victory_count = victory_count + 1
                    count = count + 1
                    index = index + 1

            for index in range(len(experience)):
                if len(experience[index].split(',')) == 14:
                    row = experience[index].split(',')
                    name = row[0]
                    race_name = row[4]
                    if winning_percentage_map.has_key(name):
                        winning_percentage = winning_percentage_map[name]
                        row.insert(13, str(winning_percentage))
                        row[14] = int(row[14])
                        if re.search('G3', race_name) or re.search('G2', race_name) or re.search('G1', race_name):
                            writer.writerow(row)

            csv_file.close()
                        
if __name__ == '__main__':
    parser = ExperienceParser()
    parser.parse()
