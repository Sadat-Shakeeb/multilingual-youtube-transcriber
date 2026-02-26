import streamlit as st
import os
import time
from utils.downloader import download_audio
from utils.transcriber import transcribe_audio
from utils.romanizer import convert_to_roman_urdu

st.set_page_config(
    page_title="Roman Urdu Transcriber",
    page_icon="🎧",
    layout="centered"
)

# -------------------------------
# Header Section
# -------------------------------

st.markdown(
    """
    <h1 style='text-align: center;'>🎥 YouTube → Roman Urdu Converter</h1>
    <p style='text-align: center; font-size:18px;'>
    Convert <b>Urdu</b> or <b>English</b> YouTube videos into Roman Urdu text
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

st.info(
    "Supports Urdu and English YouTube videos.\n\n"
    "Perfect for users who prefer Roman Urdu instead of Urdu script."
)

# -------------------------------
# Input Section
# -------------------------------

url = st.text_input("🔗 Paste YouTube URL here")

convert_btn = st.button("🚀 Convert to Roman Urdu")

st.markdown("---")

# -------------------------------
# Processing Logic
# -------------------------------

if convert_btn:

    if not url:
        st.error("Please enter a valid YouTube URL.")
        st.stop()

    status_placeholder = st.empty()

    try:
        # Step 1: Download
        with st.spinner("📥 Downloading audio from YouTube..."):
            audio_path = download_audio(url)
            time.sleep(1)

        status_placeholder.success("✅ Audio Downloaded Successfully")

        # Step 2: Transcription
        with st.spinner("📝 Transcribing audio (Speech → Text)..."):
            text, detected_lang = transcribe_audio(audio_path)
            time.sleep(1)

        st.info(f"🌍 Detected Language: **{detected_lang.upper()}**")

        if detected_lang not in ["ur", "en"]:
            st.error("❌ Only Urdu and English audio are supported.")
            os.remove(audio_path)
            st.stop()

        # Step 3: Roman Conversion
        with st.spinner("🔄 Converting to Roman Urdu using AI..."):
            roman_text = convert_to_roman_urdu(text, detected_lang)
            time.sleep(1)

        st.success("🎉 Conversion Completed Successfully!")

        st.markdown("---")

        # -------------------------------
        # Output Section
        # -------------------------------

        st.subheader("📄 Roman Urdu Transcript")

        st.text_area(
            label="Output",
            value=roman_text,
            height=300
        )

        st.download_button(
            label="⬇️ Download Transcript (.txt)",
            data=roman_text,
            file_name="roman_urdu_transcript.txt",
            mime="text/plain"
        )

        # Cleanup
        if os.path.exists(audio_path):
            os.remove(audio_path)

    except Exception as e:
        st.error(f"⚠️ An error occurred: {str(e)}")

# -------------------------------
# Footer
# -------------------------------

st.markdown("---")
st.markdown(
    """
    <div style='text-align:center; font-size:14px; color:gray;'>
    Built using Whisper + Gemini AI | Multilingual Speech Processing Project
    </div>
    """,
    unsafe_allow_html=True
)