#我第一个项目就暂定研究怎么html和md文件的互相转换问题了

#字典可储存在列表中
#列表可以作为值储存在字典中
#字典中可以嵌套字典
#这相当于双向传送门

#字典列表
#字典是叫字典没错，但是其实一个字典更像是一个“词条”
#比如说一个alien_0值包含了一个外星人的信息，无法储存第二个
#这就是为什么要字典列表，这才是真正的“字典（日常用词）”

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

#更符合现实的情况是，外星人多到需要代码自动生成.
#下面使用range()来生成

aliens = []

for alien_num in range(30):
#这里要建立一个包含了30个元素的临时列表
#range()返回的一系列数，唯一的用途就是告诉python要重复这个循环多少次。
#每次执行这个循环时，都创建一个外星人，并将其添加到列表的末尾
#在遍历这个列表的时候，每次都会执行一个append，直到这个列表被遍历完
#遍历发生在临时列表上，而append发生在空列表上
#你写的每一个循环 在逻辑结构上的存储是独立的
#在for外写的变量都可以被利用
#但是for内写的它只存储在自己的堆栈里
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
	print(aliens)

for alien in aliens[:6]:
	print(alien)
	print(alien_num)
print("...")
print(f"Total number of aliens: {len(aliens)}")

#切片复习（粘贴自Hello_Wolrd.py）
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
#这里的:3是指到3为止，不包括3号。

#如果要将前3个外星人修改为黄色、速度中等且值10分
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

for alien in aliens[:5]:
	print(alien)
print("...")

#当然也可以添加elif命令，以检查除了if外的符合某个条件的元素集合

#在字典中存储列表
#以披萨店为例
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],#这里就是列表
	}
print(f"you ordered a {pizza['crust']}-crust pizza "
	"with the follow toppings")
for topping in pizza['toppings']:
	print(f"\t{topping}")
#在遍历列表时，输出结果会自动换行
#以喜欢的语言为例
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell']
	}
for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")
#当然还可以用len()函数来检查喜欢的语言有多少种
#如果只有一种，就可以修改措辞为单数
##列表和字典的嵌套层级不应该太多，如果套了太多层，很有可能有更简单的解决方案

#字典套字典
#一般涉及到这种情况都是用来存储用户信息的
#网站运营一般都是用id来作为识别用户的基本key的
#而每个id下面又有诸如姓名性别年龄和喜好等次级键
users = {
	'aeinstein':{
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
				},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
				},
	}

for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']
	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")


#用户输入和while循环
#本章将主要介绍input()函数
#由于sublime不能运行提示用户输入的程序，我们需要用控制台来完成下面的例子。