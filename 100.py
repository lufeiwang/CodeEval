import sys
#https://www.codeeval.com/open_challenges/100
    
    
if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        for line in f:
            num_n = int(line.rstrip('\n'))
            if num_n % 2 == 0:
                print 1
            else:
                print 0