def solution(s):
    answer = s
    num = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    for i in num.items():
        answer = answer.replace(i[0], str(i[1]))	# 문자열로 변경해줘야함
        
    return int(answer)