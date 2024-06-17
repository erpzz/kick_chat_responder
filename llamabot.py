# First Ollama Python Bot
# From: Eric Paiz
import ollama
from kickScraper import Scraper

class Responder():

    scraper = Scraper()

    def question():
        question = input("Enter question: ")
        ollama_response = ollama.chat(model='llama3:latest', messages=[
            {
                'role': 'system',
                'content': 'You are a fellow chatter in the chat room. Respond to the last message in the chat_messages array.',
                
            },
            {
                'role': 'user',
                'content': question
            },
        ])
    def artificialChatter():
        ollama.generate(model='llama3:latest', prompt=f'Respond to the final message in the following array, behaving as if you were also an unhinged member of this chat: {scraper.chat_messages}')

       #print(ollama_response['message']['content'])
