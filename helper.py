from urlextract import URLExtract
extract = URLExtract()
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