import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

st.set_page_config(page_title="My Webpage",page_icon=":tada:",layout='wide')
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css(r"C:\Users\KIIT\Desktop\Streamlit\Ref\style\style.css")
img_temp=Image.open(r'C:\Users\KIIT\Desktop\Streamlit\Ref\images\Temp.png')
img_net=Image.open(r"C:\Users\KIIT\Desktop\Streamlit\Ref\images\Netflix.png")
img_port=Image.open(r"C:\Users\KIIT\Desktop\Streamlit\Ref\images\Portfolio.png")
lottie_coding=load_lottieurl("https://lottie.host/1aa6bafd-8d13-4bcc-bf26-7b1a587e49cd/x4HC0OGULC.json")


st.subheader("Hi, I am Sankhadip :wave:")
st.title("A Computer Science student from India")
st.write("I am passionate about AI & ML and finding ways to use Python to be more efficient and effective settings.")
st.write("[LinkedIn >](https://www.linkedin.com/in/sankhadiproy861/)")

with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("About Me: ")
        
        st.write(
            '''
I'm Sankhadip, a second-year CSE undergrad at KIIT University, Bhubaneswar. I have learned the fundamentals of C and JAVA programing language. My area of interest is in Full Stack Web Development. I have completed the Frontend part of Web Development. Now I try to implement those knowledge through making different projects and also try to gain more knowledge through those projects.'''
        )

with right_column:
    st_lottie(lottie_coding,height=250,key="coding")

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column,text_column=st.columns((1,2))
    with image_column:
        st.image(img_temp)
    with text_column:
        st.subheader("Temperature Converter")
        st.write('''Designed and developed a user-friendly
Temperature Converter website to provide
seamless conversion between different
temperature units. The project aimed to
offer a practical and accessible tool for
users to convert temperatures effortlessly
'''
        )
        st.markdown('[Visit>]( https://ray-stack-create.github.io/Temperature-converter/)')
    image_column,text_column=st.columns((1,2))
    with image_column:
        st.image(img_net)
    with text_column:
        st.subheader("Netflix Homepage")
        st.write('''Developed a responsive and visually
appealing Netflix home page replica using
HTML and CSS. This project aimed to
recreate the iconic Netflix interface,
showcasing proficiency in front-end
development and design.''')
        st.markdown('[Visit>]( https://ray-stack-create.github.io/netflix-home/)')

    image_column,text_column=st.columns((1,2))
    with image_column:
        st.image(img_port)
    with text_column:
        st.subheader("Portfolio Website")
        st.write('''Designed and developed a personal
portfolio website to showcase my skills,
projects, and professional background. The
website serves as a digital resume and
interactive platform for potential
employers and collaborators to learn more
about my expertise.''')
        st.markdown('[Visit>](https://ray-stack-create.github.io/portfolio/)')





with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form="""
<form action="https://formsubmit.co/sankhadiproy8@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name ="message" placeholder="your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""

left_column,right_column=st.columns(2)
with left_column:
    st.markdown(contact_form,unsafe_allow_html=True)
with right_column:
    st.empty()