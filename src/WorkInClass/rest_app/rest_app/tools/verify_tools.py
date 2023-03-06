import random

def generate_verify_code(fixed_digits = 6):
    return str(random.randrange(111111, 999999, fixed_digits))

