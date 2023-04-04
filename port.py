import streamlit as st
import smtplib, ssl

st.set_page_config(layout="wide")
st.snow()

st.title("Hey!")
st.subheader("Syed Yousuf Naqvi")
st.text('Software Engineer')
st.text('Python Developer')


link='[Freelance Services](https://www.fiverr.com/syedyousuf90?up_rollout=true)'
st.sidebar.markdown(link,unsafe_allow_html=True)
linkedin='[LinkedIn](https://www.linkedin.com/feed/)'
st.sidebar.markdown(linkedin,unsafe_allow_html=True)





st.title('Data Science')

col1,col2,col3=st.columns(3)



with col1:
    st.subheader('Web Application')
    st.text(".Dashboards")
    st.text(".Blogs")
    st.text('.Business Showcasing Applications')


with col2:
    st.subheader('Machine Learning')
    st.text(".Classification (Image, Text, Tabular Dataset)")
    st.text(".Regression")
    st.text('.Sentiment Analysis')


cer1='[Analyze Data To Answer Question](https://www.coursera.org/account/accomplishments/certificate/E77PS649V7WZ)'
cer2='[Ask Questions to Make Data-Driven Decisions](https://www.coursera.org/account/accomplishments/certificate/E77PS649V7WZ)'
cer3='[Data Analysis with R Programming](https://www.coursera.org/account/accomplishments/certificate/7MPVJXGTGXCL)'
cer4='[Python and Statistics for Financial Analysis](https://www.coursera.org/account/accomplishments/certificate/KMBHZ3MUQ96U)'
cer5='[Process Data from Dirty to Clean](https://www.coursera.org/account/accomplishments/certificate/7NBYE56RDZK8)'
cer6='[Prepare Data for Exploration](https://www.coursera.org/account/accomplishments/certificate/JFLYKV9WNZ2T)'
cer7='[Foundations: Data, Data, Everywhere](https://www.coursera.org/account/accomplishments/certificate/LZYCGV2AKZU2)'


with col3:
    st.subheader('Certifications')
    st.markdown(cer1,unsafe_allow_html=True)
    st.markdown(cer2,unsafe_allow_html=True)
    st.markdown(cer3,unsafe_allow_html=True)
    st.markdown(cer4,unsafe_allow_html=True)
    st.markdown(cer5,unsafe_allow_html=True)
    st.markdown(cer6,unsafe_allow_html=True)
    st.markdown(cer7,unsafe_allow_html=True)
