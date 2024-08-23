def current_mail(mail):
    dog = "@"
    dot = ["ru", "com", "net"]
    dot_mail = mail.split(".")
    if dot_mail[-1] in dot and dog in mail:
        return True
    else:
        return False


def send_email(message, recipient, sender="university.help@gmail.com"):
    if current_mail(recipient) != True or current_mail(sender) != True:
        print("Невозможно отправить письмо с адреса " + sender + " на адрес " + recipient)
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender != "university.help@gmail.com":
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса " + sender + " на адрес " + recipient + ".")
    else:
        print("Письмо успешно отправлено с адреса " + sender + " на адрес " + recipient + ".")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', 'urban.teacher@mail.ru')
