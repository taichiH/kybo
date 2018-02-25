import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import preprocessing

train_df = pd.read_csv('INPUT.csv', low_memory = False)
train_order_data = train_df['order']
train_feature_data  = train_df.drop('order', axis = 1)
label_encoder = preprocessing.LabelEncoder()
for label in ['name', 'age', 'evaluation', 'venue', 'race_name', 'heads', 'horsenumber', \
              'popularity', 'horseman', 'distance', 'course_status', 'horse_weight', \
              'horse_weight_ratio', 'winning_percentage']:
  train_feature_data[label] = label_encoder.fit_transform(train_feature_data[label])

test_feature_data = pd.read_csv('INPUT2.csv', low_memory = False)
label_encoder = preprocessing.LabelEncoder()
for label in ['name', 'age', 'evaluation', 'venue', 'race_name', 'heads', 'horsenumber', \
              'popularity', 'horseman', 'distance', 'course_status', 'horse_weight', \
              'horse_weight_ratio', 'winning_percentage']:
  test_feature_data[label] = label_encoder.fit_transform(test_feature_data[label])

print 'training data: ' + str(train_feature_data.shape[0])
print 'test data: ' + str(test_feature_data.shape[0])

random_forest = RandomForestRegressor(n_estimators = 210, max_depth = 50, n_jobs = 2)
random_forest.fit(train_feature_data, train_order_data)

print 'feature_importances_:\n' + str(random_forest.feature_importances_)

predict = random_forest.predict(test_feature_data)
print 'predict:'
print predict
