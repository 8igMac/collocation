from collocation.likelihood_ratio_test import likelihood_ratio_test
import sys

from collocation.ttest import ttest
from collocation.chi_square_test import chi_square_test
from collocation.utils import get_sents, get_test_data, evalutate

# Measure collocation identification method.
if len(sys.argv) == 2 and sys.argv[1] == 'measure':
    test_data = get_test_data()
    sents = get_sents()
    evalutate(ttest, test_data, sents)
    evalutate(chi_square_test, test_data, sents)
    evalutate(likelihood_ratio_test, test_data, sents)
else:
    print('Usage: python -m collocation measure')
