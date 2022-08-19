
"""Объявите класс EmailValidator для проверки корректности email-адреса. Необходимо запретить
создание объектов этого класса: при создании экземпляров должно возвращаться значение None,
например:

em = EmailValidator() # None

В самом классе реализовать следующие методы класса (@classmethod):

check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае;
get_random_email(cls) - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com,
где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка).

Корректность строки email определяется по следующим критериям:

- допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
- длина email до символа @ не должна превышать 100 (сто включительно);
- длина email после символа @ не должна быть больше 50 (включительно);
- после символа @ обязательно должна идти хотя бы одна точка;
- не должно быть двух точек подряд.

Также в классе нужно реализовать приватный статический метод класса:

is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True,
иначе - False.

Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email.
Если параметр email не является строкой, то check_email() возвращает False."""

import random
import string


class EmailValidator:
    def __new__(cls):
        return None

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        allowed_symbols = string.ascii_letters + '._@' + string.digits
        if len(email) > 151 or email.count("@") > 1:
            return False
        for index, letter in enumerate(email):
            if letter not in allowed_symbols:
                return False
            if letter == "@":
                if email[index+1] == "." or len(email[:index]) > 100\
                        or len(email[index:]) > 50\
                        or "." not in email[index:]:
                    return False
            if letter == "." and email[index + 1] == ".":
                return False
        return True

    @classmethod
    def get_random_email(cls):
        allowed_symbols = string.ascii_letters + '._' + string.digits
        generated_email = random.choices(allowed_symbols, k=random.randint(1, 100)) +\
            ["@gmail.com"]
        return "".join(generated_email)

    @staticmethod
    def __is_email_str(email):
        return type(email) == str


em = EmailValidator()
print(em)
print(EmailValidator.check_email(1466))
print(EmailValidator.check_email("sc_lib@list_ua"))
print(EmailValidator.check_email("sc_lib@list.rkgdftkdfgfktufhmtfdytfdchtdkeytdgc5edcktrdky5c5ekrdr4ttoftydi5tu"))
print(EmailValidator.check_email("sc_lib@list..ua"))

