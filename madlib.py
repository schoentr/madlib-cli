def get_words():
    """Reads all the text file and creates promps for user input"""
    with open('/home/schoentr/Documents/codefellows/401-python/madlib-cli/text.txt', 'r') as rf:
        with open('./output.txt','w') as wf:
            for line in rf:
                print(line)
                start = -1
                line_start_index = 0
                new_line = ''
                for x in range(0,len(line)):

                    if line[x] == '{':
                        if x - line_start_index == 0:
                            new_line+= ''
                        # print (line_start_index - x)
                        start = x+1
                    if line[x] == '}':
                        end = x
                        if start != -1:
                            new_line+=line[line_start_index:start-1]
                            temp_word = ''
                            temp_word = line[start: end]
                            # print(temp_word)
                            prompt = 'Enter a  ' + temp_word + ' :'
                            new_word = input(prompt)
                            # print(temp_word, new_word)
                            new_line += new_word
                            line_start_index = end + 1
                            # line.replace(temp_word, new_word)
                            if x >= len(line)-3:
                                new_line+='\n'

                    if x == len(line) - 1 and start == -1:
                        new_line = line
                        print(new_line)
                        
                print(new_line)
                wf.write(new_line)
                

get_words()

                
                