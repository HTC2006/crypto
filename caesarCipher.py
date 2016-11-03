msg = raw_input('where is your message BOI???')#'PBWRPENSG YNO EBPXF!'
key = raw_input('and WHERE THE HECK IS UR DUMB KEY!!! and BTW what is it?')
mode='encrypt'
ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result=''
msg = msg.upper()

for symbol in msg:
    if symbol in ALPHABET:
        num=ALPHABET.find(symbol)
        if mode=='encrypt':
            num=num+key
        elif mode == 'decrypt':
            num=num+key



        if num >= len (ALPHABET):
            num = num - len(ALPHABET)
        elif num < 0:
            num = num + len(ALPHABET)
        result = result + ALPHABET[num]    
    else:
        result = result + symbol

print (result)
