#Lab #7
#Due Date: 02/22/2019, 11:59PM
########################################
#                                      
# Name: Stephen D'Amico 
# Collaboration Statement: I worked alone on this assignment.         
#
########################################



#### DO NOT modify the triangle(n) function in any way! 
def triangle(n):
    return recursive_triangle(n, n)

###################

def recursive_triangle(k, n):
    '''
        >>> recursive_triangle(2,4)
        '  **\\n   *'
        >>> print(recursive_triangle(2,4))
          **
           *
        >>> triangle(4)
        '****\\n ***\\n  **\\n   *'
        >>> print(triangle(4))
        ****
         ***
          **
           *
    '''
    # --- YOUR CODE STARTS HERE
    if k ==1: 
      return ' '*(n-k) +'*'*k
    else:
      return ' '*(n-k) + '*'*k+'\n'+recursive_triangle(k-1,n)

