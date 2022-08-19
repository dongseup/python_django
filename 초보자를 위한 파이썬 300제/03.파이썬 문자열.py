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