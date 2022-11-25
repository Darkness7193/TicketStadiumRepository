from django.forms import Form, CharField


class LogInForm(Form):
    login = CharField(label='Введите логин', max_length=100)
    password = CharField(label='Введите пароль', max_length=100)


class SignInForm(Form):
    login = CharField(label='Введите логин', max_length=100)
    password = CharField(label='Введите пароль', max_length=100)
    password_conf = CharField(label='Повторно введите пароль', max_length=100)
    requisites = CharField(label='Введите номер банковской карты', max_length=100)