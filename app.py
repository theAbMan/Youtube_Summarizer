#---Importing Libraries---#

import streamlit as st
from dotenv import load_dotenv
import os
import base64
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
import time

###########################################################################

#---CONSTANTS---#

LOGO_IMAGE = "images/images.png"
PROMPT = """You are a Youtube video summarizer. You will be taking the trabnscript text 
and summarizing the entire video and providing the important summary in points within 250 words.
Please provide the summary of the text given here: """

###########################################################################


#---CONFIGURATIONS---#

load_dotenv()
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
st.set_page_config(page_title="Summarizer",layout='wide')
st.markdown(
    """
    <style>
    .container {
        display: flex;
        justify-content: center;
        
        margin-top: 2px;
    }
    .logo-text {
        font-weight:700 !important;
        font-size:70px !important;
        color: #000000!important;
        padding-top: 20px !important;
    }
    .logo-img {
        float:right;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
        <p class="logo-text">CONTENT SUMMARIZER</p>
    </div>
    """,
    unsafe_allow_html=True
)
col1, col2 = st.columns(2)

############################################################################

#---Function to generate content from Gemini---#

def generate_gemini_content(transcript_text,PROMPT):

    model = genai.GenerativeModel("gemini-1.5-flash-latest")
    response = model.generate_content(PROMPT+transcript_text)
    return response.text

############################################################################


#---Function to extract transcript from Youtube Videos---#

def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript =""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript
    except Exception as e:
        raise e
############################################################################


#---Function to display the output as a stream---# 

def stream_data(summary):
    for word in summary.split(" "):
        yield word + " "
        time.sleep(0.02)
    
############################################################################


#---Main Function---#

def main():
    with col1:
        youtube_link = st.text_input("Enter Youtube Video Link")

        if youtube_link:
            video_id = youtube_link.split("=")[1]
        

        if st.button("GET SUMMARY"):
            with col2:
                st.subheader("VIDEO THUMBNAIL", divider='grey')
                st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width = True)
            transcript_text = extract_transcript_details(youtube_link)

            if transcript_text:
                with st.spinner('Watching the video.Plese wait..'):
                    summary = generate_gemini_content(transcript_text,PROMPT)            
                    st.subheader("CONTENT SUMMARY", divider='grey')
                    st.write_stream(stream_data(summary))

############################################################################


if __name__ == "__main__":
    main()