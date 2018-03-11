import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import preprocessing
from collections import Counter

labels = ['horse_name', 'evaluation', 'venue', 'race_name', 'horse_heads', 'horse_number', \
              'popularity', 'jockey', 'jockey_winning_percentage', 'distance', 'horse_weight', \
              'horse_weight_diff', 'winning_percentage']

train_df = pd.read_csv('TrainData.csv', low_memory = False)
train_order_data = train_df['order']
train_feature_data  = train_df.drop('order', axis = 1)
label_encoder = preprocessing.LabelEncoder()
for label in labels:
	train_feature_data[label] = label_encoder.fit_transform(train_feature_data[label])


test_feature_data = pd.read_csv('TestData.csv', low_memory = False)
names = list(test_feature_data['horse_name'].values.flatten())
label_encoder = preprocessing.LabelEncoder()
for label in labels:
	test_feature_data[label] = label_encoder.fit_transform(test_feature_data[label])

print 'Training Data: ' + str(train_feature_data.shape[0])
print 'Test Data: ' + str(test_feature_data.shape[0]) + '\n'

random_forest = RandomForestRegressor(n_estimators = 210, max_depth = 50, n_jobs = 2)

# feature_importances = random_forest.feature_importances_
# if len(labels) == len(feature_importances):
# 	for index in range(len(labels)):
# 		print str(labels[index]) + ' : ' + str(round(feature_importances[index] * 100, 2)) + '[%]'
#
# print '\n'

prediction_times = 10
order_score_dictionary = {}

for index in range(prediction_times):
	random_forest.fit(train_feature_data, train_order_data)
	predicts = random_forest.predict(test_feature_data)
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
