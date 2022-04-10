chance = 3
real_password = 'a123456'

while chance > 0:
    password = input('請輸入密碼')
    chance = chance - 1
    
    if password == real_password:
        print('登入成功')
        break

    else:
        print('密碼錯誤')
        if chance > 0:
            print('還有', chance , '次機會')
        else:
            print('您的帳號已被鎖定')