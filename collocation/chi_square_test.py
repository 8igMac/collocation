from collocation.ttest import find

# Hyperparameters
window_size = 5
threshold = 7.815 # degree of freedom: 4 - 1 = 3, alpha = 0.05

# Tell if the given collocation pair is significant by using Chi-Square Test.
def chi_square_test(target, candidate, sents):
    o11 = 0
    o12 = 0
    o21 = 0
    o22 = 0

    for sent in sents:
        target_pos = find(sent, target)
        candidate_pos = find(sent, candidate)

        if target_pos != -1:
            if candidate_pos != -1 and abs(candidate_pos - target_pos) < window_size:
                o11 += 1
            else:
                o12 += 1
        else:
            if candidate_pos != -1:
                o21 += 1
            else:
                o22 += 1

    # # Debug
    # print(target, candidate)
    # print(f'o11: {o11}')
    # print(f'o12: {o12}')
    # print(f'o21: {o21}')
    # print(f'o22: {o22}')

    chi_square = len(sents) * (o11*o22 - o12*o21) ** 2 / ((o11 + o12) * (o11 + o21) * (o12 + o22) * (o21 + o22)) 
    return chi_square > threshold
