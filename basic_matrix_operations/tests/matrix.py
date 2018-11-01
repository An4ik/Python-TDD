""" 

In mathematics, a matrix is a rectangular array of numbers, symbols, or expressions, arranged in rows and columns.

This code does basic operations like addition, subtraction, transposing, multiplication and division of two matrices.

Two matrices may be added or subtracted only if they have the same dimension; that is, they must have the same number of rows and columns.Addition or subtraction is 
accomplished by adding or subtracting corresponding elements.

The matrix product AB is defined only when the number of columns in A is equal to the number of rows in B. Similarly, the matrix product BA is defined only when the 
number of columns in B is equal to the number of rows in A.

Technically, there is no such thing as matrix division. Dividing a matrix by another matrix is an undefined function.[2] The closest equivalent is multiplying by the 
inverse of another matrix. In other words, while [A] ÷ [B] is undefined, you can solve the problem [A] * [B]-1. Since these two equations would be equivalent for scalar 
quantities, this "feels" like matrix division, but it's important to use the correct terminology.


In linear algebra, the transpose of a matrix is an operator which flips a matrix over its diagonal, that is it switches the row and column indices of the matrix by 
producing another matrix denoted as A^T.

"""

def mat_addition (matrix1, matrix2): #Function that takes two matrices (matrix1,matrix2) as an argument and does an addition of them.
    result = matrix1 #A variable that takes matrix1 as a value. We should to this in order to give to the result matrix the same size as matrix1.
    for i in range (len(matrix1)):
        for j in range (len(matrix1[i])):
            result[i][j] = matrix1[i][j] + matrix2[i][j] #Writes the addition of matrix1 and matrix2 to the result matrix.
    return result #Returns the result that we get from addition of matrix1 and matrix2.

def mat_subtraction (matrix1, matrix2): #Function that takes two matrices (matrix1,matrix2) as an argument and does a subtraction of them.
    result = matrix1 #A variable that takes matrix1 as a value. We should to this in order to give to the result matrix the same size as matrix1.
    for i in range (len(matrix1)):
        for j in range (len(matrix1[i])):
            result[i][j] = matrix1[i][j] - matrix2[i][j] #Writes the subtraction of matrix1 and matrix2 to the result matrix.
    return result  #Returns the result that we get from subtraction of matrix1 and matrix2.

def mat_transpose (matrix1): #Function that flips a matrix over its diagonal, that is it switches the row and column indices of the matrix by producing another matrix.
    matrix1 = [list(i) for i in zip(*matrix1)] #Changing rows of matrix1 to the columns of itself.
    return matrix1 #Returns the result that we get from transposing of a matrix1.

def mat_check_for_addition_and_subtraction (matrix1, matrix2): #Function that checks if it is possible to add and substract matrix1 and matrix2. It is possible if and only if their sizes are equal.
    return len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]) #Returns True if it is possible to add and subtract matrix1 and matrix1 and False if it is vise versa.

def mat_check_for_multiplication (matrix1, matrix2): #Function that checks if it is possible to multiply matrix1 by matrix2. It is possible if and only if the number of rows of one matrix is equal to the number of columns of another.
    return len(matrix1[0]) == len(matrix2) #Returns True if it is possible to multiply matrix1 by matrix1 and False if it is vise versa.

def mat_multiplication (matrix1, matrix2): #Function that takes two matrices (matrix1,matrix2) as an argument and does a multiplication.
    result= [[0 for row in range(len(matrix1))] for col in range(len(matrix2[0]))] #Takes number of rows of matrix1 and number of columns of matrix2 as a result.
    for i in range (len(matrix1)):
        for j in range (len(matrix2[0])):
            for k in range (len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j] #Writes the multiplication of matrix1 by matrix2 to the result matrix.
    return result #Returns the result that we get from multiplication of matrix1 by matrix2.

def get_mat_minor (matrix,i,j): #Funtion that finds minor of a matrix. Minor is the determinant of the square matrix formed by deleting one row and one column from some larger square matrix.
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])] 

def get_mat_determinant (matrix): #Function that finds the determinant of a matrix.
    if len(matrix) == 2: #For (2x2) matrix here code just does the criss-cross multiplication, and subtracts.
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


    determinant = 0 #To find a determinant of bigger matrix we have to ignore the row and column that are the intersection of an element and do this operation to all of the elements.

    for c in range(len(matrix)):
        determinant += ((-1) ** c) * matrix[0][c] * get_mat_determinant(get_mat_minor(matrix, 0, c))
    return determinant

def get_mat_inverse (matrix2): #Functon that finds an inverse of a matrix.
    determinant = get_mat_determinant(matrix2) #Give a value to variable determinant which is calculated in get_mat_determinant() function.
    
    if len(matrix2) == 2: #Special case for 2x2 matrix: swap the positions of [0][0] and [1][1], put negatives in front of [0][1] and [1][0], and divide everything by the determinant.
        return [[matrix2[1][1] / determinant, -1 * matrix2[0][1] / determinant],
                [-1 * matrix2[1][0] / determinant, matrix2[0][0] / determinant]]
    #Find matrix of cofactors
    cofactors = [] #Create an array called cofactors.
    for r in range(len(matrix2)):
        cofactorRow = [] #Create an array called cofactorRow.
        for c in range(len(matrix2)):
            minor = get_mat_minor(matrix2, r, c) #Find a minor of a matrix using get_mat_minor() function.
            cofactorRow.append(((-1) ** (r + c)) * get_mat_determinant(minor)) #Multiply to (-1) to change the signs of an elemens escaping the one of elements and save the results in cofactorRow array.(через одну)
        cofactors.append(cofactorRow) #Save all the data that is stored in cofactorRow array to the cofactors array.
    cofactors = mat_transpose(cofactors) #Changing rows of cofactors to the columns of itself.
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant #Divide every element of a matrix to a determinant.
    return cofactors #Return the inverse of a matrix.

def mat_division(matrix1, matrix2): #Function that finds the division of matrix1 by matrix2.
    imatrix = get_mat_inverse(matrix2) #Create a variable called imatrix that takes the inverse of a matrix2 as a value using get_mat_inverse() function.
    for i in range(len(imatrix)):
        for j in range(len(imatrix[0])):
            imatrix[i][j] = int(imatrix[i][j]) #Converts all the elements of an imatrix to an integer value.
    result = mat_multiplication(matrix1, imatrix) #Multiplies matrix1 by imatrix(that is the inverse of a matrix1) to find the division of matrix1 by matrix2.
    return result #Returns the division of matrix1 by matrix2.

    
