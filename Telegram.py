import telebot
TOKEN = 'xxxyyyzzz'
URL = 'https://api.telegram.org/bot' + TOKEN + '/getUpdates'
URL_CARACTERISTICAS_BOT = 'https://api.telegram.org/bot' + TOKEN + '/getme'
URL_PERSONA = "https://api.telegram.org/bot" + TOKEN + "/sendMessage?chat_id="
tb = telebot.TeleBot(TOKEN)

class Telegram():    
    def __init__(self):
        self.echoBucle()        
                
    def echoBucle(self):
        print("iniciando escucha")
        tb.set_update_listener(self.listener)        
    
    def send(self, Id_group, Mensaje):
        tb.send_message(Id_group, Mensaje)   

    def listener(mensajes):
        print("iniciando escucha")
        for m in mensajes:
            chat_id = m.chat.id
            texto = m.text
            print('ID: ' + str(chat_id) + ' - MENSAJE: ' + texto)    
        


