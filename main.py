from os import system
from threading import Thread
from time import sleep
from webbrowser import open as open_url
from email.message import EmailMessage
from smtplib import SMTP

def send_email(gmail, password, subject, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = gmail
    msg['To'] = 'support@support.whatsapp.com'
    msg.set_content(body)
    
    try:
        with SMTP('smtp.gmail.com', 587) as s:
            s.starttls()
            s.login(gmail, password)
            s.send_message(msg)
            print("[+] Email sent successfully!")
    except Exception as e:
        print(f"[-] Failed to send email: {e}")
    sleep(0.5)

def main():
    logo = '''
===================================
 WHATSAPP SUPPORT TOOL - BY ADAM
===================================
[1] Request number ban
[2] Request number unban
[0] Exit
'''
    while True:
        system('cls' if system('echo') == 0 else 'clear')
        print(logo)
        choice = input("Select an option: ")

        if choice == '0':
            break
        elif choice in ['1', '2']:
            open_url('https://myaccount.google.com/lesssecureapps')

            number = input("Enter your phone number (e.g. +1234567890): ")
            gmail = input("Enter your Gmail address: ")
            password = input("Enter your Gmail password (use app password if 2FA is enabled): ")

            if choice == '1':
                subject = "Please deactivate my number"
                body = f"I would like to request the temporary deactivation of my WhatsApp account. My number: {number}"
            else:
                subject = "My number was unfairly banned"
                body = f"My WhatsApp account was banned without explanation. I need this number for work. Please review it. My number: {number}"

            for _ in range(1):  # You can change the range value to control how many emails are sent
                Thread(target=send_email, args=(gmail, password, subject, body)).start()
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
