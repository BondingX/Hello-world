#使用int获得数值输入
#age = input("How old are you?")#这里的输入是字符串，无法用作数值
#if int(age) >= 18:#所以可以在这里加int函数
#    print(age)
#else:
#    print("Your're not allowed to enter!")
#用符合函数定义age也可以获得和上面一样的效果，就不展示了

#上面那段代码是摘抄自输入练习文件，但是我发现如果我不输入一个数那么程序就一定报错，输入空值也报错
#怎么解决这个问题？让我输入空值的时候显示“用户跳过输入”
#在输入一个非法值也就是不是数的值的时候显示"请输入正确的年龄！"
#我想到的办法是给年龄变量预设一个默认值，然后再要求用户输入一个值附加到这个值上
#然后我们再通过检查年龄变量来确定返回的结果
#试试看吧

age = ''
prompt = "Please enter your age: "
prompt += "\n(Enter quit to exit)"
active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active == False
        break
    elif age == '':
        print("User has skipped the entering")
    else:
        if age.isdigit():
            if int(age) >= 18:
                print("Hello, welcome")                
            elif int(age) < 18:
                print("You're not allowed to enter!")                
        else:
            print(f"Please enter the right information!")
            

