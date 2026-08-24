#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

CONTESTS = {
    "physics-olympiad": {
        "title": "AI物理竞赛CPhO专项",
        "icon": "🏆",
        "subtitle": "物理竞赛系统培训 | CPhO/IO Physics",
        "price": "399",
        "desc": "李彦明AI物理竞赛专项课程，覆盖CPhO全国中学生物理竞赛培训，力学/电磁学/光学/热学/近代物理全模块竞赛专项训练",
        "keywords": "物理竞赛,CPhO,IO Physics,物理奥林匹克,竞赛培训",
        "levels": [
            ("竞赛基础", "📚", [
                "力学基础深化：运动学、牛顿定律、动量能量",
                "电磁学基础：电场、磁场、电路分析",
                "竞赛数学工具：微积分、矢量分析、微分方程入门",
                "实验基础：测量误差、数据处理、实验报告",
                "竞赛政策解读：CPhO赛制、评分标准、备赛规划",
                "入门测试：知识水平评估、个性化学习路径"
            ]),
            ("竞赛进阶", "🎯", [
                "力学进阶：振动与波、刚体转动、流体力学",
                "电磁进阶：电磁感应、交流电路、麦克斯韦方程",
                "光学进阶：几何光学、波动光学、激光原理",
                "热学进阶：气体动理论、热力学定律、统计物理",
                "近代物理：狭义相对论、量子力学基础",
                "解题技巧：量纲分析、对称性、近似方法"
            ]),
            ("竞赛冲刺", "🚀", [
                "历年真题解析：历年CPhO真题逐题详解",
                "模拟竞赛训练：限时模拟、评分标准",
                "薄弱点突破：知识点漏洞检测、专项训练",
                "实验竞赛培训：设计性实验、误差分析",
                "考前辅导：知识体系梳理、应试技巧",
                "心理调适：竞赛心态、压力管理"
            ]),
            ("竞赛拓展", "🌟", [
                "国际视野：IO Physics介绍、国际竞赛经验",
                "科研入门：物理研究方法论、学术规范",
                "前沿专题：凝聚态物理、粒子物理、天体物理",
                "竞赛校友：历年竞赛获奖者经验分享",
                "高校衔接：物理强基计划、竞赛保送政策",
                "终身学习：物理思维培养、科学素养提升"
            ])
        ],
        "features": [
            "历年真题AI解析，逐题详解解题思路",
            "竞赛知识点图谱，系统梳理知识体系",
            "实验视频演示，虚拟操作训练",
            "个性化学习路径，根据水平定制方案",
            "模拟考试系统，实时评分反馈",
            "竞赛政策解读，备赛规划指导"
        ],
        "target": "高中10-12年级学生，有志于参加CPhO物理竞赛、IO Physics国际物理奥林匹克的学生"
    },
    "math-olympiad": {
        "title": "AI数学竞赛CMO专项",
        "icon": "🏆",
        "subtitle": "数学竞赛系统培训 | CMO/IMO",
        "price": "399",
        "desc": "李彦明AI数学竞赛专项课程，覆盖CMO中国数学奥林匹克培训，数论/组合/几何/代数全模块竞赛专项训练",
        "keywords": "数学竞赛,CMO,IMO,数学奥林匹克,竞赛培训",
        "levels": [
            ("竞赛基础", "📚", [
                "竞赛数学导论：竞赛数学思维、解题方法论",
                "数论基础：整除理论、同余理论、素数分布",
                "代数基础：不等式证明、多项式理论",
                "几何基础：平面几何定理、几何变换入门",
                "组合基础：计数原理、抽屉原理、归纳法",
                "入门测试：竞赛水平评估、学习路径规划"
            ]),
            ("竞赛进阶", "🎯", [
                "数论进阶：二次剩余、费马小定理、中国剩余定理",
                "代数进阶：高级不等式、函数方程、数列与级数",
                "几何进阶：塞瓦定理、梅涅劳斯定理、反演变换",
                "组合进阶：图论基础、容斥原理、递归数列",
                "解题技巧：构造法、分类讨论、极端原理",
                "专题训练：各专题高频考点强化训练"
            ]),
            ("竞赛冲刺", "🚀", [
                "历年真题解析：历年CMO/IMO真题逐题详解",
                "模拟竞赛训练：限时模拟、评分标准",
                "薄弱点突破：知识点漏洞检测、专项训练",
                "考前辅导：知识体系梳理、应试技巧",
                "心理调适：竞赛心态、压力管理",
                "冲刺题库：高频考点专项训练"
            ]),
            ("竞赛拓展", "🌟", [
                "国际视野：IMO介绍、国际竞赛经验",
                "数学思维：数学建模、数学证明方法论",
                "前沿专题：组合几何、解析数论、图论前沿",
                "竞赛校友：历年竞赛获奖者经验分享",
                "高校衔接：数学强基计划、竞赛保送政策",
                "终身学习：数学思维培养、逻辑能力训练"
            ])
        ],
        "features": [
            "历年真题AI解析，逐题详解解题思路",
            "竞赛知识点图谱，系统梳理知识体系",
            "几何动态演示，直观理解几何变换",
            "个性化学习路径，根据水平定制方案",
            "模拟考试系统，实时评分反馈",
            "竞赛政策解读，备赛规划指导"
        ],
        "target": "高中10-12年级学生，有志于参加CMO数学竞赛、IMO国际数学奥林匹克的学生"
    },
    "chem-olympiad": {
        "title": "AI化学竞赛CChO专项",
        "icon": "🏆",
        "subtitle": "化学竞赛系统培训 | CChO/IChO",
        "price": "399",
        "desc": "李彦明AI化学竞赛专项课程，覆盖CChO全国中学生化学竞赛培训，结构/物化/分析/有机全模块竞赛专项训练",
        "keywords": "化学竞赛,CChO,IChO,化学奥林匹克,竞赛培训",
        "levels": [
            ("竞赛基础", "📚", [
                "竞赛化学导论：竞赛化学思维、解题方法论",
                "无机化学：元素化合物、配合物化学、氧化还原",
                "有机化学：有机反应、官能团转化、合成基础",
                "分析化学：定量分析、仪器分析基础",
                "实验基础：基本实验操作、数据处理方法",
                "入门测试：竞赛水平评估、学习路径规划"
            ]),
            ("竞赛进阶", "🎯", [
                "结构化学：原子结构、分子结构、晶体结构",
                "物理化学：化学热力学、化学动力学、电化学",
                "有机深化：反应机理、合成设计、谱图解析",
                "分析深化：光谱分析、色谱分析、电化学分析",
                "实验深化：有机合成实验、物质制备与提纯",
                "解题技巧：推断题方法、计算题技巧"
            ]),
            ("竞赛冲刺", "🚀", [
                "历年真题解析：历年CChO真题逐题详解",
                "模拟竞赛训练：限时模拟、评分标准",
                "薄弱点突破：知识点漏洞检测、专项训练",
                "实验竞赛培训：设计性实验、误差分析",
                "考前辅导：知识体系梳理、应试技巧",
                "冲刺题库：高频考点专项训练"
            ]),
            ("竞赛拓展", "🌟", [
                "国际视野：IChO介绍、国际竞赛经验",
                "科研入门：化学研究方法论、学术规范",
                "前沿专题：纳米化学、绿色化学、材料化学",
                "竞赛校友：历年竞赛获奖者经验分享",
                "高校衔接：化学强基计划、竞赛保送政策",
                "终身学习：化学思维培养、科学素养提升"
            ])
        ],
        "features": [
            "历年真题AI解析，逐题详解解题思路",
            "竞赛知识点图谱，系统梳理知识体系",
            "分子结构3D展示，直观理解空间构型",
            "个性化学习路径，根据水平定制方案",
            "模拟考试系统，实时评分反馈",
            "竞赛政策解读，备赛规划指导"
        ],
        "target": "高中10-12年级学生，有志于参加CChO化学竞赛、IChO国际化学奥林匹克的学生"
    },
    "bio-olympiad": {
        "title": "AI生物竞赛CBO专项",
        "icon": "🏆",
        "subtitle": "生物竞赛系统培训 | CBO/IBo",
        "price": "399",
        "desc": "李彦明AI生物竞赛专项课程，覆盖CBO全国中学生生物学竞赛培训，遗传/分子/生态/生理全模块竞赛专项训练",
        "keywords": "生物竞赛,CBO,IBo,生物奥林匹克,竞赛培训",
        "levels": [
            ("竞赛基础", "📚", [
                "竞赛生物导论：竞赛生物思维、解题方法论",
                "细胞生物学：细胞结构、细胞代谢、细胞分裂",
                "遗传学基础：孟德尔遗传、伴性遗传、群体遗传",
                "植物学基础：植物形态、植物生理、植物分类",
                "动物学基础：动物分类、动物生理、动物行为",
                "入门测试：竞赛水平评估、学习路径规划"
            ]),
            ("竞赛进阶", "🎯", [
                "分子生物学：DNA复制、基因表达、基因调控",
                "遗传学深化：突变与变异、染色体变异、基因工程",
                "生理学深化：神经调节、体液调节、免疫调节",
                "生态学深化：种群动态、群落演替、生态系统",
                "生物化学：蛋白质、核酸、酶与代谢",
                "解题技巧：长句表达、实验设计、数据分析"
            ]),
            ("竞赛冲刺", "🚀", [
                "历年真题解析：历年CBO真题逐题详解",
                "模拟竞赛训练：限时模拟、评分标准",
                "薄弱点突破：知识点漏洞检测、专项训练",
                "实验竞赛培训：显微镜操作、实验设计",
                "考前辅导：知识体系梳理、应试技巧",
                "冲刺题库：高频考点专项训练"
            ]),
            ("竞赛拓展", "🌟", [
                "国际视野：IBo介绍、国际竞赛经验",
                "科研入门：生物学研究方法论、学术规范",
                "前沿专题：合成生物学、表观遗传学、精准医学",
                "竞赛校友：历年竞赛获奖者经验分享",
                "高校衔接：生物强基计划、竞赛保送政策",
                "终身学习：生物思维培养、科学素养提升"
            ])
        ],
        "features": [
            "历年真题AI解析，逐题详解解题思路",
            "竞赛知识点图谱，系统梳理知识体系",
            "3D细胞结构展示，动态旋转观察细胞器",
            "个性化学习路径，根据水平定制方案",
            "模拟考试系统，实时评分反馈",
            "竞赛政策解读，备赛规划指导"
        ],
        "target": "高中10-12年级学生，有志于参加CBO生物竞赛、IBo国际生物学奥林匹克的学生"
    },
    "it-olympiad": {
        "title": "AI信息学竞赛NOI专项",
        "icon": "🏆",
        "subtitle": "信息学竞赛系统培训 | NOI/CSP/CTSC",
        "price": "399",
        "desc": "李彦明AI信息学竞赛专项课程，覆盖NOI全国青少年信息学奥林匹克竞赛培训，数据结构/算法/CSP/NOIP全模块竞赛专项训练",
        "keywords": "信息学竞赛,NOI,CSP,NOIP,蓝桥杯,编程竞赛",
        "levels": [
            ("竞赛基础", "📚", [
                "竞赛导论：信息学竞赛介绍、CSP/NOIP赛制",
                "编程语言：C++基础语法、输入输出、控制结构",
                "基础算法：枚举、排序、查找、递归入门",
                "数据结构：数组、链表、栈、队列",
                "编程规范：代码风格、调试技巧、错误处理",
                "入门测试：编程水平评估、学习路径规划"
            ]),
            ("竞赛进阶", "🎯", [
                "数据结构深化：树、图、堆、并查集",
                "算法深化：动态规划、贪心、分治、搜索",
                "字符串算法：KMP、Trie、哈希",
                "数论算法：素数筛、最大公约数、欧拉函数",
                "图论算法：最短路径、最小生成树、拓扑排序",
                "解题技巧：复杂度分析、优化策略"
            ]),
            ("竞赛冲刺", "🚀", [
                "历年真题解析：历年CSP/NOIP/NOI真题详解",
                "模拟竞赛训练：限时模拟、评分标准",
                "薄弱点突破：知识点漏洞检测、专项训练",
                "编程实战：Codeforces/LeetCode刷题训练",
                "考前辅导：知识体系梳理、应试技巧",
                "冲刺题库：高频考点专项训练"
            ]),
            ("竞赛拓展", "🌟", [
                "国际视野：IOI介绍、国际竞赛经验",
                "高级算法：网络流、字符串高级算法、计算几何",
                "竞赛技巧：调试方法、考场策略、心态管理",
                "竞赛校友：历年竞赛获奖者经验分享",
                "高校衔接：信息学强基计划、竞赛保送政策",
                "终身学习：编程思维培养、算法能力训练"
            ])
        ],
        "features": [
            "历年真题AI解析，逐题详解解题思路",
            "竞赛知识点图谱，系统梳理知识体系",
            "代码在线编辑，实时运行调试",
            "个性化学习路径，根据水平定制方案",
            "模拟考试系统，实时评分反馈",
            "竞赛政策解读，备赛规划指导"
        ],
        "target": "小学高年级至高中学生，有志于参加CSP-J/S、NOIP、NOI信息学竞赛的学生"
    }
}

CSS = '''<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--primary:#6366f1;--secondary:#8b5cf6;--accent:#06b6d4;--success:#10b981;--warning:#f59e0b;--danger:#ef4444;--dark:#0f172a}
body{font-family:"PingFang SC","Microsoft YaHei",system-ui,sans-serif;background:#020617;color:#e2e8f0;min-height:100vh;line-height:1.6}
::-webkit-scrollbar{width:6px}
::-webkit-scrollbar-track{background:rgba(15,23,42,0.5)}
::-webkit-scrollbar-thumb{background:var(--primary);border-radius:3px}
.header{background:linear-gradient(135deg,#0f172a 0%,#1e1b4b 50%,#4c1d95 100%);padding:60px 20px;text-align:center}
.header h1{font-size:2.5em;font-weight:900;margin-bottom:15px;background:linear-gradient(135deg,#fff,#c4b5fd);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.header .subtitle{color:#a5b4fc;font-size:1.1em;margin-bottom:20px}
.nav{background:rgba(15,23,42,0.98);padding:14px 20px;border-bottom:1px solid rgba(99,102,241,0.2)}
.nav-content{max-width:1200px;margin:0 auto;display:flex;justify-content:center;gap:20px}
.nav a{color:#e2e8f0;text-decoration:none;font-weight:500;padding:8px 16px;border-radius:8px;transition:all 0.3s}
.nav a:hover{color:var(--primary);background:rgba(99,102,241,0.1)}
.container{max-width:1200px;margin:0 auto;padding:40px 20px}
.section{margin-bottom:40px}
.card{background:linear-gradient(145deg,rgba(30,27,75,0.9),rgba(49,46,129,0.7));border-radius:18px;padding:30px;border:1px solid rgba(99,102,241,0.25);margin-bottom:25px}
.card h2{font-size:1.4em;margin-bottom:18px;color:var(--accent);display:flex;align-items:center;gap:10px}
.card h3{font-size:1.1em;margin:15px 0 10px;color:#fff}
.card p{color:#94a3b8;line-height:1.8;margin:8px 0}
.card ul{list-style:none;padding:0}
.card li{padding:8px 0 8px 25px;color:#cbd5e1;border-bottom:1px solid rgba(99,102,241,0.1);position:relative}
.card li:before{content:"✓";position:absolute;left:0;color:var(--success);font-weight:bold}
.level-card{background:rgba(15,23,42,0.8);border-radius:12px;padding:20px;margin:15px 0;border:1px solid rgba(99,102,241,0.15)}
.level-card h3{color:var(--primary);font-size:1.2em;margin-bottom:15px;display:flex;align-items:center;gap:8px}
.level-card ul li{padding:10px 0 10px 30px;font-size:0.95em}
.price-section{text-align:center;padding:40px;background:linear-gradient(135deg,#1e1b4b,#4c1d95);border-radius:20px;margin-top:30px}
.price-section .price{font-size:3em;font-weight:900;background:linear-gradient(135deg,var(--primary),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin:15px 0}
.price-section .desc{color:#94a3b8;margin-bottom:25px}
.btn{display:inline-block;padding:14px 35px;background:linear-gradient(135deg,var(--primary),var(--secondary));border-radius:50px;color:#fff;font-weight:700;text-decoration:none;font-size:1.1em;transition:all 0.3s}
.btn:hover{transform:scale(1.05);box-shadow:0 10px 30px rgba(99,102,241,0.4)}
.footer{background:rgba(15,23,42,0.98);text-align:center;padding:30px 20px;border-top:1px solid rgba(99,102,241,0.2)}
.footer p{color:#64748b;margin:6px 0;font-size:0.9em}
@media(max-width:768px){.header h1{font-size:1.8em}.nav-content{flex-direction:column;gap:10px}}
</style>'''

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} - 李彦明全学段AI课程</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
{css}
</head>
<body>

<div class="header">
<h1>{icon} {title}</h1>
<div class="subtitle">{subtitle}</div>
</div>

<div class="nav">
<div class="nav-content">
<a href="/">首页</a>
<a href="/ai-courses/">全部课程</a>
<a href="tel:15684394135">📞 联系报名</a>
</div>
</div>

<div class="container">

<div class="section">
<div class="card">
<h2>📋 课程简介</h2>
<p>{desc}</p>
</div>
</div>

<div class="section">
<div class="card">
<h2>📚 课程大纲</h2>
<p>覆盖竞赛基础→进阶→冲刺→拓展完整体系</p>
</div>
<div class="card">
<h2>📖 完整课程大纲</h2>
{levels_html}
</div>
</div>

<div class="section">
<div class="card">
<h2>📚 核心功能</h2>
<ul>
{features_html}
</ul>
</div>
</div>

<div class="section">
<div class="card">
<h2>🎯 适用对象</h2>
<p>{target}</p>
</div>
</div>

<div class="section">
<div class="card">
<h2>📊 学习效果</h2>
<ul>
<li>系统掌握竞赛全学段核心知识点</li>
<li>提升解题能力与竞赛技巧</li>
<li>培养学科思维与创新能力</li>
<li>AI辅助个性化学习路径</li>
<li>学习进度实时追踪反馈</li>
</ul>
</div>
</div>

<div class="price-section">
<h2 style="color:#fff;font-size:1.5em;margin-bottom:10px">{icon} {title}</h2>
<div class="price">¥{price}起</div>
<div class="desc">竞赛专项培训课程，AI驱动个性化学习</div>
<a href="tel:15684394135" class="btn">📞 立即报名咨询</a>
</div>

</div>

<div class="footer">
<p>© 2026 李彦明 AI课程 | 联系电话：15684394135</p>
<p>覆盖小学、初中、高中全学段AI课程开发</p>
</div>

</body>
</html>'''

for course_id, data in CONTESTS.items():
    dir_path = f"E:/liyiming-edu/ai-courses/{course_id}"
    os.makedirs(dir_path, exist_ok=True)

    # 构建课程大纲HTML
    levels_html = ""
    for level_name, level_icon, contents in data["levels"]:
        items = "".join([f'<li>{c}</li>\n' for c in contents])
        levels_html += f'''
<div class="level-card">
<h3>{level_icon} {level_name}</h3>
<ul>
{items}
</ul>
</div>
'''

    # 构建功能HTML
    features_html = "".join([f'<li>{f}</li>\n' for f in data["features"]])

    # 填充模板
    html = HTML_TEMPLATE.format(
        title=data["title"],
        icon=data["icon"],
        subtitle=data["subtitle"],
        desc=data["desc"],
        keywords=data["keywords"],
        css=CSS,
        levels_html=levels_html,
        features_html=features_html,
        target=data["target"],
        price=data["price"]
    )

    with open(f"{dir_path}/index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ 生成: {course_id}")

print("\n🎉 全部竞赛课程页面生成完成!")
