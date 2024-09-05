import streamlit as st
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
    st.dataframe(df)

    # Find unique users
    user_list = df['users'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")
    selected_user = st.sidebar.selectbox("Show Analysis with respect to", user_list)

    # Create button to show analysis
    if st.sidebar.button("Show Analysis"):
        num_messages, num_words , num_media_messages, num_links = helper.fetch_stats(selected_user, df)

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
