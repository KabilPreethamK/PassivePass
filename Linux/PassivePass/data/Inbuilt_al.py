def inbuilt(x,y):
    with open(x , "r") as f:
        import json
        data = json.load(f)

    words_tags = list(data["Words"].keys())
    integers_tags = list(data["Integers"].keys())

    words_data = data["Words"]
    integers_data = data["Integers"]

    special_characters = ["@","!","#","$","&","*","?"]

    words_tags = list(words_data.keys())
    integers_tag = list(integers_data.keys())[0] 

    for i in range(0,len(words_tags)):
        if words_tags[i] == 'Target':
            #combination word + integer base
            combinations = []
            for word_tag in words_tags:
                words_list = words_data[word_tag]
                for dob_value in integers_data[integers_tag]:
                    for word in words_list:
                        combination = word + dob_value
                        combinations.append(combination)

            with open(y+".txt", 'w') as file:
                for combination in combinations:
                    file.write(combination + '\n')
            #integer + word
            combinations = []
            for dob_value in integers_data[integers_tag]:
                for word_tag in words_tags:
                    words_list = words_data[word_tag]
                    for word in words_list:
                        
                        combination = dob_value + word
                        combinations.append(combination)

            with open(y+".txt", 'a') as file:
                for combination in combinations:
                    file.write(combination + '\n')

            #words+speacial_char+integers

            combinations = []
            for word_tag in words_tags:
                words_list = words_data[word_tag]
                for dob_value in integers_data[integers_tag]:
                    for word in words_list:
                        for i in range(0,len(special_characters)):
                            combination = word+special_characters[i] + dob_value
                            combinations.append(combination)

            with open(y+".txt", 'a') as file:
                for combination in combinations:
                    file.write(combination + '\n')

            #integers+speacial_char+words

            combinations = []
            for word_tag in words_tags:
                words_list = words_data[word_tag]
                for dob_value in integers_data[integers_tag]:
                    for word in words_list:
                        for i in range(0,len(special_characters)):
                            combination = dob_value+special_characters[i] + word
                            combinations.append(combination)
                            
            with open(y+".txt", 'a') as file:
                for combination in combinations:
                    file.write(combination + '\n')

            #words_integer + special inbetween letters

            

            combinations = []
            for word_tag in words_tags:
                words_list = words_data[word_tag]
                for dob_value in integers_data[integers_tag]:
                    for word in words_list:
                        for i in range(len(word)):
                            for j in range(0,len(special_characters)):
                                combination = word[:i] + special_characters[j]  + word[i:] + dob_value
                                combinations.append(combination)
                            
            with open(y+".txt", 'a') as file:
                for combination in combinations:
                    file.write(combination + '\n')

            combinations = []
            for word_tag in words_tags:
                words_list = words_data[word_tag]
                for dob_value in integers_data[integers_tag]:
                    for word in words_list:
                        for i in range(len(dob_value)):
                            for j in range(0,len(special_characters)):
                                combination = word + dob_value[:i]+special_characters[j]  + dob_value[i:]
                                combinations.append(combination)
                            
            with open(y+".txt", 'a') as file:
                for combination in combinations:
                    file.write(combination + '\n')

            combinations = []
            for dob_value in integers_data[integers_tag]:
                for word_tag in words_tags:
                    words_list = words_data[word_tag]
                    for word in words_list:
                        for i in range(len(word) + 1):
                            for j in range(len(word) + 1):
                                for char1 in special_characters:
                                    for char2 in special_characters:
                                        combination = word[:i] + char1 + char2 + word[i:j] + dob_value
                                        combinations.append(combination)

   
        with open(y+".txt", 'r') as file:
            words = file.read().splitlines()

    
        filtered_words = [word.capitalize() for word in words]


        with open(y+"capital.txt", 'w') as file:
            for word in filtered_words:
                file.write(word + '\n')

        return filtered_words
    
    



    
