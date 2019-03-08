import telebot
import requests
from telebot import types
TOKEN = 'xxxyyyzzz'
tb = telebot.TeleBot(TOKEN)

urlRegistroCodigoDB = "http://192.168.1.2:8080/servlet"

def listener(mensajes):
    for m in mensajes:
        chat_id = m.chat.id
        texto = m.text
        #print(chat_id)
        #print(' - MENSAJE: ' + texto)    

tb.set_update_listener(listener)

def extract_unique_code(text):
    mensaje_filtrado = text.split()
    contadorItemsLista = 0
    for item in mensaje_filtrado:
        contadorItemsLista += 1
    #print("tamano lista: ")
    #print(contadorItemsLista)

    if contadorItemsLista > 1 :
        return mensaje_filtrado[1]
    else:
        return " "

@tb.message_handler(commands=['start'])
def send_welcome(message):
    cid = message.chat.id
    tb.reply_to(message, "Hola!, soy el bot de la WISROVI, por favor digite su numero de documento despues del comando /DOC ")

@tb.message_handler(commands=['DOC'])
def comando_doc(mensaje):
    chat_id = mensaje.chat.id
    unique_code = extract_unique_code(mensaje.text)
    if unique_code == " ":
        msg = tb.send_message(chat_id, 'Comando no valido, recuerde que despues del comando /DOC debe haber un espacio antes de colocar su numero de documento')
    else:
        payload  = {'id': chat_id, 'doc': unique_code}
        r = requests.get(urlRegistroCodigoDB, params=payload, verify=False)
        respuesta = r.text.capitalize()
        caracterEncontrado = respuesta.find("<")-1
        nombrePersona = respuesta[0:caracterEncontrado].upper()
        if len(nombrePersona) > 2:
            msg = tb.reply_to(chat_id, 'Hola  %s, bienvenido!' %nombrePersona)
        else:
            msg = tb.reply_to(chat_id, 'El numero de documento no esta registrado')
        

  #tb.register_next_step_handler(msg)

tb.polling()


