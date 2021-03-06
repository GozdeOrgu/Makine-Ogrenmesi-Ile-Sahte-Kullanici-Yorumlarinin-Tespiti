#pip3 install pickle-mixin
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.preprocessing import StandardScaler
import numpy as np
from nltk import word_tokenize
from nltk.corpus import stopwords
import re
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import pickle

#Veri setini oku
dataset = pd.read_csv('dataset.csv')
dataset.head()
dataset.sort_values("Body", inplace = True)
dataset = dataset.drop(columns="B")

#Aynı verileri sil
dataset.drop_duplicates(subset ="Body",keep = False, inplace = True)


#Optimizasyon Fonksiyonu
def optimizasyon(dataset):
    dataset = dataset.dropna()

    stop_words = set(stopwords.words('turkish'))
    noktalamaIsaretleri = ['•', '!', '"', '#', '”', '“', '$', '%', '&', "'", '–', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '…']
    stop_words.update(noktalamaIsaretleri)

    for ind in dataset.index:
        body = dataset['Body'][ind]
        body = body.lower()
        body = re.sub(r'http\S+', '', body)
        body = re.sub('\[[^]]*\]', '', body)
        body = (" ").join([word for word in body.split() if not word in stop_words])
        body = "".join([char for char in body if not char in noktalamaIsaretleri])
        dataset['Body'][ind] = body
    return dataset


dataset = optimizasyon(dataset)


yorumlar_makina = dataset[dataset['Label']==0]
yorumlar_insan = dataset[dataset['Label']==1]

tfIdf = TfidfVectorizer( binary=False, ngram_range=(1,3))


makina_cv = tfIdf.fit_transform(yorumlar_makina['Body'].tolist())
insan_cv = tfIdf.fit_transform(yorumlar_insan['Body'].tolist())



X = dataset['Body']
y = dataset['Label']

x_tv = tfIdf.fit_transform(X)

x_train_tv, x_test_tv, y_train_tv, y_test_tv = train_test_split(x_tv, y, test_size=0.2, random_state=0)


log_tv = LogisticRegression() 
log_tv.fit(x_train_tv,y_train_tv)

pickle.dump(log_tv, open("egitilmis_model", 'wb'))
print("Lojistik Regresyon modeli eğitildi ve kayıt edildi !")


pickle.dump(tfIdf, open("vektorlestirici", 'wb'))
print("Tf-Idf vektörleştirici modeli kayıt edildi !")

