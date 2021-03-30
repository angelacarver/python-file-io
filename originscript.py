#! /usr/bin/env python3

import sys
import re

def find_iter(target_regex):
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

#target_regex = re.compile(r('\w*herit\w*)', re.IGNORECASE)
    print('Opening origin.txt')
    with open('origin.txt', 'r') as in_stream:
        print('Opening output.txt')
        with open('output.txt', 'w') as out_stream:
            for line_index, line in enumerate(in_stream):
                for match_object in target_regex.finditer(line):
                    yield line_index, match_object


def record_all_occurences(in_stream, out_stream, target_regex):
    occurrences = 0
    for line_index, match_obj in find_iter(target_regex):
        occurrences += 1
    for target_str in match_obj.groups():
        out_stream.write("{line_num}\t{string}\n".format(line_num = line_index +1, 
            string = target_str))
    return occurrences



if __name__ == '__main__':
    target_pattern = re.compile(r'(\w*herit\w*)', re.IGNORECASE)
    with open('origin.txt', 'r') as in_stream:
        with open('output.txt', 'w') as out_stream:
            num_occurrences = record_all_occurences(in_stream = in_stream, out_stream = out_stream,
                target_regex = target_pattern)
    message = "Charles Darwin referred to heritability {0} times!".format(num_occurrences)
    print(message)
    print("Done!")
    print('dummy.txt is closed?', in_stream.closed)
    print('output.txt is closed?', out_stream.closed)



