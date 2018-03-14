import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import preprocessing
from collections import Counter

category_labels = ['horse_name', 'venue', 'race_name', 'jockey']
numeric_labels = ['evaluation', 'horse_heads', 'horse_number', \
	'popularity', 'jockey_winning_percentage', 'distance', 'horse_weight', \
	'horse_weight_diff', 'winning_percentage']

standard_scaler = preprocessing.StandardScaler()
label_encoder = preprocessing.LabelEncoder()
one_hot_encoder = preprocessing.OneHotEncoder()

train_data_frame = pd.read_csv('TrainData.csv', low_memory = False)
train_order_data_frame = train_data_frame['order']
train_feature_data_frame  = train_data_frame.drop('order', axis = 1)
category_data_frame = train_feature_data_frame[category_labels]
category_data_frame = category_data_frame.apply(label_encoder.fit_transform)
numeric_data_frame = train_feature_data_frame[numeric_labels]
scaler = standard_scaler.fit(numeric_data_frame)
numeric_data_frame = pd.DataFrame(scaler.transform(numeric_data_frame), index = numeric_data_frame.index.values, columns = numeric_data_frame.columns.values)
train_feature_data_frame = category_data_frame.join(numeric_data_frame, how='outer')

test_feature_data_frame = pd.read_csv('TestData.csv', low_memory = False)
names = list(test_feature_data_frame['horse_name'].values.flatten())
category_data_frame = test_feature_data_frame[category_labels]
category_data_frame = category_data_frame.apply(label_encoder.fit_transform)
numeric_data_frame = test_feature_data_frame[numeric_labels]
scaler = standard_scaler.fit(numeric_data_frame)
numeric_data_frame = pd.DataFrame(scaler.transform(numeric_data_frame), index = numeric_data_frame.index.values, columns = numeric_data_frame.columns.values)
test_feature_data_frame = category_data_frame.join(numeric_data_frame, how='outer')

print 'Training Data: ' + str(train_feature_data_frame.shape[0])
print 'Test Data: ' + str(test_feature_data_frame.shape[0]) + '\n'

random_forest = RandomForestRegressor(n_estimators = 210, max_depth = 50, n_jobs = 2)

prediction_times = 1
order_score_dictionary = {}

for index in range(prediction_times):
	random_forest.fit(train_feature_data_frame, train_order_data_frame)
	predicts = random_forest.predict(test_feature_data_frame)
	if len(predicts) == len(names):
		predict_dictionary = {}
		for name_index in range(len(names)):
			predict_dictionary[names[name_index]] = predicts[name_index]
		order_index = 1
		for name, predict in sorted(predict_dictionary.items(), key = lambda x:-x[1]):
			if order_score_dictionary.has_key(name) == False:
				order_score_dictionary[name] = []
			order_score_dictionary[name].append(len(names) - order_index)
			order_index += 1

for name, orders in order_score_dictionary.items():
	total_order_score = 0
	for index in range(len(orders)):
		total_order_score += orders[index]
	del order_score_dictionary[name]
	order_score_dictionary[name] = total_order_score

for name, score in sorted(order_score_dictionary.items(), key = lambda x:-x[1]):
	print name + ' : ' + str((score / prediction_times) * 100 / (len(names) - 1)) + '[%]'
