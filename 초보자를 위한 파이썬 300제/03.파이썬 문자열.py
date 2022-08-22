# 021 문자열 인덱싱
letters = 'python'
print(letters[0], letters[2])

# 022 문자열 슬라이싱
license_plate = '24가 2210'
print(license_plate[4:])
print(license_plate[-4:])

# 023 문자열 인덱싱
string = '홀짝홀짝홀짝'
print(string[::2])

# 024 문자열 슬라이싱
string = 'PYTHON'
print(string[::-1])

# 025 문자열 치환
phone_number = "010-1111-2222"
re = phone_number.replace("-", " ")
print(re)

# 026 문자열 다루기
re2 = phone_number.replace("-", "")
print(re2)

# 027 문자열 다루기
url = "http://sharebook.kr"
print(url[-2:])
print(url.split('.')[1])

# 028 문자열은 immutable
# lang = 'python'
# lang[0] = 'P'
# print(lang)

# 029 replace 메서드
string = 'abcdfe2a354a32a'
print(string.replace('a', 'A'))

# 030 replace 메서드
string = 'abcd'
b = string.replace('b', 'B')
print(string)
print(b)

# 031 문자열 합치기
a = '3'
b= '4'
print(a + b)

# 032 문자열 곱하기
print('Hi' * 3)

# 033 문자열 곱하기
print('-' * 80)

# 034 문자열 곱하기
t1 = 'python'
t2 = 'java'
print((t1 + ' ' + t2 + ' ') * 4)

# 035 문자열 출력
name1 = '김민수'
age1 = 10
name2 = '이철희'
age2 = 13
print('이름: %s 나이: %d' % (name1, age1))
print('이름: %s 나이: %d' % (name2, age2))

# 036 문자열 출력
print('이름: {0} 나이: {1}'.format(name1, age1))
print('이름: {0} 나이: {1}'.format(name2, age2))

# 037 문자열 출력
print(f'이름: {name1} 나이: {age1}')
print(f'이름: {name2} 나이: {age2}')

# 038 컴마 제거하기
상장주식수 = "5,969,782,550"
re =상장주식수.replace(',', '')
print(int(re), type(re))

# 039 문자열 슬라이싱
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

#040 strip 메서드
data = "   삼성전자    "
print(data.strip())

# 041 upper 메서드
ticker = "btc_krw"
print(ticker.upper())

# 042 lower 메서드
ticker = "BTC_KRW"
print(ticker.lower())

# 043 capitalize 메서드
hello = 'hello'
print(hello.capitalize())

# 044 endswith 메서드
file_name = "보고서.xlsx"
print(file_name.endswith('xlsx'))

# 045 endswith 메서드
file_name = "보고서.xlsx"
print(file_name.endswith(('xlsx', 'xls')))

# 046 startswith 메서드
file_name = "2020_보고서.xlsx"
print(file_name.startswith('2020'))

# 047 split 메서드
a = "hello world"
print(a.split(' '))

# 048 split 메서드
ticker = "btc_krw"
print(ticker.split('_'))

# 049 split 메서드
date = "2020-05-01"
print(date.split("-"))

# 050 rstrip 메서드
data = "039490     "
print(data.strip())