#Solve the Matrix

MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

matrix= []
rows= MATRIX_STR.strip("\n").splitlines()
print (rows)

for row in rows:
    characters= list (rows)
    matrix.append(characters)
print (matrix)
