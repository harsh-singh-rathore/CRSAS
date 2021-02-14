import speech_recognition as sr
from joblib import load
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

count_vector = CountVectorizer(stop_words = 'english')
trainData = pd.read_csv("trainingData.csv")
xtrain = trainData['review']
train = count_vector.fit_transform(xtrain)
clf = load('voiceML1.joblib')

def class_label(predictions):
    if predictions == 0:
        return "Negative"
    elif predictions==1:
        return "Positive"

def voiceTtext(file1):
    r=sr.Recognizer()
    R=sr.Recognizer()
    with sr.AudioFile(file1) as source:
       audio=R.record(source)
    text1=r.recognize_google(audio)
    return text1

def classifier(txt):
   test_df=pd.DataFrame(data=txt,columns=['Reviews'])
   test = count_vector.transform(test_df['Reviews'])
   pred = clf.predict(test)
   print(txt)
   print(pred)
   if(pred==1):
      return "positive"
   else:
      return "negative"