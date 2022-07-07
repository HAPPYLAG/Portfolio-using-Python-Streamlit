import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
st.set_page_config(page_title="My Webpage",page_icon=":tada:",layout="wide")

def load_lottieur1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
#.......load assets from lottee pip install streamlit-lottee or download pip install requests coding---  
lottie_coding =load_lottieur1("https://assets9.lottiefiles.com/packages/lf20_hcwpcdew.json")
img_contact_form = Image.open("images\maxresdefault.jpg")
img_contact_form = Image.open("images\maxresdefault.jpg")

# Use add local CSS  
def local_css(style):
    with open(style) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css('style\style.css')

#.....header section
with st.container():
    st.subheader("Hi!I am Haris :wave:")
    st.subheader("A Data Analyst From Lahore,Pakistan.")
    st.header("01 PROFILE")
    st.write("Accomplished Data Science with a passion for delivering valuable data through analytical functions and data retrieval methods. Committed to helping companies advance by helping them to develop strategic plans based on predictive modeling and findings. Bringing forth a proven track record of analyzing complex data sets and serving as a strong advisor.")
    st.write("[linkedin](https://www.linkedin.com/in/haris-shahbaz-0433a91a5/)") 
    st.write("[github](https://github.com/HAPPYLAG)")



#........what i do
with st.container():
    st.write("--")
    left_column,right_column = st.columns(2)
    with left_column:
        st.header("02 EMPLOYMENT HISTORY")
        st.subheader("Mar 2022 — Apr 2022")
        st.subheader("Lahore")
        st.subheader("Data Analyst At Globalshala")
        #st.write("At Saint Louis University Virtual Internship Program:Week 1: Access the data from the Marketing team,• Analyze the data. Week 2: Refining Visualization.• Design. Week 3: Create a presentation.• Export our presentation Week 4: Present our presentation at Saint Louis University.• Final Report Thing's i have learned at this internship 1. Data analysis phases or steps: 1- ask 2- prepare 3- process 4- analyze 5- share 6- act Following them should result in a frame that makes decision-making and problem solving a little easier. 2. How data analysis i have done in it? Step One: Ask The Right Questions. Step Two: Data Collection. Step Three: Data Cleaning. Step Four: Analyzing The Data. Step Five: Interpreting The Results.")
        st.write("##")
        st.write(

         
            """
At Saint Louis University Virtual Internship Program:

 Week 1: Access the data from the Marketing team

 • Analyze the data.

 Week 2: Refining Visualization.

 • Design.

 Week 3: Create a presentation.

 • Export our presentation

 Week 4: Present our presentation at Saint Louis University.

 • Final Report

Thing's i have learned at this internship

Data analysis phases or steps:

  1- ask

  2- prepare

  3- process

  4- analyze

  5- share

  6- act

Following them should result in a frame that makes decision-making and problem 
solving a little easier.

2. How data analysis i have done in it? 

 1: Ask The Right Questions.

 2: Data Collection.

 3: Data Cleaning.

 4: Analyzing The Data.

 5: Interpreting The Results.

            """
        )
        st.write("[Learn More](https://github.com/HAPPYLAG)")
with right_column:
    st_lottie(lottie_coding,height=300,key="coding")

#.....projects........

with st.container():
    st.write("--")
    st.header("My Projects")
    st.write("##")
    image_column,text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Integrate lottie animations inside your streamlit app")
        st.write(

            """
            sjdkasdsajasfakjhfhgafhsajkdhaskdhsajdksajdlksajdlsajdkjsadljsdjj
            hjdsadjkhasdkhsakdhashdksahdkjhaskdhakshdahdhasdhkahdkjashskhsakjd
            dhaksjdhkjshdhdjkhsakjdhasjkdhkjsahdkjahdkahdashkd
            hasdkhaskdhksahdkjahkd.
            
            """

        )
with st.container():
    st.write("--")
    #st.header("My Projects")
    st.write("##")
    image_column,text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("how to add 2nd image lottie animations inside your streamlit app")
        st.write(
            """
            sjdkasdsajasfakjhfhgafhsajkdhaskdhsajdksajdlksajdlsajdkjsadljsdjj
            hjdsadjkhasdkhsakdhashdksahdkjhaskdhakshdahdhasdhkahdkjashskhsakjd
            dhaksjdhkjshdhdjkhsakjdhasjkdhkjsahdkjahdkahdashkd
            hasdkhaskdhksahdkjahkd.
            
            """
        )

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://www.linkedin.com/in/haris-shahbaz-0433a91a5/" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()