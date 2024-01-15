import gzip
import bz2

SHE_BANG = "#!"

# ---------------2.a ---------------
def reader(path, mode="rt", encoding="UTF-8"):
    if path.endswith('.gz'):
        return gzip.open(path, mode, encoding=encoding)
    elif path.endswith('.bz2'):
        return bz2.open(path, mode)
    else:
        return open(path, mode, encoding=encoding)

    return open(path, mode=mode, encoding=encoding)

print(reader("./example.txt"))
print(reader("./example.txt.gz", mode="rt", encoding="ascii"))
print(reader("./example.txt.bz2", mode="wb"))


# ---------------2.б ---------------
def parse_shebang(path):
    with open(path)  as file:
        line = file.readline()
    if line.startswith(SHE_BANG):
        return line[2:].strip()
    return None


def test_parse_shebang():
    assert parse_shebang("./example.txt") == "/bin/sh"
    assert parse_shebang("./example2.txt") == "/usr/bin/env python -v"

test_parse_shebang()