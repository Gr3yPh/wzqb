from pypinyin import pinyin, Style

# 学生信息列表
students = [
    {"name": "邓博驺", "role": "体育委员"},
    {"name": "胡程程", "role": "生物课代表"},
    {"name": "李贵漫", "role": "一组组长"},
    {"name": "刘家欢", "role": "化学课代表"},
    {"name": "李堂博", "role": "地理课代表"},
    {"name": "李章萍", "role": "学习委员"},
    {"name": "李仲轩", "role": "英语课代表"},
    {"name": "李晓璐", "role": "组织委员"},
    {"name": "蒲森洁", "role": "音乐委员"},
    {"name": "任蝶", "role": "班长"},
    {"name": "孙思桐", "role": "团支书"},
    {"name": "田楠", "role": "历史课代表"},
    {"name": "王本鑫", "role": "四组组长"},
    {"name": "谢馨怡", "role": "语文课代表"},
    {"name": "杨锦程", "role": "组织委员"},
    {"name": "姚楷瑞", "role": "二组组长"},
    {"name": "喻鹏杰", "role": "政治课代表"},
    {"name": "张芮", "role": "生活委员"},
    {"name": "张胜言", "role": "数学课代表"},
    {"name": "张宗奕", "role": "安全委员"},
    {"name": "赵娜", "role": "三组组长"},
    {"name": "赵仁博", "role": "五组组长"},
    {"name": "朱浩宇", "role": "物理课代表"},
    {"name": "朱闽中", "role": "心理委员"},
    {"name": "周健睿", "role": "纪律委员"},
    {"name": "周子博", "role": "副班长"}
]

# HTML 模板
html_template = '''
<!DOCTYPE html>
<html>

<head>
    <title>万源中学钱学森班</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <style>
        html {{
            scroll-behavior: smooth;
        }}

        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            text-align: center;
        }}

        .container {{
            display: grid;
            width: 100%;
            grid-template-rows: auto 1fr;
            grid-template-columns: 1fr;
            max-width: 1200px;
            margin: 0 auto;
            font-family: "楷体";
            scroll-behavior: smooth;
        }}

        .headerContainer {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 20px;
            background-color: #f8f9fa;
        }}

        .logoAndTitle {{
            display: flex;
            align-items: center;
        }}

        .logoImage {{
            height: 100px;
            margin-right: 20px;
            cursor: pointer;
        }}

        .slogan {{
            font-size: 24px;
            font-weight: bold;
            cursor: pointer;
        }}

        .navLinks {{
            display: flex;
            list-style-type: none;
            padding: 0;
            margin: 0;
        }}

        .navLinks li {{
            margin: 0 15px;
        }}

        .navLinks a {{
            text-decoration: none;
            color: #007bff;
            font-size: 18px;
            scroll-behavior: smooth;
        }}

        .contentContainer {{
            padding: 20px;
            text-align: left;
            display: grid;
            grid-template-columns: 30% auto;
            row-gap: 10px;
            column-gap: 10px;
        }}

        .mateContainer{{
            text-align: center;
            border:1px solid rgb(228, 228, 228);
            border-radius: 2px;
            padding: 10px;
        }}

        .mateTouxiang{{
            width:30%;
        }}

        .mateLink{{
            font-size: 1.2em;
            font-weight: bold;
            text-decoration: none;
            color: black;
        }}

        /* 回到顶部按钮样式 */
        #backToTopBtn {{
            display: none;
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 99;
            font-size: 18px;
            border: none;
            outline: none;
            background-color: #007bff;
            color: white;
            cursor: pointer;
            padding: 10px 15px;
            border-radius: 50%;
            transition: background-color 0.3s;
        }}

        #backToTopBtn:hover {{
            background-color: #0056b3;
        }}

        /* 移动端样式 */
        @media screen and (max-width: 768px) {{
            .headerContainer {{
                flex-direction: column;
                align-items: center;
                padding: 10px;
            }}

            .logoAndTitle {{
                flex-direction: column;
                align-items: center;
                margin-bottom: 10px;
            }}

            .logoImage {{
                height: 80px;
                margin-right: 0;
                margin-bottom: 10px;
            }}

            .slogan h1 {{
                font-size: 24px;
                text-align: center;
            }}

            .navLinks {{
                flex-direction: column;
                align-items: center;
            }}

            .navLinks li {{
                margin: 5px 0;
            }}

            .navLinks a {{
                font-size: 16px;
            }}
        }}
    </style>

    <link rel="icon" href="../favicon.ico" type="image/x-icon">
</head>

<body>
    <div class="container">
        <div class="headerContainer">
            <div class="logoAndTitle">
                <img src="../img/logo.png" class="logoImage" alt="万源中学钱学森班 Logo"
                    onclick="window.location.href='../index.html'">
                <div class="slogan">
                    <h1 onclick="window.location.href='../index.html'">万源中学钱学森班</h1>
                </div>
            </div>
            <ul class="navLinks">
                <li><a href="../index.html">回到主页</a></li>
            </ul>
        </div>
        <div class="contentContainer">
            <div class="mateContainer">
                <img src='img/unknownMate.png' class="mateTouxiang"><br>
                <a class="mateLink" href="mate_{pinyin}.html">{name}</a><br>
                <span>{role}</span>
            </div>
        </div>

        <!-- 回到顶部按钮 -->
        <button id="backToTopBtn" title="回到顶部">↑</button>
        <hr>
        <p style="color: gray;">©万源中学高2028届钱学森班 2025，保留所有权利。</p>
    </div>

    <script>
        // 回到顶部按钮逻辑
        const backToTopBtn = document.getElementById("backToTopBtn");

        // 当用户滚动页面时显示或隐藏按钮
        window.onscroll = function () {{
            if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {{
                backToTopBtn.style.display = "block";
            }} else {{
                backToTopBtn.style.display = "none";
            }}
        }};

        // 点击按钮时平滑滚动到顶部
        backToTopBtn.addEventListener("click", function () {{
            window.scrollTo({{
                top: 0,
                behavior: "smooth"
            }});
        }});
    </script>
</body>

</html>
'''

# 将中文名字转换为驼峰式拼音
def get_camelcase_pinyin(name):
    pinyin_list = pinyin(name, style=Style.NORMAL)
    camelcase_pinyin = pinyin_list[0][0]  # 首字母小写
    for pinyin_part in pinyin_list[1:]:
        camelcase_pinyin += pinyin_part[0].capitalize()  # 后续部分首字母大写
    return camelcase_pinyin

# 创建 HTML 文件
def create_student_html(student):
    pinyin_name = get_camelcase_pinyin(student["name"])  # 获取驼峰式拼音
    filename = f"mate_{pinyin_name}.html"
    content = html_template.format(name=student["name"], role=student["role"], pinyin=pinyin_name)
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"已创建文件: {filename}")

# 为每个学生生成 HTML 文件
for student in students:
    create_student_html(student)

print("所有文件已生成完毕！")
