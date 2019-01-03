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
    lines is a str:from the file
    topn is a str:N of the highest frequency
    """
    strlist=[]
    symbols=['\r\n',',','.',':','"','!','?',"'"]
    for line in lines:
        string0=line.decode().lower()
        string=' '+string0+' '
        for symbol in symbols:
            string=string.replace(symbol,' ')
        strlist.append(string)          
    all_words=[]
    for i in strlist:
        all_words.append(i.split())  
    words=list(set(all_words))           
    countlist=[]
    for word in words:
        countlist=countlist+[all_words.count(word)]    
    ziplist=zip(words,countlist)
    sortlist=sorted(ziplist,key=lambda i:i[1],reverse=True)  
    dic={}
    for item in sortlist:
        dic[item[0]]=item[1]
    maxl=max(int(topn,len(words)))
    for i in range(maxl):
        print(sortlist[i][0]+' ',dic[sortlist[i][0]])
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
