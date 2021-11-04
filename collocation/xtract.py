# Return candidate collocation pair.
def xtract(word, sents):
    candidate_tuples = list()
    candidate_tuples.append((word, '中心'))
    candidate_tuples.append((word, '病毒'))
    candidate_tuples.append((word, '說明'))
    return candidate_tuples
