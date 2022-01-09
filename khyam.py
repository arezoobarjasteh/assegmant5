n=int(input(" number_of_row "))
pascal=[[None for i in range(n)]for j in range(n)]
for i in range(n):
    pascal[i][0]=1
    pascal[i][i]=1
for i in range(2,n):
    for j in range(1,i):
        pascal[i][j]=pascal[i-1][j]+pascal[i-1][j-1]
for i in range(n):
    for j in range(i+1):
        print(pascal[i][j],end='\t')
    for j in range(i+1,n):
        pascal[i][j]=" "
        print(pascal[i][j],end='\t')
    print()