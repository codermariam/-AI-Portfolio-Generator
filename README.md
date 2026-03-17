# ✨ AI Portfolio Generator

A Python-based AI tool that instantly turns a simple LinkedIn bio into a stunning, responsive, single-page HTML portfolio and a professional GitHub Profile `README.md`. 

Powered by **Google Gemini 2.5 Flash**, this tool features a clean **Streamlit** Web UI and built-in integration with the **GitHub API** to instantly deploy your generated portfolio to the web in seconds.

## 🚀 Features
- **AI-Powered Generation:** Leverages Gemini to craft compelling copy and premium design.
- **Modern UI:** The generated portfolio features a soft, elegant light-mode design with smooth gradients, modern typography, and CSS animations. 
- **Streamlit Interface:** A simple, interactive web app—no complex command line arguments needed.
- **One-Click Deployment:** Built-in integration with PyGithub allows users to input a Personal Access Token to automatically create a new repo and publish their portfolio.

## 🛠️ Tech Stack
- **Python 3**
- **Streamlit** for the frontend UI
- **Google GenAI SDK** for LLM interactions
- **PyGithub** for automatic deployments
- **python-dotenv** for secure API key management

## 💻 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/codermariam/-AI-Portfolio-Generator.git
   cd -AI-Portfolio-Generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Environment Variables**
   Create a `.env` file in the root directory and add your Google Gemini API key:
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```

4. **Run the Application**
   ```bash
   python -m streamlit run app.py
   ```

## 📸 How it Works
1. Launch the Streamlit app.
2. Paste your LinkedIn bio or professional summary into the text box.
3. Click "Generate" to preview your stunning HTML portfolio and markdown profile.
4. Input a GitHub Personal Access Token (with `repo` scope) to instantly deploy it to a live GitHub Pages site.

---
*Created as an exploration of LLM API integrations and automated deployment pipelines.*
