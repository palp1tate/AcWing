import os
import re

# GitHub 用户名和仓库名
github_user = 'palp1tate'
github_repo = 'AcWing'
answer_url = f"https://github.com/{github_user}/{github_repo}/blob/master/markdown/"

# 获取markdown目录下的所有Markdown文件
markdown_dir = 'markdown'


# 使用正则表达式匹配文件名中的数字
def extract_number(filename):
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else 0


files = sorted(
    [f for f in os.listdir(markdown_dir) if os.path.isfile(os.path.join(markdown_dir, f)) and f.endswith('.md')],
    key=extract_number
)

# 生成Markdown表格，其中列内容和整个表都居中
table_rows = ["| 原题 | 题解 |", "| :---: | :---: |"]
for file in files:
    file_path = os.path.join(answer_url, file)
    # 读取文件的第一行来获取题目链接
    with open(os.path.join(markdown_dir, file), 'r', encoding='utf-8') as md_file:
        first_line = md_file.readline().strip().replace('# ', '')
    table_rows.append(f"| {first_line} | [{file}](<{file_path}>) |")

# 组装最终的README内容，并使标题和表格居中
readme_content = """
<div align="center">

# AcWing题解目录

""" + "\n".join(table_rows) + "\n</div>"

# 写入README.md到根目录
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)
