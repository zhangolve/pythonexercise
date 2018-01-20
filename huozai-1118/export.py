import os
import csv

tweets_path='./tweets.csv'

with open(tweets_path) as f:
    tweets_lines = csv.reader(f)
    tweets_lines = list(tweets_lines)[1:]
    tweets_lines.reverse()
    os.remove('huozai_note.md')
    for tweet in tweets_lines:
            print(tweet)
            book_note=open('huozai_note.md','a+')
            book_note.write(tweet[3]+'\n')
            book_note.write(tweet[5]+'\n')            
            book_note.close()

