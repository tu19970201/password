chance = 3

while chance > 0:
    password = input('請輸入密碼')
    
    while password != 'a123456':
        chance = chance - 1
        print('密碼錯誤，還有', chance , '次機會')
        break

    if password == 'a123456':
        print('登入成功')
        chance = 0