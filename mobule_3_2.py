def send_email(mesenge, recipient, sender = "university.help@gmail.com"):
    if ('@' and ('.com' or '.ru' or '.net')) not in (mesenge or recipient) or ('@' and ('.com' or '.ru' or '.net')) not in (mesenge or sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print('Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    elif sender != "university.help@gmail.com":
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

send_email('message','university.help@gmail.com','@.com')
send_email('message','university.help@gmail.com')
send_email('message','universi@.com')
send_email('message','universi@.co')
send_email('message','universi.com')