# 051 리스트 생성
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
print(movie_rank)

# 052 리스트에 원소 추가
movie_rank.append("배트맨")
print(movie_rank)

# 053
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(0, '슈퍼맨')
print(movie_rank)

# 054
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[3]
print(movie_rank)

# 055
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2:]
print(movie_rank)

# 056
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
print(lang1 + lang2)

# 057
nums = [1, 2, 3, 4, 5, 6, 7]
print(max(nums))
print(min(nums))

# 058
nums = [1, 2, 3, 4, 5]
print(sum(nums))

# 059
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 060
nums = [1, 2, 3, 4, 5]
print(sum(nums) / len(nums))

# 061