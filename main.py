import os
from dotenv import load_dotenv
from google import genai
import prompts

# Load environment variables
load_dotenv()

# Ensure we have the API key
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY or API_KEY == "your_gemini_api_key_here":
    print("Error: Please set your GEMINI_API_KEY in the .env file.")
    exit(1)

# Initialize the Gemini Client
client = genai.Client(api_key=API_KEY)

def generate_portfolio(bio):
    print("Generating your portfolio... Please wait.")
    
    # Generate README
    print("\nGenerating README.md...")
    readme_response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=f"{prompts.README_PROMPT}\n\nUser Bio:\n{bio}",
    )
    readme_content = readme_response.text
    
    # Generate HTML Portfolio
    print("Generating HTML Portfolio...")
    html_response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=f"{prompts.HTML_PROMPT}\n\nUser Bio:\n{bio}",
    )
    html_content = html_response.text

    # Save to files if running locally
    os.makedirs("output", exist_ok=True)
    
    cleaned_readme = readme_content.replace('```markdown', '').replace('```', '').strip()
    cleaned_html = html_content.replace('```html', '').replace('```', '').strip()

    with open("output/README.md", "w", encoding="utf-8") as f:
        f.write(cleaned_readme)

    with open("output/index.html", "w", encoding="utf-8") as f:
        f.write(cleaned_html)

    print("\nSuccess! Your portfolio files have been generated in the 'output' folder.")
    return cleaned_readme, cleaned_html

if __name__ == "__main__":
    print("=== AI Portfolio Generator ===")
    print("Paste your LinkedIn bio below (press Enter, then Ctrl+Z on Windows or Ctrl+D on Mac/Linux, then Enter to finish):")
    
    import sys
    bio_lines = sys.stdin.readlines()
    bio_input = "".join(bio_lines).strip()

    if not bio_input:
        print("Error: No bio provided.")
        exit(1)

    generate_portfolio(bio_input)
