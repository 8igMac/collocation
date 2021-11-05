# Collocation
Finding collocations from a Chinese news corpus.

## Setup
```sh
$ git clone https://github.com/8igMac/collocation.git
$ cd collocation
$ python -m venv venv
$ source venv/bin/activate
$ python -m pip install -r requirements.txt
```

## Data
1. Put data in the `data/` directory. Example data format 
(`data/news.json`)
```
{"hanlp_seg": ["你好", "我的", "名子"]}
{"hanlp_seg": ["你好", "我的", "名子"]}
{"hanlp_seg": ["你好", "我的", "名子"]}
```

2. And modify the data path in `get_sents` function in 
`collocation/utils.py`.

## Performance measurement of collocation identification methods
We measure the performance (precision, recall, F1 score) of 
4 collocation identification methods.
- T-test
- Chi-square test
- Log-likelihood ratios
- Pointwise mutual information

Usage
```sh
# Go to the project root directory.
$ python -m collocation measure
```

## Resources
- Statistical collocation extraction method: [Xtract](http://luthuli.cs.uiuc.edu/~daf/courses/Signals%20AI/Papers/Collocation/p143-smadja.pdf)
