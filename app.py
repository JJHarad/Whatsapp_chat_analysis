import streamlit as st
from matplotlib import pyplot as plt
import seaborn as sns
import preprocessor
import helper

# Title of the Streamlit app
st.sidebar.title("WhatsApp Chat Analyzer")

# File uploader widget
uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:
    # Read the file and preprocess
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    # Display the dataframe
  #  st.dataframe(df)

    # Find unique users
    user_list = df['users'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")
    selected_user = st.sidebar.selectbox("Show Analysis with respect to", user_list)

    # Create button to show analysis
    if st.sidebar.button("Show Analysis"):
        num_messages, num_words , num_media_messages, num_links = helper.fetch_stats(selected_user, df)

        st.title("Top Statistics")
        # Display the results in columns
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(num_words)
        with col3:
            st.header("Media shared")
            st.title(num_media_messages)
        with col4:
            st.header("Links Shared")
            st.title(num_links)
#finding busiest user

        if selected_user == "Overall":
            st.title("Most Busy Users")
            x,new_df = helper.most_busy_users(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index,x.values, color = 'red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)

            # Most common words
            st.title("Most Common Words")
            most_common_df = helper.most_common_words(selected_user, df)
            col1, col2 = st.columns(2)  # This will equally split the screen into two columns

            with col1:  # to show the graph
                st.dataframe(most_common_df)

            with col2:  # to show the dataframe of the graph
                fig, ax = plt.subplots(figsize=(12, 10))  # Adjust the width and height here
                ax.barh(most_common_df[0], most_common_df[1])  # barh is a kind of horizontal plot
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

#Emoji Analysis

    emoji_df = helper.emoji_helper(selected_user, df)
    st.title("Emoji Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.dataframe(emoji_df)
    with col2:
        fig, ax = plt.subplots()
        ax.pie(emoji_df[1].head(7), labels=emoji_df[0].head(7), autopct="%0.2f")
        st.pyplot(fig)

#Monthly Timeline Analysis
    st.title("Monthly Timeline")
    timeline = helper.monthly_timeline(selected_user, df)
    fig,ax=plt.subplots()
    ax.plot(timeline['time'], timeline['messages'], color='green')
    plt.xticks(rotation='vertical')
    st.pyplot(fig)

#Daily Timeline Analysis
    st.title("Daily Timeline")
    d_timeline = helper.daily_timeline(selected_user, df)
    fig, ax = plt.subplots()
    ax.plot(d_timeline['only_date'], d_timeline['messages'], color='black')
    plt.xticks(rotation='vertical')
    st.pyplot(fig)

#Activity Analysis
    st.title("Activity Map")
    col1, col2 = st.columns(2)

    with col1:
        st.header("Most Busy Day")
        busy_day = helper.Weekly_activity(selected_user, df)
        fig,ax=plt.subplots()
        ax.bar(busy_day.index, busy_day.values)
        plt.xticks(rotation='vertical', color='green')
        st.pyplot(fig)

    with col2:
        st.header("Most Busy Month")
        busy_month = helper.Monthly_activity(selected_user, df)
        fig, ax = plt.subplots()
        ax.bar(busy_month.index, busy_month.values, color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

# Activity Heat Map
    st.title("Activity Heat Map")
    activity_heatmap=helper.Activity_heatmap(selected_user, df)
    fig, ax = plt.subplots()
    ax= sns.heatmap(activity_heatmap)
    st.pyplot(fig)