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
from hashlib import sha3_512
import os

PASSWORD_HASHER_ALGO = "sha3_512"

def hashing_algorithm(password):
    import hashlib

    # 1. Create the hash object
    hash_object = hashlib.sha3_512()

    # 2. Provide the data (must be in bytes)
    data = "password"
    hash_object.update(data.encode('utf-8'))

    # 3. Get the hexadecimal representation
    hex_digest = hash_object.hexdigest()

    return hex_digest

def generate_fake_word(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def encrypt_password(password, salt_word, iterations):
    salted_password = password+salt_word
    final_hash = salted_password
    for _ in range(iterations):
        final_hash = hashing_algorithm(final_hash)

    encrypted_paasword = f"{PASSWORD_HASHER_ALGO}${salt_word}${iterations}${final_hash}"
    return encrypted_paasword

def create_account(user, password):
    # we are skipping duplicate user validation for sake of simplicity
    random_salt_word = generate_fake_word(random.randint(5,10))
    iterations = random.randint(5,10)
    encrypted_password = encrypt_password(password, random_salt_word, iterations)
    
    with open(os.path.join(os.getcwd(), 'data/authentication/01_password_based.txt'), 'a') as f:
        f.write(f"{user} {encrypted_password}\n")


def login_account(user, password):
    with open(os.path.join(os.getcwd(), 'data/authentication/01_password_based.txt'), 'r') as f:
        accounts = f.readlines()
        for acc in accounts:
            acc = acc.strip()
            acc_user, stored_encrypted_password = acc.split(' ')
            if user == acc_user:
                algorithm = stored_encrypted_password.split('$')[0]
                salt_word = stored_encrypted_password.split('$')[1]
                iterations = int(stored_encrypted_password.split('$')[2])
                stored_hash = ''.join(stored_encrypted_password.split('$')[3:])

                # regenerating encrypted password has with password passed in login attempt
                # if it matches login will be successful
                regenerate_encrypted_password = encrypt_password(password, salt_word, iterations)
                regenerated_hash = ''.join(regenerate_encrypted_password.split('$')[3:])
                if regenerated_hash == stored_hash:
                    print('logged in successfully!')
                    return
                else:
                    print('authentication failed')
                    return 
    print('user doesn\'t exist')


if __name__ == '__main__':
    print("1. sign up \n 2. log in")
    inp = int(input(">"))
    if inp == 1:
        user = input('enter email: ')
        password = input('set password: ')
        create_account(user, password)
    else:
        user = input('enter email: ')
        password = input('enter password: ')
        login_account(user, password)

    

