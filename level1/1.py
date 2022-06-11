# LEVEL1 - 신고 결과 받기

def solution(id_list, report, k):
    result = {}
    dic = {}
    reported = {}
    
    # 이용자id가 신고한id 배열 만들기
    for i in id_list:
        dic[i] = []
        result[i] = 0
        reported[i] = 0
            
    # 이용자id, 신고한 id 분리하기 & 배열에 넣기
    for i in report:
        user, reportedUser = i.split(' ')[0], i.split(' ')[1]
        dic[user].append(reportedUser)
        
    # 신고받은 id 횟수 세기
    for i in list(dic.values()):
        for j in set(i):    # 리스트 중복 제거
            reported[j] += 1
                    
                
    # 신고횟수 2회 이상인 아이디를 신고한 이용자 id 찾기
    for i in id_list:
        for j in dic[i]:
            if reported[j] == 2:
                result[i] += 1
            
    
    answer = []
    answer = list(result.values())
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
ans = solution(id_list, report, k)
print(ans)