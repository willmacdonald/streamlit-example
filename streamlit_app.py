import streamlit as st
import os
import openai

topics = "Here is some bicycle terminology that is often confused conflated or straight up mangled. This is all in good fun, as I probably make more mistakes than the average YouTuber. It's also worth nothing that I don't care what you call anything and rarely correct anyone, except when they call a damper a dampener. That is yucky."

def generate(topics):
    openai.api_key =  "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"
    openai.organization = "org-ZXIgSEZAnove37o1egimi8P8"

    response = openai.Image.create(
        prompt=topics,
        n=1,
        size="256x256",
        )
    return {
        response["data"][0]["url"]
    }

st.image(generate(topics))
