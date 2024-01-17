def hamming(seq1, seq2):
    if len(seq1) != len(seq2):
        return -1
    res = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            res+=1
    return res


def hba1(path, distance):
    with open(path, 'r') as f:
        lines = f.readlines()

    min_amount = float("-inf")
    first, second = -1, -1
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            if min_amount < hamming(lines[i], lines[j]):
                min_amount = hamming(lines[i], lines[j])
                first, second = i, j
    # print(min_amount, "min value")
    return (first, second)




# print(hba1("./HBA1.txt", hamming))
# (42, 24) # у вас должен получиться другой ответ.

print(hba1('./HBA1.txt',2))
# hba1("./HBA1.txt", hamming)


def kmers(seq, k):
    d = {}
    for i in range(len(seq)-k+1):
        d[seq[i:i+k]] = d.get(seq[i:i+k], 0) + 1
    # print(d)
    return d
# kmers("abracadabra", 2)

def distance1(seq1, seq2, k=2):
    freq1 = kmers(seq1, k)
    freq2 = kmers(seq2, k)

    keys_union = set(freq1.keys()).union(set(freq2.keys()))
    l1_distance = 0

    for key in keys_union:
        l1_distance += abs(freq1.get(key, 0) - freq2.get(key, 0))

    return l1_distance

def all_distances(path):
    with open(path, 'r') as f:
        lines = f.readlines()

    first, second = -1, -1
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
                amount = distance1(lines[i], lines[j])
                print(amount, i, j)
    # print(min_amount, "min value")
    # return (first, second)
# print(distance1("abracadabra", "abracadabra"))
# print(distance1("abracadabra", "anaconda"))
# print(distance1("abracadabra", "abra"))
# print(hamming("MVLSADDKTNIKNCWGKIGGHGGEYGEEALQRMFAAFPTTKTYFSHIDVSPGSAQVKAHGKKVADALAKAADHVEDLPGALSTLSDLHAHKLRVDPVNFKFLSHCLLVTLACHHPGDFTPAMHASLDKFLASVSTVLTSKYR", "MVLSAADKNNVKGIFTKIAGHAEEYGAETLERMFTTYPPTKTYFPHFDLSHGSAQIKGHGKKVVAALIEAANHIDDIAGTLSKLSDLHAHKLRVDPVNFKLLGQCFLVVVAIHHPAALTPEVHASLDKFLCAVGTVLTAKYR"))
all_distances('./HBA1.txt')