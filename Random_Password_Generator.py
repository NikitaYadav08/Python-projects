import random
import string
Pass_len = 9
charValues = string.ascii_letters + string.digits + string.punctuation
password = "".join([random.choice(charValues)for i in range(Pass_len)])
print("Your Random Password is: ", password)