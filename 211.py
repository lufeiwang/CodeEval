import sys
#https://www.codeeval.com/open_challenges/211/

bug_boundary = [0,2,4,6]
bug_type = ['Done','Low','Medium','High','Critical']

def wine_matcher(wines_arr, letters_str):
    res = []
    for wine in wines_arr:
        flag = 1
        wine_cpy = wine
        wine = list(wine)
        
        for letter in letters_str:
            if letter in wine:
                del wine[wine.index(letter)]
            else:
                flag = 0
                break
        if flag == 1:
            res.append(wine_cpy)
    return res
        

if __name__ == "__main__":
    with open(sys.argv[1],'r') as f:
        for line in f:
            line = line.rstrip('\n')
            [wines,letters] = line.split(' | ')
            wines = wines.split(' ')

            valid_wines = wine_matcher(wines, letters)
            if len(valid_wines) == 0:
                print False
            else:
                print ' '.join(valid_wines)