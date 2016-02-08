import sys
#https://www.codeeval.com/open_challenges/67

if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        for line in f:
            cur_num = line.rstrip('\n')
            
            # reverse list
            cur_num=cur_num[::-1]
            
            res_sum = 0            
            for i, val in enumerate(cur_num):
                if str.isalpha(val):
                    val = ord(val) - 87
                res_sum += int(val) * (16 ** i)
            
            print res_sum
            