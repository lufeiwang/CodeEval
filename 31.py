import sys
#https://www.codeeval.com/open_challenges/31/

bug_boundary = [0,2,4,6]
bug_type = ['Done','Low','Medium','High','Critical']



if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        for line in f:
            line = line.rstrip('\n')
            [string_s, char_find] = line.split(',')
            print (string_s.rfind(char_find))
            