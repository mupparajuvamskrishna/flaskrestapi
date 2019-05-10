import pandas as pd
# To read a CSV file
# df = pd.read_csv('sentences.csv')
df = pd.DataFrame({'sentence': ['I am very happy', 'I am very sad', 'I am sad but I am happy too']})

from textblob import TextBlob

# The x in the lambda function is a row (because I set axis=1)
# Apply iterates the function accross the dataframe's rows
df['polarity'] = df.apply(lambda x: TextBlob(x['sentence']).sentiment.polarity, axis=1)
df['subjectivity'] = df.apply(lambda x: TextBlob(x['sentence']).sentiment.subjectivity, axis=1)
print(df)
testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
testimonial.sentiment


for ind in df.index: 
     if df['polarity'][ind]>0:
            print('Positive')
     elif df['polarity'][ind]<0:
            print('Negative')
     else:
            print('Neutral')
