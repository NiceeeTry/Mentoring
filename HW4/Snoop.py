from collections import defaultdict
from random import randint, choice
import io

# ---------------3.a ---------------
def words(file):
    words = []
    for line in file.readlines():
        words += line.split(" ")
    return words


# ---------------3.b ---------------
def tansition_matrix(words):
    matrix = defaultdict(list)

    for i in range(len(words) - 2):
        first, second, third = words[i], words[i+1], words[i+2]
        matrix[(first, second)].append(third)

    return matrix


# ---------------3.c ---------------
def markov_chain(words, matrix, word_count):
    if len(words) < 2 or word_count < 1:
        return 

    first, second = choice(words), choice(words)
    sentence = [first, second]
    
    for _ in range(word_count):
        options = matrix[(first, second)]

        if (first, second) in matrix and options:
            word = choice(options)
        else:
            word = choice(words)

        first, second = second, word
        
        sentence.append(word)

    return " ".join(sentence)


# ---------------3.d ---------------
def snoop_says(path, word_count):
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()
    
    language = words(io.StringIO(text))
    matrix = tansition_matrix(language)
    sentence = markov_chain(language, matrix, word_count)

    return sentence



def test_app():
    f = open("./example.txt.gz")
    language = words(f)
    assert language == ['Ignorance', 'is', 'the', 'curse', 'of', 'God;\n', 'knowledge', 'is', 'the','wing', 'wherewith', 'we', 'fly', 'to', 'heaven.']
    m = tansition_matrix(language)
    assert m["is", "the"] == ['curse', 'wing']


print(snoop_says("./snoop279.txt", 23))
test_app()