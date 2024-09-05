import streamlit as st
import preprocessor
st.sidebar.title("Whatsapp chat analyser")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)
    st.dataframe(df)

    # find unique user
    user_list = df['users'].unique().tolist()
    selected_user = st.sidebar.selectbox("Show Analysis wrt", user_list)