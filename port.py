import streamlit as st
import smtplib, ssl

st.set_page_config(layout="wide")
st.snow()

st.title("Hey:exclamation:")
st.subheader("Syed Yousuf Naqvi")
st.text('Software Engineer')
st.text('Python Developer')

with st.sidebar.expander("Any Thing For Me :question:"):
    link='[Freelance Services](https://www.fiverr.com/syedyousuf90?up_rollout=true)'
    st.markdown(link,unsafe_allow_html=True)
    linkedin='[LinkedIn](https://www.linkedin.com/feed/)'
    st.markdown(linkedin,unsafe_allow_html=True)





with st.expander("There is something you need to see:eyes:"):
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

col4,col5,col6=st.columns(3)
with col4:
    with st.expander('Web Application Frameworks:spider:'):
        st.write(".Flask")
        st.write(".Streamlit")
        st.write(".Dash Plotly")


with col5:
    with st.expander('Data Science Frameworks/BI Tools:notebook::panda_face::chart:'):
        st.write(".Pandas")
        st.write(".Numpy")
        st.write(".Power BI")
        st.write(".Matplotlib")
        st.write(".Seaborn")
        st.write(".PlotlyExpress")
        st.write(".Jupyter Notebook")


with col6:
    with st.expander('ERP Systems:man_in_business_suit_levitating:'):
        st.write(".SAP B1")
        st.write(".Odoo")


col7,col8,col9=st.columns(3)
with col7:
    with st.expander('Databases:file_folder:'):
        st.write(".SQL SERVER")
        st.write(".MySQL")
        st.write(".SQL Hana")
        st.write(".MongoDB")

with col8:
    with st.expander('Web Scrapping:spider:'):
        st.write(".Beautiful Soup")
        st.write(".Scrapy")
        st.write(".Selenium")

with col9:
    with st.expander('More:heavy_plus_sign:'):
        st.write(".Requests")
        st.write(".OpenCV")
        st.write(".Twilio")
