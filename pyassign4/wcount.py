"""currency.py: To convert one currency into another at an exchange rate.
__author__ = "Zhang Tianyu"
__pkuid__  = "1800011759"
__email__  = "1800011759@pku.edu.cn"
"""

import sys
from urllib.request import urlopen

def wcount(lines, topn):

    """count words from lines of text string, then sort by their counts

    in reverse order, output the topn (word count), each in one line. 

    """
    strlst = []
    symbols = [',','.',"'",'"',':','!','?','\r\n']
    for line in lines:
        originalstr = line.decode().lower()
        strs = ' '+originalstr+' '
        strlst.extend([strs.replace(sym,' ') for sym in symbols])          
    words = [s.split() for s in strlst]   
    word = list(set(words))           
    countlst = [word.count(w) for w in word]
    sortlst = zip(word,countlst)
    sortlst.sort(key=lambda v:v[1],reverse=True)  
    worddic = {}
    for w in sortlst:
        worddic[w[0]] = w[1]
    mmax = max(int(topn),len(word))
    for i in range(mmax):
            print(sortlst[i][0]+' ',dic[sortlst[i][0]])
    pass

def main():
    doc = urlopen(sys.argv[1])
    lines = doc.readlines()
    topn = sys.argv[2]
    wcount(lines,topn)    

if __name__ == '__main__':
    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    main()
