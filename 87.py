import sys
#https://www.codeeval.com/open_challenges/87
    
    
if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        d = {}
        for line in f:
            curr_command = line.rstrip('\n')
            curr_query = curr_command.split(' ')[0]
            curr_nums = curr_command.split(' ')[1::]
            
            
            if curr_query == 'SetRow':
                for i in range(256):
                    d[(int(curr_nums[0]),i)] = int(curr_nums[1])
            elif curr_query == 'SetCol':
                for i in range(256):
                    d[(i,int(curr_nums[0]))] = int(curr_nums[1])
            elif curr_query == 'QueryRow':
                print sum([v for k,v in d.items() if k[0] == int(curr_nums[0])])
            elif curr_query == 'QueryCol':
                print sum([v for k,v in d.items() if k[1] == int(curr_nums[0])])
            