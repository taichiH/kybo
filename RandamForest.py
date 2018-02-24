import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import preprocessing

df = pd.read_csv('HorseExperience/INPUT.csv', low_memory = False)

order_data = df['order']
feature_data  = df.drop('order', axis = 1)

label_encoder = preprocessing.LabelEncoder()
for label in ['name', 'age', 'evaluation', 'venue', 'race_name', 'heads', 'horsenumber', \
              'popularity', 'horseman', 'distance', 'course_status', 'horse_weight', \
              'horse_weight_ratio', 'winning_percentage']:
  feature_data[label] = label_encoder.fit_transform(feature_data[label])

(train_feature_data, test_feature_data, train_order_data, test_order_data) = train_test_split(feature_data, order_data, test_size = 0.1, shuffle = True)

print 'training data: ' + str(train_feature_data.shape[0])
print 'test data: ' + str(test_feature_data.shape[0])

random_forest = RandomForestRegressor(n_estimators = 210, max_depth = 10, n_jobs = 2)
random_forest.fit(train_feature_data, train_order_data)

accuracy = random_forest.score(test_feature_data, test_order_data)

print 'accuracy: ' + str(accuracy * 100)
