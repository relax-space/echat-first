'''
说明: 一个简单的直方图 和饼图
'''
import pandas as pd
from pyecharts.charts import Bar, Pie

data1 = [10, 14, 16, 29, 12]

df = pd.DataFrame(data1)
# 如果需要横着显示, 则调用方法reversal_axis
# df[0]表示取第0列的series
Bar().add_xaxis(df.index.tolist()).add_yaxis(
    '', df[0].values.tolist()).render('data/1.html')
# df[0].items(): 值由index和value组成 [(0, 10), (1, 14), (2, 16), (3, 29), (4, 12)]
Pie().add('', list(df[0].items())).render('data/2.html')
