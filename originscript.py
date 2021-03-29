#! /usr/bin/env python3

import sys
import re


print('Opening origin.txt')
with open('origin.txt', 'r') as in_stream:
    print('Opening output.txt')
    with open('output.txt', 'w') as out_stream:
        for line in in_stream:
            line = line.strip()
            #word_list = line.split()
            #herit_list = word_list
          #find words with "herit" in them
            
            herit_list = line.match(target)
            for word in herit_list
                out__stream.write('{line_num}\t{string}\n'.format(line_num = line + 1, 
                string = target_string))
            
            
print("Done!")
print('dummy.txt is closed?', in_stream.closed)
print('output.txt is closed?', out_stream.closed)
