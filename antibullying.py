def function1(list_word, keyword_value_list):
    num_keyword = 0
    total_score = 0
    for word in list_word:
        for keyword_pairing in keyword_value_list:
            if word == keyword_pairing[0]:
                num_keyword += 1
                total_score += keyword_pairing[1]
    if num_keyword != 0:
        score = total_score / num_keyword
        return score
    else:
        return "none"

def function2(file, keyword_file):
    keyword_list = []
    word_value = []
    stripped_info = []

    count = 0
    total_score = 0
    average = 0
    keyword_count = 0
    total_count = 0

    try:
        # keywords file (code from assignment document)
        keywordfile = open(keyword_file,"r")

        for line in keywordfile:
            count += 1
            keyword_happiness_pair = line.split(",")

            # strip /n from number
            for word in keyword_happiness_pair:
                word_value.append(word.strip())
            # convert happiness value to integer
            word_value[1] = int(word_value[1])

            keyword_list.append(word_value)

            # resets so that the previous pair is not appended again
            word_value = []
        # closes keywords file
        keywordfile.close()

        file = open(file,"r")

        for line in file:
            total_count += 1
            info = line.split()

            for element in info:
                stripped_element = element.strip(" !@#$%^&*()-_+=;:\"\'/.>,<{[}]|\\~`")
                stripped_info.append(stripped_element)

            while "" in stripped_info:
                stripped_info.remove("")
            # word_list is a list of each word in lowercase with no punctuation
            word_list = [word.lower() for word in stripped_info]


            results = function1(word_list, keyword_list)

            if results != "none":
                total_score += results
                keyword_count += 1
                average = total_score / keyword_count

            stripped_info = []

        file.close()

    except IOError:
        return "IOError"

    tuple = (round(average, 3), keyword_count, count)

    return tuple


text = input("Please enter the name of the text file.")
keyword = input("Please enter the name of the keyword file.")

final_results = function2(text, keyword)
# empty list is returned by function2 in the case of IOError

obscenity_rating = final_results[0]
num_keyword_messages = final_results[1]
total_num_messages = final_results[2]

if final_results != "IOError":
    print("\nResults:")
    print("Average meanness score:", obscenity_rating)
    print("Number of keyword texts:", num_keyword_messages)
    print("Total number:", total_num_messages)
else:
    print("\nPlease try again.")
