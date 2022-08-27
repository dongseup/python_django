# 071
my_variable = ()
print(type(my_variable))

# 072
movie_rank = ("닥터 스트레인지", "스필릿", "럭키")

# 073
tp = (1,)
print(type(tp))

# 074
# 튜플은 수정불가

# 075
t = 1, 2, 3, 4
print(type(t))

# 076
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
print(t)

# 077
interest = ('삼성전자', 'LG전자', 'SK Hynix')
print(list(interest))

# 078
interest = ['삼성전자', 'LG전자', 'SK Hynix']
print(tuple(interest))

# 079 튜플 언팩킹
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

# 080 range 함수
num = tuple(range(2, 100, 2))
print(num)
