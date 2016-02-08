import sys
import re
from math import sqrt
#https://www.codeeval.com/open_challenges/99
    
    
if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        for line in f:
            line = line.rstrip('\n')
            
            [x1, tmp1, y1, tmp2, tmp3, x2, tmp4, y2]=re.split('[(,) ]',line)[1:-1:]
            print int(sqrt((int(x1) - int(x2)) ** 2 + (int(y1) - int(y2)) ** 2))
            