#条件测试——if语句
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:#同一个元素执行完所有逻辑后才会轮到下一个元素。
	if car == 'bmw':
	#一个等号在python里被用作【定义】
	#所以【是否相等】就成了两个等号，表示发问
	#在控制台里运行python命令时，可以用==来检查值是否true
		print(car.upper())
	else:
		print(car.title())
#两个大小写不同的值被视为不相等
	if car == 'audi':
		print(True,f"\n")
	else:
		print(False,f"\n")
#在Hello_Wolrd篇里的疑问此处得以解决
#如果想要输出结果后有一个空行，则可以在print函数内加逗号和格式化字符串f"\n"即可

#检查是否不相等（!=），惊叹号在很多编程语言中都是“不”的意思
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies!")

#数值比较
#很简单，还是用==和!=来进行检查，咱们就直接跳过了
#条件语句中可包含各种数学比较
#检查是不是可以进网吧的逻辑
ages = [12,14,23,26,19,25,21]
for age in ages:
	if age > 18:
		print(True,f"欢迎光临东湖网吧！")
	else:
		print(False,f"未满18岁禁止进入！")

#检查多个条件
#使用and和or，表示与和或逻辑
#从上面的年龄列表中，任选两个人检查，若两人都未满18岁则输出一个结果
#若不是则输出第二个结果
#这个从一个集合中任选两人的逻辑，情况有点复杂，我在这里试了一下写不出来
#需要用到排列组合函数，看来暂时是没法在这里写了。

#if-elif-else结构
#检查超过两个的情况

age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $25.")
else:
	print("Your admission cost is $40.")
#这里的elif检测的是未通过if检测的情况，而else检测的是最后剩下的部分
#elif可以不限次数地使用，但是检查顺序始终是由上至下的。
#为了使得代码更简洁，可以在每种情况中设置价格，最后调用它们
if age < 4:
	price = 0
elif age < 18:
	price = 25
else:
	price = 40
print(f"Your admission cost is ${price}")
#python并不要求if-elif结构后必须有else
#else是一个包罗万象的命令，有的时候可能会引入无效甚至恶意的数据
#为了将最后得到的数据范围缩减至一个合理的范围，我们可以直接用elif结尾
if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
elif age >= 65:
	price = 20
print(f"Your admission cost is ${price}")

#使用elif测试多个条件
#以下是一家披萨店的加料系统逻辑：
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")

print("\nFinished making your pizza")
#但是如果你用elif就不行了，因为一旦if中的条件通过了，程序就会跳过余下的测试
#下面就试一下，是吧
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")

print("\nFinished making your pizza")

#用if语句处理列表
#回到刚才的那家披萨店，如果我们青椒用完了，但顾客想要加青椒，该怎么写?
requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

#检查列表是否为空
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}.")
	print("\nFinished making your pizza!")
else:#由于列表是个空集，if中检测不到元素，所以这里就会继续执行else命令
	print("Are you sure you want a plain pizza?")

#使用多个列表
available_toppings = ['mushrooms', 'oilves', 'green peppers', 'pepperoni',
					  'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

#关于if语句的格式
#PEP 8提供的唯一建议是在==、>=和<=等比较运算符两边各添加一个空格
#这么做主要是为了好读

#字典，使用大括号建立字典集合
#复习：中括号是列表，小括号是元组。
#下面是一个简单的字典，储存了有关特定外星人的信：
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
#字典可以高效地模拟现实世界
#字典是一系列的键值对，每个键都与一个值关联，而我们就是使用键访问相关值
#与键相关的值可以是数值、字符串、列表甚至是字典。
#其实Python中的任何对象都可以被用作字典中的值
new_points = alien_0['points']
print(f"You just earned {new_points} points!")
#上面的代码可以用来模拟击杀了0号alien之后获得的分数
#首先定义字典，然后从这个字典中获取与键‘points’相关联的值，然后将此值赋给newpoints

#添加键值对
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#为字典添加键值对可以通过直接设置的方式
#Python里的字典是有顺序的，排列顺序与添加定义时的顺序相同

#先创建一个空字典
alien_1 = {}

alien_1['color'] = 'blue'
alien_1['points'] = 10

print(alien_1)
#空字典可以用来储存用户数据
#在编写能自动生成大量键值对的代码时，通常都要先定义一个空字典

#修改字典中的值
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']}.")
#只要重新定义一下就可以覆盖原先的值

#例子：移动外星人👽
alien_2 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_2['x_position']}")
#先定义一下位置坐标和速度
#然后后下面分情况检查速度，以及再定义一个移动量x_increment
if alien_2['speed'] == 'slow':
	x_increment = 1
elif alien_2['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
#用初始位置加上移动量来确定新坐标
alien_2['x_position'] = alien_2['x_position'] + x_increment
#最后打印新坐标，当然新坐标是直接覆写在键值对上的
#如果想保留原始坐标，则需要添加新的键值对。
#通过添加键值对的代码可以记录外星人的行为，从而实现读档的效果。
print(f"New position: {alien_2['x_position']}")

#del命令在字典中的运用
#del key['default']
print(alien_0)
del alien_0['points']
print(alien_0)

#pop()函数在字典中的运用，
#Dictionary = {'key': 'default'}
#pop_key = Dictionary.pop('default')
#pop函数的用处是可以显示某个值之后再删去，具体的用途目前未知
print(alien_1)
pop_key = alien_1.pop('points')
print(alien_1, f"You earn {pop_key} points!")

#由类似对象组成的字典格式
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'java',
	}
#本来想试一试遍历字典，其实不用这么着急，下面会练习的
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

#使用get()函数访问值
alien_3 = {'color': 'red', 'speed': 'slow'}
point_value = alien_3.get('points', 'No point value assigned.')
print(point_value)
#如果打印中使用了不存在的键值，就会报错
#我们可以用get函数在指定的键不存在时返回一个默认值
#这其实就是个简化版的条件检查，当存在键时就会返回相关值，没有就会返回后面的默认值
#在我们查询一个字典时，如果没法确定一个值是否存在，就应该用get函数
#如果没有指定默认值，get函数则会返回None

#遍历字典
#Python支持对键值对、键、值的遍历

User_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}
#遍历当然要用for语句，不过格式和变量要注意设置好
for key, value in User_0.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}\n")
#这里用到了items()函数，items函数的功能是用来生成包含字典内所有键值对的列表
#键值对格式为key, value，前者为key，后者为值，你可以用别的代名来赋给这两个位置
#不过为了学习的时候不混淆，我们上面就用key和value
#下面来看一个例子
for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}")
#上面就是用其他代名来指代key和value，这样在遍历的时候就可以一句话成型
#即使字典存储的是百万级别量级的数据，这种循环也管用

#遍历字典中的所有键
#我们有的时候不需要使用字典的值，函数keys()就很管用。
for name in favorite_languages.keys():
	print(name.title())
#同理values也一样
for language in favorite_languages.values():
	print(language.title())

#下面展示一下这个函数的常用用法：
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(f"Hi{name.title()}.")
	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}!")
		#这里的\t是tab的意思
#还可检查某个人是否在列表里，使用if not in命令即可
if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

#按特定顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")
	#这里对方法dictiionary.keys()调用了sorted()函数

#遍历所有值
#因为上面已经展示过values()了，这里就再展示一个set()函数
print ("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())
#对包含重复元素的列表调用set()，可以找出独一无二的元素
#用这些独一无二的元素可以创建一个没有重复元素的集合

#创建集合
languages = {'python', 'ruby', 'python', 'c'}
print(languages)
#集合也是用大括号来定义的，但是集合不同于列表和字典，它不储存顺序