#! /usr/bin/env python3

import sys
import re

def find_iter()
    """
    Iterates over all matches of 'target_regex' found in origin.txt.
    
    Parameters
    ----------
    NONE

    Yields
    ------
    A tuple of the line index and the match object
        This contains each time `target_regex` is found within `in_stream` yielded as a tuple
        containing the index of the line and the regular expression match object.
    """

target_regex = re.compile(r('\w*herit\w*)', re.IGNORECASE)
print('Opening origin.txt')
with open('origin.txt', 'r') as in_stream:
    print('Opening output.txt')
    with open('output.txt', 'w') as out_stream:
        for line_index, line in enumerate(in_stream):
             for match_object in target_regex.finditer(line)
                yield line_index, match_object
            
            

def record_all_occurences(in_stream, out_stream, target_regex)
    occurrences = 0
    for line_index, match_obj in find_iter(in_stream, target_regex, start_regex, stop_regex):
    occurrences += 1
    for target_str in match_obj.groups():
        out_stream.write("{line_num}\t{string}\n.format(
            line_num = line_index +1,
            string = target_str))
    return occurrences

    print("Done!")
    print('dummy.txt is closed?', in_stream.closed)
    print('output.txt is closed?', out_stream.closed)
