"""Consider two points,  and . We consider the inversion or point reflection, , of point  across point  to be a  rotation of point  around .

Given  sets of points  and , find  for each pair of points and print two space-separated integers denoting the respective values of  and  on a new line.

Function Description

Complete the findPoint function in the editor below.

findPoint has the following parameters:

int px, py, qx, qy: x and y coordinates for points  and 
Returns

int[2]: x and y coordinates of the reflected point 
Input Format

The first line contains an integer, , denoting the number of sets of points.
Each of the  subsequent lines contains four space-separated integers that describe the respective values of , , , and  defining points  and .

Constraints

Sample Input

2
0 0 1 1
1 1 2 2
Sample Output

2 2
3 3
Explanation

The graphs below depict points , , and  for the  points given as Sample Input"""

#program1

import math
import os
import random
import re
import sys

def findPoint(px, py, qx, qy):
    rx = 2 * qx - px
    ry = 2 * qy - py
    return rx,ry

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()

        px = int(first_multiple_input[0])

        py = int(first_multiple_input[1])

        qx = int(first_multiple_input[2])

        qy = int(first_multiple_input[3])

        result = findPoint(px, py, qx, qy)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

"""output
Input (stdin)

2
0 0 1 1
1 1 2 2
Your Output (stdout)

2 2
3 3"""

#program method 2

import math
import os
import random
import re
import sys

def findPoint(px, py, qx, qy):
     return [2 * qx - px, 2 * qy - py]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()

        px = int(first_multiple_input[0])

        py = int(first_multiple_input[1])

        qx = int(first_multiple_input[2])

        qy = int(first_multiple_input[3])

        result = findPoint(px, py, qx, qy)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

"""output
Input (stdin)

2
0 0 1 1
1 1 2 2
Your Output (stdout)

2 2
3 3"""


 
