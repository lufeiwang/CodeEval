import sys
from sets import Set

if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        for line in f:
            set_a = Set(line.rstrip('\n').split(';')[0].split(','))
            set_b = Set(line.rstrip('\n').split(';')[1].split(','))

            list_c = list(set_a.intersection(set_b))
            list_c.sort()
            if (list_c == None):
                print
            else:
                print (','.join(str(x) for x in list_c))