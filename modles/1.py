import pandas

data = pandas.read_html("https://www.boc.cn/sourcedb/whpj/")
currency_table = data[1].iloc[:, 0:5]
# 使用CSS样式设置文本颜色为白色
currency_table_html = currency_table.to_html(classes='styled-table', index=False)

# 在HTML字符串中添加样式
styled_html = currency_table_html.replace('<td>', '<td style="color:white">')

print(styled_html)