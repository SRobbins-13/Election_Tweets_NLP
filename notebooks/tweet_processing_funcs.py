import tweepy, json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from datetime import datetime
import time

def make_candidate_tweet_df(candidate_tweets):
    ###########################################
    ### Information to pull for all tweets
    tweet_meta_data = [[tweet['id_str'], 
                      tweet['created_at'], 
                      tweet['full_text'],
                      tweet['favorite_count'], 
                      tweet['retweet_count'],
                      tweet['in_reply_to_screen_name'],
                      tweet['in_reply_to_status_id_str'],
                      tweet['user']['id_str'],
                      tweet['user']['name'],
                      tweet['user']['screen_name'],
                      tweet['user']['location'],
                      tweet['user']['followers_count'],
                      tweet['user']['friends_count'],
                      tweet['user']['statuses_count']
                     ]
                     for idx,tweet in enumerate(candidate_tweets)]

    df = pd.DataFrame(tweet_meta_data,columns=['tweet_id',
                                        'created_at',
                                        'tweet_text',
                                        'num_favorites',
                                        'num_retweets',
                                        'in_reply_to_screen_name',
                                        'in_reply_to_tweet_id',
                                        'user_id',
                                        'user_name',
                                        'user_handle',
                                        'user_location',
                                        'user_followers',
                                        'user_following',
                                        'user_num_tweets'])
    
    # convert `created_at` to datetime - actually saves as timestamp
    df['created_at'] = pd.to_datetime(df['created_at'])
    
    ###########################################
    ### Pull Retweet/Quote Tweet specific data
    rt_tweet_id = []
    rt_tweet_user_id = []
    rt_tweet_user_handle = []

    for tweet in candidate_tweets:
        if 'retweeted_status' in tweet:
            rt_tweet_id.append(tweet['retweeted_status']['id_str'])
            rt_tweet_user_id.append(tweet['retweeted_status']['user']['id_str'])
            rt_tweet_user_handle.append(tweet['retweeted_status']['user']['screen_name'])
        else:
            rt_tweet_id.append(None)
            rt_tweet_user_id.append(None)
            rt_tweet_user_handle.append(None)

    qt_tweet_id = []
    qt_tweet_user_id = []
    qt_tweet_user_handle = []
    qt_tweet_text = []

    for tweet in candidate_tweets:
        if 'quoted_status' in tweet:
            qt_tweet_id.append(tweet['quoted_status']['id_str'])
            qt_tweet_user_id.append(tweet['quoted_status']['user']['id_str'])  
            qt_tweet_user_handle.append(tweet['quoted_status']['user']['screen_name'])  
            qt_tweet_text.append(tweet['quoted_status']['full_text'])  
        else:
            qt_tweet_id.append(None)
            qt_tweet_user_id.append(None)
            qt_tweet_user_handle.append(None)
            qt_tweet_text.append(None)   

    df['rt_tweet_id'] = rt_tweet_id
    df['rt_tweet_user_id'] = rt_tweet_user_id
    df['rt_tweet_user_handle'] = rt_tweet_user_handle

    df['qt_tweet_id'] = qt_tweet_id
    df['qt_tweet_user_id'] = qt_tweet_user_id
    df['qt_tweet_user_handle'] = qt_tweet_user_handle
    df['qt_tweet_text'] = qt_tweet_text
    
    ###########################################
    ### Get Mentions
    all_mentions = []
    for tweet in candidate_tweets:
        mentions_list = []
        
        num_mentions = len(tweet['entities']['user_mentions'])

        for i in range(num_mentions):
            mention_object = tweet['entities']['user_mentions'][i]
            mentions_list.append(mention_object['screen_name'])
        
        if len(mentions_list)>0:
            all_mentions.append(mentions_list)
        else:
            all_mentions.append(None)
        
    df['mentions'] = all_mentions

    ###########################################
    ### Get Hashtags
    all_hashtags = []
    for tweet in candidate_tweets:
        hashtags_list = []
        
        num_hashtags = len(tweet['entities']['hashtags'])
        
        for i in range(num_hashtags):
            hashtags_object = tweet['entities']['hashtags'][i]
            hashtags_list.append(hashtags_object['text'])
        
        if len(hashtags_list)>0: 
            all_hashtags.append(hashtags_list)
        else: 
            all_hashtags.append(None)

    df['hashtags'] = all_hashtags
    
    return df




def set_date_mask(df):
    date_mask = df.created_at.dt.year == int(2021)
    
    df_date_mask = df[date_mask]
    
    return df_date_mask

    
def set_election_day_mask(df, post_election_day):
    post_election_datetime = datetime.strptime(post_election_day, '%Y-%m-%d %H:%M:%S')
    
    df['datetime'] = df['created_at'].apply(lambda x: datetime(x.year,x.month,x.day,x.hour,x.minute,x.second)) 
    
    election_day_mask = df['datetime'] < post_election_datetime
    
    df_election_mask = df[election_day_mask].reset_index()
    df_election_mask.drop(columns = ['index'], inplace = True)
    
    return df_election_mask
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
