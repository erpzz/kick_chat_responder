To install the dependencies needed for this program to run:
    pip install -r requirements.txt

Project Overview:
-----------------
This project, AutoChat, is designed to scrape chat messages from a specified chat room on Kick and generate automated responses using the Ollama API. The main components are:

1. `kickScraper.py` - This script contains the Scraper class, which handles setting up the browser, navigating to the chat room, and collecting messages.
2. `llamabot.py` - This script contains the Responder class, which generates responses to the collected chat messages using the Ollama API.
3. `main.py` - This is the entry point of the project. It prompts the user for input, initiates the scraping process, and handles the interaction between the Scraper and Responder classes.

Instructions:
-------------
1. Ensure you have ChromeDriver installed and accessible in your PATH or provide its path in the `set_up` method of the Scraper class.
2. Run the `main.py` script to start the program.
