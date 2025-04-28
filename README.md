# Discreet Writing Streamlit App

## Setup
1. Clone this repo:
   ```bash
   git clone https://github.com/<YOUR_USERNAME>/discreet-writing-app.git
   cd discreet-writing-app
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate   # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file and add your OpenAI API key:
   ```bash
   echo "OPENAI_API_KEY=your_key_here" > .env
   ```
5. Run locally:
   ```bash
   streamlit run app.py
   ```

## Deploy to Streamlit Cloud
1. Push your code to GitHub:
   ```bash
   git add .
   git commit -m "Initial Streamlit app"
   git push origin main
   ```
2. Go to https://share.streamlit.io, log in and select your repo.
3. Set the environment variable `OPENAI_API_KEY` in the Streamlit Cloud UI.
4. The app will auto-deploy. Enjoy!
