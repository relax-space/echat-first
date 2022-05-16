import pandas as pd
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType

data1 = [{
    'name': 'apple',
    'zh': '苹果',
    'numbers': 10000
}, {
    'name': 'cherry',
    'zh': '樱桃',
    'numbers': 6181
}, {
    'name': 'dates',
    'zh': '枣子',
    'numbers': 4386
}, {
    'name': 'durian',
    'zh': '榴莲',
    'numbers': 4055
}, {
    'name': 'grape',
    'zh': '葡萄',
    'numbers': 2467
}, {
    'name': 'lemon',
    'zh': '柠檬',
    'numbers': 2244
}, {
    'name': 'lichee',
    'zh': '荔枝',
    'numbers': 1868
}, {
    'name': 'mango',
    'zh': '芒果',
    'numbers': 1484
}, {
    'name': 'olive',
    'zh': '橄榄',
    'numbers': 1112
}, {
    'name': 'orange',
    'zh': '橘子',
    'numbers': 865
}, {
    'name': 'peach',
    'zh': '桃子',
    'numbers': 847
}, {
    'name': 'pomelo',
    'zh': '柚子',
    'numbers': 582
}, {
    'name': 'pineapple',
    'zh': '菠萝',
    'numbers': 582
}, {
    'name': 'walnut',
    'zh': '核桃',
    'numbers': 360
}]

df = pd.DataFrame(data1)
WordCloud().add('',
                df[['name', 'numbers']].values.tolist(),
                shape=SymbolType.DIAMOND).render('data/3.html')
WordCloud().add('',
                df[['zh', 'numbers']].values.tolist(),
                shape=SymbolType.DIAMOND).render('data/4.html')
