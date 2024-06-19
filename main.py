# From: Eric Paiz
from kickScraper import Scraper
from llamabot import Responder

def main():
    print("=========================================================================================================")
    print("Author:              yahboy")
    print("Project Title:       AutoChat")
    print("Purpose:             A tool that scrapes the kick chat of your choosing. Auto chat responder in works")  
    print("=========================================================================================================")
    chat_choice = input("Enter chat to scan: ")
    duration = float(input("How long do you want to scan?: "))
    scraper = Scraper()
    scraper.set_up()
    responder = Responder()
    # scraper.get_user_names(chat_choice, duration)
    scraper.get_messages(duration, chat_choice)
    scraper.driver.quit()
    #scraper.printMessages()
    #print(scraper.last_message)
    
    responder.artificialChatter(scraper.chat_messages)
    
if __name__ == "__main__":
    main()
