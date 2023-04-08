    
def tweets(term:str):
    import snscrape.modules.twitter as sntwitter
    import pandas as pd
    
    # Creating list to append tweet data 
    tweets_list1 = []
    
    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('{}'.format(term)).get_items()): #declare a username 
        if i>1000: #number of tweets you want to scrape
            break
        tweets_list1.append([ tweet.content, tweet.user.username]) #declare the attributes to be returned
        
    # Creating a dataframe from the tweets list above 
    tweets_df1 = pd.DataFrame(tweets_list1, columns=['Text', 'Username'])
    return tweets_df1.head()
print(tweets('lyanna'))