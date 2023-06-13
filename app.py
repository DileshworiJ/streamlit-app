from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/

st.set_page_config(page_title='Dileshwori Joshi',page_icon=":tada",layout='wide')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
     with open(file_name) as f:
          st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

#Load Assets
lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_pwPfN3fri7.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# Header Section

with st.container(): 
    st.subheader("Hi, I am Dileshwori :wave:")
    st.title("An Aspiring Data Analyst.")
    st.write("I am passionate about finding ways to make things simpler and clearer.")
    st.write("[Learn More>](https://python.com)")

#what I do
with st.container():
    st.write("...")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write(
            """
            I love working on data:
                - Working on machine learning technologies
            """
        )
        st.write("[GitHub >](https://github.com/DileshworiJ)")
    with right_column:
        st_lottie(lottie_coding, height=300, key = "coding")


#projects
with st.container():
    st.write("----")
    st.header("My Projects")
    st.write("##")
    image_column, text_column =st.columns((1, 2))
    with image_column:
        #insert image
        st.image(img_lottie_animation)
    with text_column:
            st.subheader("First Project")
            st.write(
                """
                Learn how to use Lottie Files in Streamlit!
                Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do i
                In this tutorial, I'll show you exactly how to do it 
                """
            )
            st.markdown("[Watch video...](https://www.linkedin.com/in/dileshwori-joshi-16515a162/)")

with st.container():
    image_column, text_column =st.columns((1, 2))
    with image_column:
        #insert image
        st.image(img_lottie_animation)
    with text_column:
            st.subheader("Second Project")
            st.write(
                """
                Learn how to use Lottie Files in Streamlit!
                Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do i
                In this tutorial, I'll show you exactly how to do it 
                """
            )
            st.markdown("[Watch video...](https://www.linkedin.com/in/dileshwori-joshi-16515a162/)")


### contact
with st.container():
     st.write("...")
     st.header("Get in touch with me!")
     st.write("##")

     # Documentation: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!

     contact_form = """
     <form action="https://formsubmit.co/jdileshwori@email.com" method="POST">
        <input type = "hidden" name = "_captcha" value = "false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder = "Your Message here" required></textarea>
        <button type="submit">Send</button>
    </form>
     """

     left_column, right_column = st.columns(2)
     with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
     with right_column:
        st.empty()