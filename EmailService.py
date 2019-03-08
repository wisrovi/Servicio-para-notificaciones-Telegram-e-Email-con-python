import smtplib
import base64

email_user = 'wisrovi.rodriguez@gmail.com'  
email_password = 'password'

class ServicioEmail():

    def decoBase64UrlSafe(self,s):
        var=base64.urlsafe_b64decode(s + '=' * (4 - len(s) % 4))
        return str(var, 'utf-8')

    def sendEmail(self,nombreGrupo,namefrom,emailto,subject,body):

        newnamefrom = self.decoBase64UrlSafe(namefrom)
        newemailto = self.decoBase64UrlSafe(emailto)
        newsubject = self.decoBase64UrlSafe(subject)
        newbody = self.decoBase64UrlSafe(body)
        newnombreGrupo = self.decoBase64UrlSafe(nombreGrupo)
        
        message = """From: %s <%s>
To: %s <%s>
MIME-Version: 1.0
Content-type: text/html
Subject: %s

%s
        """ % (newnamefrom, email_user, newnombreGrupo, newemailto.split(), newsubject, newbody)

        print(message)
        
        try:
            server = smtplib.SMTP_SSL('webmail.fcv.org', 465)
            server.ehlo()
            server.login(email_user, email_password)
            server.sendmail(email_user, newemailto.split(), message)
            server.close()
            return "OK"
            #server.starttls()
        except:
            return "BAD"
   
        
        


