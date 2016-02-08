import sys

#https://www.codeeval.com/open_challenges/214
    
    
if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        for line in f:
            line = line.rstrip('\n')
            d = dict()
            
            times_str = line.split(' ')
            for n in times_str:
                x = int(n[0:2]) * 3600 + int(n[3:5]) * 60 + int(n[6:8])
                d[n] = x
            
            #print d
            print(' '.join(sorted(d, key=lambda(x):d[x], reverse = True)))
            