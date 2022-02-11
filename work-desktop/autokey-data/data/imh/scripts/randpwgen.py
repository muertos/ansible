# generate a random string for on the fly passwords
# store string into clipboard

import random, string

random.seed()
randstring = ''
iterable = string.ascii_letters + string.digits
for i in range(12):
    randstring += random.choice(iterable)

clipboard.fill_clipboard(randstring)
keyboard.send_keys(randstring)
