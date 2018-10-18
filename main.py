import numpy as np

def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])
def generate_title(corpus, word_dict):
    first_word = np.random.choice(corpus)
    while first_word.islower():
        first_word = np.random.choice(corpus)
    chain = [first_word]
    n_words = np.random.randint(5, 10)
    i = 0
    while i < n_words:
        new_word = np.random.choice(word_dict[chain[-1]])
        if i == n_words -1:
            if new_word.islower():
                n_words = n_words+1
            inwords = [':', ',','\'s']
            for foo in inwords:
                if foo in new_word:
                    n_words = n_words + 1
            forbiddenwords = ['the', 'my', 'may', 'a', 'by', 'let', 'i', 'is']
            for foo in forbiddenwords:
                if new_word.lower() == foo:
                    n_words = n_words + 1
        chain.append(new_word)
        i = i+1
    return ' '.join(chain).strip(')')
novelsource = open('ln_names.txt', encoding='utf8').read()
corpus = novelsource.split()
pairs = make_pairs(corpus)
word_dict = {}
for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]
i = 0
while i < 50:
    print(generate_title(corpus, word_dict))
    i = i+1