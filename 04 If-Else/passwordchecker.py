set_pwd = input('Your Set Password - ')
user_pwd = input('Enter Your Password - ')

if set_pwd == user_pwd:
    print("1. Who invented Java Programming  \n 1.  Guido van Rossum \n 2.  James Gosling \n 3.  Dennis Ritchie \n 4.  Bjarne Stroustrup")
    ans1 = int(input('Select Answer  only number - '))
    if ans1 ==  2 :
       print("1. Who invented Java Programming  \n 1.  Guido van Rossum \n 2.  James Gosling \n 3.  Dennis Ritchie \n 4.  Bjarne Stroustrup")
       ans2 = int(input('Select Answer  only number - '))
       if ans2 == 2:
           print('Your Result is pass')
else:
    if set_pwd != user_pwd:
       print("Password Doesn't Match")