try:
    t = int(input())
    final_list = []
    for test_case in range(t):
        dolls_list = []
        no_of_dolls = int(input())
        for i in range(no_of_dolls):
            doll = input()
            dolls_list.append(doll)
        dolls_list_set = set(dolls_list)
        dolls_list_2 = list(dolls_list_set)
        for doll in dolls_list_2:
            count = dolls_list.count(doll)
            if count%2 != 0:
                final_list.append(count)
        for i in final_list:
            print(i)
except:
    pass