def generate_magic_matrix(n):
    magic_matrix=[[0]*n for x in range(n)]
    num=1
    i,j=0,n//2
    while num<=n*n:
        magic_matrix[i][j]=num
        num+=1
        new_i,new_j=(i-1)%n,(j+1)%n
        if magic_matrix[new_i][new_j]:
            i+=1
        else:
            i,j=new_i,new_j
    return magic_matrix
def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str,row)))
n=int(input("Enter The Size Of The Matrix : "))
matrix=generate_magic_matrix(n)
print_matrix(matrix)