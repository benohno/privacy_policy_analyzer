from readability import Readability


def readability_score(text):
    r = Readability(text)

    return round(r.flesch_kincaid().score)


def word_count(text):
    return (len(text.strip().split(" ")))
