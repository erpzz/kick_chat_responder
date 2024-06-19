# First Ollama Python Bot
# From: Eric Paiz
import ollama
from kickScraper import Scraper

class Responder():

    scraper = Scraper()

   
    def artificialChatter(self, chat_messages):
        last_messaage = chat_messages[-1]
        ollama_response = ollama.generate(model='llama3:latest', prompt=f'Respond to the final message in the following array, behaving as if you were also a member of this chat: {last_messaage}')

        print(ollama_response)
