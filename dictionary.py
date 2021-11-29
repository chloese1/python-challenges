import random
import string

def random_string(length):
    result = ''.join((random.choice(string.ascii_lowercase) for x in range(length)))
    return result

def generate_dict():
    for i in range(100):
        print("'" + random_string(random.randint(1,10)) +  "': " + "'" + random_string(random.randint(1,10)) +"',")



generate_dict()
