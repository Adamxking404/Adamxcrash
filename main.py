Azul='\033[1;34m';Branco='\033[1;37m'
##################
from os import system, execl
from sys import argv, executable
from threading import Thread
from time import sleep
from webbrowser import open
from email.message import Message
from smtplib import SMTP
##################
system('git pull')
##################
def init(gmail, password, titulo, body):
	msg=Message()
	msg['Subject'] = titulo
	msg['From'] = gmail
	msg['To'] = 'support@support.whatsapp.com'
	password = password
	msg.add_header('Content-Type', 'text/html')
	msg.set_payload(body )
	s = SMTP('smtp.gmail.com: 587')
	s.starttls()
	s.login(msg['From'], password)
	s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
	sleep(0.0007)

def main():
	while True:
		system('cls||clear')
		op = input('''\n%s- %sDiscord%s  : kine azul#3189
- %sGithub%s   : https://github.com/Adamxking404
- %sTelegram%s : @Adamxking\n\n[%s 1 %s] %s|%s Ban number\n[%s 2 %s] %s|%s Unban number\n[%s 0 %s] %s|%s Exit\n\n%s===> %s'''%(logo,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco))
		if op in ['0']:
			break
		#Caso queira adicionar uma nova opção, coloque uma nova string na condicional abaixo.
		elif op in ['1','2']:
			open('https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4OSggjYOgt8g8HbgSU58LpUqQ5GsD63ipENqa84YegMHionqqvIXMMoc4bqu-C0GH0N--Kal_AFpd5rRJYyO0g-y1AbEQ');system('termux-open-url https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4OSggjYOgt8g8HbgSU58LpUqQ5GsD63ipENqa84YegMHionqqvIXMMoc4bqu-C0GH0N--Kal_AFpd5rRJYyO0g-y1AbEQ')
			try:
				numero=str(input('%s[ %sNumber %s ] -%s'%(Azul,Branco,Azul,Branco,Azul,Branco)))
		                #Aqui você pode colocar um novo texto ou alterar um já existente.
				op={
				'1':'Desative este número|Estou solicitando a desativação temporária da minha conta no whatsapp, meu numero: %s'%numero,
				'2':'Meu número foi banido injustamente|Nossa! Eu estou trabalhando e de repente meu número foi banido, eu não sei o quê aconteceu, preciso do meu número pois é do trabalho, eu preciso atender meus clientes. Meu número: %s'%numero
				}[op]
				gmail=str(input('%s[ %sGmail%s ] -%s '%(Azul,Branco,Azul,Branco)))
				password=str(input('%s[ %sPassword%s ] -%s' %(Azul,Branco,Azul,Branco,Azul,Branco)))
                                # Caso queira mudar a quantidade de mensagens que serão enviadas, altere no range
				for _ in range(1):
					Thread(target = init, args = (gmail, password, op.split('|')[0],op.split('|')[1])).start()
			except:
				pass
	system('cls||clear')

logo='''%s                              
  ___            ___  __   __ 
 / _ \    /\    / _ \|  \ /  |
| |_| |  /  \  | |_| |   v   |
|  _  | / /\ \ |  _  | |\_/| |
| | | |/ /__\ \| | | | |   | |
|_| |_/________\_| |_|_|   |_|
%s
%s•%sA WHATSAPP NUMBER BAN TOOL BY DARK ADAM\n\n'''%(Azul,Branco,Azul,Branco)
##################
if __name__ == '__main__':
	main()
