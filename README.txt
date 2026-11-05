GREATDEVMASTER PORTFOLIO
========================

PROJECT CONTENTS
- templates/index.html : website structure (HTML)
- static/style.css     : dark responsive styling (CSS)
- static/script.js     : navigation, animations and contact form (JavaScript)
- app.py               : Python Flask backend and contact API
- schema.sql           : SQL table definition
- requirements.txt     : Python packages

RUN LOCALLY
1. Install Python 3 on your computer.
2. Open a terminal in this Greatdevmaster folder.
3. Install dependencies:
      python -m pip install -r requirements.txt
4. Start the website:
      python app.py
5. Open this address in your browser:
      http://127.0.0.1:5000

The first run creates greatdevmaster.db automatically.
Contact form messages are saved in that SQLite database.

IMPORTANT
- This project is a working starter portfolio, not yet deployed online.
- Replace the sample email and project concepts with your own real details.
- The skill bars are placeholders; adjust them honestly.
- For public deployment, turn off Flask debug mode and configure a production
  server, secret configuration, HTTPS and a managed database.
