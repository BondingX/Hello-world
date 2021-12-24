#函数是带名字的代码块，也就是一个黑箱
#要执行这个函数定义的特定任务，可反复调用该函数
#1 编写显示信息的函数
#2 编写处理数据并返回一个或一组值的函数
#3 学习如何将函数存储在称为模块的独立文件中，让主程序的文件组织更有序

#定义函数
def greet_user():
    """显示简单的问候语。"""#这一行是文档字符串
    #上面那行是用来生成有关程序中函数的文档的
    print("Hello!")#跟在def xx(): 下的所有代码定义了xx()这个函数。

greet_user()

##向函数传递信息
def greet_user(username):
    """显示简单的问候语"""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

##实参和形参
##上面这个函数的定义中，变量username是一个形参parameter，就是函数需要什么
##而在具体的代码greet_user('jesse')中，值‘jesse’是一个实参argument
##实参是调用函数时传递给函数的信息
##有很多人形参实参不分，看到这种情况不要大惊小怪
###其实这不就是元模型和模型吗？
###元模型中的变量是形参，填入一个信息就成了实参，整段代码也就变成了具体的模型了

#传递实参
#传递实参的方法有很多也很灵活
#主要有位置实参、关键字实参、列表和字典等方式

##位置实参
##要求：实参与形参的排列顺序一致
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
#当然可以根据需要调用任意次函数
describe_pet('dog', '旺财')
#多次调用函数，效率极高！建立元模型库的基本要素也在于此。

##关键字实参
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')
##只要指出了对应的形参，顺序什么的也就无所谓了。

##默认值
##编写函数时，可给每个形参制定默认值
##因此在调用函数的时候省略实参就会使用默认值
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
#如果显式地给animal_type提供了实参，Python将忽略这个形参的默认值
describe_pet(pet_name='Gorge', animal_type='hamster')

##等效函数调用
##鉴于可混用多种方式，所以调用函数有多种等效方式
##这里就不演示了你懂的

##避免实参错误
##如果你没有指定形参的默认值，又缺少实参输入，那么程序就会报错
##这个的解决也不用我多说了吧

##返回值
##函数当然可以用来处理数据而不是只能用来print
##使用return语句

##返回简单值
def get_formatted_name(first_name, last_name):
    """返回格式化的姓名"""
    full_name=f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

##让实参变成可选的
def get_formatted_name(first_name, middle_name, last_name):
    """返回格式化的姓名（带中间名）。"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
##上面这个程序，如果没有中间名的话就会报错
##我们就可以指定中间名为空字符就行了，有的就会覆盖，没有的就会默认是空
##习惯上我们会把有默认值的形参移动到函数定义的末尾
##这种设置可选的方式可以让函数灵活处理各种不同的情况
##还能确保函数调用尽可能简单

##返回字典
##函数可返回任何类型的值，包括列表和字典等复杂数据结构
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息。"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

##下面展示如何扩展函数，使其接受可选值
def build_person(first_name, last_name, age=None):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:#这个的意思是如果age作为小行星                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        person['age'] = age
        return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
musician = build_person(first_name='nox', last_name='stallman', age=19)
print(musician)
##如果是想要在有年龄的时候才存储这个姓名，那就不用给none打引号
##条件测试中，None相当于是False。
##如果调用中包含形参age的值，这个值将被存储在字典中
##如果没有则直接只显示None，姓名和