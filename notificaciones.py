import base64

from Telegram import *
Telegram = Telegram()

from EmailService import *
Email = ServicioEmail()




from flask import Flask, request

app = Flask(__name__)

def decoBase64UrlSafe(s):
    return base64.urlsafe_b64decode(s + '=' * (4 - len(s) % 4))


@app.route('/telegram', methods=['GET', 'POST'])
def telegram():
    print("telegram solicitado")
    ID_GROUP = ""
    if request.method == 'GET':
        ID_GROUP = request.values.get('ID_GROUP')
        dato = request.values.get('MENSAJE')
        MENSAJE = decoBase64UrlSafe(dato)
        #print(MENSAJE)
        Telegram.send(ID_GROUP, MENSAJE)
        return "OK"    
    return "Error"

@app.route('/email', methods=['GET', 'POST'])
def email():
    print("Email solicitado")
    TO_EMAIL = ""
    if request.method == 'GET':
        FROM_NAME = request.values.get('FROM_NAME')
        GROUP = request.values.get('GROUP')
        TO_EMAIL = request.values.get('TO_EMAIL')
        SUBJECT = request.values.get('SUBJECT')
        BODY = request.args.get('BODY')
        return Email.sendEmail(GROUP, FROM_NAME, TO_EMAIL, SUBJECT, BODY)
    return "Error"



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8190)

