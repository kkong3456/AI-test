# from dotenv import load_dotenv
import streamlit as st 
import time

# load_dotenv()


st.title('인공지능 시인')
content = st.text_input("시의 주제를 제시해 주세요", "")
# result=chat_model.predict(content+'에 대한 시를 써죠')

st.write("시의 주제는", content)

if st.button("시 작성 요청하기"):
    with st.spinner('Wait for it...'):
        time.sleep(5)
        st.write("시")
