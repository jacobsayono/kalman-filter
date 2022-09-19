import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        z = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(z)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
    
def get_row(matrix, row_number):
    row = matrix[row_number]
    return row

def get_col(matrix, col_number):
    col = []
    for r in range(len(matrix)):
        col.append(matrix[r][col_number])
    return col

def dot_product(vector1, vector2):
    dot = 0
    for i in range(len(vector1)):
        dot += vector1[i] * vector2[i]
    return dot

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1:
            a = self.g[0][0]
            return a
        if self.h == 2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            return a * d - b * c

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        trace = 0
        for i in range(self.h):
            trace += self.g[i][i]
        return trace

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        # TODO - your code here
        if self.h == 1:
            a = self.g[0][0]
            inverse = 1/a
            return Matrix([[inverse]])
        if self.h == 2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            if a * d == b * c:
                raise(ValueError, "The matrix is not invertible.")
            else:
                inverse = zeroes(2, 2)
                for r in range(self.h):
                    for c in range(self.w):
                        inverse[r][c] = (1 / self.determinant()) * (self.trace() * identity(2)[r][c] - self.g[r][c])
        return inverse
            

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        transpose = []
        for c in range(self.w):
            rowT = []
            for r in range(self.h):
                rowT.append(self.g[r][c])
            transpose.append(rowT)
        return Matrix(transpose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        add = []
        for r in range(self.h):
            row = []
            for c in range(self.w):
                row.append(self.g[r][c] + other.g[r][c])
            add.append(row)
        return Matrix(add)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        negative = []
        for r in range(self.h):
            row = []
            for c in range(self.w):
                row.append(-self.g[r][c])
            negative.append(row)
        return Matrix(negative)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
        
        subtract = []
        for r in range(self.h):
            row = []
            for c in range(self.w):
                row.append(self.g[r][c] - other.g[r][c])
            subtract.append(row)
        return Matrix(subtract)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        mul = []
        for r in range(self.h):
            row_result = []
            row_self = get_row(self.g, r)
            for c in range(other.w):
                col_other = get_col(other.g, c)
                dot = dot_product(row_self, col_other)
                row_result.append(dot)
            mul.append(row_result)
        return Matrix(mul)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            #   
            # TODO - your code here
            #
            rmul = []
            for r in range(self.h):
                row = []
                for c in range(self.w):
                    row.append(other * self.g[r][c])
                rmul.append(row)
            return Matrix(rmul)