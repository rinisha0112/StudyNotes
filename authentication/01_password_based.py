# I know this is pretty basic but hey I want to keep trackof everything and something is better than nothing.

# In this authentication method you set a password while creating your account. 
# Later, while logging back in - you will be given access only if you provide correct password pretaining to your account. Standard process.
# This falls under the umbrella of 'something you know' principle of authentication method.
# This is not robust as weak passwords may lead to identity theft. This in single factor authentication.
# This can be made robust by implementing multi-factor authenticaton. [out-of-scope] for this script.


#   passwords are stored as hashes instead of plain text.


# TO DO: Check out Python Django framework for setting up user accounts and look into how it stores passwords
# TLS/ssl encrypted password from frontend --> salting + hashing --> inserting/matching the hash in database