import os
import re

def remove_icp_from_files():
    # 更新正则表达式匹配新样式
    icp_pattern = re.compile(
        r'<a\s+[^>]*href="https://icp\.gov\.moe/\?keyword=20251209"[^>]*'
        r'style\s*=\s*"[^"]*text-align:\s*center[^"]*"[^>]*>'
        r'萌ICP备20251209号</a><br>\n?'
    )
    
    # 遍历当前目录及子目录
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 删除所有ICP链接
                new_content, count = icp_pattern.subn('', content)
                
                # 写回修改后的内容
                if count > 0:
                    with open(file_path, 'w', encoding='utf-8', newline='') as f:
                        f.write(new_content)
                    print(f'已清理文件：{file_path}（移除{count}处备案）')
                else:
                    print(f'未找到备案信息：{file_path}')

if __name__ == '__main__':
    remove_icp_from_files()