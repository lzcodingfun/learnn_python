while True:#注意冒号
    reply=input('Enter text')
    if reply=='stop':
        break
    elif not reply.isdigit():
        print('bad!'*8)
    else:
         print(int(reply)**2)
print('Bye!')
