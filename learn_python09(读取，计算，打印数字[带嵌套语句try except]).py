while True:
    reply=input('Enter text:')
    if reply=='stop': break
    try:#try用于拦截错误
        num=int(reply)
    except:
        print('bad!'*8)
    else:
        print(int(reply)**2)
print('Bye!')
