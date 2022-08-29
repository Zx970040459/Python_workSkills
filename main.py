# coding:utf-8
import os
import pdfplumber
import pandas as pd

file = os.path.expanduser("test2.pdf")

with pdfplumber.open(file) as pdf:
    item = []  # 定义保存pdf表格内数据的数据集
    save = []  # 定义输入Excel的数据集
    hangshu = 0
    for page in pdf.pages:
        text = page.extract_table()
        if text is not None:
            for i in text:
                item.append(i)
                if len(item[0]) == 6:  # 如果列数为6
                    save = pd.DataFrame(item[0:],
                                        columns=['Object / part', 'Manufacturer/', 'Type / model', 'Technical data',
                                                 'Standard', 'Mark(s) of conformity1)'])
                    print('第 [%s] 页输出成功！列数为：6' % str(page))
                if len(item[0]) == 8:  # 如果列数为8
                    save = pd.DataFrame(item[0:],  # 从第0行开始保存
                                        columns=['Object / part', 'Manufacturer/', 'Type / model', 'Technical data',
                                                 'Standard', 'Mark(s) of conformity1)', '', ''])
                    print('第 [%s] 页输出成功！列数为：8' % str(page))
                else:
                    print('第 [%s] 页不存在表格或者不存在列数为6，8的表格！' % str(page))
                hangshu = hangshu + 1
            print('行数为：%d' % hangshu)
        else:
            print('页面为空，无法处理！')
    save.to_excel('output.xlsx')
    print('PDF总页数为：%d' % len(pdf.pages))
    print('导出成功！文件名为：output.xlsx')
