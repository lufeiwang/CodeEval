import sys
#https://www.codeeval.com/open_challenges/225/

bug_boundary = [0,2,4,6]
bug_type = ['Done','Low','Medium','High','Critical']



if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        for line in f:
            line = line.rstrip('\n')
            [dev_str, des_str] = line.split(' | ')
            bugs = sum([1 for ind, dev_x in enumerate(dev_str) if dev_x != des_str[ind]])
            res_type = bug_type[-1];
            
            for ind,i in enumerate(bug_boundary):
                if bugs <= i:
                    res_type = bug_type[ind]
                    break

            print res_type