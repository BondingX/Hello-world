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
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien)
print("...")
print(f"Total number of aliens: {len(aliens)}")