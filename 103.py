import sys
#https://www.codeeval.com/open_challenges/103/

def find_winner(num_ind):
    for ind, pair in enumerate(num_ind):
        flag = 1
        if ind >= 1:
            if pair[-1] == num_ind[ind-1][-1]:
                flag=0
                next
        if ind < len(num_ind) - 1:
            if pair[-1] == num_ind[ind+1][-1]:
                flag=0
                next
        if flag==1:
            return pair[0]
    return 0

if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        for line in f:
            num_str = line.rstrip('\n').split(' ')
            
            num_ind = [[ind_x+1, int(num_x)] for ind_x, num_x in enumerate(num_str)]
            
            # sort by y in (x,y)
            num_ind.sort(key=lambda(x):x[-1])
            winner = find_winner(num_ind)
            print winner
                        
            