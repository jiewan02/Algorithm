def solution(order):
    answer = 0
    am= ['americano', 'iceamericano', 'americanoice', 'hotamericano', 'americanohot', 'anything']
    lat = ['cafelatte', 'icecafelatte', 'cafelatteice', 'hotcafelatte', 'cafelattehot']
    
    for i in order: 
        if i in am: 
            answer += 4500
        else: 
            answer += 5000
    return answer