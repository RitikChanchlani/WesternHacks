from bs4 import BeautifulSoup
import requests


def check_misspelt_profanity(word, dict_entry):
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k',
                  'l', 'm', 'n', 'p', 'q', 'r', 's', 't',
                  'v', 'w', 'x', 'y', 'z']

    if len(dict_entry) != len(word):
        return False
    else:
        for index in range(len(word)):
            if word[index] != dict_entry[index]:
                for consonant in consonants:
                    if word[index] == consonant or dict_entry[index] == consonant:
                        return False
        return True


def writefile(f1, f2):
    l1 = []
    l2 = []
    try:
        with open(f1, "r") as reader:
            lines = reader.readlines()
            for line in lines:
                l1.append(line)
        with open(f2, "r") as reader:
            lines = reader.readlines()
            for line in lines:
                l2.not_good_words.append(line)
    except FileNotFoundError:
        pass
    l2 = set(l2) - set(l1)
    f = open(f1, 'w')
    for word in l2:
        f.write(word)
    f.close()


class Detector:
    def __init__(self):
        self.good_words = []
        self.not_good_words = []
        self.bad_words = []
        self.filler_words = []
        self.pronouns_file = []

    def checkTweet(self, tweet):
        info = tweet.split()
        for word in info:
            if word in self.filler_words:
                info.remove(word)
        tweet_bad_words = []
        tweet_not_good_words = []
        tweet_bad_emojis = []

        for unaltered_word_index in range(len(info)):
            word = info[unaltered_word_index].lower()
            found = False
            for entry in self.good_words:
                if word == entry:
                    found = True
                    break
            if not found:
                for entry in self.bad_words:
                    if word == entry:
                        tweet_bad_words.append(entry)
                        found = True
                        break
            if not found:
                if word == "🖕":
                    tweet_bad_emojis.append(word)
                    found = True
            if not found:
                for i in range(len(self.not_good_words)):
                    if word == self.not_good_words[i]:
                        negation_words_list = []
                        negation_words_file = open("negation_words.txt", "r")
                        for word in negation_words_file:
                            stripped_word = word.strip()
                            negation_words_list.append(stripped_word)
                        previous_word_index = unaltered_word_index - 1
                        not_counter = 0
                        # continues until the previous word is not a negation word
                        while info[previous_word_index] in negation_words_list:
                            not_counter += 1
                            previous_word_index -= 1
                        # ex: "not not ___" does not count
                        if (not_counter % 2) != 0:
                            found = True
                            break
                        else:
                            if (info[previous_word_index] in self.pronouns_file) or (
                                    info[unaltered_word_index + 1] in self.pronouns_file):
                                tweet_not_good_words.append(self.not_good_words[i])
                                found = True
                                break
            if not found:
                for entry in self.bad_words:
                    if word.find(entry) != -1:
                        tweet_bad_words.append(entry)
                        found = True
                        break
            if not found:
                for entry in self.not_good_words:
                    if word.find(entry) != -1:
                        tweet_not_good_words.append(entry)
                        found = True
                        break
            if not found:
                for entry in self.not_good_words:
                    if check_misspelt_profanity(word, entry):
                        tweet_not_good_words.append(entry)
                        found = True
            if not found:
                for entry in self.bad_words:
                    if check_misspelt_profanity(word, entry):
                        tweet_bad_words.append(entry)

        output = ''
        output += "List of vulgar words: "
        for word in tweet_bad_words:
            output += word + ", "
        output += "           "
        output += "List of concerning words: "
        for word in tweet_not_good_words:
            output += word + ", "
        output += "         "

        return output

    def load_dictionary(self, bad_words_file, not_good_words_file, good_words_file, filler_words_file, pronouns_file):
        try:
            with open(bad_words_file, "r") as reader:
                lines = reader.readlines()
                for line in lines:
                    line = line.replace('\n', '')
                    self.bad_words.append(line)
            with open(not_good_words_file, "r") as reader:
                lines = reader.readlines()
                for line in lines:
                    line = line.replace('\n', '')
                    self.not_good_words.append(line)
            with open(good_words_file, "r") as reader:
                lines = reader.readlines()
                for line in lines:
                    line = line.replace('\n', '')
                    self.good_words.append(line)
            with open(filler_words_file, "r") as reader:
                lines = reader.readlines()
                for line in lines:
                    line = line.replace('\n', '')
                    self.filler_words.append(line)
            with open(pronouns_file, "r") as reader:
                lines = reader.readlines()
                for line in lines:
                    line = line.replace('\n', '')
                    self.pronouns_file.append(line)
        except FileNotFoundError:
            pass

    def check_webpage(self, url):
        res = requests.get(url)
        html_page = res.content
        soup = BeautifulSoup(html_page, 'html.parser')
        text = soup.find_all(text=True)

        output = ''
        blacklist = [
            '[document]',
            'noscript',
            'header',
            'html',
            'meta',
            'head',
            'input',
            'script',
            # there may be more elements you don't want, such as "style", etc.
        ]

        for t in text:
            if t.parent.name not in blacklist:
                output += '{} '.format(t)

        return output


# user_text = input("Please enter the text you would like to scan:\n")


d = Detector()
d.load_dictionary("restricted_words.txt", "concerning_words.txt", "dictionary.txt", "filler_words.txt",
                  "pronouns_file.txt")
string = d.check_webpage("https://www.urbandictionary.com")
results = d.checkTweet(string)
print(results)
