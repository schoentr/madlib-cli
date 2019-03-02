""" madlib module that reads text.txt and outputs to output.txt"""

def get_words():
    """Reads all the text file and creates promps for user input"""
    with open('./text.txt', 'r') as rf:
        with open('./output.txt','w') as wf:
            for line in rf:
                start_prompt_index = -1
                line_start_index = 0
                new_line = ''
                for char_index in range(0,len(line)):
                    if line[char_index] == '{':
                        if char_index - line_start_index == 0:
                            new_line+= ' '
                        start_prompt_index = char_index+1
                    if line[char_index] == '}':
                        end_prompt_index = char_index
                        if start_prompt_index != -1:
                            new_line+=line[line_start_index:start_prompt_index-1]
                            temp_word = ''
                            temp_word = line[start_prompt_index: end_prompt_index]
                            prompt = 'Enter a ' + temp_word + ' :'
                            new_word = input(prompt)
                            new_line += new_word
                            line_start_index = end_prompt_index + 1
                            if char_index >= len(line)-3:
                                new_line+='\n'
                    if char_index == len(line) - 1 and start_prompt_index == -1:
                        new_line = line
                wf.write(new_line)
                

get_words()

                
                