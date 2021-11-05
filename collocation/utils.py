import json

data_dir = 'data'

# TODO: Replace this implementation with built-in function.
# Return a list of seg.
def _seg_list(words, sep):
    segs = list()
    prev = 0
    for i, word in enumerate(words):
        if word in sep:
            if prev != i:
                segs.append(words[prev:i])
            prev = i + 1
    return segs

def get_sents():
    sents = list()
    # with open(f'{data_dir}/news10000.json') as f:
    with open(f'{data_dir}/hanlp_seg.json') as f:
        for line in f:
            news = json.loads(line)
            for sent in _seg_list(news['hanlp_seg'], '，。！？'):
                sents.append(sent)
    return sents

# Return a list of: (word1, word2, isCollocation), 
def get_test_data():
    test_data = list()

    # True collocation: N, V.
    test_data.append(('疫情', '升溫', 1))
    test_data.append(('大規模', '爆發', 1))
    test_data.append(('肺炎', '確診', 1))
    test_data.append(('社交', '維持', 1))
    test_data.append(('疫苗', '提供', 1))
    test_data.append(('疫苗', '接種', 1))
    test_data.append(('疫苗', '劑', 1))
    test_data.append(('臨床', '試驗', 1))
    test_data.append(('臉書', '發文', 1))
    test_data.append(('產業', '推動', 1))
    test_data.append(('關注', '焦點', 1))

    # False collocation.
    test_data.append(('國家', '長期', 0))
    test_data.append(('民主', '政治', 0))
    test_data.append(('家鄉', '疫情', 0))
    test_data.append(('市長', '表示', 0))
    test_data.append(('主席', '選舉', 0))
    test_data.append(('防疫', '事務', 0))
    test_data.append(('疫苗', '檢討', 0))
    test_data.append(('昨晚', '發文', 0))
    test_data.append(('媒體', '網路', 0))
    test_data.append(('授權', '程序', 0))

    return test_data

def evalutate(method, test_data, sents):
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0
    for word1, word2, is_collocation in test_data:
        result = method(word1, word2, sents)

        if result:
            if is_collocation == 1:
                true_positive += 1
            else:
                print(f'false_positive: {word1}, {word2}')
                false_positive += 1
        else:
            if is_collocation == 1:
                true_negative += 1
            else:
                print(f'false_negative: {word1}, {word2}')
                false_negative += 1

    # Evaluate result.
    precision = true_positive / (true_positive + false_positive)
    recall = true_positive / (true_positive + false_negative)
    f1 = 2 * (precision * recall) / (precision + recall)

    print(f'[{method.__name__}]')
    print(f'precision: {precision}')
    print(f'recall: {recall}')
    print(f'f1 score: {f1}')
    print()
