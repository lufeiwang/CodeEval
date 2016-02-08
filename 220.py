#https://www.codeeval.com/open_challenges/220/

import sys

def CandyLineParser(line):
    inputs = [int(line.split(',')[i].split(': ')[1]) for i in range(len(line.split(',')))]    
    candies = (inputs[0] * 3 + inputs[1] * 4 + inputs[2] * 5) * inputs[3] / sum(inputs[:-1])
    return candies

if __name__ == "__main__":
    with open(sys.argv[1],'r') as test_cases:
        for test in test_cases:
            candies = CandyLineParser(test)
            print(candies)

