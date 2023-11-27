from telegram.ext import *
import keys
from datetime import datetime

print('Starting the bot...')

def start_command(update, context):
    update.message.reply_text('Hello, there! Thanks for chatting with me! I\'m Vasu! Nice to Meet You!')
    
def help_command(update, context):
    update.message.reply_text('Try typing anything and i will responde!')
    
def custom_command(update, context):
    update.message.reply_text('This is custom command!')
    
def handle_response(text: str) -> str:
    current_time = datetime.now()
    if 'hello' in text:
        return 'Hey there!'
    
    if 'which time is it now?' in text:
        return f'The current time is: {current_time.strftime("%Y-%m-%d %H:%M:%S")}'
    
    if 'how are you' in text:
        return 'I am fine. Thank You.'
    
    if 'which day is it today?' in text:
        return f'Today is {current_time.strftime("%A")}'
    
    if 'I love python' or 'i like python' in text:
        return f'Dont forget to subscribe PythonWithVasu channel'
    
    return 'I dont know!'

def handle_message(update, context):
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''
    
    print(f'User ({update.message.chat.id}) says "{text} in: {message_type}"')
    
    if message_type == 'group':
        if '@python_with_vasu' in text:
            new_text = text.replace('@python_with_vasu', '').strip()
            response = handle_response(new_text)
    else:
            response = handle_response(text)
    update.message.reply_text(response)        
    
def error(update, context):
    print(f'User {update} caused error: {context.error}')
    
if __name__ == '__main__':
    updater = Updater(token=keys.token, use_context=True)
    dp = updater.dispatcher
    
    #Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))
    
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    
    #Errors
    dp.add_error_handler(error)
    
    #Run Bot
    updater.start_polling()
    updater.idle()
