# I know this is pretty basic but hey I want to keep trackof everything and something is better than nothing.

# In this authentication method you set a password while creating your account. 
# Later, while logging back in - you will be given access only if you provide correct password pretaining to your account. Standard process.
# This falls under the umbrella of 'something you know' principle of authentication method.
# This is not robust as weak passwords may lead to identity theft. This in single factor authentication.
# This can be made robust by implementing multi-factor authenticaton. [out-of-scope] for this script.


#   passwords are stored as hashes instead of plain text.


# TO DO: Check out Python Django framework for setting up user accounts and look into how it stores passwords
# TLS/ssl encrypted password from frontend --> salting + hashing --> inserting(account creation)/matching(loggin in) the hash in database

# Completeing todo: so django also does something like:
# password --> random salt --> encryptsusing hasing algo algo --> repeats encryption for i iterations --> final hash
# in db it stores password as algorithm$salt$iteration$finalhash


# we will mimick something similar here but instead of db we will save password in a local file

import random
import string
from argon2 import PasswordHasher
import os

PASSWORD_HASHER_ALGO = "argon"

def generate_fake_word(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))



def create_account(user, password):
    # we are skipping duplicate user validation for sake of simplicity
    random_salt_word = generate_fake_word(random.randint(5,10))
    iterations = random.randint(5,10)
    salted_password = password+random_salt_word
    hasher = PasswordHasher()
    final_hash = salted_password
    for i in range(iterations):
        final_hash = hasher.hash(final_hash)

    password_to_store = f"{PASSWORD_HASHER_ALGO}${random_salt_word}${iterations}${final_hash}"
    
    with open(os.path.join(os.getcwd(), 'data/authentication/01_password_based.txt'), 'w+') as f:
        f.write(f"{user};{password_to_store}")




    


if __name__ == '__main__':
    print("1. sign up \n 2. log in")
    inp = int(input(">"))
    if inp == 1:
        user = input('enter email: ')
        password = input('set password: ')
        create_account(user, password)
    else:
        pass

    

