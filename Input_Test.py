message = input("Tell me something, and I will repeat it back to you: ")
print(message)
#由于sublime难以运行input()这种交互性的函数，我们改用vscode
#vscode的运行调试是ctrl+F5，和sublime不一样
name = input("Please enter your name: ")
print(f"\nHello, {name.title()}!")
#当然我们也可以写超过一行的提示文字，用+=即可
prompt = "If you tell us who you are, we can personalize the messages"
prompt += "\nWhat is your first name"

name = input(prompt)
print(f"\nHello, {name}!")

#使用int获得数值输入
age = input("How old are you?")#这里的输入是字符串，无法用作数值
if int(age) >= 18:#所以可以在这里加int函数
    print(age)
else:
    print("Your're not allowed to enter!")
#用符合函数定义age也可以获得和上面一样的效果，就不展示了

#求模运算符%
#可以返回两数相除之余数，用于判断奇偶性非常好用
4 % 3

#while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
#+=不仅可以用于添加字符串，也当然可以用于添加数值
#while可以确保程序不断运行，并且可以用户的意思停下来

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit to end the program. "
message = ""
while message != 'quit':#!=是不等于号
    message = input(prompt)
    print(message)
#上面这个程序还是会返回quit，我们可以添加下面两行
#   if message != 'quit':
#       print(message)
#从而也就筛选掉了quit的情况

#使用指示标志（flag）
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. " 

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
#这里是将变量active设置为True
#我们可以设置很多不同的条件以赋给active不同的值

#使用break推出循环
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")