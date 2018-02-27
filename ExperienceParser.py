# -*- coding: utf-8 -*-
import codecs
import unicodecsv as csv
import copy
import os
import sys
import re

class ExperienceParser:
    def parse(self):
        csv_file = codecs.open('Temp.csv', 'r', 'utf-8')
        csv_file_lines = len(csv_file.readlines())
        csv_file.seek(0)
        reader = csv.reader(csv_file)
        csv_write_file = codecs.open('TrainData.csv', 'w')
        writer = csv.writer(csv_write_file)
            
        horse_winning_percentage_map = {}
        horse_past_name = ''
        horse_victory_count = 0
        horse_data_count = 0
        jockey_winning_count_map = {}
        jockey_winning_percentage_map = {}
        experience = []
        labels = ['horse_name', 'evaluation', 'venue', 'race_name', 'horse_heads', \
                  'horse_number', 'popularity', 'jockey', 'jockey_winning_percentage', \
                  'distance', 'horse_weight', 'horse_weight_diff', 'winning_percentage', \
                  'order']
        writer.writerow(labels)

        for index, row in enumerate(csv_file):
            if len(row.split(',')) == 14:
                experience.append(row)
                horse_current_name = row.split(',')[0]
                jockey_name = row.split(',')[8]
                order = row.split(',')[13]
                if jockey_winning_count_map.has_key(jockey_name):
                    jockey_data_count = jockey_winning_count_map[jockey_name][0]
                    jockey_winning_count = jockey_winning_count_map[jockey_name][1]
                    if re.search('1', order) != None:
                        jockey_winning_count += 1
                    jockey_data_count += 1
                    jockey_winning_count_map.update({jockey_name: \
                    [jockey_data_count, jockey_winning_count]})
                else:
                    jockey_winning_count = 0
                    if re.search('1', order) != None:
                        jockey_winning_count = 1
                    jockey_winning_count_map[jockey_name] = [1, jockey_winning_count]
                if index != 0:
                    if (horse_past_name != horse_current_name or csv_file_lines - 1 == index):
                        horse_winning_percentage = horse_victory_count / float(horse_data_count)
                        horse_winning_percentage_map.update({horse_past_name: \
                        horse_winning_percentage})
                        horse_data_count = 0
                        horse_victory_count = 0
                        horse_past_name = horse_current_name
                if re.search('1', order) != None:
                    horse_victory_count = horse_victory_count + 1
                horse_data_count += 1
        for key, value in jockey_winning_count_map.items():
            jockey_winning_percentage = value[1] / float(value[0])
            jockey_winning_percentage_map.update({key: jockey_winning_percentage})
                
        for index in range(len(experience)):
            experience_row = experience[index].split(',')
            experience_row.pop(1)
            experience_row.pop(9)
            horse_name = experience_row[0]
            jockey_name = experience_row[7]
            race_name = experience_row[3]

            horse_winning_percentage = horse_winning_percentage_map[horse_name]
            experience_row.insert(11, str(('%.6f' % (horse_winning_percentage * 100))))
            jockey_winning_percentage = jockey_winning_percentage_map[jockey_name]
            experience_row.insert(8, str(('%.6f' % (jockey_winning_percentage * 100))))
            
            experience_row[len(experience_row) - 1] = int(experience_row[len(experience_row) - 1])
            if re.search('G3', race_name) \
            or re.search('G2', race_name) \
            or re.search('G1', race_name):
                writer.writerow(experience_row)

        csv_file.close()
                        
if __name__ == '__main__':
    result = os.system('cat HorseExperience/*.csv > Temp.csv')
    if result != 0:
        sys.exit()
    parser = ExperienceParser()
    parser.parse()
    os.system('rm Temp.csv')
