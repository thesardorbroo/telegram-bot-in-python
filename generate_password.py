from random import randint
from config import word,db

async def customer_check():
    while True:
        new_pass = ""
        i = 0
        while i < 8:
            num = randint(0,61)
            new_pass += word[num]
            i += 1

        if not await db.is_data_exist('*','sales','seria',new_pass): return new_pass
