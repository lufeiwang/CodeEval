import sys
#https://www.codeeval.com/open_challenges/82/

if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        for line in f:
            cur_num = line.rstrip('\n')
            
            n = len(cur_num)
            if int(cur_num) == sum([int(x)**n for x in cur_num]):
                print True
            else:
                print False