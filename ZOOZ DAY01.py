
t = int(input())

for test_case in range(t):
    def zooz(n):
        s =''
        list1 = ["0"]*n
        if n%2 == 0:
            list1[0] = "1"
            list1[n-1] = "1"
            res = "".join(map(str,list1))
            
            
        else:
            val =int(n/2)
            list1[val] = "1"
            res = "".join(map(str,list1))
        return res
        
            
    n = int(input())
    print(zooz(n))
    
            