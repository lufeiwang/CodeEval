import sys
#https://www.codeeval.com/open_challenges/29/

bug_boundary = [0,2,4,6]
bug_type = ['Done','Low','Medium','High','Critical']



if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        for line in f:
            line = line.rstrip('\n')
            [N,M] = line.split(',')
            
            print int(N) - (int(N) // int(M)) * int(M)
