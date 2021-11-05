import math

from scipy.stats import binom

from collocation.ttest import find

# Hyperparameters
window_size = 5
threshold = 7.815 # degree of freedom: 4 - 1 = 3, alpha = 0.05

# Tell if the given collocation pair is significant by using 
# likelihood ratio test.
def likelihood_ratio_test(target, candidate, sents):
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

    total = o11 + o12 + o21 + o22

    # H1: w1 and w2 are independent.
    # H2: w1 and w2 are dependent.
    # 
    # log(L(H1) / L(H2))
    llr = math.log10(binom.pmf(o11, o11+o12, (o11+o21)/total)) +\
        math.log10(binom.pmf(o21, o21+o22, (o11+o21)/total)) -\
        math.log10(binom.pmf(o11, o11+o12, o11/(o11+o12))) -\
        math.log10(binom.pmf(o21, o21+o22, o21/(o21+o22)))

    # -2 * Log likelihood ratio is asymtotically chi-square distributed.
    return -2 * llr > threshold
