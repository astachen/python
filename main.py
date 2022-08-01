# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_var():
    """
    使用变量保存数据并进行加减乘除运算

    Version: 0.1
    Author: 骆昊
    """
    a = 32
    b = 8
    print(a + b)  # 333
    print(a - b)  # 309
    print(a * b)  # 3852
    print(a / b)  # 26.75
    print(a % b)  #
    print(a // b)  #

    # TIPS / 产生浮点数，整数要做强制转换 @astatim
    i = a / b + 5
    print(int(i))  #guess


def type_var():
    """
    使用type()检查变量的类型

    Version: 0.1
    Author: 骆昊
    """
    a = 100
    b = 12.345
    c = 1 + 5j
    d = 'hello, world'
    e = True
    f = int(e)
    print(type(a))  # <class 'int'>
    print(type(b))  # <class 'float'>
    print(type(c))  # <class 'complex'>
    print(type(d))  # <class 'str'>
    print(type(e))  # <class 'bool'>
    print(f)  #
    print(type(f))  #


def var_convert():
    """
    使用int()等内置函数对变量类型进行转换

    Version: 0.1
    Author:
    """
    a = 100
    b = 12.345
    c = 1 + 5j
    d = 'hello, world'
    e = True

    print(int(b))
    # print(int(c))
    # print(int(d))
    # print(float(d))
    print(str(a))
    print(str(b))
    print(str(c))
    print((chr(a)))
    # https://www.habaijian.com/ ASCII码对照表
    for i in range(255):
        print(str(i) + ": " + chr(i))

    fo = open("foo.txt", "wb")

    buf = bytes(chr(e), encoding="utf8")
    fo.write(buf)
    fo.close()

    # print(ord(d))


def int_compute():
    """
    使用input()函数获取键盘输入(字符串)
    使用int()函数将输入的字符串转换成整数
    使用print()函数输出带占位符的字符串

    Version: 0.1
    Author: 骆昊
    """
    a = int(input('a = '))
    b = int(input('b = '))
    print('%d + %d = %d' % (a, b, a + b))
    print('%d - %d = %d' % (a, b, a - b))
    print('%d * %d = %d' % (a, b, a * b))
    print('%d / %d = %f' % (a, b, a / b))
    print('%d // %d = %d' % (a, b, a // b))
    print('%d %% %d = %d' % (a, b, a % b))
    print('%d ** %d = %d' % (a, b, a ** b))


def var_initiate():
    """
    赋值运算符和复合赋值运算符

    Version: 0.1
    Author: 骆昊
    """
    a = 10
    b = 3
    a += b  # 相当于：a = a + b
    a *= a + 2  # 相当于：a = a * (a + 2)
    print(a)  # 算一下这里会输出什么


def var_compare():
    """
    比较运算符和逻辑运算符的使用

    Version: 0.1
    Author: 骆昊
    """
    flag0 = 1 == 1
    flag1 = 3 > 2
    flag2 = 2 < 1
    flag3 = flag1 and flag2
    flag4 = flag1 or flag2
    flag5 = not (1 != 2)
    print('flag0 =', flag0)  # flag0 = True
    print('flag1 =', flag1)  # flag1 = True
    print('flag2 =', flag2)  # flag2 = False
    print('flag3 =', flag3)  # flag3 = False
    print('flag4 =', flag4)  # flag4 = True
    print('flag5 =', flag5)  # flag5 = False


def temperature_convert():
    """
    将华氏温度转换为摄氏温度

    Version: 0.1
    Author: 骆昊
    """
    f = float(input('请输入华氏温度: '))
    c = (f - 32) / 1.8
    print('%.1f华氏度 = %.1f摄氏度' % (f, c))


def circle_calculate():
    """
    输入半径计算圆的周长和面积

    Version: 0.1
    Author: 骆昊
    """
    radius = float(input('请输入圆的半径: '))
    perimeter = 2 * 3.1416 * radius
    area = 3.1416 * radius * radius
    print('周长: %.2f' % perimeter)
    print('面积: %.2f' % area)


def leap_year():
    """
    输入年份 如果是闰年输出True 否则输出False

    Version: 0.1
    Author: 骆昊
    """
    year = int(input('请输入年份: '))
    # 如果代码太长写成一行不便于阅读 可以使用\对代码进行折行
    is_leap = year % 4 == 0 and year % 100 != 0 or \
              year % 400 == 0
    print(is_leap)


def identification():
    """
    用户身份验证

    Version: 0.1
    Author: 骆昊
    """
    username = input('请输入用户名: ')
    password = input('请输入口令: ')
    # 用户名是admin且密码是123456则身份验证成功否则身份验证失败
    if username == 'admin' and password == '123456':
        print('身份验证成功!')
    else:
        print('身份验证失败!')


def part_function():
    """
    分段函数求值
            3x - 5	(x > 1)
    f(x) =	x + 2	(-1 <= x <= 1)
            5x + 3	(x < -1)

    Version: 0.1
    Author: 骆昊
    """

    x = float(input('x = '))
    if x > 1:
        y = 3 * x - 5
    else:
        if x >= -1:
            y = x + 2
        else:
            y = 5 * x + 3
    print('f(%.2f) = %.2f' % (x, y))


def meter_change():
    """
    英制单位英寸和公制单位厘米互换

    Version: 0.1
    Author: 骆昊
    """
    value = float(input('请输入长度: '))
    unit = input('请输入单位: ')
    if unit == 'in' or unit == '英寸':
        print('%f英寸 = %f厘米' % (value, value * 2.54))
    elif unit == 'cm' or unit == '厘米':
        print('%f厘米 = %f英寸' % (value, value / 2.54))
    else:
        print('请输入有效的单位')


def grade_change():
    """
    百分制成绩转换为等级制成绩

    Version: 0.1
    Author: 骆昊
    """
    score = float(input('请输入成绩: '))
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'E'
    print('对应的等级是:', grade)


def triangle_determine():
    """
    判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积

    Version: 0.1
    Author: 骆昊
    """
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    if a + b > c and a + c > b and b + c > a:
        print('周长: %f' % (a + b + c))
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print('面积: %f' % (area))
    else:
        print('不能构成三角形')


def sum_loop():
    """
    用for循环实现1~100求和

    Version: 0.1
    Author: 骆昊
    """

    sum = 0
    for x in range(101):
        sum += x
    print(sum)


def second_loop1():
    """
    用for循环实现1~100之间的偶数求和

    Version: 0.1
    Author: 骆昊
    """

    sum = 0
    for x in range(2, 101, 2):
        sum += x
    print(sum)


def second_loop2():
    """
    用for循环实现1~100之间的偶数求和

    Version: 0.1
    Author: 骆昊
    """

    sum = 0
    for x in range(1, 101):
        if x % 2 == 0:
            sum += x
    print(sum)


def number_game():
    """
    猜数字游戏

    Version: 0.1
    Author: 骆昊
    """
    import random

    answer = random.randint(1, 100)
    counter = 0
    while True:
        counter += 1
        number = int(input('请输入: '))
        if number < answer:
            print('大一点')
        elif number > answer:
            print('小一点')
        else:
            print('恭喜你猜对了!')
            break
    print('你总共猜了%d次' % counter)
    if counter > 7:
        print('你的智商余额明显不足')


def multiply_table():
    """
    输出乘法口诀表(九九表)

    Version: 0.1
    Author: 骆昊
    """

    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%d*%d=%d' % (i, j, i * j), end='\t')
        print()


def prime_number():
    """
    输入一个正整数判断它是不是素数

    Version: 0.1
    Author: 骆昊
    Date: 2018-03-01
    """
    from math import sqrt

    num = int(input('请输入一个正整数: '))
    end = int(sqrt(num))
    is_prime = True
    for x in range(2, end + 1):
        if num % x == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        print('%d是素数' % num)
    else:
        print('%d不是素数' % num)


def special_multiply():
    """
    输入两个正整数计算它们的最大公约数和最小公倍数

    Version: 0.1
    Author: 骆昊
    Date: 2018-03-01
    """

    x = int(input('x = '))
    y = int(input('y = '))
    # 如果x大于y就交换x和y的值
    if x > y:
        # 通过下面的操作将y的值赋给x, 将x的值赋给y
        x, y = y, x
    # 从两个数中较小的数开始做递减的循环
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            print('%d和%d的最大公约数是%d' % (x, y, factor))
            print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
            break


def print_triangle():
    """
    打印三角形图案

    Version: 0.1
    Author: 骆昊
    """

    row = int(input('请输入行数: '))
    for i in range(row):
        for _ in range(i + 1):
            print('*', end='')
        print()

    for i in range(row):
        for j in range(row):
            if j < row - i - 1:
                print(' ', end='')
            else:
                print('*', end='')
        print()

    for i in range(row):
        for _ in range(row - i - 1):
            print(' ', end='')
        for _ in range(2 * i + 1):
            print('*', end='')
        print()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def armstrong_number():
    """
    找出所有水仙花数

    Version: 0.1
    Author: 骆昊
    """

    for num in range(100, 1000):
        low = num % 10
        mid = num // 10 % 10
        high = num // 100
        if num == low ** 3 + mid ** 3 + high ** 3:
            print(num)


def reverse_number():
    """
    正整数的反转

    Version: 0.1
    Author: 骆昊
    """

    num = int(input('num = '))
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    print(reversed_num)


def chicken_question():
    """
    《百钱百鸡》问题

    Version: 0.1
    Author: 骆昊
    """

    for x in range(0, 20):
        for y in range(0, 33):
            z = 100 - x - y
            if 5 * x + 3 * y + z / 3 == 100:
                print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))


def craps_gambling():
    """
    Craps赌博游戏
    我们设定玩家开始游戏时有1000元的赌注
    游戏结束的条件是玩家输光所有的赌注

    Version: 0.1
    Author: 骆昊
    """
    from random import randint

    money = 1000
    while money > 0:
        print('你的总资产为:', money)
        needs_go_on = False
        while True:
            debt = int(input('请下注: '))
            if 0 < debt <= money:
                break
        first = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % first)
        if first == 7 or first == 11:
            print('玩家胜!')
            money += debt
        elif first == 2 or first == 3 or first == 12:
            print('庄家胜!')
            money -= debt
        else:
            needs_go_on = True
        while needs_go_on:
            needs_go_on = False
            current = randint(1, 6) + randint(1, 6)
            print('玩家摇出了%d点' % current)
            if current == 7:
                print('庄家胜')
                money -= debt
            elif current == first:
                print('玩家胜')
                money += debt
            else:
                needs_go_on = True
    print('你破产了, 游戏结束!')


def apple_function():
    """
    输入M和N计算C(M,N)

    Version: 0.1
    Author: 骆昊
    """
    m = int(input('m = '))
    n = int(input('n = '))
    fm = 1
    for num in range(1, m + 1):
        fm *= num
    fn = 1
    for num in range(1, n + 1):
        fn *= num
    fm_n = 1
    for num in range(1, m - n + 1):
        fm_n *= num
    print(fm // fn // fm_n)


def apple_simplized():
    """
    输入M和N计算C(M,N)

    Version: 0.1
    Author: 骆昊
    """

    def fac(num):
        """求阶乘"""
        result = 1
        for n in range(1, num + 1):
            result *= n
        return result

    m = int(input('m = '))
    n = int(input('n = '))
    # 当需要计算阶乘的时候不用再写循环求阶乘而是直接调用已经定义好的函数
    print(fac(m) // fac(n) // fac(m - n))


def dice():
    from random import randint

    def roll_dice(n=2):
        """摇色子"""
        total = 0
        for _ in range(n):
            total += randint(1, 6)
        return total

    def add(a=0, b=0, c=0):
        """三个数相加"""
        return a + b + c

    # 如果没有指定参数那么使用默认值摇两颗色子
    print(roll_dice())
    # 摇三颗色子
    print(roll_dice(3))
    print(add())
    print(add(1))
    print(add(1, 2))
    print(add(1, 2, 3))
    # 传递参数时可以不按照设定的顺序进行传递
    print(add(c=50, a=100, b=200))


def dice_add():
    # 在参数名前面的*表示args是一个可变参数
    def add(*args):
        total = 0
        for val in args:
            total += val
        return total

    # 在调用add函数时可以传入0个或多个参数
    print(add())
    print(add(1))
    print(add(1, 2))
    print(add(1, 2, 3))
    print(add(1, 3, 5, 7, 9))


def same_name():
    def foo():
        print('hello, world!')

    def foo():
        print('goodbye, world!')

    # 下面的代码会输出什么呢？
    foo()


def same_name_solution():
    from module1 import foo

    # 输出hello, world!
    foo()

    from module2 import foo

    # 输出goodbye, world!
    foo()

    import module1 as m1
    import module2 as m2

    m1.foo()
    m2.foo()


def import_proceed():
    import module3

    # 导入module3时 不会执行模块中if条件成立时的代码 因为模块的名字是module3而不是__main__


def gcd_lcm():
    def gcd(x, y):
        """求最大公约数"""
        (x, y) = (y, x) if x > y else (x, y)
        for factor in range(x, 0, -1):
            if x % factor == 0 and y % factor == 0:
                return factor

    def lcm(x, y):
        """求最小公倍数"""
        return x * y // gcd(x, y)


def palindrome_prime():
    num = int(input("请输入数字："))

    def is_palindrome(num):
        """判断一个数是不是回文数"""
        temp = num
        total = 0
        while temp > 0:
            total = total * 10 + temp % 10
            temp //= 10
        return total == num

    def is_prime(num):
        """判断一个数是不是素数"""
        for factor in range(2, int(num ** 0.5) + 1):
            if num % factor == 0:
                return False
        return True if num != 1 else False

    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数' % num)


def variable_definitive():
    def foo():
        b = 'hello'

        # Python中可以在函数内部再定义函数
        def bar():
            c = True
            print(a)
            print(b)
            print(c)

        bar()
        # print(c)  # NameError: name 'c' is not defined

    if __name__ == '__main__':
        a = 100
        # print(b)  # NameError: name 'b' is not defined
        foo()

    def foo():
        a = 200
        print(a)  # 200

    if __name__ == '__main__':
        a = 100
        foo()
        print(a)  # 100

    def foo():
        global a
        a = 200
        print(a)  # 200

    if __name__ == '__main__':
        a = 100
        foo()
        print(a)  # 200

    def main():
        # Todo: Add your code here
        pass

    if __name__ == '__main__':
        main()


def string_def():
    s1 = 'hello, world!'
    s2 = "hello, world!"
    # 以三个双引号或单引号开头的字符串可以折行
    s3 = """
    hello, 
    world!
    """
    print(s1, s2, s3, end='')

    # `\`后面的字符不再是它原来的意义
    s1 = '\'hello, world!\''
    s2 = '\n\\hello, world!\\\n'
    print(s1, s2, end='')

    # 在`\`后面还可以跟一个八进制或者十六进制数来表示字符
    s1 = '\141\142\143\x61\x62\x63'
    s2 = '\u9a86\u660a'
    print(s1, s2)

    # 如果不希望字符串中的`\`表示转义，我们可以通过在字符串的最前面加上字母`r`来加以说明
    s1 = r'\'hello, world!\''
    s2 = r'\n\\hello, world!\\\n'
    print(s1, s2, end='')


def string_compute():
    s1 = 'hello ' * 3
    print(s1)  # hello hello hello
    s2 = 'world'
    s1 += s2
    print(s1)  # hello hello hello world
    print('ll' in s1)  # True
    print('good' in s1)  # False
    str2 = 'abc123456'

    # 从字符串中取出指定位置的字符(下标运算)
    print(str2[2])  # c

    # 字符串切片(从指定的开始索引到指定的结束索引)
    print(str2[2:5])  # c12
    print(str2[2:])  # c123456
    print(str2[2::2])  # c246
    print(str2[::2])  # ac246
    print(str2[::-1])  # 654321cba
    print(str2[-3:-1])  # 45

    str1 = 'hello, world!'

    # 通过内置函数len计算字符串的长度
    print(len(str1))  # 13

    # 获得字符串首字母大写的拷贝
    print(str1.capitalize())  # Hello, world!

    # 获得字符串每个单词首字母大写的拷贝
    print(str1.title())  # Hello, World!

    # 获得字符串变大写后的拷贝
    print(str1.upper())  # HELLO, WORLD!

    # 从字符串中查找子串所在位置
    print(str1.find('or'))  # 8
    print(str1.find('shit'))  # -1

    # 与find类似但找不到子串时会引发异常
    # print(str1.index('or'))
    # print(str1.index('shit'))

    # 检查字符串是否以指定的字符串开头
    print(str1.startswith('He'))  # False
    print(str1.startswith('hel'))  # True

    # 检查字符串是否以指定的字符串结尾
    print(str1.endswith('!'))  # True

    # 将字符串以指定的宽度居中并在两侧填充指定的字符
    print(str1.center(50, '*'))

    # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    print(str1.rjust(50, ' '))


    str2 = 'abc123456'

    # 检查字符串是否由数字构成
    print(str2.isdigit())  # False

    # 检查字符串是否以字母构成
    print(str2.isalpha())  # False

    # 检查字符串是否以数字和字母构成
    print(str2.isalnum())  # True
    str3 = '  jackfrued@126.com '
    print(str3)

    # 获得字符串修剪左右两侧空格之后的拷贝
    print(str3.strip())

def string_reformat():
    a, b = 5, 10
    print('%d * %d = %d' % (a, b, a * b))

    # 当然，我们也可以用字符串提供的方法来完成字符串的格式，代码如下所示。
    a, b = 5, 10
    print('{0} * {1} = {2}'.format(a, b, a * b))

    # Python 3.6 以后，格式化字符串还有更为简洁的书写方式，就是在字符串前加上字母`f`，我们可以使用下面的语法糖来简化上面的代码。
    a, b = 5, 10
    print(f'{a} * {b} = {a * b}')

def list_def():
    list1 = [1, 3, 5, 7, 100]
    print(list1)  # [1, 3, 5, 7, 100]

    # 乘号表示列表元素的重复
    list2 = ['hello'] * 3
    print(list2)  # ['hello', 'hello', 'hello']

    # 计算列表长度(元素个数)
    print(len(list1))  # 5

    # 下标(索引)运算
    print(list1[0])  # 1
    print(list1[4])  # 100
    # print(list1[5])  # IndexError: list index out of range
    print(list1[-1])  # 100
    print(list1[-3])  # 5
    list1[2] = 300
    print(list1)  # [1, 3, 300, 7, 100]

    # 通过循环用下标遍历列表元素
    for index in range(len(list1)):
        print(list1[index])

    # 通过for循环遍历列表元素
    for elem in list1:
        print(elem)

    # 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
    for index, elem in enumerate(list1):
        print(index, elem)

def array_compute():
    list1 = [1, 3, 5, 7, 100]

    # 添加元素
    list1.append(200)
    list1.insert(1, 400)

    # 合并两个列表
    # list1.extend([1000, 2000])
    list1 += [1000, 2000]
    print(list1)  # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
    print(len(list1))  # 9

    # 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
    if 3 in list1:
        list1.remove(3)
    if 1234 in list1:
        list1.remove(1234)
    print(list1)  # [1, 400, 5, 7, 100, 200, 1000, 2000]

    # 从指定的位置删除元素
    list1.pop(0)
    list1.pop(len(list1) - 1)
    print(list1)  # [400, 5, 7, 100, 200, 1000]

    # 清空列表元素
    list1.clear()
    print(list1)  # []

    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']

    # 列表切片
    fruits2 = fruits[1:4]
    print(fruits2)  # apple strawberry waxberry

    # 可以通过完整切片操作来复制列表
    fruits3 = fruits[:]
    print(fruits3)  # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
    fruits4 = fruits[-3:-1]
    print(fruits4)  # ['pitaya', 'pear']

    # 可以通过反向切片操作来获得倒转后的列表的拷贝
    fruits5 = fruits[::-1]
    print(fruits5)  # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']

def list_compute():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']

    # 列表切片
    fruits2 = fruits[1:4]
    print(fruits2)  # apple strawberry waxberry

    # 可以通过完整切片操作来复制列表
    fruits3 = fruits[:]
    print(fruits3)  # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
    fruits4 = fruits[-3:-1]
    print(fruits4)  # ['pitaya', 'pear']

    # 可以通过反向切片操作来获得倒转后的列表的拷贝
    fruits5 = fruits[::-1]
    print(fruits5)  # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']


def list_sort():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用
    list3 = sorted(list1, reverse=True)

    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    list4 = sorted(list1, key=len)
    print(list1)
    print(list2)
    print(list3)
    print(list4)

    # 给列表对象发出排序消息直接在列表对象上进行排序
    list1.sort(reverse=True)
    print(list1)

def generator_function():
    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
            yield a

    def main():
        for val in fib(20):
            print(val)

    if __name__ == '__main__':
        main()

def list_tuple():
    # 定义元组
    t = ('骆昊', 38, True, '四川成都')
    print(t)

    # 获取元组中的元素
    print(t[0])
    print(t[3])

    # 遍历元组中的值
    for member in t:
        print(member)

    # 重新给元组赋值
    # t[0] = '王大锤'  # TypeError
    # 变量t重新引用了新的元组原来的元组将被垃圾回收
    t = ('王大锤', 20, True, '云南昆明')
    print(t)

    # 将元组转换成列表
    person = list(t)
    print(person)

    # 列表是可以修改它的元素的
    person[0] = '李小龙'
    person[1] = 25
    print(person)

    # 将列表转换成元组
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)

def list_set():
    # 创建集合的字面量语法
    set1 = {1, 2, 3, 3, 3, 2}
    print(set1)
    print('Length =', len(set1))

    # 创建集合的构造器语法(面向对象部分会进行详细讲解)
    set2 = set(range(1, 10))
    set3 = set((1, 2, 3, 3, 2, 1))
    print(set2, set3)

    # 创建集合的推导式语法(推导式也可以用于推导集合)
    set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
    print(set4)

    # 向集合添加元素和从集合删除元素

    set1.add(4)
    set1.add(5)
    set2.update([11, 12])
    set2.discard(5)
    if 4 in set2:
        set2.remove(4)
    print(set1, set2)
    print(set3.pop())
    print(set3)

    # 集合的交集、并集、差集、对称差运算
    print(set1 & set2)
    # print(set1.intersection(set2))
    print(set1 | set2)
    # print(set1.union(set2))
    print(set1 - set2)
    # print(set1.difference(set2))
    print(set1 ^ set2)
    # print(set1.symmetric_difference(set2))

    # 判断子集和超集
    print(set2 <= set1)
    # print(set2.issubset(set1))
    print(set3 <= set1)
    # print(set3.issubset(set1))
    print(set1 >= set2)
    # print(set1.issuperset(set2))
    print(set1 >= set3)
    # print(set1.issuperset(set3))

def list_dictionary():
    # 创建字典的字面量语法
    scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
    print(scores)

    # 创建字典的构造器语法
    items1 = dict(one=1, two=2, three=3, four=4)

    # 通过zip函数将两个序列压成字典
    items2 = dict(zip(['a', 'b', 'c'], '123'))

    # 创建字典的推导式语法
    items3 = {num: num ** 2 for num in range(1, 10)}
    print(items1, items2, items3)

    # 通过键可以获取字典中对应的值
    print(scores['骆昊'])
    print(scores['狄仁杰'])

    # 对字典中所有键值对进行遍历
    for key in scores:
        print(f'{key}: {scores[key]}')

    # 更新字典中的元素
    scores['白元芳'] = 65
    scores['诸葛王朗'] = 71
    scores.update(冷面=67, 方启鹤=85)
    print(scores)
    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))

    # get方法也是通过键获取对应的值但是可以设置默认值
    print(scores.get('武则天', 60))

    # 删除字典中的元素
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('骆昊', 100))

    # 清空字典
    scores.clear()
    print(scores)

def show_context():
    import os
    import time

    def main():
        content = '北京欢迎你为你开天辟地…………'
        while True:
            # 清理屏幕上的输出
            os.system('cls')  # os.system('clear')
            print(content)
            # 休眠200毫秒
            time.sleep(0.2)
            content = content[1:] + content[0]

    if __name__ == '__main__':
        main()

def generate_classifycode():
    import random

    def generate_code(code_len=4):
        """
        生成指定长度的验证码

        :param code_len: 验证码的长度(默认4个字符)

        :return: 由大小写英文字母和数字构成的随机验证码
        """
        all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        last_pos = len(all_chars) - 1
        code = ''
        for _ in range(code_len):
            index = random.randint(0, last_pos)
            code += all_chars[index]
        return code

def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''

def max2(x):
        m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
        for index in range(2, len(x)):
            if x[index] > m1:
                m2 = m1
                m1 = x[index]
            elif x[index] > m2:
                m2 = x[index]
        return m1, m2

def is_leap_year(year):
    """
    判断指定的年份是不是闰年

    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    """
    计算传入的日期是这一年的第几天

    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date


def Yanghui_triangle():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


    if __name__ == '__main__':
        Yanghui_triangle()


def double_colors_balls():
    from random import randrange, randint, sample

    def display(balls):
        """
        输出列表中的双色球号码
        """
        for index, ball in enumerate(balls):
            if index == len(balls) - 1:
                print('|', end=' ')
            print('%02d' % ball, end=' ')
        print()

    def random_select():
        """
        随机选择一组号码
        """
        red_balls = [x for x in range(1, 34)]
        selected_balls = []
        selected_balls = sample(red_balls, 6)
        selected_balls.sort()
        selected_balls.append(randint(1, 16))
        return selected_balls

    def main():
        n = int(input('机选几注: '))
        for _ in range(n):
            display(random_select())

    if __name__ == '__main__':
        main()

def joseph_ring():
    def main():
        persons = [True] * 30
        counter, index, number = 0, 0, 0
        while counter < 15:
            if persons[index]:
                number += 1
                if number == 9:
                    persons[index] = False
                    counter += 1
                    number = 0
            index += 1
            index %= 30
        for person in persons:
            print('基' if person else '非', end='')

    if __name__ == '__main__':
        main()

def cross_chess():
    import os

    def print_board(board):
        print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
        print('-+-+-')
        print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
        print('-+-+-')
        print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

    def main():
        init_board = {
            'TL': ' ', 'TM': ' ', 'TR': ' ',
            'ML': ' ', 'MM': ' ', 'MR': ' ',
            'BL': ' ', 'BM': ' ', 'BR': ' '
        }
        begin = True
        while begin:
            curr_board = init_board.copy()
            begin = False
            turn = 'x'
            counter = 0
            os.system('clear')
            print_board(curr_board)
            while counter < 9:
                move = input('轮到%s走棋, 请输入位置: ' % turn)
                if curr_board[move] == ' ':
                    counter += 1
                    curr_board[move] = turn
                    if turn == 'x':
                        turn = 'o'
                    else:
                        turn = 'x'
                os.system('clear')
                print_board(curr_board)
            choice = input('再玩一局?(yes|no)')
            begin = choice == 'yes'

    if __name__ == '__main__':
        main()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # print_var()
    # type_var()
    # var_convert()
    # int_compute()
    # var_initiate()
    # var_compare()
    # temperature_convert()
    # circle_calculate()
    # leap_year()
    # identification()
    # meter_change()
    # grade_change()
    # triangle_determine()
    # sum_loop()
    # second_loop1()
    # second_loop2()
    # number_game()
    # multiply_table()
    # prime_number()
    # special_multiply()
    # print_triangle()
    # armstrong_number()
    # reverse_number()
    # chicken_question()
    # craps_gambling()
    # apple_function()
    # apple_simplized()
    # dice()
    # dice_add()
    # same_name()
    # same_name_solution()
    # import_proceed()
    # gcd_lcm()
    # palindrome_prime()
    # variable_definitive()
    # string_def()
    # string_compute()
    # string_reformat()
    # list_sort()
    # generator_function()
    # list_tuple()
    # list_set()
    # list_dictionary()
    # show_context()
    # generate_classifycode()
    # get_suffix()
    # max2()
    # is_leap_year()
    # which_day()
    # Yanghui_triangle()
    # double_colors_balls()
    # joseph_ring()
    # cross_chess()




# mingge


def initialize():
    age = 18
    name = "王炳明"
    a = b = c = 1
    anotherAge = 17 + 1
    d, e, f = 1, 2, 3
    PI = 3.14159265359


def string_id():
    a = "Jack"
    b = a  # Jack
    id(a)
    id(b)
    a = "Tom"
    id(a)
    id(b)


def string_initialize():
    name_1 = 'Jack'  # 单引号
    name_2 = "Jack"  # 双引号
    name_3 = '''Jack'''  # 三个单引号
    name_4 = """Jack"""  # 三个双引号
    msg = "my name is 'Jack'"


def string_method():
    msg = "    Python编程时光    "
    msg.lstrip()  # 去除左边空格
    # 'Python编程时光    '
    msg.rstrip()  # 去除右边空格
    # '    Python编程时光'
    msg.strip()  # 去除左右两边空格
    # 'Python编程时光'
    msg = "Hello, Python"
    msg.startswith("Hello")
    msg.startswith("hello")
    msg.endswith("Python")
    msg.endswith("python")
    name = "王炳明"
    msg = f"你好，我是{name}"  # '你好，我是王炳明'
    languages = "Python,Java,Golang"
    languages.split(",")  # ['Python', 'Java', 'Golang']


def num_type():
    a = 100
    type(a)
    b = -100
    type(b)
    a = 1.23
    type(a)
    a = 10 + 0.2j
    type(a)
    b = complex(10, 0.2)
    type(b)


def num_method():
    a = 10
    b = 20
    print(a + b)
    print(b - a)
    print(a * b)
    print(b / a)
    b = 3
    print(a // b)
    print(a % b)
    a = -10
    print(abs(a))
    a = 3.14
    print(int(a))
    b = 3.78
    print(int(b))
    print(round(a))
    print(round(b))


def if_age():
    age = 16

    if age >= 18:
        print("你是个成年人")
    else:
        print("你还未成年")


def boolean_method():
    print(3 > 2)
    print(3 > 5)
    print(3 in [1, 2, 3])
    print(3 == 9 / 3)
    bool(1)  # True
    bool(0)  # False
    bool([])  # False
    bool(())  # False
    bool({})  # False
    bool(-1)  # True
    bool('')  # False
    bool(None)  # False
    bool("False")  # True
    bool("True")  # True
    bool(0.0)  # False
    bool(1.0)  # True
    bool(-0.0)  # False


def boolean_compute():
    print(True and True)  # True
    print(True and False)  # False
    print(False and False)  # False
    print(5 > 3 and 3 > 1)  # True

    # or运算是或运算，只要其中有一个为True，or运算结果就是True：
    print(True or True)  # True
    print(True or False)  # True
    print(False or False)  # False
    print(5 > 3 or 1 > 3)  # True

    # not运算是非运算，它是单目运算符，把True变成False，False变成True：
    print(not True)  # False
    print(not False)  # True
    print(not 1 > 2)  # True
    print(True > False)  # True
    print(True < False)  # False
    print(True >= False)  # True
    print(True - 1)  # 0
    print(True + 1)  # 2
    print(True * 3)  # 3
    print(False - 1)  # -1


def decimal_compute():
    a = 60  # 60 = 0011 1100
    b = 13  # 13 = 0000 1101
    c = 0

    # 与运算
    print(a & b)  # 12 = 0000 1100

    # 或运算
    print(a | b)  # 61 = 0011 1101

    # 异或运算
    print(a ^ b)  # 49 = 0011 0001

    # 取反运算
    print(~a)  # -61 = 1100 0011

    # 左移动运算符
    print(a << 2)  # 240 = 1111 0000

    # 右移动运算符
    print(a >> 2)  # 15 = 0000 1111


def if_score():
    score = 75
    if score >= 90:
        print("优秀")
    elif score >= 80:
        print("良好")
    elif score >= 70:
        print("一般")
    elif score >= 60:
        print("合格")
    else:
        print("不合格")


def for_loop():
    phones = ["Apple", "Huawei", "Xiaomi"]
    for phone in phones:
        print("当前手机是: " + phone)


def index_loop():
    phones = ["Apple", "Huawei", "Xiaomi"]
    for index, phone in enumerate(phones):
        print("我的第 {} 把手机是: {}".format(index + 1, phone))


def break_loop():
    for i in [0, 1, 2]:
        if i == 1:
            print(f"当前的数是 {i}, 将退出循环")
            break
    print("当前的数是 " + str(i))


def continue_loop():
    for i in [0, 1, 2]:
        if i == 1:
            continue
    print("当前的数是 " + str(i))


def for_else():
    for i in [0, 1, 2]:
        if i == 1:
            continue
        print("当前的数是 " + str(i))
    else:
        print("循环非常正常")


def for_else2():
    for i in [0, 1, 2]:
        if i == 1:
            break
        print("当前的数是 " + str(i))
    else:
        print("循环非常正常")


def while_loop():
    age = 1
    while age <= 3:
        print(f"孩子当前 {age} 岁，还不能上幼儿园")
        age += 1

    print("年龄够了，可以上幼儿园了")


def while_else():
    age = 1
    while age <= 3:
        print(f"我已经 {age} 岁了")
        age += 1
    else:
        print("可以上幼儿园了")

    age = 1
    while age <= 3:
        ...
        if age == 2:
            break
        print(f"我已经 {age} 岁了")
        age += 1
    else:
        print("可以上幼儿园了")


def comprehensions():
    # 列表推导式
    # 找出一个数值列表中为偶数的元素，并组成新列表
    old_list = [0, 1, 2, 3, 4, 5]
    new_list = [item for item in old_list if item % 2 == 0]
    print(new_list)  # output: [0, 2, 4]# [0, 2, 4]

    # 字典推导式
    # 从一个包含所有学生成绩信息的字典中，找出数学考满分的同学
    old_student_score_info = {
        "Jack": {
            "chinese": 87,
            "math": 92,
            "english": 78
        },
        "Tom": {
            "chinese": 92,
            "math": 100,
            "english": 89
        }
    }

    new_student_score_info = {name: scores for name, scores in old_student_score_info.items() if scores["math"] == 100}
    print(new_student_score_info)  # output: {'Tom': {'chinese': 92, 'math': 100, 'english': 89}}

    # 集合推导式
    # 把一个数值列表里的数进行去重处理
    old_list = [0, 0, 0, 1, 2, 3]
    new_set = {item for item in old_list}
    print(new_set)  # {0, 1, 2, 3}

    # 生成器推导式
    # 找出一个数值列表中所有的偶数
    old_list = [0, 1, 2, 3, 4, 5]
    new_list = (item for item in old_list if item % 2 == 0)
    for i in new_list:
        print(i)

    # 嵌套推导式
    # 打印一个乘法表
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{}x{}={}\t'.format(j, i, i * j), end='')
        print("")


if __name__ == '__main__':
    # initialize()
    # string_id()
    # string_initialize()
    # num_type()
    # num_method()
    # if_age()
    # boolean_method()
    # boolean_compute()
    # decimal_compute()
    # if_score()
    # for_loop()
    # index_loop()
    # while_loop()
    # while_else()
    comprehensions()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
