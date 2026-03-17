import streamlit as st
import os
from dotenv import load_dotenv

# Load our generator function
from main import generate_portfolio
from github_deploy import deploy_to_github

# Load env in case API key is there
load_dotenv()

st.set_page_config(page_title="AI Portfolio Generator", page_icon="✨", layout="wide")

st.title("✨ AI Portfolio Generator")
st.markdown("Instantly generate a premium, single-page HTML portfolio and a GitHub README.md using your LinkedIn Bio.")

# Ensure we have the Gemini API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key or api_key == "your_gemini_api_key_here":
    st.error("Missing Gemini API Key. Please add GEMINI_API_KEY to your .env file or the environment.")
    st.stop()

# --- INPUT SECTION ---
st.header("Step 1: Your Profile details")
bio_input = st.text_area("Paste your LinkedIn Bio or professional summary here:", height=200, 
                         placeholder="I am a highly motivated Frontend Developer with 3 years of experience in React, Next.js...")

if "readme" not in st.session_state:
    st.session_state.readme = None
if "html" not in st.session_state:
    st.session_state.html = None

generate_clicked = st.button("Generate Portfolio", type="primary")

if generate_clicked:
    if not bio_input.strip():
        st.warning("Please enter your bio first.")
    else:
        with st.spinner("Generating your professional portfolio..."):
            try:
                # Call our core logic
                readme_content, html_content = generate_portfolio(bio_input)
                
                # Store in session state so it doesn't disappear on re-renders
                st.session_state.readme = readme_content
                st.session_state.html = html_content
                st.success("Successfully generated!")
            except Exception as e:
                st.error(f"Error generating portfolio: {e}")

# --- PREVIEW SECTION ---
if st.session_state.html and st.session_state.readme:
    st.header("Step 2: Preview")
    
    tab1, tab2 = st.tabs(["HTML Website Preview", "README.md Preview"])
    
    with tab1:
        st.components.v1.html(st.session_state.html, height=600, scrolling=True)
        st.download_button("Download index.html", data=st.session_state.html, file_name="index.html", mime="text/html")
        
    with tab2:
        st.markdown(st.session_state.readme)
        st.download_button("Download README.md", data=st.session_state.readme, file_name="README.md", mime="text/markdown")

    # --- DEPLOYMENT SECTION ---
    st.header("Step 3: Deploy to GitHub")
    st.markdown("Automatically push this to a new GitHub repository so it's live on the web!")
    
    with st.expander("Deployment Settings", expanded=True):
        st.info("You need a GitHub Personal Access Token (classic) with `repo` scope to use this feature.")
        
        gh_token = st.text_input("GitHub Personal Access Token:", type="password")
        gh_repo_name = st.text_input("Repository Name:", value="my-ai-portfolio")
        
        if st.button("Deploy to GitHub"):
            if not gh_token or not gh_repo_name:
                st.warning("Please provide both the token and the repository name.")
            else:
                with st.spinner("Deploying to GitHub..."):
                    success, message = deploy_to_github(
                        gh_token, 
                        gh_repo_name, 
                        st.session_state.readme, 
                        st.session_state.html
                    )
                    
                    if success:
                        st.success(message)
                        st.balloons()
                    else:
                        st.error(message)
