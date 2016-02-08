import sys
#https://www.codeeval.com/open_challenges/227
    
    
if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        for line in f:
            line = line.rstrip('\n')
            check_sum = 0
            ind = 0
            
            for val in line:
                if str.isdigit(val):
                    check_sum += int(val)
                    if ind % 2 == 0:
                        check_sum += int(val)
                    ind += 1
            if check_sum % 10 == 0:
                print 'Real'
            else:
                print 'Fake'