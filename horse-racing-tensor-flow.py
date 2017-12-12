# -*- coding: utf-8 -*-
import csv
import time
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn import preprocessing
from sklearn.feature_extraction import DictVectorizer

CSV_FILE_PATH = '../Desktop/python/sample.csv'
TRAIN_SIZE = 5
FEATURE_INPUT = 5
TRAIN_STEP = 5

class TensorFlowAdapter:

    def __init__(self, data_class, test_data_y, train_data_y, test_data_x, train_data_x) :
      self.data_class_ = data_class
      self.test_data_y_ = test_data_y
      self.train_data_y_ = train_data_y
      self.test_data_x_ = test_data_x
      self.train_data_x_ = train_data_x

    def run(self) :
      x = tf.placeholder(tf.float32, [None, FEATURE_INPUT])
      W = tf.Variable(tf.zeros([FEATURE_INPUT, self.data_class_]))
      b = tf.Variable(tf.zeros([self.data_class_]))
      y = tf.nn.softmax(tf.matmul(x, W) + b)
      y_ = tf.placeholder(tf.float32, [None, self.data_class_])
      cross_entropy = -tf.reduce_sum(y_*tf.log(y))
      train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
      init = tf.initialize_all_variables()
      sess = tf.Session()
      sess.run(init)
      for index in range(TRAIN_STEP):
        batch_xs = self.train_data_x_[[index]]
        batch_ys = self.train_data_y_[[index]]
        sess.run(train_step, feed_dict={x: batch_xs, y_:batch_ys})
      correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
      accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
      print(sess.run(accuracy, feed_dict={x: self.test_data_x_, y_: self.test_data_y_}))

class FileHelper:

    def load_csv(self, file_name):
      return pd.read_csv(file_name)

    def parse_csv(self, data):
      labelEncoder = preprocessing.LabelEncoder()
      data['Date'] = labelEncoder.fit_transform(data['Date'])
      data['AreaName'] = labelEncoder.fit_transform(data['AreaName'])
      data['HorseName'] = labelEncoder.fit_transform(data['HorseName'])
      data['HorseSex'] = labelEncoder.fit_transform(data['HorseSex'])
      data['HorseAge'] = labelEncoder.fit_transform(data['HorseAge'])
      data_x = np.array(data[['Date', 'AreaName', 'HorseName', 'HorseSex', 'HorseAge']].fillna(0))
      temp_y = data[['FinishOrder']].to_dict('record')
      vectorizer = DictVectorizer(sparse = False)
      data_y = vectorizer.fit_transform(temp_y)
      data_class = len(vectorizer.get_feature_names())
      [train_data_x, test_data_x] = np.vsplit(data_x, [TRAIN_SIZE])
      [train_data_y, test_data_y] = np.vsplit(data_y, [TRAIN_SIZE])
      batch_size = TRAIN_SIZE
      return data_class, test_data_y, train_data_y, test_data_x, train_data_x

file_helper = FileHelper()
data = file_helper.load_csv(CSV_FILE_PATH)
data_class, test_data_y, train_data_y, test_data_x, train_data_x = file_helper.parse_csv(data)
tensorflow_adapter = TensorFlowAdapter(data_class, test_data_y, train_data_y, test_data_x, train_data_x)
tensorflow_adapter.run()
