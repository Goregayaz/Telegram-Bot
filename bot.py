import telebot
import schedule
import time

TOKEN = '7685346273:AAGs6nNb1EeGEj4DZ-Elw-HfHvdse1vAErQ'
CHAT_ID = '-1004132248408'
LINK = 'https://docs.google.com/spreadsheets/d/179laJfTQ_5sGZx6xS3n7BlQmqYt6MbPQ-pHwnNAgCuU/edit?usp=sharing'

bot = telebot.TeleBot(TOKEN)

def send_link():
    bot.send_message(CHAT_ID, LINK)

schedule.every().day.at("10:00").do(send_link)

while True:
    schedule.run_pending()
    time.sleep(1)