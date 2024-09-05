import streamlit as st
import preprocessor,helper
st.sidebar.title("Whatsapp chat analyser")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)
    st.dataframe(df)

    # find unique user
    user_list = df['users'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall")
    selected_user = st.sidebar.selectbox("Show Analysis wrt", user_list)

    #create button
    if st.sidebar.button("show analysis"):
        num_messages = helper.fetch_stats(selected_user,df)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Total Messages")
            st.title(num_messages)
