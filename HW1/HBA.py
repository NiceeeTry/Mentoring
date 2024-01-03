def hamming(seq1, seq2):
    if len(seq1) != len(seq2):
        return -1
    res = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            res+=1
    return res

# print(hamming("foo", "boo"))

def hba1(path, distance):
    with open(path, 'r') as f:
        lines = f.readlines()
    print(lines)

    gorilla = lines[2].strip()
    human = lines[7].strip()

    print(hamming(gorilla, human))



# hba1("./HBA1.txt", hamming)
# (42, 24) # у вас должен получиться другой ответ.

# hba1('./HBA1.txt',1)
# hba1("./HBA1.txt", hamming)


def kmers(seq, k):
    d = {}
    for i in range(len(seq)-k+1):
        # print(seq[i:i+k])
        d[seq[i:i+k]] = d.get(seq[i:i+k], 0) + 1
    print(d)
kmers("abracadabra", 2)