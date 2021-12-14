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

#字典