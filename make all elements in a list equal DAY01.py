t = int(input())
for test_case in range(t):
    len_arr = int(input())
    arr = input().split()
    occurance_count =[]
    for ele in arr:
        count = 0
        count = arr.count(ele)
        occurance_count.append(count)
    max_freq = max(set(occurance_count))
    min_operations = len_arr - max_freq
    print(min_operations)
        
        
        