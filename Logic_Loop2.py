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