#!/usr/bin/env python3
"""全ワイヤーフレームの内部リンクを相互接続するスクリプト"""

import os
import re
from pathlib import Path

WIREFRAMES_DIR = Path("C:/tmp/anzu-ichinomiyanishi-sitemap/wireframes")

# Define all link mappings: text pattern -> target file
# These will be applied across all pages

LINK_RULES = [
    # === Global Navigation (gnav) ===
    # Already set in templates, but ensure consistency

    # === Breadcrumb links ===
    (r'<a href="#">HOME</a>', '<a href="top.html">HOME</a>'),
    (r'<a href="#">ご利用案内</a>', '<a href="guide-top.html">ご利用案内</a>'),
    (r'<a href="#">診療科紹介</a>', '<a href="department-list.html">診療科紹介</a>'),
    (r'<a href="#">専門医療</a>', '<a href="special-top.html">専門医療</a>'),
    (r'<a href="#">医療連携・紹介</a>', '<a href="area-top.html">医療連携・紹介</a>'),
    (r'<a href="#">病院紹介</a>', '<a href="about-top.html">病院紹介</a>'),
    (r'<a href="#">採用情報</a>', '<a href="recruit-top.html">採用情報</a>'),
    (r'<a href="#">お知らせ</a>', '<a href="news-list.html">お知らせ</a>'),
    (r'<a href="#">市民公開講座</a>', '<a href="seminar.html">市民公開講座</a>'),

    # === Footer links ===
    (r'<a href="#">受診方法</a>', '<a href="guide-outpatient.html">受診方法</a>'),
    (r'<a href="#">外来診療担当表</a>', '<a href="guide-outpatient.html">外来診療担当表</a>'),
    (r'<a href="#">休診案内</a>', '<a href="guide-outpatient.html">休診案内</a>'),
    (r'<a href="#">入院のご案内</a>', '<a href="guide-inpatient.html">入院のご案内</a>'),
    (r'<a href="#">お見舞い・面会</a>', '<a href="guide-inpatient.html">お見舞い・面会</a>'),
    (r'<a href="#">交通アクセス</a>', '<a href="access.html">交通アクセス</a>'),
    (r'<a href="#">病院長ご挨拶</a>', '<a href="about-top.html">病院長ご挨拶</a>'),
    (r'<a href="#">病院概要</a>', '<a href="about-top.html">病院概要</a>'),
    (r'<a href="#">沿革</a>', '<a href="about-top.html">沿革</a>'),
    (r'<a href="#">病棟案内</a>', '<a href="about-ward.html">病棟案内</a>'),
    (r'<a href="#">活動実績</a>', '<a href="about-top.html">活動実績</a>'),
    (r'<a href="#">病院指標</a>', '<a href="about-top.html">病院指標</a>'),
    (r'<a href="#">個人情報保護方針</a>', '<a href="about-top.html">個人情報保護方針</a>'),
    (r'<a href="#">サイト利用について</a>', '<a href="about-top.html">サイト利用について</a>'),
    (r'<a href="#">アクセシビリティ</a>', '<a href="about-top.html">アクセシビリティ</a>'),
    (r'<a href="#">サイトマップ</a>', '<a href="index.html">サイトマップ</a>'),
]

# Per-file specific link fixes
FILE_SPECIFIC_RULES = {
    "top.html": [
        # Quick links
        (r'href="#for-outpatient"', 'href="guide-outpatient.html"'),
        (r'href="#for-inpatient"', 'href="guide-inpatient.html"'),
        (r'href="#for-dock"', 'href="dock.html"'),
        (r'href="#for-medical"', 'href="area-top.html"'),
        # Section links
        (r'href="#news-all"', 'href="news-list.html"'),
        (r'href="#column"', 'href="column-detail.html"'),
        (r'href="#recruit"', 'href="recruit-top.html"'),
    ],
    "guide-top.html": [
        (r'href="#outpatient"', 'href="guide-outpatient.html"'),
        (r'href="#inpatient"', 'href="guide-inpatient.html"'),
        (r'href="#dock"', 'href="dock.html"'),
        (r'href="#access"', 'href="access.html"'),
    ],
    "about-top.html": [
        (r'href="#ward"', 'href="about-ward.html"'),
        (r'href="#column"', 'href="column-detail.html"'),
        (r'href="#seminar"', 'href="seminar.html"'),
    ],
    "department-list.html": [
        (r'href="#detail"', 'href="department-detail.html"'),
    ],
    "recruit-top.html": [
        (r'href="#nurse"', 'href="nurse.html"'),
        (r'href="#resident"', 'href="resident.html"'),
    ],
}

# Sidebar common link patterns to replace
SIDEBAR_RULES = [
    # Guide sidebar
    ('href="#">外来受診', 'href="guide-outpatient.html">外来受診'),
    ('href="#">入院', 'href="guide-inpatient.html">入院'),
    ('href="#">人間ドック', 'href="dock.html">人間ドック'),
    ('href="#">健康診断', 'href="dock.html">健康診断'),
    ('href="#">健診', 'href="dock.html">健診'),
    ('href="#">交通アクセス', 'href="access.html">交通アクセス'),
    # Department sidebar
    ('href="#">消化器内科', 'href="department-detail.html">消化器内科'),
    ('href="#">循環器内科', 'href="department-detail.html">循環器内科'),
    ('href="#">脳神経外科', 'href="department-detail.html">脳神経外科'),
    ('href="#">整形外科', 'href="department-detail.html">整形外科'),
    ('href="#">産婦人科', 'href="department-detail.html">産婦人科'),
    # Center sidebar
    ('href="#">内視鏡センター', 'href="center-detail.html">内視鏡センター'),
    ('href="#">脳卒中センター', 'href="center-detail.html">脳卒中センター'),
    ('href="#">不整脈センター', 'href="center-detail.html">不整脈センター'),
    ('href="#">糖尿病センター', 'href="center-detail.html">糖尿病センター'),
    ('href="#">人工関節センター', 'href="center-detail.html">人工関節センター'),
    # Special sidebar
    ('href="#">レディース外来', 'href="special-top.html">レディース外来'),
    ('href="#">ドクター特集', 'href="special-interview.html">ドクター特集'),
    ('href="#">医療機器', 'href="special-top.html">医療機器'),
    # About sidebar
    ('href="#">病院長', 'href="about-top.html">病院長'),
    ('href="#">病棟のご案内', 'href="about-ward.html">病棟のご案内'),
    ('href="#">市民公開WEB講座', 'href="column-detail.html">市民公開WEB講座'),
    ('href="#">健康のつボ', 'href="column-detail.html">健康のつボ'),
    # News sidebar
    ('href="#">ニュース', 'href="news-list.html">ニュース'),
    ('href="#">お知らせ一覧', 'href="news-list.html">お知らせ一覧'),
    # Recruit sidebar
    ('href="#">看護師採用', 'href="nurse.html">看護師採用'),
    ('href="#">看護師募集', 'href="nurse.html">看護師募集'),
    ('href="#">研修医', 'href="resident.html">研修医'),
    ('href="#">キャリア医師', 'href="recruit-top.html">キャリア医師'),
    # Seminar
    ('href="#">市民公開講座', 'href="seminar.html">市民公開講座'),
    # Area
    ('href="#">医療連携', 'href="area-top.html">医療連携'),
    ('href="#">診察のご予約', 'href="area-top.html">診察のご予約'),
    ('href="#">検査のご予約', 'href="area-top.html">検査のご予約'),
]


def fix_file(filepath):
    """Apply link fixes to a single file."""
    content = filepath.read_text(encoding='utf-8')
    original = content

    # Apply global rules
    for pattern, replacement in LINK_RULES:
        content = content.replace(pattern, replacement)

    # Apply sidebar rules (simple string replacement)
    for pattern, replacement in SIDEBAR_RULES:
        content = content.replace(pattern, replacement)

    # Apply file-specific rules
    filename = filepath.name
    if filename in FILE_SPECIFIC_RULES:
        for pattern, replacement in FILE_SPECIFIC_RULES[filename]:
            content = re.sub(pattern, replacement, content)

    # Fix remaining orphan "#" links in card/button elements with meaningful text
    # Only fix links that have recognizable destination text
    card_link_map = {
        '外来受診の方': 'guide-outpatient.html',
        '入院・お見舞いの方': 'guide-inpatient.html',
        '入院・お見舞い': 'guide-inpatient.html',
        '健診の方': 'dock.html',
        '医療関係者の方': 'area-top.html',
        '診療科一覧': 'department-list.html',
        '診療科紹介': 'department-list.html',
        'センター一覧': 'center-detail.html',
        '専門医療': 'special-top.html',
        '専門外来': 'special-top.html',
        '医療連携': 'area-top.html',
        '病院紹介': 'about-top.html',
        '病棟のご案内': 'about-ward.html',
        '採用情報': 'recruit-top.html',
        '看護師': 'nurse.html',
        '研修医': 'resident.html',
        'ニュース一覧': 'news-list.html',
        '記事一覧': 'news-list.html',
        'お知らせ': 'news-list.html',
        'コラム': 'column-detail.html',
        'WEB講座': 'column-detail.html',
        '市民公開講座': 'seminar.html',
        '交通アクセス': 'access.html',
        '人間ドック': 'dock.html',
        'トップページ': 'top.html',
        'HOME': 'top.html',
        'ワイヤーフレーム一覧': 'index.html',
    }

    for text, target in card_link_map.items():
        # Match <a href="#...">TEXT</a> or <a href="#" ...>TEXT</a>
        pattern = f'href="#"([^>]*)>{re.escape(text)}'
        replacement = f'href="{target}"\\1>{text}'
        content = re.sub(pattern, replacement, content)

    if content != original:
        filepath.write_text(content, encoding='utf-8')
        return True
    return False


def add_home_button_to_all():
    """Add a floating home/index button to all pages except index.html."""
    style_block = """<style>
.wf-home-btn {
  position: fixed; bottom: 20px; right: 20px; z-index: 9998;
  display: flex; gap: 8px;
}
.wf-home-btn a {
  display: flex; align-items: center; gap: 6px;
  background: #0f172a; color: #e2e8f0; padding: 10px 16px;
  border-radius: 8px; font-size: 12px; font-weight: 600;
  box-shadow: 0 4px 12px rgba(0,0,0,.3); text-decoration: none;
  transition: background .2s;
}
.wf-home-btn a:hover { background: #0ea5e9; color: #fff; text-decoration: none; }
</style>"""

    nav_block = """<div class="wf-home-btn">
  <a href="index.html">&#9776; WF一覧</a>
  <a href="top.html">&#8962; TOP</a>
</div>"""

    for filepath in WIREFRAMES_DIR.glob("*.html"):
        if filepath.name == "index.html":
            continue
        content = filepath.read_text(encoding='utf-8')
        if 'wf-home-btn' in content:
            continue
        # Insert style before </head> and nav before </body>
        content = content.replace('</head>', f'{style_block}\n</head>')
        content = content.replace('</body>', f'{nav_block}\n</body>')
        filepath.write_text(content, encoding='utf-8')


def main():
    print("=== ワイヤーフレーム相互リンク修正 ===")

    files = list(WIREFRAMES_DIR.glob("*.html"))
    print(f"対象ファイル数: {len(files)}")

    fixed_count = 0
    for filepath in files:
        if fix_file(filepath):
            fixed_count += 1
            print(f"  [FIXED] {filepath.name}")
        else:
            print(f"  [OK]    {filepath.name}")

    print(f"\n修正ファイル数: {fixed_count}/{len(files)}")

    print("\n=== フローティングナビ追加 ===")
    add_home_button_to_all()
    print("完了")


if __name__ == "__main__":
    main()
