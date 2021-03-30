#! /usr/bin/env python3

import sys
import re

def find_iter(target_regex, in_stream, out_stream):
    """
    Iterates over all matches of 'target_regex' found in origin.txt.
    
    Parameters
    ----------
    target_regex
        the regular expression that is searched for in in_stream

    in_stream
        the text to be searched

    out_stream
        the file to which the results are written

    Yields
    ------
    A tuple of the line index and the match object
        This contains each time `target_regex` is found within `in_stream` yielded as a tuple
        containing the index of the line and the regular expression match object.
    """

    for line_index, line in enumerate(in_stream):
        for match_object in target_regex.finditer(line):
            yield line_index, match_object


def record_all_occurences(in_stream, out_stream, target_regex):
    """
    Uses find_iter function to find all occurrences of target_regex in in_stream and writes
    them to out_stream with the line index.

    Parameters
    ----------
    in_stream
        The text to search

    out_stream
        The file to which the results should be written

    target_regex
        The regular expression which is searched for in in_stream

    Returns
    -------

    occurrences
         The number of times that target_regex is found in in_stream

    """

    occurrences = 0
    for line_index, match_obj in find_iter(target_regex, in_stream, out_stream):
        occurrences += 1
        for target_str in match_obj.groups():
            out_stream.write("{line_num}\t{string}\n".format(line_num = line_index + 1, 
                string = target_str))
    return occurrences



if __name__ == '__main__':
    target_pattern = re.compile(r'(\w*herit\w*)', re.IGNORECASE)
    with open('origin.txt', 'r') as in_stream:
        with open('output.txt', 'w') as out_stream:
            num_occurrences = record_all_occurences(in_stream = in_stream, 
                out_stream = out_stream,
                target_regex = target_pattern)
    message = "Charles Darwin referred to heritability {0} times!".format(num_occurrences)
    print(message)
    print("Done!")
    print('origin.txt is closed?', in_stream.closed)
    print('output.txt is closed?', out_stream.closed)



