#!/usr/bin/env python3
"""全下層ページを元サイトの構造に忠実に再生成"""
import os
from pathlib import Path

BASE = Path("C:/tmp/anzu-ichinomiyanishi-sitemap/site")
IMG = "https://www.anzu.or.jp/ichinomiyanishi"

def css_js(depth):
    p = "../" * depth
    return f"""<link rel="stylesheet" href="{p}css/bxslider.css">
<link rel="stylesheet" href="{p}css/style.css">
<style>
.junction {{margin-bottom:40px;font-family:'Noto Serif JP',serif}}
.junction > div:first-child {{font-size:1.2em;color:#36637E;text-align:center;border-bottom:1px solid #1F5B80;padding:20px;margin-bottom:10px}}
.junction-list {{list-style:none;padding:0}}
.junction-list li {{border-bottom:1px solid #E8EFF2}}
.junction-list li a {{display:block;padding:18px 20px 18px 30px;font-size:15px;color:#022634;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='8' height='12' viewBox='0 0 8 12'%3E%3Cpath d='M1.5 0L0 1.5 4.5 6 0 10.5 1.5 12l6-6z' fill='%234F819F'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:left 12px center;text-decoration:none;transition:background-color .2s}}
.junction-list li a:hover {{background-color:#F2F8FA;opacity:1!important}}
.junction-list li a span {{font-size:13px;color:#678A9D;font-family:'Noto Sans JP',sans-serif;display:block;margin-top:4px}}
.sns-box {{display:flex;gap:.5rem;align-items:center}}
.btn-sns {{display:flex;justify-content:center;align-items:center;width:2.5rem;height:2.5rem;border-radius:50%;color:#fff;text-decoration:none;transition:.3s}}
.btn-sns svg {{fill:#fff;width:1.2em;height:1.2em}}
.btn-line {{background-color:#5DB40F}}
.h1-area {{padding:0 0 20px;margin-bottom:30px}}
.h1-area h1 {{font-family:'Noto Serif JP',serif;font-size:28px;font-weight:400;color:#022634;position:relative;padding-left:0}}
.under-main-img {{margin-bottom:30px}}
.under-main-img img {{width:100%;border-radius:0;display:block}}
@media screen and (max-width:767px) {{
  .junction-list li a {{padding:14px 16px 14px 26px;font-size:14px}}
  .h1-area h1 {{font-size:22px}}
}}
</style>
<script src="{p}js/jquery.min.js"></script>
<script src="{p}js/jquery.bxslider.min.js"></script>
<script src="{p}js/main.js"></script>"""

def header(depth, current=""):
    p = "../" * depth
    def nav(href, label, key):
        c = ' class="current"' if key == current else ''
        return f'<li><a href="{p}{href}"{c}><span>{label}</span></a></li>'
    return f"""<body>
<div id="body-in">
<p class="hide"><a href="#gnavi">グローバルナビゲーションへ</a></p>
<p class="hide"><a href="#main">本文へ</a></p>
<p class="hide"><a href="#footer">フッターへ</a></p>
<hr>
<header>
  <div class="container header__wrapper">
    <div id="header" class="header header3">
      <div class="header__inner">
        <div class="header__main header-main">
          <h1 class="header-main__logo">
            <a class="header-main__link" href="{p}index.html">
              <img id="js-header-main-logo" class="header-main__image" src="{IMG}/common/image/header-logo001.svg" alt="一宮西病院 | 社会医療法人 杏嶺会">
            </a>
          </h1>
        </div>
        <div class="header__sub header-sub">
          <div class="header-sub__nav-wrapper">
            <ul class="header-sub-nav__lists">
              <li class="header-sub-nav__list"><a href="https://req.qubo.jp/anzu/form/inquiry" class="header-sub-nav__link"><span>お問い合わせ</span></a></li>
              <li class="header-sub-nav__list"><a href="{p}guide/access.html" class="header-sub-nav__link"><span>交通アクセス</span></a></li>
            </ul>
          </div>
          <div class="gnavi-area">
            <div id="gnavi">
              <ul>
                {nav("guide/index.html","ご利用案内","guide")}
                {nav("department/index.html","診療科紹介","dept")}
                {nav("special/index.html","専門医療","special")}
                {nav("area/index.html","医療連携・紹介","area")}
                {nav("about/index.html","病院紹介","about")}
                {nav("recruit/index.html","採用情報","recruit")}
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</header>
"""

def bread(items, depth):
    p = "../" * depth
    parts = [f'<li><a href="{p}index.html">HOME</a></li>']
    for href, label in items[:-1]:
        parts.append(f'<li><a href="{p}{href}">{label}</a></li>')
    parts.append(f'<li>{items[-1][1]}</li>')
    return f'<div class="bread-area"><ul>{"".join(parts)}</ul></div>'

def sns_share():
    return """<div style="width:100%;display:flex;align-items:center;justify-content:flex-end;margin-bottom:20px">
  <div class="sns-box">
    <span style="display:flex;align-items:center;color:#5DB40F;font-size:90%;font-weight:bold">このページをシェア</span>
    <a id="line-share" class="btn-sns btn-line" target="_blank" rel="noopener">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M311 196.8v81.3c0 2.1-1.6 3.7-3.7 3.7h-13c-1.3 0-2.4-.7-3-1.5l-37.3-50.3v48.2c0 2.1-1.6 3.7-3.7 3.7h-13c-2.1 0-3.7-1.6-3.7-3.7V196.9c0-2.1 1.6-3.7 3.7-3.7h12.9c1.1 0 2.4.6 3 1.6l37.3 50.3V196.9c0-2.1 1.6-3.7 3.7-3.7h13c2.1-.1 3.8 1.6 3.8 3.5zm-93.7-3.7h-13c-2.1 0-3.7 1.6-3.7 3.7v81.3c0 2.1 1.6 3.7 3.7 3.7h13c2.1 0 3.7-1.6 3.7-3.7V196.8c0-1.9-1.6-3.7-3.7-3.7zm-31.4 68.1H150.3V196.8c0-2.1-1.6-3.7-3.7-3.7h-13c-2.1 0-3.7 1.6-3.7 3.7v81.3c0 1 .3 1.8 1 2.5.7.6 1.5 1 2.5 1h52.2c2.1 0 3.7-1.6 3.7-3.7v-13c0-1.9-1.6-3.7-3.5-3.7zm193.7-68.1H327.3c-1.9 0-3.7 1.6-3.7 3.7v81.3c0 1.9 1.6 3.7 3.7 3.7h52.2c2.1 0 3.7-1.6 3.7-3.7V265c0-2.1-1.6-3.7-3.7-3.7H344V247.7h35.5c2.1 0 3.7-1.6 3.7-3.7V230.9c0-2.1-1.6-3.7-3.7-3.7H344V213.5h35.5c2.1 0 3.7-1.6 3.7-3.7v-13c-.1-1.9-1.7-3.7-3.7-3.7zM512 93.4V419.4c-.1 51.2-42.1 92.7-93.4 92.6H92.6C41.4 511.9-.1 469.8 0 418.6V92.6C.1 41.4 42.2-.1 93.4 0H419.4c51.2.1 92.7 42.1 92.6 93.4zM441.6 233.5c0-83.4-83.7-151.3-186.4-151.3s-186.4 67.9-186.4 151.3c0 74.7 66.3 137.4 155.9 149.3 21.8 4.7 19.3 12.7 14.4 42.1-.8 4.7-3.8 18.4 16.1 10.1s107.3-63.2 146.5-108.2c27-29.7 39.9-59.8 39.9-93.1z"/></svg>
    </a>
  </div>
</div>
<script>window.onload=function(){var u=encodeURIComponent(window.location.href);var el=document.getElementById("line-share");if(el)el.href="https://social-plugins.line.me/lineit/share?url="+u}</script>"""

def sidebar_under(depth, cat_name, cat_href, nav_items, banners=None):
    p = "../" * depth
    nav_html = ""
    for href, label in nav_items:
        full_href = href if href.startswith("http") else f"{p}{href}"
        nav_html += f'<li><a href="{full_href}">{label}</a></li>\n'
    banner_html = ""
    if banners:
        banner_html = '<div class="banner-area"><div class="banner-area-in"><ul class="clearfix">\n'
        for href, img_src, alt in banners:
            full_href = href if href.startswith("http") else f"{p}{href}"
            banner_html += f'<li><a href="{full_href}"><img src="{img_src}" alt="{alt}"></a></li>\n'
        banner_html += '</ul></div></div><hr>\n'
    return f"""<div id="side">
  <div class="lnavi-area">
    <div class="category-area"><p class="category"><a href="{p}{cat_href}">{cat_name}</a></p></div>
    <div class="lnavi clearfix"><ul class="second">{nav_html}</ul><hr></div>
  </div>
  {banner_html}
</div>"""

def footer(depth):
    p = "../" * depth
    return f"""
<footer>
  <div class="container footer__wrapper">
    <div id="footer" class="footer">
      <div class="footer-upper">
        <div class="footer-group">
          <div class="footer-group__title-wrapper"><p class="footer-group__title">Group</p><p class="footer-group__subtitle">関連施設</p></div>
          <ul class="footer-group__list">
            <li class="footer-group__item"><a href="https://www.anzu.or.jp/kamibayashikinen/" class="footer-group-item__link"><div class="footer-group-item__image-wrapper"><img src="{IMG}/common/image/footer-ph001.webp" alt="" class="footer-group-item__image"></div><p class="footer-group-item__title">上林記念病院</p><p class="footer-group-item__description">"心"と"体"のリハビリテーション</p></a><ul class="footer-group-item__menu"><li><a href="https://www.anzu.or.jp/kamibayashikinen/">病院詳細</a></li><li><a href="https://www.anzu.or.jp/kamibayashikinen/access/">アクセス</a></li></ul></li>
            <li class="footer-group__item"><a href="https://www.anzu.or.jp/health-facilities/" class="footer-group-item__link"><div class="footer-group-item__image-wrapper"><img src="{IMG}/common/image/footer-ph003.webp" alt="" class="footer-group-item__image"></div><p class="footer-group-item__title">老人保健施設やすらぎ</p><p class="footer-group-item__description">要介護者の快適で安心した自立を応援</p></a><ul class="footer-group-item__menu"><li><a href="https://www.anzu.or.jp/health-facilities/">施設詳細</a></li><li><a href="https://www.anzu.or.jp/health-facilities/access/">アクセス</a></li></ul></li>
            <li class="footer-group__item"><a href="https://www.anzu.or.jp/shafuku/" class="footer-group-item__link"><div class="footer-group-item__image-wrapper"><img src="{IMG}/common/image/footer-ph004.webp" alt="" class="footer-group-item__image"></div><p class="footer-group-item__title">一宮医療療育センター</p><p class="footer-group-item__description">医療型障がい児者入所施設</p></a><ul class="footer-group-item__menu"><li><a href="https://www.anzu.or.jp/shafuku/">施設詳細</a></li><li><a href="https://www.anzu.or.jp/shafuku/access/index.html">アクセス</a></li></ul></li>
          </ul>
        </div>
      </div>
      <div class="footer-middle"><div class="footer-middle-in">
        <div class="footer__main footer-main"><div class="footer-main__list">
          <div class="footer-main__brand"><img src="{IMG}/common/image/footer-logo001.svg" alt="一宮西病院" class="footer-main__logo"></div>
          <div class="footer-main__meta"><p class="footer-main__address">〒494-0001 愛知県一宮市開明字平1番地</p><div class="footer-main__info"><p class="footer-meta__tel"><a href="tel:0586480077"><span>0586-48-0077</span><span>（代表）</span></a></p><ul class="footer-sns__list"><li><a href="https://www.facebook.com/ichinomiyanishi/"><img src="{IMG}/common/image/sns-ic001.svg" alt="Facebook"></a></li><li><a href="https://www.instagram.com/ichinomiyanishi.hospital/"><img src="{IMG}/common/image/sns-ic002.svg" alt="Instagram"></a></li><li><a href="https://www.youtube.com/channel/UCIRqbvkvLDvAoT_UaSycrCQ"><img src="{IMG}/common/image/sns-ic003.svg" alt="YouTube"></a></li></ul></div></div>
        </div></div>
        <div class="footer-sub"><ul class="footer-sub__menu"><li><a href="{p}guide/access.html"><span>交通アクセス</span></a></li><li><a href="https://www.anzu.or.jp/"><span>社会医療法人 杏嶺会</span></a></li></ul></div>
      </div></div>
      <div class="footer-under"><div class="footer__nav-wrapper"><ul class="footer-nav__lists">
        <li class="footer-nav__list"><a class="footer-nav__link" href="{p}about/index.html">個人情報保護方針</a></li>
        <li class="footer-nav__list"><a class="footer-nav__link" href="{p}about/index.html">このサイトの利用について</a></li>
        <li class="footer-nav__list"><a class="footer-nav__link" href="{p}about/index.html">アクセシビリティについて</a></li>
        <li class="footer-nav__list"><a class="footer-nav__link" href="{p}index.html">サイトマップ</a></li>
      </ul></div></div>
      <p class="footer__copy">&copy; Kyouryoukai All Rights Reserved.</p>
    </div>
  </div>
  <div class="footer-floating-menu">
    <div class="footer__sp-nav-wrapper js-footer-menu" id="js-footer-menu1"><div class="footer__sp-nav-wrap-in"><ul class="footer-sp-nav__lists">
      <li class="footer-sp-nav__list"><a class="footer-sp-nav__link" href="{p}guide/index.html">ご利用案内</a></li>
      <li class="footer-sp-nav__list"><a class="footer-sp-nav__link" href="{p}department/index.html">診療科紹介</a></li>
      <li class="footer-sp-nav__list"><a class="footer-sp-nav__link" href="{p}special/index.html">専門医療</a></li>
      <li class="footer-sp-nav__list"><a class="footer-sp-nav__link" href="{p}area/index.html">医療連携・紹介</a></li>
      <li class="footer-sp-nav__list"><a class="footer-sp-nav__link" href="{p}about/index.html">病院紹介</a></li>
      <li class="footer-sp-nav__list"><a class="footer-sp-nav__link" href="{p}recruit/index.html">採用情報</a></li>
    </ul></div></div>
    <div class="footer__sp-btn-nav-wrapper"><nav class="footer__sp-btn"><ul class="footer-sp-btn-nav__lists">
      <li class="footer-sp-btn-nav__list"><a class="footer-sp-btn-nav__link" href="https://req.qubo.jp/anzu/form/inquiry"><span class="footer-sp-btn-nav__label">お問い合わせ</span></a></li>
      <li class="footer-sp-btn-nav__list"><a class="footer-sp-btn-nav__link" href="{p}guide/access.html"><span class="footer-sp-btn-nav__label">交通アクセス</span></a></li>
      <li class="footer-sp-btn-nav__list js-footer-button" id="js-footer-button1" data-target="js-footer-menu1"><p class="footer-sp-btn-nav__link"><span class="footer-sp-btn-nav__label">メニュー</span></p></li>
    </ul></nav></div>
    <div class="footer-bg" id="js-footer-bg"></div>
  </div>
</footer>
<div class="js-floating_btn_area footer__floating-btn-wrapper"><a class="footer__floating-btn footer-floating-btn" href="#body-in"><span class="footer-floating-btn__item"></span></a></div>
</div></body></html>"""

def junction(title, items):
    """Generate a junction-style navigation list matching original site."""
    li_html = ""
    for href, label, desc in items:
        if desc:
            li_html += f'<li><a href="{href}">{label}<span>{desc}</span></a></li>\n'
        else:
            li_html += f'<li><a href="{href}">{label}</a></li>\n'
    return f"""<div class="junction clearfix">
  <div>{title}</div>
  <div class="junction-list-area clearfix"><ul class="junction-list clearfix">{li_html}</ul></div>
</div>"""

def page(path, title, bc, current, depth, main_img, main_content, side_html):
    p = "../" * depth
    img_html = f'<div class="under-main-img"><img src="{main_img}" alt=""></div>' if main_img else ""
    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title} | 一宮西病院 | 社会医療法人 杏嶺会</title>
{css_js(depth)}
</head>
{header(depth, current)}
{bread(bc, depth)}
<div class="main-container">
  <div class="wrapper-area underbg clearfix">
    <div id="wrapper-under" class="clearfix">
      <article><div id="main" class="clearfix">
        <div class="h1-area"><div class="h1-area-in"><h1>{title}</h1></div></div><hr>
        <div class="main-contents">
          {sns_share()}
          {img_html}
          {main_content}
        </div>
      </div></article>
      {side_html}
    </div>
  </div>
</div>
{footer(depth)}"""
    full = BASE / path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(html, encoding="utf-8")
    print(f"  Created: {path}")

def yt_banner():
    return [(f"http://www.youtube.com/channel/UCIRqbvkvLDvAoT_UaSycrCQ?sub_confirmation=1",
             f"{IMG}/media/banner_youtube_202412.webp", 'YouTube「一宮西病院チャンネル」')]

# ============================================================
# GUIDE
# ============================================================
def gen_guide():
    side = sidebar_under(1, "ご利用案内", "guide/index.html",
        [("guide/index.html","外来受診"),("guide/index.html","入院・お見舞い"),
         ("guide/index.html","院内の施設・窓口"),("guide/index.html","イベント・体制")],
        yt_banner())

    junc1 = junction("外来受診", [
        (f"{IMG}/guide/surgery/consultation/","受診方法","お持ちいただくもの、受付から精算までの流れなど"),
        (f"{IMG}/guide/surgery/first_aid/","夜間・休日外来の受診","夜間・休日を含む24時間365日対応"),
        (f"{IMG}/guide/surgery/time_table/","外来診療担当表",""),
        (f"{IMG}/guide/surgery/surgery_hour/","休診案内",""),
        (f"{IMG}/guide/surgery/floor/","外来フロア案内","フロアマップ"),
        (f"{IMG}/guide/equipment/","院内の設備・店舗","コンビニ、カフェ、ATMなど"),
        (f"{IMG}/guide/surgery/vaccination/","予防接種について","予約方法、実施しているワクチンの種類など"),
        (f"{IMG}/guide/surgery/second-opinion/","セカンドオピニオン外来","当院以外の医療機関を受診されている患者さまに"),
    ])
    junc2 = junction("入院・お見舞い", [
        (f"{IMG}/guide/stay/expense/","入院のご案内","手続き、持ち物、お部屋、入院生活など"),
        (f"{IMG}/guide/stay/visit/","お見舞い・ご面会にお越しの方へ","面会の時間、条件、方法"),
        (f"{IMG}/about/ward/","病棟のご案内","各階案内"),
        (f"{IMG}/guide/equipment/","院内の設備・店舗","コンビニ、カフェ、ATMなど"),
        (f"{IMG}/guide/stay/rihabilitation-hope/","訪問リハビリテーション ほーぷ","退院後のリハビリテーション"),
        (f"{IMG}/guide/stay/parking/","入院中の駐車場利用について",""),
    ])
    junc3 = junction("院内の施設・窓口", [
        (f"{IMG}/for-dock/","人間ドック・健康診断について",""),
        (f"{IMG}/guide/medical-consultation/","医療福祉相談課",""),
        (f"{IMG}/guide/cancer_consultation_support_center/","がん相談支援センター",""),
        (f"{IMG}/guide/anzu-no-ki/","患者さま相談窓口 あんずの樹",""),
        (f"{IMG}/guide/free-wifi/","フリーWi-Fi・電子書籍読み放題",""),
        (f"{IMG}/guide/restaurant-shukran/","レストラン シュクラン",""),
        (f"{IMG}/guide/accsess/","交通アクセス・駐車場のご案内",""),
    ])
    junc4 = junction("イベント・体制", [
        (f"{IMG}/guide/seminor/","各種教室・イベント紹介",""),
        (f"{IMG}/guide/anzu-marche/","あんずマルシェ",""),
        (f"{IMG}/guide/documents/","各種書類発行について",""),
        (f"{IMG}/guide/kaiji/","診療情報の開示について",""),
        (f"{IMG}/guide/2nd_opinion/","他院でのセカンドオピニオンについて",""),
        (f"{IMG}/guide/kakaritsuke/","身近なかかりつけ医をもちましょう",""),
        (f"{IMG}/guide/electronic-prescription/","電子処方せん対応施設",""),
        (f"{IMG}/guide/donichi-kensa-chiryou/","土日におこなう検査・治療",""),
        (f"{IMG}/guide/covid-19/","新型コロナウイルス感染症への対応",""),
    ])
    content = f"""<div class="column-area"><div class="column2-11 clearfix">
<div class="column-left column-box clearfix">{junc1}{junc2}</div>
<div class="column-right column-box clearfix">{junc3}{junc4}</div>
</div></div>"""
    page("guide/index.html","ご利用案内",[("guide/index.html","ご利用案内")],"guide",1,
         f"{IMG}/media/guide_main_2403.webp", content, side)

# ============================================================
# DEPARTMENT
# ============================================================
def gen_department():
    side = sidebar_under(1, "診療科紹介", "department/index.html",
        [("department/index.html","内科系"),("department/index.html","外科系"),
         ("department/index.html","その他"),("department/index.html","センター"),
         ("department/index.html","専門外来")], yt_banner())

    internal = [("消化器内科","digestive"),("血液内科","hematology"),("呼吸器内科","respiratory"),
        ("循環器内科","circulatory"),("内分泌・糖尿病内科","diabetes"),("脳神経内科","nerve"),
        ("リウマチ・膠原病内科","rheumatism"),("腎臓内科","nephrology"),("腫瘍内科","oncology"),
        ("小児科","pediatrics"),("総合内科","general"),("緩和ケア内科","palliative_care_internal_medicine")]
    surgery = [("外科","surgery_intro"),("乳腺外科・内分泌外科","mammary"),("肛門外科","anus"),
        ("呼吸器外科","thoracic"),("心臓血管外科","sinzokekkangeka"),("脳神経外科","neurosurgery"),
        ("整形外科","orthopedics"),("形成外科","plastic"),("耳鼻咽喉科・頭頸部外科","ear"),
        ("泌尿器科","urinary"),("眼科","ophthalmology"),("皮膚科","skin"),("産婦人科","maternity")]
    other_d = [("精神科","psychiatry-hospitalization"),("歯科口腔外科","oral-surgery"),
        ("総合救急部 救急科","emergency"),("麻酔科・集中治療科","anesthesia"),
        ("病理診断科","pathology"),("放射線診断科","radiation"),("放射線治療科","radiotherapy"),
        ("リハビリテーション科","rehabilitation")]
    centers = [("内視鏡センター","endoscope"),("肝胆膵センター","hpb"),("不整脈センター","arrhythmia"),
        ("肥満症治療センター","obesity"),("糖尿病センター","diabetes"),("脳卒中センター","stroke"),
        ("透析センター","dialysis"),("腎&シャント・レミッションセンター","jin-and-shunt"),
        ("腹腔鏡センター","fukukukyo"),("ステントグラフト血管センター","stent"),
        ("レーザー静脈瘤センター","vein"),("脊椎・側彎センター","sekitsui_sokuwan"),
        ("人工関節センター","jinko"),("手外科・マイクロサージャリーセンター","hand_surgery"),
        ("肩関節センター","shoulder_joint"),("股関節センター","hipjoint"),
        ("四肢・骨盤骨折治療センター","fracture"),("エイジングケアセンター","aging-care")]

    def dept_list(items, base):
        return "\n".join([f'<li><a href="{IMG}/{base}/{slug}/">{name}</a></li>' for name,slug in items])

    junc_int = f'<div class="junction clearfix"><div>診療科（内科系）</div><div class="junction-list-area clearfix"><ul class="junction-list clearfix">{dept_list(internal,"medicine")}</ul></div></div>'
    junc_sur = f'<div class="junction clearfix"><div>診療科（外科系）</div><div class="junction-list-area clearfix"><ul class="junction-list clearfix">{dept_list(surgery,"surgery")}</ul></div></div>'
    junc_oth = f'<div class="junction clearfix"><div>その他</div><div class="junction-list-area clearfix"><ul class="junction-list clearfix">{dept_list(other_d,"other")}</ul></div></div>'
    junc_cen = f'<div class="junction clearfix"><div>センター</div><div class="junction-list-area clearfix"><ul class="junction-list clearfix">{dept_list(centers,"center")}</ul></div></div>'

    content = f"""<div class="column-area"><div class="column2-11 clearfix">
<div class="column-left column-box clearfix">{junc_int}{junc_sur}</div>
<div class="column-right column-box clearfix">{junc_oth}{junc_cen}</div>
</div></div>"""
    page("department/index.html","診療科紹介",[("department/index.html","診療科紹介")],"dept",1,
         None, content, side)

# ============================================================
# SPECIAL
# ============================================================
def gen_special():
    side = sidebar_under(1, "専門医療", "special/index.html",
        [("special/index.html","専門外来"),("special/index.html","専門医療分野"),
         ("special/index.html","ドクター特集インタビュー")], yt_banner())

    outpatients = [
        (f"{IMG}/special/ladies_outpatient/","レディース外来","婦人科・乳腺外科・内分泌外科・形成外科"),
        (f"{IMG}/medicine/circulatory/footarteriosclerosis/footoutpatien/","末梢血管・足の外来","末梢動脈疾患PAD専門"),
        (f"{IMG}/medicine/diabetes/thyroid/","甲状腺超音波外来",""),
        (f"{IMG}/medicine/pediatrics/#kidney","小児腎臓外来",""),
        (f"{IMG}/medicine/pediatrics/#circulatory","小児循環器外来",""),
        (f"{IMG}/special/woc/","WOC外来（ストーマ外来）",""),
        (f"{IMG}/special/peritonealseeding/","腹膜播種外科外来",""),
        (f"{IMG}/surgery/mammary/#lymphedema","リンパ浮腫外来",""),
        (f"{IMG}/surgery/orthopedics/sports/","スポーツ外来",""),
        (f"{IMG}/center/jinko/mis/","ひざ関節外来",""),
        (f"{IMG}/surgery/maternity/genetic_outpatient/","遺伝診療科",""),
        (f"{IMG}/surgery/maternity/maternity-nipt/","NIPT外来","出生前診断"),
        (f"{IMG}/surgery/maternity/specialsite/support-class/#milk","母乳外来",""),
    ]
    fields = [
        (f"{IMG}/special/medical_equipment/","医療機器のご案内",""),
        (f"{IMG}/special/cancer/","がんの総合案内","愛知県がん診療拠点病院"),
        (f"{IMG}/special/endoscopic/","体にやさしい鏡視下手術",""),
        (f"{IMG}/medicine/circulatory/footarteriosclerosis/","末梢動脈疾患(PAD)",""),
        (f"{IMG}/medicine/circulatory/tavi/","経カテーテル大動脈弁留置術・TAVI",""),
        (f"{IMG}/medicine/circulatory/impella/","補助循環用ポンプカテーテル・IMPELLA",""),
        (f"{IMG}/surgery/surgery_intro/robot/","ロボット支援下手術",""),
        (f"{IMG}/surgery/mammary/#mammary","乳腺疾患",""),
        (f"{IMG}/surgery/neurosurgery/treat_neuro2/","脊髄・脊椎疾患",""),
        (f"{IMG}/surgery/ophthalmology/minimallyinvasivevitreoretinalsurgerymivs/","低侵襲硝子体手術・MIVS",""),
        (f"{IMG}/surgery/ophthalmology/micro_invasive_gulaucoma_surgery/","低侵襲緑内障手術・MIGS",""),
        (f"{IMG}/surgery/ophthalmology/multifocal_intraocular_lens/","多焦点眼内レンズ",""),
        (f"{IMG}/surgery/maternity/gynecology/minimallyinvasive/","婦人科低侵襲手術",""),
        (f"{IMG}/surgery/maternity/gynecology/davinci/","婦人科ロボット支援下手術",""),
    ]
    interviews = [
        ("special/interview.html","消化器内視鏡の3つのチカラ","消化器内科"),
        ("special/interview.html","大腸がんに関する5つのポイント","消化器内科"),
        ("special/interview.html","肺がんに関する5つのポイント","呼吸器内科"),
        ("special/interview.html","腹腔鏡手術の3つのポイント","外科"),
        ("special/interview.html","乳がんに関する6つのポイント","乳腺外科"),
        ("special/interview.html","脳卒中に関する5つのポイント","脳神経外科"),
        ("special/interview.html","変形性膝関節症の3つのポイント","整形外科"),
        ("special/interview.html","肩の痛みに関する3つの知識","整形外科"),
        ("special/interview.html","股関節痛に関する3つの疑問","整形外科"),
        ("special/interview.html","前立腺がんに関する6つのポイント","泌尿器科"),
        ("special/interview.html","緑内障に関する5つのポイント","眼科"),
    ]

    junc_op = junction("専門外来", outpatients)
    junc_field = junction("専門医療分野", fields)
    iv_items = [(f"../{h}",t,c) for h,t,c in interviews]
    junc_iv = junction("ドクター特集インタビュー", iv_items)

    content = f"""<div class="column-area"><div class="column2-11 clearfix">
<div class="column-left column-box clearfix">{junc_op}{junc_iv}</div>
<div class="column-right column-box clearfix">{junc_field}</div>
</div></div>"""
    page("special/index.html","専門医療",[("special/index.html","専門医療")],"special",1,
         f"{IMG}/media/specialty_main_2407.webp", content, side)

# ============================================================
# AREA
# ============================================================
def gen_area():
    side = sidebar_under(1, "医療連携・紹介", "area/index.html",
        [("area/index.html","一般の方"),("area/index.html","医療機関の方")], yt_banner())

    junc1 = junction("一般の方", [
        (f"{IMG}/area/shinryou_yoyaku/","診察のご予約",""),
        (f"{IMG}/area/kenshin_2ji/","健康診断 二次精査",""),
        ("https://app.medigle.jp/ichinomiya-nishi/","連携医療機関・クリニック",""),
        (f"{IMG}/area/shinryouka/","診療科紹介",""),
    ])
    junc2 = junction("医療機関の方", [
        (f"{IMG}/area/kensa_yoyaku/","検査のご予約",""),
        (f"{IMG}/area/onedayset/","診察・検査 1DAYセット",""),
        (f"{IMG}/about/ward/b8910/","回復期リハビリテーション病棟",""),
        (f"{IMG}/about/ward/palliative-care-ward/#interview","緩和ケア病棟 入棟面談について",""),
    ])
    info = """<div style="background:#F2F8FA;border:1px solid #D0E0E6;border-radius:6px;padding:24px;margin-top:30px">
<p style="font-family:'Noto Serif JP',serif;font-size:18px;color:#36637E;margin-bottom:12px">地域連携室</p>
<table style="font-size:14px"><tr><td style="padding:4px 16px 4px 0;color:#678A9D;white-space:nowrap">TEL</td><td style="padding:4px 0"><strong>0586-48-0022</strong></td></tr>
<tr><td style="padding:4px 16px 4px 0;color:#678A9D">FAX</td><td style="padding:4px 0"><strong>0586-48-0053</strong></td></tr>
<tr><td style="padding:4px 16px 4px 0;color:#678A9D">受付</td><td style="padding:4px 0">月〜金 8:00〜17:00 / 土 8:00〜12:00</td></tr>
<tr><td style="padding:4px 16px 4px 0;color:#678A9D">時間外</td><td style="padding:4px 0">0586-48-0077（24時間対応）</td></tr></table></div>"""

    page("area/index.html","医療連携・紹介",[("area/index.html","医療連携・紹介")],"area",1,
         None, f"{junc1}{junc2}{info}", side)

# ============================================================
# ABOUT
# ============================================================
def gen_about():
    side = sidebar_under(1, "病院紹介", "about/index.html",
        [("about/index.html","病院について"),("about/index.html","当院の取り組み"),
         ("about/index.html","医療体制"),("about/index.html","医療情報・コラム記事"),
         ("about/index.html","当院の紹介")], yt_banner())

    junc1 = junction("病院について", [
        (f"{IMG}/about/hospital/greeting/","病院長からのご挨拶",""),
        (f"{IMG}/about/hospital/interview/","病院長インタビュー",""),
        (f"{IMG}/about/hospital/history/","沿革",""),
        (f"{IMG}/about/hospital/outline/","病院概要",""),
        ("../about/ward.html","病棟のご案内","各階案内"),
        (f"{IMG}/special/medical_equipment/","医療機器のご案内",""),
        (f"{IMG}/about/hospital/list_archive/","活動実績",""),
        (f"{IMG}/about/hospital/data/","病院指標",""),
        (f"{IMG}/about/hospital/dpc2/","DPC特定病院群",""),
        (f"{IMG}/special/cancer/","愛知県がん診療拠点病院",""),
        (f"{IMG}/about/hospital/disaster/","災害拠点病院",""),
        (f"{IMG}/about/hospital/request/","病院からのお願い",""),
    ])
    junc2 = junction("当院の取り組み", [
        (f"{IMG}/about/effort/facility-standards/","施設基準に関する事項一覧",""),
        (f"{IMG}/about/effort/medical-safety/","医療安全・患者さま相談窓口",""),
        (f"{IMG}/about/effort/infection_control/","院内感染対策に関する取組事項",""),
        (f"{IMG}/about/effort/nosmoke/","敷地内全面禁煙",""),
        (f"{IMG}/about/effort/database/","NCD及びJNDデータベース事業",""),
        (f"{IMG}/about/effort/yuketsu/","輸血拒否に対する当院の方針",""),
        (f"{IMG}/about/effort/iryoujyuujisya/","医療従事者の負担軽減",""),
        (f"{IMG}/about/effort/rinri/","主要な倫理的課題における指針",""),
        (f"{IMG}/about/effort/clinical_pathways/","クリニカルパス",""),
        (f"{IMG}/about/effort/optout/","院内がん登録オプトアウト",""),
        (f"{IMG}/about/effort/acp/","人生会議 ACP",""),
        (f"{IMG}/about/effort/research/","治験および臨床研究",""),
    ])
    junc3 = junction("医療体制", [
        (f"{IMG}/about/system/conference/","中央診療部門カンファレンス",""),
        (f"{IMG}/about/system/committee/","医療安全管理委員会",""),
        (f"{IMG}/about/system/nst/","栄養サポートチーム(NST)",""),
        (f"{IMG}/about/system/dst/","認知症ケアサポートチーム(DST)",""),
        (f"{IMG}/about/system/infection-control/","感染対策チーム",""),
        (f"{IMG}/nurse/moreinfo/interview/ninteimenbers/","認定看護師",""),
        (f"{IMG}/nurse/moreinfo/interview/tokuteikangomenbers/","特定行為看護師",""),
    ])
    junc4 = junction("医療情報・コラム記事", [
        (f"{IMG}/about/column/","市民公開WEB講座",""),
        (f"{IMG}/about/kenkouno_tsubo/","健康のつボ!",""),
        (f"{IMG}/about/information/byoukininarumaenisitteokitai/","病気になる前に知っておきたいこと",""),
        (f"{IMG}/about/information/syokunokoramu/","ショコラ",""),
        (f"{IMG}/about/information/lowcarbsweets/","低糖質スイーツ",""),
    ])
    junc5 = junction("当院の紹介", [
        (f"{IMG}/about/pr/media/","メディア情報",""),
        (f"{IMG}/about/pr/press/","広報物・パンフレット",""),
        (f"{IMG}/about/pr/movie/","紹介動画",""),
        ("../special/interview.html","ドクター特集インタビュー",""),
    ])
    content = f"""<div class="column-area"><div class="column2-11 clearfix">
<div class="column-left column-box clearfix">{junc1}{junc3}{junc5}</div>
<div class="column-right column-box clearfix">{junc2}{junc4}</div>
</div></div>"""
    page("about/index.html","病院紹介",[("about/index.html","病院紹介")],"about",1,
         f"{IMG}/media/outline_main_2403.webp", content, side)

# ============================================================
# RECRUIT
# ============================================================
def gen_recruit():
    side = sidebar_under(1, "採用情報", "recruit/index.html",
        [("recruit/resident.html","臨床研修医・後期研修医"),
         ("recruit/index.html","キャリア医師"),
         ("recruit/nurse.html","看護師"),
         ("recruit/index.html","その他")], yt_banner())

    junc = junction("募集職種", [
        ("../recruit/resident.html","臨床研修医・後期研修医","充実の症例数と指導体制で実践力を磨く"),
        (f"{IMG}/recruit/","キャリア医師","専門性を活かせる環境で地域医療に貢献"),
        ("../recruit/nurse.html","看護師","教育体制充実・ワークライフバランスを重視"),
        ("https://www.anzu.or.jp/recruit/","その他の職種","薬剤師・臨床検査技師・放射線技師・リハビリ・事務"),
    ])
    stats = """<div style="display:flex;gap:16px;margin:30px 0;flex-wrap:wrap;justify-content:center">
<div style="flex:1;min-width:130px;text-align:center;background:#F2F8FA;padding:24px;border-radius:8px"><div style="font-size:36px;font-weight:900;color:#4F819F;font-family:Roboto,sans-serif">600</div><div style="font-size:13px;color:#678A9D">病床数</div></div>
<div style="flex:1;min-width:130px;text-align:center;background:#F2F8FA;padding:24px;border-radius:8px"><div style="font-size:36px;font-weight:900;color:#4F819F;font-family:Roboto,sans-serif">33</div><div style="font-size:13px;color:#678A9D">診療科</div></div>
<div style="flex:1;min-width:130px;text-align:center;background:#F2F8FA;padding:24px;border-radius:8px"><div style="font-size:36px;font-weight:900;color:#4F819F;font-family:Roboto,sans-serif">10,000<span style="font-size:16px">+</span></div><div style="font-size:13px;color:#678A9D">年間手術件数</div></div>
<div style="flex:1;min-width:130px;text-align:center;background:#F2F8FA;padding:24px;border-radius:8px"><div style="font-size:36px;font-weight:900;color:#4F819F;font-family:Roboto,sans-serif">8,000<span style="font-size:16px">+</span></div><div style="font-size:13px;color:#678A9D">年間救急搬送</div></div></div>"""

    page("recruit/index.html","採用情報",[("recruit/index.html","採用情報")],"recruit",1,
         None, f"{stats}{junc}", side)

# ============================================================
def main():
    print("=== Rebuilding pages with original site structure ===")
    gen_guide()
    gen_department()
    gen_special()
    gen_area()
    gen_about()
    gen_recruit()
    print("\n=== Done ===")

if __name__ == "__main__":
    main()
