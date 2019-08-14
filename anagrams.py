def init_words(fname):
    words = {}
    with open(fname) as f:
        for line in f:
            word = line.strip()
            words[word] = 1
    return words

def init_anagram_dict(words):
    anagram_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(list(word)))
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = []
        anagram_dict[sorted_word].append(word)
    return anagram_dict

def is_anagram_from_dict(word, anagram_dict):
    key = ''.join(sorted(list(word)))
    if key in anagram_dict:
        values = anagram_dict[key]
        if len(values) >= 2:
            return True
        return False

def get_all_anagrams_from_dict(words, anagram_dict):
    anagrams = []
    for word in words:
        if is_anagram_from_dict(word, anagram_dict):
            anagrams.append(word)
    return anagrams

def find_anagrams(word, anagram_dict):
    key = ''.join(sorted(list(word)))
    if key in anagram_dict:
        return set(anagram_dict[key]).difference(set([word]))
    return set([])



filename = 'popular.txt'
word_dict = init_words (filename)
anagram_dict = init_anagram_dict(word_dict.keys())


allanas = get_all_anagrams_from_dict(word_dict, anagram_dict)
#print(allanas)
#print(len(allanas)), 'anagrams'
mykey = 'silent'
#print(find_anagrams(mykey, anagram_dict))
print('the anagrams of', mykey, 'are', find_anagrams(mykey, anagram_dict))
