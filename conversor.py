
#tranform string in matrix
def convert_to_matrix(s, k, n):
    matrix = []

    for i in range(0,len(s), n):
        l =[]
        l = [int(s[w]) for w in range(i, i+n)]
        matrix.append(l)
    return matrix

s = '10101011001001'

#transform matrix in string
def revert_to_string(m):
    s=[]
    for i in m:
        for w in i:
            s.append(str(w))
    return ''.join(s)

#print (revert_to_string((convert_to_matrix(s))))
#print (convert_to_matrix(s))

#s = '101001'
#print(convert_to_matrix(s, 6,1))