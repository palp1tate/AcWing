import os

# GitHub 用户名和仓库名
github_user = 'palp1tate'
github_repo = 'AcWing'
base_url = f"https://github.com/{github_user}/{github_repo}/blob/master/markdown/"

# 获取markdown目录下的所有Markdown文件
markdown_dir = 'markdown'
files = [f for f in os.listdir(markdown_dir) if os.path.isfile(os.path.join(markdown_dir, f)) and f.endswith('.md')]

# 生成Markdown表格
table_rows = ["| 题目 | 链接 |"]
table_rows.append("| --- | --- |")
for file in files:
    file_path = os.path.join(base_url, file)
    table_rows.append(f"| {file[:-3]} | [{file}]({file_path}) |")  # 假设文件名没有扩展名，如你的题解文件名为'001.md'

# 组装最终的README内容
readme_content = "# 题解目录\n\n" + "\n".join(table_rows) + "\n"

# 写入README.md到根目录
with open('README.md', 'w') as f:
    f.write(readme_content)
