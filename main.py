from telegram.ext import Updater

def main():
    myBot = Updater('')

    myBot.start_polling()
    
main()
