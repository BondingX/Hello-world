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
    if age:#这个的意思是如果age存在，也就是age变量被赋予了某个值                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        person['age'] = age
        return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
musician = build_person(first_name='nox', last_name='stallman')
print(musician)
##如果是想要在有年龄的时候才存储这个姓名，那就不用给none打引号
##条件测试中，None相当于是False。
##如果调用中包含形参age的值，这个值将被存储在字典中
##如果没有则直接只显示None，姓名直接不予显示
##因为函数里定义了只有age存在赋值的情况下才会返回字典

##结合使用while循环
##下面演示结合使用get_formatted_name()和while循环

def get_formatted_name(first_name, last_name):
    """返回一个人的正写全名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
#以下是一个无限循环！没有退出选项
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
    break#这个break是后来加的，没有这个break就是无限循环
#但是我们想循环，而且让用户自行选择如何退出，就可以这么修改
def get_formatted_name(first_name, last_name):
    """返回一个人的正写全名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'quit' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'quit':
        print('Program terminated')
        break
    l_name = input("Last name: ")
    if l_name == 'quit':
        print('Program terminated')
        break
#检查用户的输入值，检测到值为quit的时候就退出
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

#传递列表
#向函数传递列表很有用，函数可以直接访问列表中的内容以提高处理列表的效率

def greet_users(names):
    """向列表中的每位用户发出简单的问候"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

##在函数中修改列表
##只要将列表传递给函数之后，函数对列表的任何修改都是永久性的

#下面看一个3D打印公司自动化打印设计方案的案例
#首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

#模拟打印每个设计，直到没有未打印的设计为止
#打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

#显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

#下面用函数改写上面的代码，使其在复用的时候效率更高
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止。
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """
    显示打印好的所有模型
    """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
#这样定义了两个专用的函数之后，日后对付同样的工作只需对列表调用两个函数即可
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
#这样完成大部分工作的代码都移交给了两个函数，极大地简化了主程序
#主程序越简单，代码逻辑越容易懂，日后越方便维护与扩展内容
#一个函数只需要修改一次，就可以影响所有调用该函数的地方，大大提升了维护效率

##禁止函数修改列表
##如果我们不想对unprinted_designs做任何修改，就需要创建该列表的副本
##列表副本的创建就是用[:]对原列表进行整体切片
#基本格式为function_name(list_name[:])
print_models(unprinted_designs[:], completed_models)

#虽然可以用上面的的那种操作，但是在处理大型列表的时候，这个操作会非常费时间
#如果有一份大型列表，而且我们还不想对原始列表进行永久修改
#我们就可以换一种处理方式，可以对原始列表进行副本存档，但是直接去处理原始列表
#临时生成列表是需要花费额外的时间和算力的。
