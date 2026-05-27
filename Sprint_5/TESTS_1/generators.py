import random
import string

FIRST_NAME = "nikolay"
LAST_NAME = "kuznetsov"
COHORT = "46"
DOMAIN = "@yandex.ru"

def generate_unique_email() -> str:
    random_digits = ''.join(random.choices(string.digits, k=3))
    return f"{FIRST_NAME}_{LAST_NAME}_{COHORT}_{random_digits}{DOMAIN}".lower()

def generate_valid_password() -> str:
    length = random.randint(6, 10)
    letters = string.ascii_letters + string.digits
    return ''.join(random.choices(letters, k=length))

def generate_invalid_password() -> str:
    length = random.randint(1, 5)
    letters = string.ascii_letters + string.digits
    return ''.join(random.choices(letters, k=length)) 
