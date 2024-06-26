To install the dependencies needed for this program to run:
    pip install -r requirements.txt
    (So far the requirements.txt only includes the dependencies for the Selenium based Kick chat scraper, but does not yet include the other dependencies such as ollama)

Project Overview:
-----------------
This project, AutoChat, is designed to scrape chat messages from a specified chat room on Kick and generate automated responses using the Ollama API. The main components are:

1. `kickScraper.py` - This script contains the Scraper class, which handles setting up the browser, navigating to the chat room, and collecting messages.
    Note - Currently, I am in the middle of refactoring the Scraper portion of the program. Rather than using the Selenium based scraper I wrote, the next iteration which I am working on interacts with an open websocket that the kick chat uses. The Selenium based scraper will be replaced by a parser, which will parse the json objects pulled from the chat using the websocket connection that this program will establish. 

    This will provide several benefits: 
        - It will be faster, more responsive
        - Can easily run in perpetuity
        - Doesn't risk the same issues I usually see with front-end Selenium scrapers that will interact with the website directly such as rate limiting or straight up having some requests IP banned. 
2. `llamabot.py` - This script contains the Responder class, which generates responses to the collected chat messages using the Ollama API.
3. `main.py` - This is the entry point of the project. It prompts the user for input, initiates the scraping process, and handles the interaction between the Scraper and Responder classes.

Instructions:
-------------
1. Ensure you have ChromeDriver installed and accessible in your PATH or provide its path in the `set_up` method of the Scraper class.
2. Run the `main.py` script to start the program.
