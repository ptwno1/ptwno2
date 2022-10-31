# set = 집합

s1 = set([1,3,5]) # == si = set{1,3,5}
s2 = set([1,5,7,10])

# set 관련 함수

# .add()         값 1개 추가
# .update()      값 여러개 추가
# .remove()      해당값 삭제 없을 시 오류
# .discard()     해당값 삭제

# 합집합 
s1 | s2

#교집합
s1.interssection(s2)

#차집합
s1.difference(s2)
