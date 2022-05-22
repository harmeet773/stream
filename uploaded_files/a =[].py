
# t is number of test case s 
t= int(input())

def findavg(i,j,l,k,aaar):
    k = aaar[i][j]-aaar[i-1][j]-aaar[i][j-1]+aaar[i-1][j-1]
    return k
# if length 0 then element itself 

for ii in range(t):
    nmk=input()
    a=nmk.split()
    a = [int(z) for z in a ]
    print
    arr=[] 
    for j in range(a[0]):
        ar = list(map(int,input().split()))
        arr.append(ar)

    pref = arr[::]
    print(pref,"sss",a[1])


    for i in range(1,a[1]):
        print(pref[0][i])
        pref[0][i] += pref[0][i-1]

    for i in range(1,a[0]):
        pref[i][0] += pref[i-1][0]




    for i in range(1,a[0]):
        for  j in range(1,a[1]):
            pref[i][j] = pref[i-1][j] +pref[i][j-1] - pref[i-1][j-1]

            # created  prefix matrix 
    ans=0
    for i in range(a[0]):
        for i in range(a[1]):
            low , high = i , a[0]-1
            while low<high:
                mid = int((low +high)/2)


                avg = findavg(a[0],a[1],mid,a[2],pref)
                if avg >=a[2] and low ==high:
                    final_length = low
                    ans+= final_length
                if avg >=a[2]:
                    high=mid
                else :
                    low = mid

    print(final_length)
        

    






        




a =[]
a=list(map(int(),))
