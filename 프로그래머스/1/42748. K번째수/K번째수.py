def solution(array, commands):
    answer = []
    new_list = []
    for i in commands: 
        first_idx = i[0]
        sec_idx = i[1]
        new_list = array[first_idx-1:sec_idx]
        new_list.sort()
        print(new_list)
        answer.append(new_list[i[2]-1])
    return answer