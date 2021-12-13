#print
Message="hello world"
print(Message.title())
print("Hello World")

#variable setting
first_name="ada"
last_name="lovelace"
full_name=f"{first_name} {last_name}"
Mesage=f"Hello, {full_name.title()}"
print(Mesage)

#Tab symbol
print("Python")
print("\tPython")
print("languages:\n\tPython\n\tC\n\tJavaScript")

#remove space
favorite_language = ' python '
print(favorite_language.rstrip().lstrip())

#name_case
first_name="Eric"
Message=f"Hello {first_name.title()}, would you like to learn some Python today?"
print(Message)

#你注意到了没有，当你第二次定义message的时候，这个变量就不再是上面那个message了
#这个变量在最新的print中被替换成了最近一次定义的值。但是并不影响上面的结果
#也就是说这个代码也是逐行处理的，变量并不是全局性的
#我们并不需要担心前后冲突的问题
#我试了下F9，F9可以将所有的文字重排，定义、导出和注释的部分分别放在一起

famous_person = "Albert Einstein"
message = f"{famous_person} once said, “A person who never made a mistake never tried anything new.”"
print(message)

#数字运算
a = 0.1
b = 0.1
c = a + b 
d = a*b
print(c)
print(d)
#Python没有办法进行直接计算，必须赋值给变量之后再计算变量
e = 14_0000_0000
print(e)
#Python会忽略数字之间的空格号，所以可以为了方便查看数字加入空格
x, y, z=0, 0, 0
g=x*y*z
print(g)
print(5+3)#运用print函数即可完成直接计算……我上面说无法直接计算并不正确。

#列表
bicycles = ['trek', 'cannodale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0],bicycles[1])
#打印多个结果，可以用逗号隔开。每次输入都需要带上变量头
#有没有办法省略这个变量头部呢？
print(bicycles[-1])#-1指的是列表最后一个元素
message = f"my first bicycle was a {bicycles[0].title()}"
print(message)
#Exercise
names = ['Janis', 'Alex', 'Tony', 'Fenix', 'Bob']
print(names[0])
print(names)
names.append('Vi')#这个函数可以为列表添加元素，可以建立一个空列表然后再添加元素
print(names)
names.insert(1, 'Paul')#插值函数
print(names)
del names[3]#删除列表中的任意位置的元素
print(names)
popped_names = names.pop()#弹出栈顶元素，也就是删除列表的最后一个元素
#pop函数可以用于web应用程序中，将用户从活跃成员列表中删除并添加到非活跃成员中的操作
print(names)
print(popped_names)
#当然，也可以用于显示最新消息，最近消费记录这类功能
last_met = names.pop()
print(names)
print(f"The last person I met was {last_met.title()}")
#这个pop函数也可以用来删除列表中任意位置的元素，只需要在括弧里指定索引即可
first_met = names.pop(0)
print(names)
print(f"The first person I met was {first_met.title()}")
#所以说如果你还想保留那个数据，就用pop()函数
#不过每当用一次pop(),那个删掉的元素就不在列表中了，你看上面的列表就可以观察出来
#永久删除某个元素就用del语句
names.remove('Fenix')#此处的代码原理可以分解为1.定位该值的位置2.删除具有该值的元素
print(names)#这是根据值删除元素
#试一下如果具有相同值的元素删除操作会导致什么结果
motorcycles = ['honda', 'yamaha', 'suzuki', 'lambogini','honda', 'yamaha']
print(motorcycles)
motorcycles.remove('honda')
print(motorcycles)
#上面的测试表明有多个元素具有相同值时，执行一次remove()函数只会移除一个元素
#下面来测试使用删除的值打印一条消息
too_expensive = 'lambogini'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
#可以使用循环语句替代重复的print操作，但是暂时先不管

#列表排序案例，sort()是按字母排列顺序永久改变列表的顺序
#若想按倒序排列，则使用sort(reverse=True)即可
#使用sorted()可对列表进行临时排序，同上面也可以使用倒序参数
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
#倒序打印列表可用reverse()，反转但是不会按照字母排列顺序
cars.reverse()
print(cars)#这个操作会永久改变列表排序
cars.reverse()
print(sorted(cars))
#reverse并没有reversed这种临时倒序函数，当然如果你想你可以自己定义一个
#目前先不用太过于发散思维，先去了解哪些句法和函数是可用和常用的即可
print(cars)
print(len(cars))#len()函数可以表示列表长度，这个非常有用。

#遍历——循环语句的引入
#下面试着用for语句来打印一列名单
magicians = ["alice", 'david', 'carolina']
for magician in magicians: 
#上面这行代码在遍历magicians这个列表的同时，也将其中的每个元素都与magician相关联
	print(magician)
#循环的概念相当重要，想要自动化完成工作循环是必不可缺的。

#用for循环执行更多操作
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait for your next trick, {magician.title()}!\n")
print("Thank you, everyone. That was a great magic show!")
#这里有个问题，你如何才能使用/n在每个消息之间插入一个空行呢？
#下面的预览里每行都是挨在一起的
#这好奇怪啊，我上面输写了空行代码之后预览里面居然显示两行空行，
#看来应该是预览器的问题而不是代码的问题

#练习

Food_list = ['croquette', 'fuet', 'metworst', 'saucisson sec', 'tarator']
for food in Food_list:
	print(f"{food.title()} is tasty,")
	print(f"I wonder how to make {food.title()}?")
print("If you know how to make them well, please upload your video!")
#下面试着用一个语句来完成一样的效果
for food in Food_list:
	print(f"{food.title()} is tasty,\nI wonder how to make {food.title()}?\n")
print("If you know how to make them well, please upload your video!")

#函数range()
for value in range(1,5):
	print(value)
for value in range(7,5):
	print(value)
for value in range(-3,5):
	print(value)
#上面的例子说明了只能顺序打印整数，负数也是可以打印的。
#来试试看给句子前生成数字序列
for value in range(1,10), food in Food_list:
	print(f"{value} {food.title()}")
#看来两个列表嵌套使用for循环并没有想象中那样容易。
#下面用range函数生成数字列表
numbers = list(range(1,6))
print(numbers)
#除了连续整数外，还可以指定步长，用法是在后面加一个数
even_numbers = list(range(2,11,2))
print(even_numbers)
#刚才试过了，range里必须为整数，浮点数不知道该怎么实现
squares = []
for value in range(1,11):
	square = value ** 2
	squares.append(square)
print(squares)
#还可以不设置临时变量square，直接用append添加想要的结果以缩小代码量
for value in range(1,11):
	squares.append(value**2)
print(squares)
#min，max和sum函数
digits = range(0,11)
print(min(digits)) 
print(digits)
#如果想要打印一个列表，必须得先建立一个空集合，然后逐个添加元素
digits = []
for value in range(0,11):
	digit = value
	digits.append(digit)
print(digits)

#大数列表测试
Grootnummer_list = []
for value in range(1,1001):
#本来这里是百万单位，但是为了下面运算不用等我这里改成了一千
	nummer = value
	Grootnummer_list.append(nummer)
print(Grootnummer_list)#生成百万单位列表计算耗时2.6秒
print(min(Grootnummer_list))
print(max(Grootnummer_list))
print(sum(Grootnummer_list))
#切片处理
Players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(Players[0:3])
#切片也就是选取列表的一部分元素，指定索引的两个位置进行切片。
#切片如果省略索引头，就会自动从第一个元素开始
#省略索引尾，则会终止于最后一个元素。
#使用负数作为索引头，则可以输出列表末尾的任意切片，也就是倒数几名
#切片可以同时省略索引头和索引尾，这样可以输出整个列表为副本

#遍历切片：for 循环
print("Here are the first three players on my team")
for player in Players[:3]:
	print(player.title())

my_foods = Food_list[:]
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#下面来核实经过上面的操作后确实有两个列表
my_foods.append('cannelloni')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#元组
#列表适于储存变化的数据集，列表是可修改的
#例如网站用户列表或游戏角色列表
#而元组是一系列不可修改的元素，尝试修改元组的操作是被禁止的会报错。
#如果元组内只有一个元素，这个元素后也必须加逗号，我也不知道为啥

dimensions = (200,50)#使用圆括号而不是方括号
print(dimensions[0])
print(dimensions[1])

#当然你硬要修改的话，只能重新定义元组了。
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)

#设置代码格式——PEP8
#代码被阅读的次数比编写的次数多得多，尤其是要分享给其他程序员时
#在python这里，易读性比易写性更重要

##缩进
##每级缩进四个空格
##你可以用制表符，但是制表符需要设置成等于四个空格
##当混用制表符和空格时，应当将所有的制表符转换为空格

##行长
##没有固定限制，但是绝对不要出现那种需要左右拖动的屎条代码行

##空行
##空行这个也没有固定限制，你只要记住添加空行的目的为了增加可读性就行了

#后面的章节要开始介绍if语句了，我会再开一个.py继续接下来的练习