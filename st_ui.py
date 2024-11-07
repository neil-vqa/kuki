import streamlit as st
from kuki.core import stt_model

st.set_page_config(page_title="Kuki | Simple Speech-to-Text App", layout="wide")
st.markdown(
    """
    <style>
        .reportview-container {
            margin-top: 0;
        }
        #MainMenu {display:none;}
        .stAppDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
        .stAppHeader {display:none;}
        code {white-space: pre-wrap !important;}
    </style>
""",
    unsafe_allow_html=True,
)


def transcribe_transaction(audio_value):
    transcript = ""
    with st.spinner("Transcribing..."):
        segments, _ = stt_model.transcribe(audio_value)
        for s in segments:
            transcript = f"{transcript} {s.text}"

    return transcript


audio_value = st.audio_input("Record")

transcript = ""
if audio_value:
    transcript = transcribe_transaction(audio_value)
    st.code(f"{transcript}", language="md")
