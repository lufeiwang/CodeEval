import sys
#https://www.codeeval.com/open_challenges/29/
from sets import Set

bug_boundary = [0,2,4,6]
bug_type = ['Done','Low','Medium','High','Critical']



if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        for line in f:
            line = line.rstrip('\n')
            line_arr = list(Set([int(x) for x in line.split(',')]))
            
            line_arr.sort()
            print (','.join([str(x) for x in line_arr]))
