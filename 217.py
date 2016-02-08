import sys
#https://www.codeeval.com/open_challenges/217
    
    
if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        for line in f:
            line = line.rstrip('\n')
            
            [n_zeros, n] = line.split(' ')
            n = int(n)
            n_zeros = int(n_zeros)
            
            num_qualified = 0
            for i in range(1,n+1):
                if bin(i).count('0', 2) == n_zeros:
                    num_qualified += 1    
            
            print num_qualified