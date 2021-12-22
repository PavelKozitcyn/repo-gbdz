import re


def emil_parse(email):
    user_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not user_email.match(email):
        raise ValueError(f'wrong email:{email}')
    print(user_email.match(email).groupdict())


user_e = input("ведите свой Email: ")
emil_parse(user_e)
