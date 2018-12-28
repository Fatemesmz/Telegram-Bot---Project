import telepot
from gtts import gTTS
import time
import urllib3
import telegram
from translate import Translator

bot = telepot.Bot('631626465:AAGcBLbqNmjM50pH3sh-J-NbjUfP8wSCt7A')


def handle(msg):
  content_type, chat_type, chat_id= telepot.glance(msg)
  print(content_type, chat_type, chat_id)
    
  	
  if content_type == 'text':
    Text=msg["text"].lower()

    if Text=='/start':
      bot.sendMessage(chat_id, f'Hello {msg["chat"]["first_name"]}\nWelcome to the bot.\nThis bot can change your English texts into voice with translation.\nEnjoy! ')

    else:
      bot.sendChatAction(chat_id, "upload_audio")
      tts=gTTS(text=Text)
      tts.save(f'\{msg["date"]}.ogg')
      bot.sendVoice(chat_id, voice=open(f'\{msg["date"]}.ogg', 'rb'))

      bot.sendChatAction(chat_id, "typing")
      translator= Translator(to_lang="fa")
      translation = translator.translate(Text)
      bot.sendMessage(chat_id,translation)

  else:
    bot.sendMessage(chat_id, "Please only enter text for translating and pronouciation.")
 

#main :
        
bot.message_loop(handle)

print ('Bot\'s waiting for user to send a text...')

# Keep the program running.
while 1:
    time.sleep(10)
