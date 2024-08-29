def send_email(messange, recipient, sender = 'university.help@gmail.com'):
    recipient.replace('.ru', '$')
    recipient.replace('.com', '$')
    recipient.replace('.net', '$')
    messange.replace('.ru', '$')
    messange.replace('.com', '$')
    messange.replace('.net', '$')
    if '$' in recipient or '$' in messange:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    elif sender != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('message','university.help@gmail.com','@.com')
send_email('message','university.help@gmail.com')
send_email('message','universi@.com')
send_email('message','universi@.co')
send_email('message','universi.com')