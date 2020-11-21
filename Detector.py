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

    def checkTweet(self, tweet):
        info = tweet.split()
        print(info)
        tweet_bad_words = []
        tweet_not_good_words = []

        for unaltered_word in info:
            word = unaltered_word.lower()
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
                for i in self.not_good_words:
                    if word == i:
                        tweet_not_good_words.append(i)
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

        return [tweet_bad_words, tweet_not_good_words]

    def load_dictionary(self, bad_words_file, not_good_words_file, good_words_file):
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
        except FileNotFoundError:
            pass

d = Detector()
d.load_dictionary("restricted_words.txt", "concerning_words.txt", "dictionary.txt")
results = d.checkTweet("I railed your mom")
print(results)




