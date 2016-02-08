import sys
#https://www.codeeval.com/open_challenges/96
    
    
if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        for line in f:
            line = line.rstrip('\n')
            res =''
            for i in line:
                if str.isalpha(i):
                    if i.isupper():
                        res += i.lower()
                    else:
                        res += i.upper()
                else:
                    res += i
            print res