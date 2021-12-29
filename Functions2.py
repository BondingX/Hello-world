#传递任意数量的实参
#如果披萨店无法预先确定顾客要多少种调料怎么办？
def make_pizza(*toppings):
    """打印顾客点的所有配料。"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
#星号*是创建元组的意思，可将收到的所有值都封装到这个元组中。

#下面将print()替换为一个循环，遍历配料列表并对顾客点的披萨进行描述
def make_pizza(*toppings):
    """概述要制作的披萨"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:#遍历元组
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#如果要让函数接受不同类型的实参
#必须在函数定义中将接纳任意数量实参的形参放在最后
#这样Python就会先匹配位置实参和关键字实参
#最后将余下的实参都收集到最后一个形参中

