import sys

if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        for line in f:
            line = line.rstrip('\n')
            processed_dict = {i: line.count(str(i)) for i, v in enumerate(line)}
            flag = 1       
            for ind, val in enumerate(line):
                if processed_dict[int(ind)] != int(val):
                    flag = 0
                    break
            print flag
            