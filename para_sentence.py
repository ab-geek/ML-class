path =r"output.csv"
file = r"31_51262.txt"

import sys
import codecs

temp = sys.stdout
sys.stdout = open(path,encoding='utf-8', mode = 'w+')

f = codecs.open(file, encoding='utf-8')

for char in f:
        text = char.replace(u'\u0964', u'\u0964\n')
        print(text.replace(u'?', u'?\n'))
        

        
        
