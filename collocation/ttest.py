import math

# Hyperparameters
window_size = 5
threshold = 1.645

# TODO: replace this function by other method.
# Find target in a given list and return its index.
# Return -1 if not found.
def find(l, target):
    for i, elem in enumerate(l):
        if elem == target:
            return i
    return -1

# Tell if the given collocation pair is significant by using T-test.
def ttest(target, candidate, sents):
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

    # Calculate tvalue.
    total_word_cnt = sum([len(sent) for sent in sents])
    pr_chance = (target_cnt * candidate_cnt) / total_word_cnt ** 2
    pr_pair = joint_cnt / total_word_cnt
    variance = pr_pair - pr_pair ** 2
    if pr_pair == 0:
        tvalue = 0
    else:
        tvalue = (pr_pair - pr_chance) / math.sqrt(variance/total_word_cnt)

    # # debug
    # print(f'Word pair ({target}, {candidate}):')
    # print(f'joint_cnt: {joint_cnt}')
    # print(f'total_word_cnt: {total_word_cnt}')
    # print(f'pr_chance: {pr_chance}')
    # print(f'pr_pair: {pr_pair}')
    # print(f'variance: {variance}')
    # print(f'tvalue: {tvalue}')

    # Return true if we reject the null hypothesis, otherwise return 
    # false.
    return tvalue > threshold
