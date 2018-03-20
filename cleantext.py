import nltk

import pandas as pd

import string
from nltk.corpus import stopwords

comments=[line.rstrip() for line in open("out1.csv")]

len(comments)

import pandas as pd

comment=pd.read_csv("out.csv",sep='\t',names=['Comment'])
stopwords.words('english')
dictionary=pd.read_csv("sentiment_dict.csv",sep='\t',names=['Words','Classifier'])

def clean_text(mess):
    nopunc = [char for char in mess if char not in string.punctuation]
    nopunc = "".join(nopunc)

    return ([word for word in nopunc.split() if word.lower() not in stopwords.words("english")])

print(comment['Comment'].head(5).apply(clean_text))

'''
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics 

# Generate counts from text using a vectorizer.  There are other vectorizers available, and lots of options you can set.
# This performs our step of computing word counts.
vectorizer = CountVectorizer(stop_words='english')
train_features = vectorizer.fit_transform([r[0] for r in dictionary])
test_features = vectorizer.transform([r[0] for r in comment])

# Fit a naive bayes model to the training data.
# This will train the model using the word counts we computer, and the existing classifications in the training set.
nb = MultinomialNB()
nb.fit(train_features, [int(r[1]) for r in dictionary])

# Now we can use the model to predict classifications for our test features.
predictions = nb.predict(test_features)

# Compute the error.  It is slightly different from our model because the internals of this process work differently from our implementation.
fpr, tpr, thresholds = metrics.roc_curve(actual, predictions, pos_label=1)
print("Multinomial naive bayes AUC: {0}".format(metrics.auc(fpr, tpr))) 

'''
