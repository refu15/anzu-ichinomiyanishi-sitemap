#!/usr/bin/env python3
"""一宮西病院サイト全22ページを一括生成"""
import os

BASE = "C:/tmp/anzu-ichinomiyanishi-sitemap/site"
IMG = "https://www.anzu.or.jp/ichinomiyanishi"

def css_path(depth):
    return "../" * depth

def head(title, depth=0, extra_css=""):
    p = css_path(depth)
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="format-detection" content="email=no,telephone=no,address=no">
<title>{title} | 一宮西病院</title>
<link rel="stylesheet" href="{p}css/bxslider.css">
<link rel="stylesheet" href="{p}css/style.css">
{extra_css}
<script src="{p}js/jquery.min.js"></script>
<script src="{p}js/jquery.bxslider.min.js"></script>
<script src="{p}js/main.js"></script>
</head>
"""

def header_html(depth=0, current="", is_home=False):
    p = css_path(depth)
    home_class = ' class="home"' if is_home else ''
    def nav_link(href, label, key):
        c = ' class="current"' if key == current else ''
        return f'<li><a href="{p}{href}"{c}><span>{label}</span></a></li>'
    return f"""<body>
<div id="body-in"{home_class}>
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
              <img class="header-main__image" src="{IMG}/common/image/header-logo001.svg" alt="一宮西病院 | 社会医療法人 杏嶺会">
            </a>
          </h1>
        </div>
        <div class="header__sub header-sub">
          <div class="header-sub__nav-wrapper">
            <ul class="header-sub-nav__lists">
              <li class="header-sub-nav__list"><a href="#" class="header-sub-nav__link"><span>お問い合わせ</span></a></li>
              <li class="header-sub-nav__list"><a href="{p}guide/access.html" class="header-sub-nav__link"><span>交通アクセス</span></a></li>
            </ul>
          </div>
          <div class="gnavi-area">
            <div id="gnavi">
              <ul>
                {nav_link("guide/index.html","ご利用案内","guide")}
                {nav_link("department/index.html","診療科紹介","dept")}
                {nav_link("special/index.html","専門医療","special")}
                {nav_link("area/index.html","医療連携・紹介","area")}
                {nav_link("about/index.html","病院紹介","about")}
                {nav_link("recruit/index.html","採用情報","recruit")}
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</header>
"""

def breadcrumb(items, depth=0):
    p = css_path(depth)
    parts = [f'<li><a href="{p}index.html">HOME</a></li>']
    for href, label in items[:-1]:
        parts.append(f'<li><a href="{p}{href}">{label}</a></li>')
    parts.append(f'<li>{items[-1][1]}</li>')
    return f"""<div class="bread-area"><ul>{"".join(parts)}</ul></div>"""

def page_title(ja, en):
    return f"""<div class="page-title-area">
  <h2 class="page-title">{ja}</h2>
  <p class="page-title-en">{en}</p>
</div>"""

def footer_html(depth=0):
    p = css_path(depth)
    return f"""
<footer>
  <div class="container footer__wrapper">
    <div id="footer" class="footer">
      <div class="footer-upper">
        <div class="footer-group">
          <div class="footer-group__title-wrapper">
            <p class="footer-group__title">Group</p>
            <p class="footer-group__subtitle">関連施設</p>
          </div>
          <ul class="footer-group__list">
            <li class="footer-group__item">
              <a href="https://www.anzu.or.jp/kamibayashikinen/" class="footer-group-item__link">
                <div class="footer-group-item__image-wrapper"><img src="{IMG}/common/image/footer-ph001.webp" alt="" class="footer-group-item__image"></div>
                <p class="footer-group-item__title">上林記念病院</p>
                <p class="footer-group-item__description">"心"と"体"のリハビリテーション</p>
              </a>
              <ul class="footer-group-item__menu">
                <li><a href="https://www.anzu.or.jp/kamibayashikinen/">病院詳細</a></li>
                <li><a href="https://www.anzu.or.jp/kamibayashikinen/access/">アクセス</a></li>
              </ul>
            </li>
            <li class="footer-group__item">
              <a href="https://www.anzu.or.jp/health-facilities/" class="footer-group-item__link">
                <div class="footer-group-item__image-wrapper"><img src="{IMG}/common/image/footer-ph003.webp" alt="" class="footer-group-item__image"></div>
                <p class="footer-group-item__title">老人保健施設やすらぎ</p>
                <p class="footer-group-item__description">要介護者の快適で安心した自立を応援</p>
              </a>
              <ul class="footer-group-item__menu">
                <li><a href="https://www.anzu.or.jp/health-facilities/">施設詳細</a></li>
                <li><a href="https://www.anzu.or.jp/health-facilities/access/">アクセス</a></li>
              </ul>
            </li>
            <li class="footer-group__item">
              <a href="https://www.anzu.or.jp/shafuku/" class="footer-group-item__link">
                <div class="footer-group-item__image-wrapper"><img src="{IMG}/common/image/footer-ph004.webp" alt="" class="footer-group-item__image"></div>
                <p class="footer-group-item__title">一宮医療療育センター</p>
                <p class="footer-group-item__description">医療型障がい児者入所施設</p>
              </a>
              <ul class="footer-group-item__menu">
                <li><a href="https://www.anzu.or.jp/shafuku/">施設詳細</a></li>
                <li><a href="https://www.anzu.or.jp/shafuku/access/index.html">アクセス</a></li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
      <div class="footer-middle">
        <div class="footer-middle-in">
          <div class="footer__main footer-main">
            <div class="footer-main__list">
              <div class="footer-main__brand">
                <img src="{IMG}/common/image/footer-logo001.svg" alt="一宮西病院 | 社会医療法人 杏嶺会" class="footer-main__logo">
              </div>
              <div class="footer-main__meta">
                <p class="footer-main__address">〒494-0001 愛知県一宮市開明字平1番地</p>
                <div class="footer-main__info">
                  <p class="footer-meta__tel"><a href="tel:0586480077"><span>0586-48-0077</span><span>（代表）</span></a></p>
                  <ul class="footer-sns__list">
                    <li><a href="https://www.facebook.com/ichinomiyanishi/"><img src="{IMG}/common/image/sns-ic001.svg" alt="Facebook"></a></li>
                    <li><a href="https://www.instagram.com/ichinomiyanishi.hospital/"><img src="{IMG}/common/image/sns-ic002.svg" alt="Instagram"></a></li>
                    <li><a href="https://www.youtube.com/channel/UCIRqbvkvLDvAoT_UaSycrCQ"><img src="{IMG}/common/image/sns-ic003.svg" alt="YouTube"></a></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <div class="footer-sub">
            <ul class="footer-sub__menu">
              <li><a href="{p}guide/access.html"><span>交通アクセス</span></a></li>
              <li><a href="https://www.anzu.or.jp/"><span>社会医療法人 杏嶺会</span></a></li>
            </ul>
          </div>
        </div>
      </div>
      <div class="footer-under">
        <div class="footer__nav-wrapper">
          <ul class="footer-nav__lists">
            <li class="footer-nav__list"><a class="footer-nav__link" href="{p}about/index.html">個人情報保護方針</a></li>
            <li class="footer-nav__list"><a class="footer-nav__link" href="{p}about/index.html">このサイトの利用について</a></li>
            <li class="footer-nav__list"><a class="footer-nav__link" href="{p}about/index.html">アクセシビリティについて</a></li>
            <li class="footer-nav__list"><a class="footer-nav__link" href="{p}about/index.html">サイトマップ</a></li>
          </ul>
        </div>
      </div>
      <p class="footer__copy">&copy; Kyouryoukai All Rights Reserved.</p>
    </div>
  </div>
  <div class="footer-floating-menu">
    <div class="footer__sp-nav-wrapper js-footer-menu" id="js-footer-menu1">
      <div class="footer__sp-nav-wrap-in">
        <ul class="footer-sp-nav__lists">
          <li class="footer-sp-nav__list"><a class="footer-sp-nav__link" href="{p}guide/index.html">ご利用案内</a></li>
          <li class="footer-sp-nav__list"><a class="footer-sp-nav__link" href="{p}department/index.html">診療科紹介</a></li>
          <li class="footer-sp-nav__list"><a class="footer-sp-nav__link" href="{p}special/index.html">専門医療</a></li>
          <li class="footer-sp-nav__list"><a class="footer-sp-nav__link" href="{p}area/index.html">医療連携・紹介</a></li>
          <li class="footer-sp-nav__list"><a class="footer-sp-nav__link" href="{p}about/index.html">病院紹介</a></li>
          <li class="footer-sp-nav__list"><a class="footer-sp-nav__link" href="{p}recruit/index.html">採用情報</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__sp-btn-nav-wrapper">
      <nav class="footer__sp-btn footer-sp-btn">
        <ul class="footer-sp-btn-nav__lists">
          <li class="footer-sp-btn-nav__list"><a class="footer-sp-btn-nav__link" href="#"><span class="footer-sp-btn-nav__label">お問い合わせ</span></a></li>
          <li class="footer-sp-btn-nav__list"><a class="footer-sp-btn-nav__link" href="{p}guide/access.html"><span class="footer-sp-btn-nav__label">交通アクセス</span></a></li>
          <li class="footer-sp-btn-nav__list js-footer-button" id="js-footer-button1" data-target="js-footer-menu1"><p class="footer-sp-btn-nav__link"><span class="footer-sp-btn-nav__label">メニュー</span></p></li>
        </ul>
      </nav>
    </div>
    <div class="footer-bg" id="js-footer-bg"></div>
  </div>
</footer>
<div class="js-floating_btn_area footer__floating-btn-wrapper">
  <a class="footer__floating-btn footer-floating-btn" href="#body-in"><span class="footer-floating-btn__item"></span></a>
</div>
</div>
</body>
</html>"""

def sidebar(depth=0, active_section=""):
    p = css_path(depth)
    return f"""<div id="side">
  <div class="side-section">
    <div class="side-title">ご利用案内</div>
    <ul class="side-nav">
      <li><a href="{p}guide/outpatient.html">外来受診の方</a></li>
      <li><a href="{p}guide/inpatient.html">入院・お見舞いの方</a></li>
      <li><a href="{p}guide/dock.html">人間ドック・健康診断</a></li>
      <li><a href="{p}guide/access.html">交通アクセス</a></li>
    </ul>
  </div>
  <div class="side-section">
    <div class="side-title">診療科紹介</div>
    <ul class="side-nav">
      <li><a href="{p}department/index.html">診療科一覧</a></li>
      <li><a href="{p}department/detail.html">循環器内科</a></li>
      <li><a href="{p}department/center.html">脳卒中センター</a></li>
    </ul>
  </div>
  <div class="side-section">
    <div class="side-title">専門医療</div>
    <ul class="side-nav">
      <li><a href="{p}special/index.html">専門医療トップ</a></li>
      <li><a href="{p}special/interview.html">ドクターインタビュー</a></li>
    </ul>
  </div>
  <div class="side-section">
    <div class="side-title">病院紹介</div>
    <ul class="side-nav">
      <li><a href="{p}about/index.html">病院紹介トップ</a></li>
      <li><a href="{p}about/ward.html">病棟のご案内</a></li>
      <li><a href="{p}news/index.html">お知らせ</a></li>
      <li><a href="{p}news/column.html">健康のつボ!</a></li>
      <li><a href="{p}seminar/index.html">市民公開講座</a></li>
    </ul>
  </div>
  <div class="side-section">
    <div class="side-title">採用情報</div>
    <ul class="side-nav">
      <li><a href="{p}recruit/index.html">採用情報トップ</a></li>
      <li><a href="{p}recruit/nurse.html">看護師採用</a></li>
      <li><a href="{p}recruit/resident.html">臨床研修医</a></li>
    </ul>
  </div>
</div>"""

def write(path, content):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Created: {path}")

# =====================================================================
# 1. TOP PAGE
# =====================================================================
def gen_top():
    sliders_pc = [
        ("center/diabetes/", "topbanner_diabetes_20260401_pc.webp", "糖尿病センター"),
        ("http://www.youtube.com/channel/UCIRqbvkvLDvAoT_UaSycrCQ", "topbanner_youtube_20240704_pc.webp", "一宮西病院チャンネル"),
        ("center/dialysis/", "topbanner_dialysis_20250627_pc.webp", "透析センター"),
        ("center/obesity/", "topbanner_obesity_20250519_pc.webp", "肥満症治療センター"),
        ("surgery/maternity/new-obstetrics/", "topbanner_obstetrics_20241218_pc.webp", "産科外来"),
        ("special/medical_equipment/ctc/", "topbanner_ctc_20241225_pc.webp", "大腸CT検査"),
        ("surgery/maternity/genetic_outpatient/", "topbanner_hboc_20240613_pc.webp", "遺伝学的検査外来"),
        ("special/medical_equipment/index.html#davinci", "topbanner_davincisp_20240731_pc.webp", "ダビンチ手術"),
        ("special/ladies_outpatient/", "topbanner_womens_20230922_pc.webp", "レディース外来"),
        ("nurse/", "topbanner_nurse_20241226_pc.webp", "看護師募集"),
    ]
    slider_html = ""
    for href, img, alt in sliders_pc:
        url = href if href.startswith("http") else f"{IMG}/{href}"
        slider_html += f'<li><a href="{url}"><img src="{IMG}/media/{img}" alt="{alt}"></a></li>\n'

    sliders_sp = [(h, i.replace("_pc.", "_sp."), a) for h, i, a in sliders_pc]
    slider_sp_html = ""
    for href, img, alt in sliders_sp:
        url = href if href.startswith("http") else f"{IMG}/{href}"
        slider_sp_html += f'<li><a href="{url}"><img src="{IMG}/media/{img}" alt="{alt}"></a></li>\n'

    pickups = [
        ("news/detail.html", "pickup_meitetsu-bus_20260401.webp", "一宮駅から当院まで、新路線バス「一宮西線」が運行開始!"),
        ("special/index.html", "pickup_obstetrics.webp", "【産科】産前から産後まで、赤ちゃんとお母さんをサポートします。"),
        ("news/column.html", "pickup_column.webp", "【市民公開WEB講座】当院の医師たちが監修するWEB講座"),
        ("https://www.instagram.com/ichinomiyanishi.hospital/", "pickup001.webp", "【公式Instagram】医療情報・イベント情報を発信中"),
    ]
    pickup_html = ""
    for href, img, txt in pickups:
        pickup_html += f"""<div class="pickup-box">
<a href="{href}"><div class="box">
<div class="img-area"><p><img src="{IMG}/media/{img}" alt="IMAGE"></p></div>
<div class="right"><p class="title-area">{txt}</p></div>
</div></a></div>\n"""

    news_items = [
        ("ic003", "2026.03.12", "news/index.html", '3/29(日)、院内にて開催! "健康づくりフェア"'),
        ("ic003", "2026.03.08", "news/index.html", "【世界緑内障週間】ライトアップ in グリーン運動に参加しています"),
        ("ic003", "2026.03.01", "news/index.html", "【大腸がん啓発月間】ブルーリボンライトアップを実施しています"),
        ("ic003", "2026.02.17", "guide/index.html", '来週3/4(水)、院内にて開催! 地域とふれあう"あんずマルシェ"'),
        ("ic003", "2026.01.28", "guide/index.html", '来週2/4(水)、院内にて開催! 地域とふれあう"あんずマルシェ"'),
    ]
    news_html = ""
    for ic, date, href, txt in news_items:
        news_html += f'<dl class="clearfix"><dt class="{ic}">{date}</dt><dd><a href="{href}">{txt}</a></dd></dl>\n'

    centers = [
        ("内視鏡センター","Endoscopy"),("肝胆膵センター","HPB"),("不整脈センター","Arrhythmia"),
        ("肥満症治療センター","Obesity"),("糖尿病センター","Diabetes"),("脳卒中センター","Stroke"),
        ("透析センター","Dialysis"),("腎&シャント・レミッションセンター","Kidney & Shunt"),
        ("腹腔鏡センター","Laparoscopy"),("ステントグラフト血管センター","Stent Graft"),
        ("レーザー静脈瘤センター","Varicose Vein"),("脊椎・側彎センター","Spine & Scoliosis"),
        ("人工関節センター","Joint Replacement"),("手外科・マイクロサージャリーセンター","Hand Surgery"),
        ("肩関節センター","Shoulder"),("股関節センター","Hip Joint"),
        ("四肢・骨盤骨折治療センター","Fracture"),("エイジングケアセンター","Aging Care"),
    ]
    center_html = ""
    for name, en in centers:
        center_html += f'<a href="department/center.html" class="center-item"><div class="icon">●</div><div class="name">{name}</div><div class="name-en">{en}</div></a>\n'

    columns = [
        ("消化器内科","消化器内視鏡 3つのチカラ"),("消化器内科","大腸がんに関する5つのポイント"),
        ("呼吸器内科","肺がんに関する5つのポイント"),("外科","腹腔鏡手術 3つのポイント"),
        ("乳腺外科","乳がんに関する6つのポイント"),("脳神経外科","脳卒中に関する5つのポイント"),
    ]
    column_html = ""
    for cat, ttl in columns:
        column_html += f"""<a href="special/interview.html" class="column-item">
<div class="img-area" style="height:180px;background:#E6F0F5;display:flex;align-items:center;justify-content:center;color:#678A9D;font-size:13px">{cat}</div>
<div class="txt-area"><span class="cat">{cat}</span><p class="ttl">{ttl}</p></div></a>\n"""

    banners = ["topbanner007.webp","topbanner001.webp","topbanner002.webp","topbanner003.webp",
               "topbanner004.webp","topbanner005.webp","topbanner006.webp","banner001.png",
               "banner002_202412.png","banner003-2.png","banner_youtube_202412.webp"]
    banner_html = ""
    for b in banners:
        banner_html += f'<li><a href="#"><img src="{IMG}/media/{b}" alt=""></a></li>\n'

    recruits = [("臨床研修医・後期研修医","Resident"),("キャリア医師","Career Doctor"),
                ("看護師","Nurse"),("その他の職種","Other")]
    recruit_html = ""
    for name, en in recruits:
        recruit_html += f'<a href="recruit/index.html" class="recruit__item"><div class="ttl">{name}</div><div class="ttl-en">{en}</div></a>\n'

    content = head("一宮西病院", 0) + header_html(0, "", True) + f"""
<div class="mainvisual-area">
  <ul id="mainvisual">{slider_html}</ul>
  <p class="mainvisual__tel-wrapper"><a href="tel:0586480077"><span>0586-48-0077</span><span>（代表）</span></a></p>
</div>
<div class="mainvisual-sp-area">
  <ul id="mainvisual-sp">{slider_sp_html}</ul>
  <p class="mainvisual-sp__tel-wrapper"><a href="tel:0586480077"><span>0586-48-0077</span><span>（代表）</span></a></p>
</div>

<div class="main-container">
  <div class="wrapper-area">
    <div id="wrapper" class="clearfix">
      <div id="main">

        <!-- Target -->
        <div class="home-section target-section">
          <div class="home-target">
            <ul class="target__list">
              <li class="target__item target__item--item1">
                <a href="guide/outpatient.html" class="target-item__link">
                  <div class="target-item__body"><span class="target-item__t1">外来受診</span><span class="target-item__t2">Outpatient</span></div>
                </a>
                <ul class="target-item__menu">
                  <li class="target-item-menu__item"><a href="guide/outpatient.html"><span>外来診療担当表</span></a></li>
                  <li class="target-item-menu__item"><a href="guide/outpatient.html"><span>休診情報</span></a></li>
                </ul>
              </li>
              <li class="target__item target__item--item2">
                <a href="guide/outpatient.html" class="target-item__link">
                  <div class="target-item__body"><span class="target-item__t1">夜間・休日外来<br class="sp-only">（救急外来）</span><span class="target-item__t2">Emergency</span></div>
                </a>
              </li>
              <li class="target__item target__item--item3">
                <a href="guide/inpatient.html" class="target-item__link">
                  <div class="target-item__body"><span class="target-item__t1">入院・お見舞い</span><span class="target-item__t2">Inpatient</span></div>
                </a>
              </li>
              <li class="target__item target__item--item4">
                <a href="guide/dock.html" class="target-item__link">
                  <div class="target-item__body"><span class="target-item__t1">人間ドック・<br class="sp-only">健康診断</span><span class="target-item__t2">Checkup</span></div>
                </a>
              </li>
            </ul>
          </div>
        </div>

        <!-- Important News -->
        <div class="home-section important-section">
          <div class="important-area clearfix" id="breaking-news">
            <div class="important-area-in clearfix">
              <div class="title"><h2>重要なお知らせ</h2></div>
              <div class="news-list important-list"><div class="news-list-in">
                <dl class="clearfix"><dt>2026.04.01</dt><dd><a href="about/index.html">当院が愛知県より「災害拠点病院」に指定されました</a></dd></dl>
                <dl class="clearfix"><dt>2026.04.01</dt><dd><a href="news/detail.html">2026年4月1日(水)より新路線バス「一宮西線」の運行が開始</a></dd></dl>
                <dl class="clearfix"><dt>2025.10.23</dt><dd><a href="guide/index.html">院内の全エリアにて、電子書籍読み放題サービスを導入しました</a></dd></dl>
              </div></div>
              <p class="list-link"><a href="news/index.html">一覧</a></p>
            </div>
          </div>
        </div>

        <!-- Pickup -->
        <div class="home-section pickup-section">
          <div class="pickup-area">
            <div class="pickup__title-wrapper home-title-wrapper">
              <h2 class="pickup__title home-title">Pick Up</h2>
              <p class="pickup__subtitle home-subtitle">ピックアップ</p>
            </div>
            <div class="pickup-area-in">{pickup_html}</div>
          </div>
        </div>

        <!-- News -->
        <div class="home-section news-section">
          <div class="news-area clearfix" id="news">
            <div class="news-area-in">
              <div class="title">
                <h2>News</h2><p class="subtitle">お知らせ</p>
                <p class="list-link"><a href="news/index.html">一覧</a></p>
                <div class="news-tab-list">
                  <h3 id="all-tab"><a href="javascript:void(0);">すべて</a></h3>
                  <h3 id="tab01"><a href="javascript:void(0);">お知らせ</a></h3>
                  <h3 id="tab02"><a href="javascript:void(0);">採用情報</a></h3>
                  <h3 id="tab03"><a href="javascript:void(0);">イベント</a></h3>
                  <h3 id="tab04"><a href="javascript:void(0);">メディア</a></h3>
                  <h3 id="tab05"><a href="javascript:void(0);">広報</a></h3>
                </div>
              </div>
              <div class="news-list" id="tab-area">
                <div id="all-tab-content" class="clearfix"><div class="news-list-in">{news_html}</div></div>
                <div id="tab01-content" class="clearfix"><div class="news-list-in">{news_html}</div></div>
                <div id="tab02-content" class="clearfix"><div class="news-list-in"><dl class="clearfix"><dt class="ic002">2025.11.01</dt><dd><a href="recruit/index.html">リハビリテーション技術部 採用面接会のお知らせ</a></dd></dl></div></div>
                <div id="tab03-content" class="clearfix"><div class="news-list-in">{news_html}</div></div>
                <div id="tab04-content" class="clearfix"><div class="news-list-in"><dl class="clearfix"><dt class="ic004">2025.09.30</dt><dd><a href="news/index.html">ZIP-FM乳がん啓発放送</a></dd></dl></div></div>
                <div id="tab05-content" class="clearfix"><div class="news-list-in"><dl class="clearfix"><dt class="ic005">2025.04.17</dt><dd><a href="news/index.html">ドクター紹介ページリニューアル</a></dd></dl></div></div>
              </div>
            </div>
          </div>
        </div>

        <!-- Column -->
        <div class="home-section column-section">
          <div class="column-area">
            <div class="home-title-wrapper"><h2 class="home-title">Column</h2><p class="home-subtitle">市民公開WEB講座</p></div>
            <div class="column-list">{column_html}</div>
          </div>
        </div>

        <!-- Centers -->
        <div class="home-section center-section">
          <div class="center-area">
            <div class="home-title-wrapper"><h2 class="home-title">Center</h2><p class="home-subtitle">専門医療センター</p></div>
            <div class="center-list">{center_html}</div>
          </div>
        </div>

        <!-- Recruit -->
        <div class="home-section recruit-section">
          <div class="home-recruit">
            <div class="home-title-wrapper"><h2 class="home-title" style="color:#fff">Recruit</h2><p class="home-subtitle" style="color:rgba(255,255,255,.7)">採用情報</p></div>
            <div class="recruit__body"><div class="recruit__list">{recruit_html}</div>
            <a href="recruit/index.html" class="recruit__button">一覧</a></div>
          </div>
        </div>

        <!-- Banners -->
        <div class="home-section banner-section">
          <div class="banner-area"><div class="banner-area-in"><ul>{banner_html}</ul></div></div>
        </div>

      </div>
    </div>
  </div>
</div>
""" + footer_html(0)
    write("index.html", content)

# =====================================================================
# UNDER PAGES (template)
# =====================================================================
def gen_under_page(path, title_ja, title_en, bc_items, current, depth, main_content):
    content = head(title_ja, depth)
    content += header_html(depth, current, False)
    content += breadcrumb(bc_items, depth)
    content += page_title(title_ja, title_en)
    content += f"""
<div class="main-container">
  <div class="wrapper-area underbg">
    <div id="wrapper" class="clearfix">
      <div id="main">
        <div class="main-contents">
{main_content}
        </div>
      </div>
{sidebar(depth)}
    </div>
  </div>
</div>
"""
    content += footer_html(depth)
    write(path, content)

# =====================================================================
# Generate all under pages
# =====================================================================
def gen_all():
    print("=== Generating site pages ===")
    gen_top()

    # 2. Guide Top
    gen_under_page("guide/index.html", "ご利用案内", "Guide",
        [("guide/index.html","ご利用案内")], "guide", 1,
        f"""<h2 class="heading01">外来受診</h2>
<div class="card-grid col-3">
  <a href="outpatient.html" class="card-item"><div class="card-img" style="height:120px;background:#E6F0F5;display:flex;align-items:center;justify-content:center;color:#4F819F">外来受診</div><div class="card-body"><div class="ttl">外来受診の方</div><div class="desc">受診方法・外来診療担当表・休診案内</div></div></a>
  <a href="inpatient.html" class="card-item"><div class="card-img" style="height:120px;background:#E6F0F5;display:flex;align-items:center;justify-content:center;color:#4F819F">入院</div><div class="card-body"><div class="ttl">入院・お見舞いの方</div><div class="desc">入院手続き・面会ルール・費用</div></div></a>
  <a href="dock.html" class="card-item"><div class="card-img" style="height:120px;background:#E6F0F5;display:flex;align-items:center;justify-content:center;color:#4F819F">健診</div><div class="card-body"><div class="ttl">人間ドック・健康診断</div><div class="desc">健診コース・予約方法</div></div></a>
</div>
<h2 class="heading01" style="margin-top:50px">院内の施設・窓口</h2>
<ul style="line-height:2.4;font-size:15px">
  <li><a href="outpatient.html" style="text-decoration:underline">外来フロア案内</a></li>
  <li><a href="outpatient.html" style="text-decoration:underline">予防接種について</a></li>
  <li><a href="outpatient.html" style="text-decoration:underline">セカンドオピニオン外来</a></li>
  <li><a href="#" style="text-decoration:underline">医療福祉相談課</a></li>
  <li><a href="#" style="text-decoration:underline">がん相談支援センター</a></li>
  <li><a href="#" style="text-decoration:underline">患者さま相談窓口 あんずの樹</a></li>
  <li><a href="#" style="text-decoration:underline">フリーWi-Fi・電子書籍読み放題</a></li>
  <li><a href="#" style="text-decoration:underline">レストラン シュクラン</a></li>
  <li><a href="access.html" style="text-decoration:underline">交通アクセス・駐車場のご案内</a></li>
</ul>
<h2 class="heading01" style="margin-top:50px">各種サービス</h2>
<ul style="line-height:2.4;font-size:15px">
  <li><a href="#" style="text-decoration:underline">各種教室・イベント紹介</a></li>
  <li><a href="#" style="text-decoration:underline">あんずマルシェ</a></li>
  <li><a href="#" style="text-decoration:underline">各種書類発行について</a></li>
  <li><a href="#" style="text-decoration:underline">身近なかかりつけ医をもちましょう</a></li>
  <li><a href="#" style="text-decoration:underline">電子処方せん対応施設</a></li>
  <li><a href="#" style="text-decoration:underline">土日におこなう検査・治療</a></li>
  <li><a href="#" style="text-decoration:underline">新型コロナウイルス感染症への対応</a></li>
</ul>""")

    # 3. Outpatient
    gen_under_page("guide/outpatient.html", "外来受診の方へ", "Outpatient",
        [("guide/index.html","ご利用案内"),("guide/outpatient.html","外来受診の方")], "guide", 1,
        f"""<h2 class="heading01">受診の流れ</h2>
<div style="display:flex;gap:8px;margin:30px 0;flex-wrap:wrap">
  <div style="flex:1;min-width:140px;text-align:center;background:#F2F8FA;padding:20px 10px;border-radius:8px"><div style="width:36px;height:36px;background:#4F819F;color:#fff;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-weight:700;margin-bottom:8px">1</div><div style="font-size:14px;font-weight:600">来院</div></div>
  <div style="flex:1;min-width:140px;text-align:center;background:#F2F8FA;padding:20px 10px;border-radius:8px"><div style="width:36px;height:36px;background:#4F819F;color:#fff;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-weight:700;margin-bottom:8px">2</div><div style="font-size:14px;font-weight:600">受付</div></div>
  <div style="flex:1;min-width:140px;text-align:center;background:#F2F8FA;padding:20px 10px;border-radius:8px"><div style="width:36px;height:36px;background:#4F819F;color:#fff;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-weight:700;margin-bottom:8px">3</div><div style="font-size:14px;font-weight:600">待合</div></div>
  <div style="flex:1;min-width:140px;text-align:center;background:#F2F8FA;padding:20px 10px;border-radius:8px"><div style="width:36px;height:36px;background:#4F819F;color:#fff;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-weight:700;margin-bottom:8px">4</div><div style="font-size:14px;font-weight:600">診察</div></div>
  <div style="flex:1;min-width:140px;text-align:center;background:#F2F8FA;padding:20px 10px;border-radius:8px"><div style="width:36px;height:36px;background:#4F819F;color:#fff;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-weight:700;margin-bottom:8px">5</div><div style="font-size:14px;font-weight:600">会計</div></div>
</div>
<div class="info-box-blue"><strong>初診の方へ</strong><br>初めてご来院の方は、健康保険証をお持ちの上、A棟1階の初診受付までお越しください。紹介状をお持ちの方は、受付時にご提出ください。</div>
<h3 class="heading02">診察受付時間</h3>
<table><tr><th></th><th>午前</th><th>午後</th></tr><tr><td>月〜金</td><td>8:00〜11:30</td><td>完全予約制</td></tr><tr><td>土曜</td><td>8:00〜11:30</td><td>休診</td></tr><tr><td>日曜・祝日</td><td colspan="2">休診（救急外来は24時間対応）</td></tr></table>
<h3 class="heading02">持ち物チェックリスト</h3>
<table><tr><th>必須</th><td>健康保険証、診察券（再診の方）、紹介状（お持ちの方）</td></tr><tr><th>あれば</th><td>お薬手帳、各種医療証、検査データ</td></tr></table>
<div class="info-box-red" style="margin-top:30px"><strong>夜間・休日外来（救急外来）</strong><br>24時間365日対応しています。A棟1階の救急入口よりお入りください。<br>TEL: 0586-48-0077（代表）</div>
<p style="margin-top:30px"><a href="../department/index.html" class="btn-main">外来診療担当表を見る</a></p>""")

    # 4. Inpatient
    gen_under_page("guide/inpatient.html", "入院・お見舞いの方へ", "Inpatient",
        [("guide/index.html","ご利用案内"),("guide/inpatient.html","入院・お見舞い")], "guide", 1,
        """<h2 class="heading01">入院までの流れ</h2>
<p>主治医より入院の説明を受けた後、入退院支援センター（A棟2階）にて入院手続きを行っていただきます。</p>
<h3 class="heading02">入院時の持ち物</h3>
<table><tr><th>書類</th><td>健康保険証、診察券、印鑑、限度額適用認定証</td></tr><tr><th>衣類</th><td>パジャマ、下着、タオル（レンタルあり）</td></tr><tr><th>日用品</th><td>歯ブラシ、コップ、ティッシュ、スリッパ</td></tr><tr><th>その他</th><td>お薬手帳、服用中のお薬、イヤホン</td></tr></table>
<h3 class="heading02">入院費用の目安</h3>
<table><tr><th>部屋タイプ</th><th>差額ベッド代（税込/日）</th></tr><tr><td>4人部屋</td><td>なし</td></tr><tr><td>2人部屋</td><td>5,500円</td></tr><tr><td>個室A</td><td>11,000円</td></tr><tr><td>個室B（トイレ・シャワー付）</td><td>16,500円</td></tr></table>
<div class="info-box-blue"><strong>面会時間</strong><br>14:00〜20:00（平日・休日共通）<br>面会は1回15分程度、2名までとさせていただいております。</div>
<h3 class="heading02">オンライン面会</h3>
<p>ご来院が難しい方のために、タブレットを使用したオンライン面会を実施しています。事前予約制となりますので、病棟ナースステーションまでお問い合わせください。</p>
<p style="margin-top:20px"><a href="../about/ward.html" class="btn-main">病棟のご案内</a></p>""")

    # 5. Access
    gen_under_page("guide/access.html", "交通アクセス・駐車場のご案内", "Access",
        [("guide/index.html","ご利用案内"),("guide/access.html","交通アクセス")], "guide", 1,
        """<div style="height:400px;background:#E6F0F5;display:flex;align-items:center;justify-content:center;color:#678A9D;font-size:16px;border-radius:8px;margin-bottom:30px">Google Maps 埋め込みエリア</div>
<h2 class="heading01">所在地・連絡先</h2>
<table><tr><th>住所</th><td>〒494-0001 愛知県一宮市開明字平1番地</td></tr><tr><th>電話</th><td>0586-48-0077（代表）</td></tr><tr><th>FAX</th><td>0586-48-0078</td></tr></table>
<h2 class="heading01" style="margin-top:40px">交通手段別アクセス</h2>
<h3 class="heading02">電車でお越しの方</h3>
<p>名鉄本線「開明駅」より徒歩約10分<br>JR東海道本線「尾張一宮駅」よりタクシー約10分</p>
<h3 class="heading02">バスでお越しの方</h3>
<div class="info-box-blue"><strong>NEW! 新路線バス「一宮西線」</strong><br>2026年4月1日より運行開始。名鉄一宮駅バスターミナルより当院まで直通。所要時間約20分。</div>
<p>名鉄バス「一宮西病院」バス停下車すぐ</p>
<h3 class="heading02">お車でお越しの方</h3>
<p>東海北陸自動車道「一宮西IC」より約5分<br>名神高速道路「一宮IC」より約15分</p>
<h2 class="heading01" style="margin-top:40px">駐車場のご案内</h2>
<table><tr><th>駐車場</th><th>台数</th><th>料金</th></tr><tr><td>立体駐車場</td><td>約400台</td><td>外来受診の方：無料</td></tr><tr><td>平面駐車場</td><td>約200台</td><td>外来受診の方：無料</td></tr><tr><td>第2駐車場</td><td>約100台</td><td>外来受診の方：無料</td></tr><tr><td>身体障がい者用</td><td>約50台</td><td>無料（ゲート式）</td></tr></table>""")

    # 6. Dock
    gen_under_page("guide/dock.html", "人間ドック・健康診断", "Health Checkup",
        [("guide/dock.html","健診の方")], "guide", 1,
        """<h2 class="heading01">健診センターについて</h2>
<p>一宮西病院 健診センターでは、最新の医療機器を活用した精度の高い健康診断・人間ドックを提供しています。異常が見つかった場合は、院内の各専門診療科へスムーズに連携できる体制を整えています。</p>
<h2 class="heading01" style="margin-top:40px">健診コース一覧</h2>
<table><tr><th>コース名</th><th>主な検査内容</th><th>料金（税込）</th><th>所要時間</th></tr>
<tr><td>基本健診</td><td>身体計測、血液検査、尿検査、心電図、胸部X線</td><td>11,000円</td><td>約1.5時間</td></tr>
<tr><td>生活習慣病健診</td><td>基本健診＋腹部超音波、眼底検査</td><td>22,000円</td><td>約2時間</td></tr>
<tr><td>人間ドック</td><td>生活習慣病健診＋胃内視鏡、便潜血</td><td>44,000円</td><td>約3時間</td></tr>
<tr><td>レディースドック</td><td>人間ドック＋乳がん・子宮がん検査</td><td>55,000円</td><td>約3.5時間</td></tr>
<tr><td>脳ドック</td><td>頭部MRI/MRA、頸部超音波</td><td>33,000円</td><td>約2時間</td></tr>
<tr><td>心臓ドック</td><td>心臓超音波、運動負荷心電図、BNP</td><td>33,000円</td><td>約2時間</td></tr>
<tr><td>午後ドック</td><td>人間ドックと同等（13:00開始）</td><td>44,000円</td><td>約3時間</td></tr>
<tr><td>PETがんドック</td><td>人間ドック＋PET-CT</td><td>132,000円</td><td>約5時間</td></tr></table>
<h3 class="heading02">よくある質問</h3>
<div style="border:1px solid #D0E0E6;border-radius:6px;margin:8px 0"><div style="padding:14px 18px;font-weight:600;cursor:pointer;background:#F2F8FA">Q. 予約はどのくらい前から可能ですか？</div><div style="padding:14px 18px;font-size:14px;color:#333">A. 約3ヶ月前からご予約いただけます。WEB予約または電話予約をご利用ください。</div></div>
<div style="border:1px solid #D0E0E6;border-radius:6px;margin:8px 0"><div style="padding:14px 18px;font-weight:600;cursor:pointer;background:#F2F8FA">Q. 健診結果はいつ届きますか？</div><div style="padding:14px 18px;font-size:14px;color:#333">A. 受診後約2〜3週間で郵送いたします。</div></div>
<div style="border:1px solid #D0E0E6;border-radius:6px;margin:8px 0"><div style="padding:14px 18px;font-weight:600;cursor:pointer;background:#F2F8FA">Q. 当日の食事制限はありますか？</div><div style="padding:14px 18px;font-size:14px;color:#333">A. 前日21時以降は食事を控えていただきます。水・お茶は当日朝まで可能です。</div></div>
<p style="margin-top:30px"><a href="#" class="btn-main">WEB予約はこちら</a> <a href="#" class="btn-outline-main" style="margin-left:12px">電話予約: 0586-48-0077</a></p>""")

    # Department list
    depts_internal = ["消化器内科","血液内科","呼吸器内科","循環器内科","内分泌・糖尿病内科","脳神経内科","リウマチ・膠原病内科","腎臓内科","腫瘍内科","小児科","総合内科","緩和ケア内科"]
    depts_surgery = ["外科","乳腺外科・内分泌外科","肛門外科","呼吸器外科","心臓血管外科","脳神経外科","整形外科","形成外科","耳鼻咽喉科・頭頸部外科","泌尿器科","眼科","皮膚科","産婦人科"]
    depts_other = ["精神科","歯科口腔外科","総合救急部 救急科","麻酔科・集中治療科","病理診断科","放射線診断科","放射線治療科","リハビリテーション科"]
    d_cards = lambda ds: "\n".join([f'<a href="detail.html" class="card-item"><div class="card-body"><div class="ttl">{d}</div></div></a>' for d in ds])
    gen_under_page("department/index.html", "診療科紹介", "Department",
        [("department/index.html","診療科紹介")], "dept", 1,
        f"""<h2 class="heading01">内科系（12科）</h2><div class="card-grid col-3">{d_cards(depts_internal)}</div>
<h2 class="heading01" style="margin-top:40px">外科系（13科）</h2><div class="card-grid col-3">{d_cards(depts_surgery)}</div>
<h2 class="heading01" style="margin-top:40px">その他（8科）</h2><div class="card-grid col-4">{d_cards(depts_other)}</div>
<h2 class="heading01" style="margin-top:40px">中央診療部</h2>
<ul style="line-height:2.2;font-size:15px"><li>薬剤科</li><li>臨床検査科</li><li>放射線科</li><li>医療機器管理室</li><li>栄養科</li></ul>""")

    # Department detail
    gen_under_page("department/detail.html", "循環器内科", "Cardiology",
        [("department/index.html","診療科紹介"),("department/detail.html","循環器内科")], "dept", 1,
        """<h2 class="heading01">診療科紹介</h2>
<p>循環器内科では、虚血性心疾患（狭心症・心筋梗塞）、不整脈、心不全、弁膜症、末梢動脈疾患など、心臓・血管に関わる幅広い疾患の診断・治療を行っています。24時間体制でカテーテル治療に対応し、地域の救急医療を支えています。</p>
<h3 class="heading02">主な対象疾患</h3>
<table><tr><th>疾患名</th><th>主な治療法</th></tr>
<tr><td>虚血性心疾患（狭心症・心筋梗塞）</td><td>カテーテル治療(PCI)、冠動脈バイパス術</td></tr>
<tr><td>不整脈</td><td>カテーテルアブレーション、ペースメーカー</td></tr>
<tr><td>心不全</td><td>薬物療法、デバイス治療</td></tr>
<tr><td>弁膜症</td><td>TAVI、外科的弁置換術・弁形成術</td></tr>
<tr><td>末梢動脈疾患(PAD)</td><td>カテーテル治療、バイパス術</td></tr>
<tr><td>大動脈疾患</td><td>ステントグラフト、外科手術</td></tr></table>
<h3 class="heading02">ドクター紹介</h3>
<div class="doctor-card"><div class="doctor-photo" style="display:flex;align-items:center;justify-content:center;font-size:12px;color:#678A9D">写真</div><div class="doctor-info"><div class="position">部長</div><div class="name">医師名</div><div class="name-en">Doctor Name</div><div class="specialty">専門: 虚血性心疾患、カテーテル治療</div><div class="cert">日本循環器学会 循環器専門医<br>日本内科学会 総合内科専門医</div></div></div>
<h3 class="heading02">治療実績</h3>
<div style="display:flex;gap:16px;margin:20px 0;flex-wrap:wrap">
<div style="flex:1;min-width:160px;text-align:center;background:#F2F8FA;padding:24px;border-radius:8px"><div style="font-size:36px;font-weight:900;color:#4F819F;font-family:Roboto,sans-serif">1,200</div><div style="font-size:13px;color:#678A9D;margin-top:4px">年間カテーテル件数</div></div>
<div style="flex:1;min-width:160px;text-align:center;background:#F2F8FA;padding:24px;border-radius:8px"><div style="font-size:36px;font-weight:900;color:#4F819F;font-family:Roboto,sans-serif">120</div><div style="font-size:13px;color:#678A9D;margin-top:4px">年間TAVI件数</div></div>
<div style="flex:1;min-width:160px;text-align:center;background:#F2F8FA;padding:24px;border-radius:8px"><div style="font-size:36px;font-weight:900;color:#4F819F;font-family:Roboto,sans-serif">500</div><div style="font-size:13px;color:#678A9D;margin-top:4px">年間PCI件数</div></div>
</div>""")

    # Center detail
    gen_under_page("department/center.html", "脳卒中センター", "Stroke Center",
        [("department/index.html","診療科紹介"),("department/center.html","脳卒中センター")], "dept", 1,
        """<div style="height:300px;background:linear-gradient(135deg,#E6F0F5,#F2F8FA);display:flex;align-items:center;justify-content:center;color:#678A9D;font-size:16px;border-radius:8px;margin-bottom:30px">脳卒中センター キービジュアル</div>
<h2 class="heading01">脳卒中センターについて</h2>
<p>脳卒中センターは、脳梗塞・脳出血・くも膜下出血などの脳血管疾患に対し、24時間365日体制で迅速な診断と治療を提供しています。SCU（脳卒中集中治療室）を完備し、急性期から回復期まで一貫した治療を行います。</p>
<div style="display:flex;gap:16px;margin:30px 0;flex-wrap:wrap">
<div style="flex:1;min-width:200px;text-align:center;background:#F2F8FA;padding:24px;border-radius:8px"><div style="font-size:32px;font-weight:900;color:#4F819F">24h</div><div style="font-size:13px;color:#678A9D;margin-top:4px">365日対応</div></div>
<div style="flex:1;min-width:200px;text-align:center;background:#F2F8FA;padding:24px;border-radius:8px"><div style="font-size:32px;font-weight:900;color:#4F819F">SCU</div><div style="font-size:13px;color:#678A9D;margin-top:4px">脳卒中集中治療室完備</div></div>
<div style="flex:1;min-width:200px;text-align:center;background:#F2F8FA;padding:24px;border-radius:8px"><div style="font-size:32px;font-weight:900;color:#4F819F">150+</div><div style="font-size:13px;color:#678A9D;margin-top:4px">年間血栓回収療法</div></div>
</div>
<h3 class="heading02">対象疾患</h3>
<ul style="line-height:2.2;font-size:15px"><li>脳梗塞（rt-PA療法、血栓回収療法）</li><li>脳出血（外科的治療、保存的治療）</li><li>くも膜下出血（クリッピング術、コイル塞栓術）</li><li>一過性脳虚血発作（TIA）</li></ul>
<div class="info-box-red" style="margin-top:30px"><strong>脳卒中は時間との戦いです</strong><br>突然の頭痛、片側の手足のしびれ、ろれつが回らない等の症状があれば、すぐに救急車を呼んでください。</div>""")

    # Special top
    outpatients = ["レディース外来","WOC外来（ストーマ外来）","腹膜播種外科外来","末梢血管・足の外来","甲状腺超音波外来","スポーツ外来","ひざ関節外来","遺伝診療科","NIPT外来","母乳外来"]
    interviews = [("消化器内視鏡 3つのチカラ","消化器内科"),("大腸がんに関する5つのポイント","消化器内科"),("肺がんに関する5つのポイント","呼吸器内科"),("腹腔鏡手術 3つのポイント","外科"),("乳がんに関する6つのポイント","乳腺外科"),("脳卒中に関する5つのポイント","脳神経外科"),("変形性膝関節症 3つのポイント","整形外科"),("肩の痛みに関する3つの知識","整形外科"),("股関節痛に関する3つの疑問","整形外科"),("前立腺がんに関する6つのポイント","泌尿器科"),("緑内障に関する5つのポイント","眼科")]
    op_cards = "\n".join([f'<a href="interview.html" class="card-item"><div class="card-body"><div class="ttl">{o}</div></div></a>' for o in outpatients])
    iv_cards = "\n".join([f'<a href="interview.html" class="card-item"><div class="card-body"><div class="desc" style="font-size:12px;margin-bottom:4px">{cat}</div><div class="ttl">{t}</div></div></a>' for t,cat in interviews])
    gen_under_page("special/index.html", "専門医療", "Specialty",
        [("special/index.html","専門医療")], "special", 1,
        f"""<h2 class="heading01">専門外来</h2><div class="card-grid col-3">{op_cards}</div>
<h2 class="heading01" style="margin-top:40px">専門医療分野</h2>
<div class="card-grid col-2">
<a href="#" class="card-item"><div class="card-body"><div class="ttl">がんの総合案内</div><div class="desc">愛知県がん診療拠点病院</div></div></a>
<a href="#" class="card-item"><div class="card-body"><div class="ttl">医療機器のご案内</div><div class="desc">ダビンチSP、大腸CT等</div></div></a>
<a href="#" class="card-item"><div class="card-body"><div class="ttl">体にやさしい鏡視下手術</div><div class="desc">低侵襲手術の実績</div></div></a>
<a href="#" class="card-item"><div class="card-body"><div class="ttl">愛知県がん診療拠点病院</div><div class="desc">がん治療の総合的な体制</div></div></a>
</div>
<h2 class="heading01" style="margin-top:40px">ドクター特集インタビュー</h2><div class="card-grid col-3">{iv_cards}</div>""")

    # Special interview
    gen_under_page("special/interview.html", "大腸がんに関する5つのポイント", "Special Interview",
        [("special/index.html","専門医療"),("special/interview.html","ドクター特集インタビュー")], "special", 1,
        """<div class="doctor-card"><div class="doctor-photo" style="display:flex;align-items:center;justify-content:center;font-size:12px;color:#678A9D">写真</div><div class="doctor-info"><div class="position">消化器内科 部長</div><div class="name">医師名</div><div class="name-en">Doctor Name</div><div class="specialty">専門: 消化器内視鏡、大腸がん</div></div></div>
<h2 class="heading01">ポイント1: 大腸がんは増えている</h2>
<p>大腸がんは日本において罹患数が最も多いがんの一つです。食生活の欧米化や高齢化に伴い、年々増加傾向にあります。しかし、早期発見・早期治療により、高い治癒率が期待できます。</p>
<h2 class="heading01">ポイント2: 自覚症状が少ない</h2>
<p>大腸がんの初期段階では、ほとんど自覚症状がありません。血便や便通の変化、腹痛などの症状が現れた時には、進行していることもあります。定期的な検診が重要です。</p>
<h2 class="heading01">ポイント3: 検査方法</h2>
<table><tr><th>検査方法</th><th>特徴</th><th>所要時間</th></tr><tr><td>便潜血検査</td><td>簡易的なスクリーニング</td><td>結果まで数日</td></tr><tr><td>大腸内視鏡検査</td><td>直接観察・生検・治療が可能</td><td>約30分</td></tr><tr><td>大腸CT検査</td><td>身体への負担が少ない</td><td>約15分</td></tr></table>
<h2 class="heading01">ポイント4: 早期発見の重要性</h2>
<p>ステージIで発見された場合の5年生存率は90%以上です。定期的な便潜血検査と、陽性の場合の二次検査（内視鏡検査）を受けることが大切です。</p>
<h2 class="heading01">ポイント5: 当院の治療体制</h2>
<p>当院では内視鏡センターを中心に、外科・腫瘍内科・放射線治療科が連携し、患者さまに最適な治療を提供しています。ロボット支援手術（ダビンチ）にも対応しています。</p>
<p style="margin-top:30px"><a href="../department/detail.html" class="btn-main">消化器内科のページへ</a></p>""")

    # Area
    gen_under_page("area/index.html", "医療連携・紹介", "Medical Cooperation",
        [("area/index.html","医療連携・紹介")], "area", 1,
        """<h2 class="heading01">一般の方</h2>
<h3 class="heading02">診察のご予約</h3>
<div style="display:flex;gap:8px;margin:20px 0;flex-wrap:wrap">
<div style="flex:1;min-width:180px;text-align:center;background:#F2F8FA;padding:20px;border-radius:8px"><div style="width:36px;height:36px;background:#4F819F;color:#fff;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-weight:700;margin-bottom:8px">1</div><div style="font-size:14px;font-weight:600">かかりつけ医を受診</div></div>
<div style="flex:1;min-width:180px;text-align:center;background:#F2F8FA;padding:20px;border-radius:8px"><div style="width:36px;height:36px;background:#4F819F;color:#fff;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-weight:700;margin-bottom:8px">2</div><div style="font-size:14px;font-weight:600">紹介状の発行</div></div>
<div style="flex:1;min-width:180px;text-align:center;background:#F2F8FA;padding:20px;border-radius:8px"><div style="width:36px;height:36px;background:#4F819F;color:#fff;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-weight:700;margin-bottom:8px">3</div><div style="font-size:14px;font-weight:600">当院の予約・受診</div></div>
</div>
<h2 class="heading01" style="margin-top:40px">医療機関の方</h2>
<h3 class="heading02">検査のご予約</h3>
<table><tr><th>検査種別</th><th>予約方法</th></tr><tr><td>CT・MRI</td><td>FAX予約</td></tr><tr><td>内視鏡検査</td><td>FAX予約</td></tr><tr><td>超音波検査</td><td>FAX予約</td></tr><tr><td>心臓カテーテル</td><td>電話予約</td></tr><tr><td>核医学検査</td><td>FAX予約</td></tr></table>
<h3 class="heading02">診察・検査 1DAYセット</h3>
<p>1日で診察と検査を同時に受けられるセットプランをご用意しています。</p>
<div class="info-box-blue"><strong>地域連携室</strong><br>TEL: 0586-48-0077（内線2180）<br>FAX: 0586-48-0038<br>受付時間: 月〜金 9:00〜17:00 / 土 9:00〜12:00</div>""")

    # About top
    gen_under_page("about/index.html", "病院紹介", "About Us",
        [("about/index.html","病院紹介")], "about", 1,
        """<h2 class="heading01">病院について</h2>
<div class="card-grid col-3">
<a href="#" class="card-item"><div class="card-body"><div class="ttl">病院長からのご挨拶</div></div></a>
<a href="#" class="card-item"><div class="card-body"><div class="ttl">沿革</div></div></a>
<a href="#" class="card-item"><div class="card-body"><div class="ttl">病院概要</div></div></a>
<a href="#" class="card-item"><div class="card-body"><div class="ttl">活動実績</div></div></a>
<a href="#" class="card-item"><div class="card-body"><div class="ttl">病院指標</div></div></a>
<a href="#" class="card-item"><div class="card-body"><div class="ttl">DPC特定病院群</div></div></a>
<a href="#" class="card-item"><div class="card-body"><div class="ttl">災害拠点病院</div></div></a>
<a href="#" class="card-item"><div class="card-body"><div class="ttl">病院からのお願い</div></div></a>
</div>
<div class="info-box-blue" style="margin-top:30px"><strong>2023年7月 新館B棟オープン</strong><br>回復期リハビリテーション病棟、緩和ケア病棟を新設し、急性期から回復期まで一貫した医療を提供できる体制を整えました。</div>
<p style="margin-top:20px"><a href="ward.html" class="btn-main">病棟のご案内</a></p>
<h2 class="heading01" style="margin-top:40px">当院の取り組み</h2>
<ul style="line-height:2.4;font-size:15px">
<li>施設基準関連事項一覧</li><li>医療安全・患者相談窓口</li><li>院内感染対策</li><li>敷地内全面禁煙</li><li>NCD及びJNDデータベース事業</li><li>輸血拒否に対する方針</li><li>医療従事者負担軽減</li><li>倫理的課題指針</li><li>クリニカルパス</li><li>院内がん登録オプトアウト</li><li>人生会議 ACP</li><li>治験・臨床研究</li></ul>
<h2 class="heading01" style="margin-top:40px">医療情報・コラム</h2>
<div class="card-grid col-2">
<a href="../news/column.html" class="card-item"><div class="card-body"><div class="ttl">市民公開WEB講座</div><div class="desc">当院の医師が監修するWEB講座</div></div></a>
<a href="../news/column.html" class="card-item"><div class="card-body"><div class="ttl">健康のつボ!</div><div class="desc">CBCラジオ連動 健康情報</div></div></a>
</div>""")

    # About ward
    floors_a = [("11F","A11病棟（産婦人科）"),("10F","A10病棟"),("9F","A9病棟"),("8F","A8病棟"),("7F","A7病棟"),("6F","A6病棟"),("5F","A5病棟"),("4F","A4病棟"),("3F","手術室・中央材料室"),("2F","外来・入退院支援センター"),("1F","外来・救急外来")]
    floors_b = [("11F","B11病棟（緩和ケア）"),("10F","B10病棟（回復期リハ）"),("9F","B9病棟（回復期リハ）"),("8F","B8病棟（回復期リハ）"),("7F","B7病棟"),("6F","B6病棟"),("5F","B5病棟"),("4F","B4病棟"),("3F","手術室・デイサージャリー"),("2F","外来・化学療法室")]
    fa = "\n".join([f"<tr><td style='font-weight:700;background:#F2F8FA;text-align:center;width:60px'>{f}</td><td>{n}</td></tr>" for f,n in floors_a])
    fb = "\n".join([f"<tr><td style='font-weight:700;background:#F2F8FA;text-align:center;width:60px'>{f}</td><td>{n}</td></tr>" for f,n in floors_b])
    gen_under_page("about/ward.html", "病棟のご案内", "Ward Guide",
        [("about/index.html","病院紹介"),("about/ward.html","病棟のご案内")], "about", 1,
        f"""<h2 class="heading01">A棟・B棟 フロアガイド</h2>
<p>一宮西病院はA棟（既存棟）とB棟（2023年7月新設）の2棟構成です。計約600床の病床を有しています。</p>
<div style="display:flex;gap:20px;margin-top:30px;flex-wrap:wrap">
<div style="flex:1;min-width:380px"><h3 class="heading02">A棟</h3><table>{fa}</table></div>
<div style="flex:1;min-width:380px"><h3 class="heading02">B棟</h3><table>{fb}</table></div>
</div>
<h3 class="heading02" style="margin-top:40px">特殊施設</h3>
<div class="card-grid col-3">
<div class="card-item"><div class="card-body"><div class="ttl">脳卒中集中治療室(SCU)</div><div class="desc">脳卒中専用の集中治療室</div></div></div>
<div class="card-item"><div class="card-body"><div class="ttl">手術室</div><div class="desc">A棟・B棟 計16室</div></div></div>
<div class="card-item"><div class="card-body"><div class="ttl">集中治療室(ICU)</div><div class="desc">重症患者の24時間監視</div></div></div>
</div>""")

    # News list
    nlist = [
        ("2026.04.01","お知らせ","災害拠点病院指定"),("2026.04.01","お知らせ","新路線バス「一宮西線」運行開始"),
        ("2026.03.12","イベント","健康づくりフェア"),("2026.03.08","イベント","世界緑内障週間ライトアップ"),
        ("2026.03.01","イベント","大腸がん啓発ブルーリボン"),("2026.02.17","イベント","あんずマルシェ"),
        ("2025.12.02","お知らせ","歯科口腔外科WEB診療予約開始"),("2025.11.17","お知らせ","無痛分娩提供開始"),
        ("2025.10.23","お知らせ","電子書籍読み放題サービス導入"),("2025.09.30","メディア","ZIP-FM乳がん啓発放送"),
        ("2025.09.07","メディア","救急フェス2025メディア掲載"),("2025.08.29","メディア","中京テレビ「キャッチ!」放送"),
        ("2025.08.10","メディア","産経新聞記事"),("2025.07.07","お知らせ","発熱・発疹患者へのお願い"),
        ("2025.05.14","お知らせ","瑞宝単光章叙勲"),
    ]
    nhtml = "\n".join([f'<dl class="clearfix"><dt class="ic001">{d}</dt><dd><a href="detail.html">[{c}] {t}</a></dd></dl>' for d,c,t in nlist])
    gen_under_page("news/index.html", "お知らせ・ニュース", "News",
        [("news/index.html","お知らせ")], "", 1,
        f"""<div class="news-list"><div class="news-list-in">{nhtml}</div></div>
<div class="pagination"><span class="current">1</span><a href="#">2</a><a href="#">3</a><a href="#">次へ</a></div>""")

    # News detail
    gen_under_page("news/detail.html", "新路線バス「一宮西線」運行開始", "News Detail",
        [("news/index.html","お知らせ"),("news/detail.html","新路線バス「一宮西線」")], "", 1,
        """<p style="color:#678A9D;font-size:14px;margin-bottom:16px">2026.04.01 ｜ お知らせ</p>
<h2 class="heading01">2026年4月1日(水)より新路線バス「一宮西線」の運行が開始</h2>
<p>名鉄バスの新路線「一宮西線」が運行を開始しました。名鉄一宮駅バスターミナルから当院まで、直通で約20分でお越しいただけます。</p>
<div style="height:300px;background:#E6F0F5;display:flex;align-items:center;justify-content:center;color:#678A9D;font-size:14px;border-radius:8px;margin:30px 0">路線図イメージ</div>
<h3 class="heading02">主な停留所</h3>
<table><tr><th>停留所名</th><th>所要時間（目安）</th></tr><tr><td>名鉄一宮駅</td><td>0分（始発）</td></tr><tr><td>一宮市役所前</td><td>約5分</td></tr><tr><td>開明</td><td>約15分</td></tr><tr><td>一宮西病院</td><td>約20分（終点）</td></tr></table>
<p style="margin-top:30px"><a href="../guide/access.html" class="btn-main">交通アクセスの詳細へ</a></p>""")

    # Column
    gen_under_page("news/column.html", "健康のつボ! — 脳卒中について", "Health Column",
        [("about/index.html","病院紹介"),("news/column.html","健康のつボ!")], "about", 1,
        """<p style="color:#678A9D;font-size:14px;margin-bottom:20px">CBCラジオ連動企画 ｜ 全13回シリーズ</p>
<div class="doctor-card"><div class="doctor-photo" style="display:flex;align-items:center;justify-content:center;font-size:12px;color:#678A9D">写真</div><div class="doctor-info"><div class="position">脳神経外科 部長</div><div class="name">医師名</div><div class="name-en">Doctor Name</div><div class="specialty">専門: 脳血管障害、脳卒中</div></div></div>
<h2 class="heading01">第1回「脳卒中とは？」</h2>
<p>脳卒中とは、脳の血管に異常が起こる病気の総称です。大きく分けて、脳の血管が詰まる「脳梗塞」、脳の血管が破れる「脳出血」、脳を覆う膜の血管にできたこぶが破裂する「くも膜下出血」の3種類があります。</p>
<div class="info-box-blue"><strong>ポイント</strong><br>脳卒中は突然発症します。「FAST」を覚えましょう。<br>Face（顔の麻痺）/ Arm（腕の麻痺）/ Speech（言葉の障害）/ Time（発症時刻）→ すぐに救急車を!</div>
<h3 class="heading02">シリーズ目次</h3>
<ul style="line-height:2.4;font-size:14px">
<li>第1回「脳卒中とは？」</li><li>第2回「ストロークチームについて」</li><li>第3回「脳梗塞とは① 〜夏でも起こる脳梗塞」</li><li>第4回「脳梗塞とは② 〜時間との闘い」</li><li>第5回「脳梗塞とは③ 〜血栓回収療法」</li><li>第6回「くも膜下出血とは①」</li><li>第7回「くも膜下出血とは②」</li><li>第8回「脳出血とは」</li><li>第9回「脳卒中は時間との闘い」</li><li>第10回「FASTは救急車を呼ぶサイン!」</li><li>第11回「脳ドックについて」</li><li>第12回「脳卒中予防10か条」</li><li>第13回「まとめ」</li></ul>
<p style="margin-top:20px"><a href="../department/center.html" class="btn-main">脳卒中センターのページへ</a></p>""")

    # Seminar
    gen_under_page("seminar/index.html", "市民公開講座", "Public Seminar",
        [("seminar/index.html","市民公開講座")], "", 1,
        """<h2 class="heading01">2026年の講座</h2>
<div class="card-grid col-2">
<div class="card-item"><div class="card-body"><div class="desc" style="font-size:12px;color:#678A9D;margin-bottom:4px">2026年6月予定</div><div class="ttl">大腸がんの最新治療</div><div class="desc" style="margin-top:8px">消化器内科 医師が解説する、大腸がんの早期発見と最新の治療法</div><p style="margin-top:12px"><a href="#" class="btn-main" style="padding:8px 20px;font-size:13px">申込み</a></p></div></div>
<div class="card-item"><div class="card-body"><div class="desc" style="font-size:12px;color:#678A9D;margin-bottom:4px">2026年7月予定</div><div class="ttl">心臓病と生活習慣</div><div class="desc" style="margin-top:8px">循環器内科医が語る、心臓を守るための生活習慣</div><p style="margin-top:12px"><a href="#" class="btn-main" style="padding:8px 20px;font-size:13px">申込み</a></p></div></div>
</div>
<h2 class="heading01" style="margin-top:40px">過去の講座アーカイブ</h2>
<table><tr><th>日付</th><th>テーマ</th><th>講師</th></tr>
<tr><td>2025.11.15</td><td>胃がんの早期発見</td><td>消化器内科</td></tr>
<tr><td>2025.09.20</td><td>乳がん検診の重要性</td><td>乳腺外科</td></tr>
<tr><td>2025.07.12</td><td>脳卒中の予防と対策</td><td>脳神経外科</td></tr>
<tr><td>2025.05.18</td><td>膝の痛みと人工関節</td><td>整形外科</td></tr></table>""")

    # Recruit top
    gen_under_page("recruit/index.html", "採用情報", "Recruit",
        [("recruit/index.html","採用情報")], "recruit", 1,
        """<div style="background:linear-gradient(135deg,#022634,#0a3d54);padding:50px 40px;border-radius:12px;color:#fff;text-align:center;margin-bottom:40px">
<h2 style="font-family:'Noto Serif JP',serif;font-size:28px;font-weight:400;margin-bottom:20px">共に成長し、地域医療を支える仲間を募集しています</h2>
<div style="display:flex;gap:20px;justify-content:center;flex-wrap:wrap;margin-top:24px">
<div style="min-width:120px"><div style="font-size:36px;font-weight:900;font-family:Roboto,sans-serif">600</div><div style="font-size:12px;opacity:.8">病床数</div></div>
<div style="min-width:120px"><div style="font-size:36px;font-weight:900;font-family:Roboto,sans-serif">33</div><div style="font-size:12px;opacity:.8">診療科</div></div>
<div style="min-width:120px"><div style="font-size:36px;font-weight:900;font-family:Roboto,sans-serif">10,000<span style="font-size:16px">+</span></div><div style="font-size:12px;opacity:.8">年間手術件数</div></div>
<div style="min-width:120px"><div style="font-size:36px;font-weight:900;font-family:Roboto,sans-serif">8,000<span style="font-size:16px">+</span></div><div style="font-size:12px;opacity:.8">年間救急搬送</div></div>
</div></div>
<h2 class="heading01">募集職種</h2>
<div class="card-grid col-2">
<a href="resident.html" class="card-item"><div class="card-body"><div class="ttl">臨床研修医・後期研修医</div><div class="desc">充実の症例数と指導体制で実践力を磨く</div></div></a>
<a href="#" class="card-item"><div class="card-body"><div class="ttl">キャリア医師</div><div class="desc">専門性を活かせる環境で地域医療に貢献</div></div></a>
<a href="nurse.html" class="card-item"><div class="card-body"><div class="ttl">看護師</div><div class="desc">教育体制充実・ワークライフバランスを重視</div></div></a>
<a href="#" class="card-item"><div class="card-body"><div class="ttl">その他の職種</div><div class="desc">薬剤師・臨床検査技師・放射線技師・リハビリ・事務</div></div></a>
</div>""")

    # Nurse
    gen_under_page("recruit/nurse.html", "看護師採用", "Nurse Recruitment",
        [("recruit/index.html","採用情報"),("recruit/nurse.html","看護師採用")], "recruit", 1,
        """<h2 class="heading01">看護部について</h2>
<p>一宮西病院 看護部は、「患者さまに寄り添い、質の高い看護を提供する」を理念に掲げ、約650名の看護師が33の診療科で活躍しています。</p>
<div style="display:flex;gap:16px;margin:30px 0;flex-wrap:wrap">
<div style="flex:1;min-width:140px;text-align:center;background:#F2F8FA;padding:24px;border-radius:8px"><div style="font-size:36px;font-weight:900;color:#4F819F;font-family:Roboto,sans-serif">650</div><div style="font-size:13px;color:#678A9D">看護師数</div></div>
<div style="flex:1;min-width:140px;text-align:center;background:#F2F8FA;padding:24px;border-radius:8px"><div style="font-size:36px;font-weight:900;color:#4F819F;font-family:Roboto,sans-serif">32.5</div><div style="font-size:13px;color:#678A9D">平均年齢</div></div>
<div style="flex:1;min-width:140px;text-align:center;background:#F2F8FA;padding:24px;border-radius:8px"><div style="font-size:36px;font-weight:900;color:#4F819F;font-family:Roboto,sans-serif">78%</div><div style="font-size:13px;color:#678A9D">有給取得率</div></div>
<div style="flex:1;min-width:140px;text-align:center;background:#F2F8FA;padding:24px;border-radius:8px"><div style="font-size:36px;font-weight:900;color:#4F819F;font-family:Roboto,sans-serif">8.2%</div><div style="font-size:13px;color:#678A9D">離職率</div></div>
</div>
<h2 class="heading01">教育制度</h2>
<h3 class="heading02">キャリアラダー</h3>
<div style="display:flex;gap:4px;margin:20px 0;flex-wrap:wrap">
<div style="flex:1;min-width:100px;text-align:center;background:#E7F2F8;padding:16px 8px;border-radius:8px;font-size:13px;font-weight:600;color:#4F819F">新人</div>
<div style="flex:1;min-width:100px;text-align:center;background:#DDEAEF;padding:16px 8px;border-radius:8px;font-size:13px;font-weight:600;color:#3D7597">一人前</div>
<div style="flex:1;min-width:100px;text-align:center;background:#B8D4E3;padding:16px 8px;border-radius:8px;font-size:13px;font-weight:600;color:#fff">中堅</div>
<div style="flex:1;min-width:100px;text-align:center;background:#6694AF;padding:16px 8px;border-radius:8px;font-size:13px;font-weight:600;color:#fff">エキスパート</div>
<div style="flex:1;min-width:100px;text-align:center;background:#4F819F;padding:16px 8px;border-radius:8px;font-size:13px;font-weight:600;color:#fff">管理職</div>
</div>
<h2 class="heading01" style="margin-top:40px">募集要項</h2>
<table><tr><th>職種</th><td>看護師（新卒・既卒）</td></tr><tr><th>応募資格</th><td>看護師免許取得者（取得見込み含む）</td></tr><tr><th>給与</th><td>大学卒 月給約270,000円〜（夜勤手当等含む）</td></tr><tr><th>勤務時間</th><td>二交替制（日勤 8:30-17:00 / 夜勤 16:30-9:00）</td></tr><tr><th>休日</th><td>4週8休、年間休日120日以上</td></tr><tr><th>賞与</th><td>年2回（計4.0ヶ月分）</td></tr></table>
<p style="margin-top:30px;text-align:center"><a href="#" class="btn-main" style="padding:16px 48px;font-size:16px">エントリーはこちら</a></p>""")

    # Resident
    gen_under_page("recruit/resident.html", "臨床研修医募集", "Resident Recruitment",
        [("recruit/index.html","採用情報"),("recruit/resident.html","臨床研修医募集")], "recruit", 1,
        """<h2 class="heading01">初期臨床研修の特長</h2>
<div style="display:flex;gap:16px;margin:20px 0;flex-wrap:wrap">
<div style="flex:1;min-width:200px;text-align:center;background:#F2F8FA;padding:30px 16px;border-radius:8px"><div style="font-size:28px;font-weight:900;color:#4F819F">豊富な症例数</div><div style="font-size:13px;color:#678A9D;margin-top:8px">年間救急搬送8,000件超<br>手術10,000件超</div></div>
<div style="flex:1;min-width:200px;text-align:center;background:#F2F8FA;padding:30px 16px;border-radius:8px"><div style="font-size:28px;font-weight:900;color:#4F819F">充実の指導</div><div style="font-size:13px;color:#678A9D;margin-top:8px">各科専門医による<br>マンツーマン指導</div></div>
<div style="flex:1;min-width:200px;text-align:center;background:#F2F8FA;padding:30px 16px;border-radius:8px"><div style="font-size:28px;font-weight:900;color:#4F819F">手技の機会</div><div style="font-size:13px;color:#678A9D;margin-top:8px">積極的に手技を<br>経験できる環境</div></div>
</div>
<h2 class="heading01" style="margin-top:40px">研修医の1日</h2>
<div style="padding-left:30px;position:relative;margin:20px 0">
<div style="position:absolute;left:8px;top:0;bottom:0;width:2px;background:#D0E0E6"></div>
<div style="position:relative;padding-bottom:20px"><div style="position:absolute;left:-26px;top:4px;width:12px;height:12px;background:#4F819F;border-radius:50%"></div><div style="font-weight:700;color:#4F819F;font-size:14px">7:30</div><div style="font-size:14px;color:#333;margin-top:2px">出勤・カルテチェック</div></div>
<div style="position:relative;padding-bottom:20px"><div style="position:absolute;left:-26px;top:4px;width:12px;height:12px;background:#4F819F;border-radius:50%"></div><div style="font-weight:700;color:#4F819F;font-size:14px">8:00</div><div style="font-size:14px;color:#333;margin-top:2px">カンファレンス</div></div>
<div style="position:relative;padding-bottom:20px"><div style="position:absolute;left:-26px;top:4px;width:12px;height:12px;background:#4F819F;border-radius:50%"></div><div style="font-weight:700;color:#4F819F;font-size:14px">9:00</div><div style="font-size:14px;color:#333;margin-top:2px">病棟回診</div></div>
<div style="position:relative;padding-bottom:20px"><div style="position:absolute;left:-26px;top:4px;width:12px;height:12px;background:#4F819F;border-radius:50%"></div><div style="font-weight:700;color:#4F819F;font-size:14px">10:00</div><div style="font-size:14px;color:#333;margin-top:2px">手術・検査</div></div>
<div style="position:relative;padding-bottom:20px"><div style="position:absolute;left:-26px;top:4px;width:12px;height:12px;background:#6694AF;border-radius:50%"></div><div style="font-weight:700;color:#6694AF;font-size:14px">12:00</div><div style="font-size:14px;color:#333;margin-top:2px">昼食</div></div>
<div style="position:relative;padding-bottom:20px"><div style="position:absolute;left:-26px;top:4px;width:12px;height:12px;background:#4F819F;border-radius:50%"></div><div style="font-weight:700;color:#4F819F;font-size:14px">13:00</div><div style="font-size:14px;color:#333;margin-top:2px">外来・検査</div></div>
<div style="position:relative;padding-bottom:20px"><div style="position:absolute;left:-26px;top:4px;width:12px;height:12px;background:#4F819F;border-radius:50%"></div><div style="font-weight:700;color:#4F819F;font-size:14px">16:00</div><div style="font-size:14px;color:#333;margin-top:2px">振り返りカンファレンス</div></div>
<div style="position:relative"><div style="position:absolute;left:-26px;top:4px;width:12px;height:12px;background:#BCB476;border-radius:50%"></div><div style="font-weight:700;color:#BCB476;font-size:14px">17:30</div><div style="font-size:14px;color:#333;margin-top:2px">自主学習・帰宅</div></div>
</div>
<h2 class="heading01" style="margin-top:40px">募集要項</h2>
<table><tr><th>募集人数</th><td>10名</td></tr><tr><th>身分</th><td>常勤嘱託医</td></tr><tr><th>給与</th><td>1年次 月額約350,000円 / 2年次 月額約380,000円</td></tr><tr><th>当直手当</th><td>1回あたり20,000円</td></tr><tr><th>休日</th><td>4週8休、年末年始、有給休暇</td></tr><tr><th>宿舎</th><td>病院近隣に研修医用宿舎完備（家賃補助あり）</td></tr></table>
<div style="background:linear-gradient(135deg,#022634,#4F819F);padding:40px;border-radius:12px;text-align:center;color:#fff;margin-top:40px">
<h3 style="font-size:20px;margin-bottom:12px">病院見学 随時受付中</h3>
<p style="font-size:14px;opacity:.9;margin-bottom:20px">実際の研修環境を見て、先輩研修医と話してみませんか？</p>
<a href="#" style="display:inline-block;background:#fff;color:#022634;padding:14px 40px;border-radius:6px;font-weight:700;font-size:15px">見学を申し込む</a>
</div>""")

    print(f"\n=== 全22ページ生成完了 ===")

if __name__ == "__main__":
    gen_all()
