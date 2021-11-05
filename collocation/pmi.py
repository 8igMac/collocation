import math

from collocation.ttest import find

# Hyperparameters
window_size = 5
threshold = 3

# Identify collocation by pointwise mutual information.
def pmi(target, candidate, sents):
    target_cnt = 0
    candidate_cnt = 0
    joint_cnt = 0

    # Count word in the corpus.
    for sent in sents:
        target_pos = find(sent, target)
        candidate_pos = find(sent, candidate)

        if target_pos != -1:
            target_cnt += 1

        if candidate_pos != -1:
            candidate_cnt += 1

        if target_pos != -1 and candidate_pos != -1 and abs(candidate_pos - target_pos) < window_size:
            joint_cnt += 1

    total_word_cnt = sum([len(sent) for sent in sents])
    p12 = joint_cnt / total_word_cnt
    p1 = target_cnt / total_word_cnt
    p2 = candidate_cnt /total_word_cnt

    pmi = math.log2(p12 / (p1 * p2))

    return pmi > threshold
