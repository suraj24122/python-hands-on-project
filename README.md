🐍 Python Mini Projects
This repository contains three beginner-friendly Python projects built for fun and learning:

PDF Merger Tool – Combine multiple PDF files into a single document.

News Fetcher App – Retrieve and display the latest news articles using NewsAPI.

Who Wants to Be a Millionaire (CLI Game) – A simple command-line quiz game based on the famous TV show.

📁 Projects Overview
1. 📎 PDF Merger
File: pdf_merger.py

Description:
This script takes multiple PDF file names from the user and merges them into a single PDF file called merged-pdf.pdf.

How to Run:

bash
Copy
Edit
python pdf_merger.py
Requirements:

PyPDF2 (Install using pip install PyPDF2)

2. 📰 News Fetcher App
File: news app.py

Description:
Fetches the latest news articles based on a user’s query using the NewsAPI.

Note: The script is currently commented out. You’ll need to:

Uncomment the code

Replace the API key (api = "your_api_key")

Install the requests module (pip install requests)

How to Run:

bash
Copy
Edit
python "news app.py"
3. 🎮 Millionaire Quiz Game
File: millionare.py

Description:
A command-line trivia quiz game where the player answers multiple-choice questions. Each correct answer awards a higher prize.

How to Run:

bash
Copy
Edit
python millionare.py
📌 Requirements
Install all required packages using:

bash
Copy
Edit
pip install -r requirements.txt
Or manually install as needed:

PyPDF2

requests (for News App)

💡 Suggestions for Improvement
Add GUI using Tkinter or PyQt for PDF Merger.

Store user scores in a file or database for the Millionaire game.

Allow category and date filtering in the News App.

📜 License
This project is open-source and available under the MIT License.
