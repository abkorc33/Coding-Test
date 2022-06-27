def solution(participant, completion):
    # 1. 두 리스트를 sorting 한다
    participant.sort()
    completion.sort()

    # 2. completion list의 length 만큼 돌면서, participant에만 존재하는 한 명을 찾는다
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    # 3. list를 전부 뒤져도 답이 없다면, participant의 마지막 주자가 완주하지 못한 선수이다
    return participant[len(participant) -1]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))