def fetch_stats(selected_user, df):
    if selected_user == 'Overall':
        # Number of messages
        num_messages = df.shape[0]
        # Number of words
        words = []
        for message in df['messages']:
            words.extend(message.split())
        return num_messages, len(words)

    else:
        new_df = df[df['users'] == selected_user]
        num_messages = new_df.shape[0]
        words = []
        for message in new_df['messages']:
            words.extend(message.split())
        return num_messages, len(words)
