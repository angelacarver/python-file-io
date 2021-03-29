print('Opening origin.txt')
with open('origin.txt', 'r') as in_stream:
    print('Opening output.txt')
    with open('output.txt', 'w') as out_stream:
        for line in in_stream:
            line = line.strip()
            word_list = line.split()
            #find words with "herit" in them
            for word in herit_list
                out__stream.write('{}\s{}\t'.format(line, word))
            #write line number \s
            #write word \t
            
