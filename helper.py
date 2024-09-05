from urlextract import URLExtract
from wordcloud import WordCloud
extract = URLExtract()
import pandas as pd
from collections import Counter
def fetch_stats(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['users'] == selected_user]

    # Number of messages
    num_messages = df.shape[0]

    # Number of words
    words = []
    for message in df['messages']:  # Ensure 'messages' is the correct column name
        words.extend(message.split())

    # Number of media messages
    num_media_messages = df[df['messages'] == '<Media omitted>\n'].shape[0]  # Adjust string as needed

    #fetch number of links shared
    links = []
    for message in df['messages']:
        links.extend(extract.find_urls(message))


    return num_messages, len(words), num_media_messages, len(links)

def most_busy_users(df):
    x = df['users'].value_counts().head()
    df=round((df['users'].value_counts() / df.shape[0])*100 , 2).reset_index().rename(columns={'index':'name', 'user':'percentage'})
    #reset_index() is used to convert the data into dataframe
    return x,df

#Function to find most common words
def most_common_words(selected_user, df):

    f=open('stop_hinglish.txt','r')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['users']==selected_user]

    temp=df[df['users']!='group_notification']
    temp=temp[temp['messages']!='<Media omitted>\n']

    words =[]

    for message in temp['messages']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df
