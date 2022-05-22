# -- coding: utf-8 --
'''
Created on 12-April-2022 23:33
Project: Sentiment Analyser 
@author: Gourav Atre
@email: gouravkumar1815@gmail.com
'''
import json
from libraries.whatsapp_text_processing import create_df_from_wp_txt
from libraries.sentiment_analyser import GroupSentimentAnalyser
from datetime import datetime
import validators


def main(config, start_date, end_date):
    """
    Group Sentiment Analyser works in 2 phases with the help of respective pipelines :
        1. Whatsapp text processing
        2. Sentiment Analyser Model
    """

    try:
        # The first module - To transform whatsapp group chat into pandas DataFrames
        df = create_df_from_wp_txt(config)


        # Filter the DF as per the date range and a
        filtered_df_txt = filterDF(df,start_date, end_date)
        # print("######filtered_df_txt##########", filtered_df_txt)   # Just to Debug


        # The second library - To analyse the text and give out sentiment
        sentiment = GroupSentimentAnalyser.find_sentiment(filtered_df_txt)


        return {"The sentiment analyzed is:", str(sentiment)}
    
    except:
        return 0


def filterDF(df, start_date_, end_date_):
    filtered_df = df

    _start_date = datetime.strptime(start_date_, "%d-%m-%Y")
    _end_date = datetime.strptime(end_date_, "%d-%m-%Y")

    start_date_sec = (_start_date-datetime(1970,1,1)).total_seconds()
    end_date_sec = (_end_date-datetime(1970,1,1)).total_seconds()

    filtered_df = df.loc[(df['timestamp'] >= start_date_sec)
                     & (df['timestamp'] < end_date_sec)]

    _DF =filtered_df.drop(columns=['timestamp', 'conversationId', 'conversationWithName', 'senderName','outgoing', 'language' ])
    remove_char = ['Krishna', 'Arpit', 'Gourav', 'Neha', 'Shubhi', 'Anuradha', 'Pratik', '<Media', '@918770864383' ]
    data = ''

    # _df =  filtered_df.groupby('platform')['platform'].apply(' '.join).reset_index()
    
    for index, row in _DF.iterrows():
        if row['text'].split(' ')[0] not in remove_char:
            if not validators.url(row['text'].split(' ')[0]):
                # print(type(row['text']))
                data = data + row['text']
                print(row['text'])

    return data


if __name__ == "__main__":

    config_path = "/media/gourav/LEARN/1_Code/1_Projects/SentimentAnalyser/config/config.json"
    config = json.load(open(config_path))
    
    start_date = "01-02-2022"
    end_date = "27-02-2022"
    
    main(config, start_date , end_date)