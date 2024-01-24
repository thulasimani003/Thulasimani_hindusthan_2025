"""At the annual meeting of Board of Directors of Acme Inc. If everyone attending shakes hands exactly one time with every other attendee, how many handshakes are there?

Example

There are 3 attendees, p1,p2 and p3.p1 shakes hands with p2 and p3, and p2 shakes hands with p3. Now they have all shaken hands after  handshakes.

Function Description

Complete the handshakes function in the editor below.

handshakes has the following parameter:

int n: the number of attendees
Returns

int: the number of handshakes
Input Format
The first line contains the number of test cases .
Each of the following  lines contains an integer, .

Constraints



Sample Input

2
1
2
Sample Output

0
1
Explanation

Case 1 : The lonely board member shakes no hands, hence 0.
Case 2 : There are 2 board members, so 1 handshake takes place."""

#program

import math
import os
import random
import re
import sys

def handshake(n):
    return n*(n-1)//2
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = handshake(n)

        fptr.write(str(result) + '\n')

    fptr.close()

    
"""output


Input (stdin)
2
1
2
Your Output (stdout)
0
1"""

