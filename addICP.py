import os
import re

def add_icp_to_files():
    # 修改后的ICP链接样式
    copyright_pattern = re.compile(r'<p\s+style="color:\s*gray;">©万源中学高2028届钱学森班 2025，保留所有权利。</p>')
    icp_html = '\n    <a href="https://icp.gov.moe/?keyword=20251209" target="_blank" style="text-align: center;color: gray;text-decoration: none;">萌ICP备20251209号</a><br>'
    
    # 遍历当前目录及子目录
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.readlines()
                
                # 查找并插入ICP链接
                modified = False
                for i, line in enumerate(content):
                    if copyright_pattern.search(line):
                        # 在匹配行后插入ICP链接
                        content.insert(i+1, icp_html + '\n')
                        modified = True
                        break  # 每个文件只修改第一个匹配项
                
                # 写回修改后的内容
                if modified:
                    with open(file_path, 'w', encoding='utf-8', newline='') as f:
                        f.writelines(content)
                    print(f'已更新文件：{file_path}')
                else:
                    print(f'未找到版权声明：{file_path}')

if __name__ == '__main__':
    add_icp_to_files()