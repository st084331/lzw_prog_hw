from io import StringIO


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def encode(unencoded):
    dict_size = 6
    dictionary = {
        "b": 0,
        "a": 1,
        "c": 2,
        "d": 3,
        "_": 4,
        "e": 5
    }
    w = ""
    result = []
    for c in unencoded:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
    if w:
        result.append(dictionary[w])
    return result


def decode(encoded):
    dict_size = 6
    dictionary = {
        "b": 0,
        "a": 1,
        "c": 2,
        "d": 3,
        "_": 4,
        "e": 5
    }
    result = StringIO()
    w = get_key(dictionary, encoded.pop(0))
    result.write(w)
    for k in encoded:
        if k in dictionary.values():
            entry = get_key(dictionary, k)
        elif k >= dict_size:
            entry = w + w[0]
        result.write(entry)
        dictionary[w + entry[0]] = dict_size
        dict_size += 1
        w = entry
    return result.getvalue()


print(encode(
    "abcbbbbbacabbacddacdbbaccbbadadaddd_abcccccbacabbacbbaddbdaccbbddadadcc_bcabbcdabacbbacbbddcbbaccbbdbdadaace"))
print(decode(encode(
    "abcbbbbbacabbacddacdbbaccbbadadaddd_abcccccbacabbacbbaddbdaccbbddadadcc_bcabbcdabacbbacbbddcbbaccbbdbdadaace")))
print(
    "abcbbbbbacabbacddacdbbaccbbadadaddd_abcccccbacabbacbbaddbdaccbbddadadcc_bcabbcdabacbbacbbddcbbaccbbdbdadaace" == decode(
        encode(
            "abcbbbbbacabbacddacdbbaccbbadadaddd_abcccccbacabbacbbaddbdaccbbddadadcc_bcabbcdabacbbacbbddcbbaccbbdbdadaace")))
