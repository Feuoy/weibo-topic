# -*- coding: utf-8 -*-
from snownlp import sentiment

sentiment.train('train/neg.txt', 'train/pos.txt')
sentiment.save('sentiment2.marshal')

