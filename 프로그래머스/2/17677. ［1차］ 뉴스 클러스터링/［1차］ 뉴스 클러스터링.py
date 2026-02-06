from collections import Counter

def solution(str1, str2):

    def get_multiset(s):
        s = s.lower()
        res = []
        for i in range(len(s) - 1):
            pair = s[i:i+2]
            if pair.isalpha():
                res.append(pair)
        return res

    list1 = get_multiset(str1)
    list2 = get_multiset(str2)

    counter1 = Counter(list1)
    counter2 = Counter(list2)

    intersection = list((counter1 & counter2).elements())
    union = list((counter1 | counter2).elements())

    if not union:
        j_similarity = 1
    else:
        j_similarity = len(intersection) / len(union)

    return int(j_similarity * 65536)