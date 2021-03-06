# -*- coding: utf-8 -*-
"""KNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pK_tVN03L3s92WaE_HhzZA7GB2dbekEB
"""

pip install plotly --upgrade

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

"""**Aprendizagem Baseado em Instâmcias - KNN**"""
"""**Instance Based Learning - KNN**"""

from sklearn.neighbors import KNeighborsClassifier

import pickle
with open('credito.pkl', 'rb') as f:  
  x_credit_treinamento, y_credit_treinamento, x_credit_teste, y_credit_teste = pickle.load(f)

x_credit_treinamento.shape, y_credit_treinamento.shape

x_credit_teste.shape, y_credit_teste.shape

knn_credito = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p = 2)
knn_credito.fit(x_credit_treinamento, y_credit_treinamento)

previsoes = knn_credito.predict(x_credit_teste)
previsoes

y_credit_teste

from sklearn.metrics import accuracy_score, classification_report
accuracy_score(y_credit_teste, previsoes)

from yellowbrick.classifier import ConfusionMatrix
cm = ConfusionMatrix(knn_credito)
cm.fit(x_credit_treinamento, y_credit_treinamento)
cm.score(x_credit_teste, y_credit_teste)

print(classification_report(y_credit_teste, previsoes))
