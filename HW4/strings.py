# --------------- 1.a ---------------
def capwords(s, sep=None):
    if sep:
        words = s.strip().title().replace('\n', '').split(sep)
        return sep.join(words)
    words = s.strip().title().replace('\n', '').split()
    return ' '.join(words)

def test_capwords():
    assert capwords("foo,,bar,", sep=",") == "Foo,,Bar,"
    assert capwords(" foo \nbar\n") == "Foo Bar"
    assert capwords("this-is-a-test", sep="-") == "This-Is-A-Test"

test_capwords()

# --------------- 1.б ---------------
def cut_suffix(s, suffix):
    if suffix and s.endswith(suffix):
        return s[:-len(suffix)]
    return s


def test_cut_suffix():
    assert cut_suffix("foobar", "bar") == 'foo'
    assert cut_suffix("foobar", "baz") == 'foobar'
    assert cut_suffix("hello world", "world") == 'hello '
    assert cut_suffix("abcabcabc", "abc") == 'abcabc'
    assert cut_suffix("abcdef", "xyz") == 'abcdef'
    assert cut_suffix("", "") == ''
    assert cut_suffix("suffix", "") == 'suffix'

test_cut_suffix()

# --------------- 1.в ---------------
def boxed(s, fill="*", pad=1):
    border = fill * (len(s) + 2 * pad + 2)
    s = f" {s} "
    s = s.center(len(s) + 2 * pad, fill)
    return f"{border}\n{s}\n{border}"
    
def test_boxed():
    assert boxed("Hello world", fill="*", pad=2) == "*****************\n** Hello world **\n*****************"
    assert boxed("Fishy", fill="#", pad=1) == "#########\n# Fishy #\n#########"

test_boxed()

# --------------- 1.г ---------------
def find_all(s, sub):
    count = s.count(sub)
    res = []
    start = 0
    for _ in range(count):
        start = s.find(sub, start)
        if start == -1:
            break
        res.append(start)
        start += 1
    return res


def test_find_all():
    assert find_all("abracadabra", "a") == [0, 3, 5, 7, 10]
    assert find_all("hello world", "o") == [4, 7]
    assert find_all("mississippi", "ss") == [2, 5]
    assert find_all("python is awesome", "z") == []
    assert find_all("", "a") == []

test_find_all()

# --------------- 1.д ---------------
def common_prefix(s1, s2, *args):
    arr = sorted([s1,s2]+list(args))
    first = arr[0]
    last = arr[-1]
    min_length = min(len(first), len(last))
    answer = ""
    for i in range(min_length):
        if first[i] != last[i]:
            return answer
        answer += first[i]
    return answer

def test_common_prefix():
    assert common_prefix("abra", "abracadabra", "abrasive") == "abra"
    assert common_prefix("abra", "foobar") == ""
    assert common_prefix("apple", "apricot", "april") == "ap"
    assert common_prefix("cat", "dog", "cow") == ""
    assert common_prefix("", "abc", "def") == ""
    
test_common_prefix