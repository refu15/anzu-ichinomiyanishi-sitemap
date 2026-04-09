#!/usr/bin/env python3
"""一宮西病院サイトマップから全画像をダウンロードするスクリプト"""

import os
import re
import time
import hashlib
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, unquote
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = "https://www.anzu.or.jp/ichinomiyanishi/"
OUTPUT_DIR = Path("C:/tmp/anzu-ichinomiyanishi-sitemap/images")
SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
})

# Track downloaded URLs to avoid duplicates
downloaded_urls = set()
downloaded_hashes = set()

# All pages to crawl from sitemap
PAGES = [
    # Top
    "/ichinomiyanishi/",
    # Guide
    "/ichinomiyanishi/guide/",
    "/ichinomiyanishi/guide/surgery/consultation/",
    "/ichinomiyanishi/guide/surgery/first_aid/",
    "/ichinomiyanishi/guide/surgery/time_table/",
    "/ichinomiyanishi/guide/surgery/surgery_hour/",
    "/ichinomiyanishi/guide/surgery/floor/",
    "/ichinomiyanishi/guide/surgery/vaccination/",
    "/ichinomiyanishi/guide/surgery/second-opinion/",
    "/ichinomiyanishi/guide/stay/expense/",
    "/ichinomiyanishi/guide/stay/visit/",
    "/ichinomiyanishi/guide/stay/visit/online/",
    "/ichinomiyanishi/guide/stay/rihabilitation-hope/",
    "/ichinomiyanishi/guide/stay/parking/",
    "/ichinomiyanishi/guide/equipment/",
    "/ichinomiyanishi/guide/medical-consultation/",
    "/ichinomiyanishi/guide/cancer_consultation_support_center/",
    "/ichinomiyanishi/guide/anzu-no-ki/",
    "/ichinomiyanishi/guide/free-wifi/",
    "/ichinomiyanishi/guide/restaurant-shukran/",
    "/ichinomiyanishi/guide/accsess/",
    "/ichinomiyanishi/guide/seminor/",
    "/ichinomiyanishi/guide/anzu-marche/",
    "/ichinomiyanishi/guide/documents/",
    "/ichinomiyanishi/guide/kaiji/",
    "/ichinomiyanishi/guide/2nd_opinion/",
    "/ichinomiyanishi/guide/kakaritsuke/",
    "/ichinomiyanishi/guide/electronic-prescription/",
    "/ichinomiyanishi/guide/donichi-kensa-chiryou/",
    "/ichinomiyanishi/guide/covid-19/",
    "/ichinomiyanishi/for-outpatient/",
    "/ichinomiyanishi/for-inpatient-visit/",
    # Health checkup
    "/ichinomiyanishi/for-dock/",
    "/ichinomiyanishi/for-dock/about/",
    "/ichinomiyanishi/for-dock/checkup/",
    "/ichinomiyanishi/for-dock/checkup/afternoon/",
    "/ichinomiyanishi/for-dock/guide/",
    "/ichinomiyanishi/for-dock/faq/",
    "/ichinomiyanishi/for-dock/staff_msc/",
    # Department
    "/ichinomiyanishi/department/",
    # Medicine (internal)
    "/ichinomiyanishi/medicine/digestive/",
    "/ichinomiyanishi/medicine/hematology/",
    "/ichinomiyanishi/medicine/respiratory/",
    "/ichinomiyanishi/medicine/circulatory/",
    "/ichinomiyanishi/medicine/diabetes/",
    "/ichinomiyanishi/medicine/nerve/",
    "/ichinomiyanishi/medicine/rheumatism/",
    "/ichinomiyanishi/medicine/nephrology/",
    "/ichinomiyanishi/medicine/oncology/",
    "/ichinomiyanishi/medicine/pediatrics/",
    "/ichinomiyanishi/medicine/general/",
    "/ichinomiyanishi/medicine/palliative_care_internal_medicine/",
    "/ichinomiyanishi/medicine/circulatory/footarteriosclerosis/",
    "/ichinomiyanishi/medicine/circulatory/tavi/",
    "/ichinomiyanishi/medicine/circulatory/impella/",
    "/ichinomiyanishi/medicine/diabetes/thyroid/",
    # Surgery (external)
    "/ichinomiyanishi/surgery/surgery_intro/",
    "/ichinomiyanishi/surgery/mammary/",
    "/ichinomiyanishi/surgery/anus/",
    "/ichinomiyanishi/surgery/thoracic/",
    "/ichinomiyanishi/surgery/sinzokekkangeka/",
    "/ichinomiyanishi/surgery/neurosurgery/",
    "/ichinomiyanishi/surgery/orthopedics/",
    "/ichinomiyanishi/surgery/plastic/",
    "/ichinomiyanishi/surgery/ear/",
    "/ichinomiyanishi/surgery/urinary/",
    "/ichinomiyanishi/surgery/ophthalmology/",
    "/ichinomiyanishi/surgery/skin/",
    "/ichinomiyanishi/surgery/maternity/",
    "/ichinomiyanishi/surgery/surgery_intro/difficult_major_surgery/",
    "/ichinomiyanishi/surgery/surgery_intro/robot/",
    "/ichinomiyanishi/surgery/anus/snms-urgery/",
    "/ichinomiyanishi/surgery/sinzokekkangeka/benmakushou/",
    "/ichinomiyanishi/surgery/neurosurgery/treat_neuro2/",
    "/ichinomiyanishi/surgery/orthopedics/sports/",
    "/ichinomiyanishi/surgery/ophthalmology/minimallyinvasivevitreoretinalsurgerymivs/",
    "/ichinomiyanishi/surgery/ophthalmology/micro_invasive_gulaucoma_surgery/",
    "/ichinomiyanishi/surgery/ophthalmology/multifocal_intraocular_lens/",
    "/ichinomiyanishi/surgery/ophthalmology/gannkaryokunaisyou/",
    "/ichinomiyanishi/surgery/urinary/hinyoukikazenritusengan/",
    "/ichinomiyanishi/surgery/maternity/new-obstetrics/",
    "/ichinomiyanishi/surgery/maternity/genetic_outpatient/",
    "/ichinomiyanishi/surgery/maternity/maternity-nipt/",
    "/ichinomiyanishi/surgery/maternity/specialsite/",
    "/ichinomiyanishi/surgery/maternity/gynecology/minimallyinvasive/",
    "/ichinomiyanishi/surgery/maternity/gynecology/davinci/",
    # Other departments
    "/ichinomiyanishi/other/psychiatry-hospitalization/",
    "/ichinomiyanishi/other/oral-surgery/",
    "/ichinomiyanishi/other/emergency/",
    "/ichinomiyanishi/other/anesthesia/",
    "/ichinomiyanishi/other/pathology/",
    "/ichinomiyanishi/other/radiation/",
    "/ichinomiyanishi/other/radiotherapy/",
    "/ichinomiyanishi/other/rehabilitation/",
    # Centers
    "/ichinomiyanishi/center/endoscope/",
    "/ichinomiyanishi/center/hpb/",
    "/ichinomiyanishi/center/arrhythmia/",
    "/ichinomiyanishi/center/obesity/",
    "/ichinomiyanishi/center/diabetes/",
    "/ichinomiyanishi/center/stroke/",
    "/ichinomiyanishi/center/dialysis/",
    "/ichinomiyanishi/center/jin-and-shunt/",
    "/ichinomiyanishi/center/fukukukyo/",
    "/ichinomiyanishi/center/stent/",
    "/ichinomiyanishi/center/vein/",
    "/ichinomiyanishi/center/sekitsui_sokuwan/",
    "/ichinomiyanishi/center/jinko/",
    "/ichinomiyanishi/center/hand_surgery/",
    "/ichinomiyanishi/center/shoulder_joint/",
    "/ichinomiyanishi/center/hipjoint/",
    "/ichinomiyanishi/center/fracture/",
    "/ichinomiyanishi/center/aging-care/",
    # Special
    "/ichinomiyanishi/special/",
    "/ichinomiyanishi/special/ladies_outpatient/",
    "/ichinomiyanishi/special/woc/",
    "/ichinomiyanishi/special/peritonealseeding/",
    "/ichinomiyanishi/special/medical_equipment/",
    "/ichinomiyanishi/special/medical_equipment/ctc/",
    "/ichinomiyanishi/special/cancer/",
    "/ichinomiyanishi/special/endoscopic/",
    "/ichinomiyanishi/special/special_interview/interview_5/",
    "/ichinomiyanishi/special/special_interview/interview_14_colorectalcancer/",
    "/ichinomiyanishi/special/special_interview/interview_14/",
    "/ichinomiyanishi/special/special_interview/interview_1/",
    "/ichinomiyanishi/special/special_interview/interview_4/",
    "/ichinomiyanishi/special/special_interview/interview_15_stroke/",
    "/ichinomiyanishi/special/special_interview/oa-knee/",
    "/ichinomiyanishi/special/special_interview/interview_09/",
    "/ichinomiyanishi/special/special_interview/hippain/",
    "/ichinomiyanishi/special/special_interview/12/",
    "/ichinomiyanishi/special/special_interview/2/",
    # Area
    "/ichinomiyanishi/area/",
    "/ichinomiyanishi/area/shinryou_yoyaku/",
    "/ichinomiyanishi/area/kenshin_2ji/",
    "/ichinomiyanishi/area/shinryouka/",
    "/ichinomiyanishi/area/kensa_yoyaku/",
    "/ichinomiyanishi/area/onedayset/",
    # About
    "/ichinomiyanishi/about/",
    "/ichinomiyanishi/about/hospital/greeting/",
    "/ichinomiyanishi/about/hospital/interview/",
    "/ichinomiyanishi/about/hospital/history/",
    "/ichinomiyanishi/about/hospital/outline/",
    "/ichinomiyanishi/about/hospital/list_archive/",
    "/ichinomiyanishi/about/hospital/data/",
    "/ichinomiyanishi/about/hospital/dpc2/",
    "/ichinomiyanishi/about/hospital/disaster/",
    "/ichinomiyanishi/about/hospital/request/",
    "/ichinomiyanishi/about/ward/",
    "/ichinomiyanishi/about/ward/a4/",
    "/ichinomiyanishi/about/ward/a5/",
    "/ichinomiyanishi/about/ward/a6/",
    "/ichinomiyanishi/about/ward/a7/",
    "/ichinomiyanishi/about/ward/a8/",
    "/ichinomiyanishi/about/ward/a9/",
    "/ichinomiyanishi/about/ward/a10/",
    "/ichinomiyanishi/about/ward/a11/",
    "/ichinomiyanishi/about/ward/b4/",
    "/ichinomiyanishi/about/ward/b5/",
    "/ichinomiyanishi/about/ward/b6/",
    "/ichinomiyanishi/about/ward/b7/",
    "/ichinomiyanishi/about/ward/b8910/",
    "/ichinomiyanishi/about/ward/palliative-care-ward/",
    "/ichinomiyanishi/about/ward/scu/",
    "/ichinomiyanishi/about/ward/operating/",
    "/ichinomiyanishi/about/effort/facility-standards/",
    "/ichinomiyanishi/about/effort/medical-safety/",
    "/ichinomiyanishi/about/effort/infection_control/",
    "/ichinomiyanishi/about/effort/nosmoke/",
    "/ichinomiyanishi/about/effort/database/",
    "/ichinomiyanishi/about/effort/yuketsu/",
    "/ichinomiyanishi/about/effort/iryoujyuujisya/",
    "/ichinomiyanishi/about/effort/rinri/",
    "/ichinomiyanishi/about/effort/clinical_pathways/",
    "/ichinomiyanishi/about/effort/optout/",
    "/ichinomiyanishi/about/effort/acp/",
    "/ichinomiyanishi/about/effort/research/",
    "/ichinomiyanishi/about/system/conference/",
    "/ichinomiyanishi/about/system/committee/",
    "/ichinomiyanishi/about/system/nst/",
    "/ichinomiyanishi/about/system/dst/",
    "/ichinomiyanishi/about/system/infection-control/",
    "/ichinomiyanishi/about/column/",
    "/ichinomiyanishi/about/column/colon-cancer/",
    "/ichinomiyanishi/about/column/seminar_stomach-cancer/",
    "/ichinomiyanishi/about/column/seminar_colon/",
    "/ichinomiyanishi/about/column/copd/",
    "/ichinomiyanishi/about/column/seminar_lung-cancer/",
    "/ichinomiyanishi/about/column/seminar_arrhythmia/",
    "/ichinomiyanishi/about/column/seminar_headache/",
    "/ichinomiyanishi/about/column/child-heatstroke/",
    "/ichinomiyanishi/about/column/202401_palliative_care/",
    "/ichinomiyanishi/about/column/202402_palliative_care/",
    "/ichinomiyanishi/about/column/stroke/",
    "/ichinomiyanishi/about/column/seminar_stroke/",
    "/ichinomiyanishi/about/column/knee-pain/",
    "/ichinomiyanishi/about/column/trigger-finger/",
    "/ichinomiyanishi/about/column/carpal-tunnel/",
    "/ichinomiyanishi/about/column/202310_fracture/",
    "/ichinomiyanishi/about/column/202312_fracture/",
    "/ichinomiyanishi/about/column/breast_reconstruction_1/",
    "/ichinomiyanishi/about/column/ptosis/",
    "/ichinomiyanishi/about/column/dizziness/",
    "/ichinomiyanishi/about/column/prostate-cancer/",
    "/ichinomiyanishi/about/column/psa-test/",
    "/ichinomiyanishi/about/column/seminar_prostate-cancer/",
    "/ichinomiyanishi/about/column/seminar_breast-cancer_1/",
    "/ichinomiyanishi/about/column/seminar_breast-cancer_2/",
    "/ichinomiyanishi/about/kenkouno_tsubo/",
    "/ichinomiyanishi/about/information/byoukininarumaenisitteokitai/",
    "/ichinomiyanishi/about/information/byoukininarumaenisitteokitaikoto/",
    "/ichinomiyanishi/about/information/syokunokoramu/",
    "/ichinomiyanishi/about/information/lowcarbsweets/",
    "/ichinomiyanishi/about/pr/media/",
    "/ichinomiyanishi/about/pr/press/",
    "/ichinomiyanishi/about/pr/movie/",
    # News
    "/ichinomiyanishi/breaking-news/index.html",
    "/ichinomiyanishi/news/index.html",
    "/ichinomiyanishi/breaking-news/20260401_meitetsu-bus/",
    "/ichinomiyanishi/news/job-festival2025-82076/",
    "/ichinomiyanishi/news/20260308_lightupingreen/",
    "/ichinomiyanishi/news/20260301_blueribbon/",
    # Seminar
    "/ichinomiyanishi/seminar/",
    "/ichinomiyanishi/seminar/open-seminar_2026/",
    "/ichinomiyanishi/seminar/open-seminar_2025/",
    "/ichinomiyanishi/seminar/open-seminar_2024/",
    # Recruitment
    "/ichinomiyanishi/resident/",
    "/ichinomiyanishi/resident/intern/",
    "/ichinomiyanishi/resident/intern/features",
    "/ichinomiyanishi/resident/intern/program-i",
    "/ichinomiyanishi/recruit/",
    "/ichinomiyanishi/nurse/",
    "/ichinomiyanishi/nurse/about/",
    "/ichinomiyanishi/nurse/education/",
    "/ichinomiyanishi/nurse/welfare/",
    "/ichinomiyanishi/nurse/recruit/",
    "/ichinomiyanishi/nurse/moreinfo/",
    "/ichinomiyanishi/nurse/moreinfo/interview/",
]

IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.ico', '.bmp', '.avif'}


def get_folder_name(page_path):
    """Convert URL path to folder name."""
    path = page_path.replace("/ichinomiyanishi/", "").strip("/")
    if not path:
        return "top"
    # Clean up for folder name
    path = path.replace("/", "_").replace("index.html", "").strip("_")
    return path or "top"


def extract_image_urls(html, page_url):
    """Extract all image URLs from HTML."""
    soup = BeautifulSoup(html, "html.parser")
    urls = set()

    # <img> tags
    for img in soup.find_all("img"):
        src = img.get("src") or img.get("data-src") or img.get("data-lazy-src")
        if src:
            full_url = urljoin(page_url, src)
            urls.add(full_url)
        # srcset
        srcset = img.get("srcset") or ""
        for part in srcset.split(","):
            part = part.strip().split(" ")[0]
            if part:
                urls.add(urljoin(page_url, part))

    # <source> tags (picture element)
    for source in soup.find_all("source"):
        srcset = source.get("srcset") or ""
        for part in srcset.split(","):
            part = part.strip().split(" ")[0]
            if part:
                urls.add(urljoin(page_url, part))

    # background-image in style attributes
    for tag in soup.find_all(style=True):
        style = tag["style"]
        bg_urls = re.findall(r'url\(["\']?(.*?)["\']?\)', style)
        for u in bg_urls:
            urls.add(urljoin(page_url, u))

    # <link rel="icon"> or <link rel="apple-touch-icon">
    for link in soup.find_all("link", rel=True):
        if any(r in link["rel"] for r in ["icon", "apple-touch-icon"]):
            href = link.get("href")
            if href:
                urls.add(urljoin(page_url, href))

    # Filter: only keep image URLs from anzu.or.jp
    filtered = set()
    for url in urls:
        parsed = urlparse(url)
        # Only anzu.or.jp images
        if "anzu.or.jp" not in parsed.netloc and parsed.netloc != "":
            continue
        # Check extension
        path_lower = parsed.path.lower()
        ext = os.path.splitext(path_lower)[1]
        if ext in IMAGE_EXTENSIONS:
            # Remove query string for cleaner URL but keep for download
            clean_url = url.split("?")[0]
            filtered.add(clean_url)

    return filtered


def download_image(url, folder_path):
    """Download a single image."""
    if url in downloaded_urls:
        return None

    try:
        resp = SESSION.get(url, timeout=15, stream=True)
        resp.raise_for_status()

        # Get filename from URL
        parsed = urlparse(url)
        filename = os.path.basename(unquote(parsed.path))
        if not filename:
            return None

        # Check content hash to avoid duplicates
        content = resp.content
        content_hash = hashlib.md5(content).hexdigest()
        if content_hash in downloaded_hashes:
            downloaded_urls.add(url)
            return None

        # Save
        filepath = folder_path / filename
        # Handle filename conflicts
        if filepath.exists():
            name, ext = os.path.splitext(filename)
            filepath = folder_path / f"{name}_{content_hash[:6]}{ext}"

        filepath.write_bytes(content)
        downloaded_urls.add(url)
        downloaded_hashes.add(content_hash)
        return str(filepath)

    except Exception as e:
        return None


def process_page(page_path):
    """Fetch a page and download all its images."""
    url = f"https://www.anzu.or.jp{page_path}"
    folder_name = get_folder_name(page_path)
    folder_path = OUTPUT_DIR / folder_name
    folder_path.mkdir(parents=True, exist_ok=True)

    try:
        resp = SESSION.get(url, timeout=20)
        resp.raise_for_status()
        image_urls = extract_image_urls(resp.text, url)

        count = 0
        for img_url in image_urls:
            result = download_image(img_url, folder_path)
            if result:
                count += 1

        # Remove empty folders
        if count == 0 and folder_path.exists() and not any(folder_path.iterdir()):
            folder_path.rmdir()

        return folder_name, count, len(image_urls)

    except Exception as e:
        return folder_name, 0, 0


def main():
    print(f"=== 一宮西病院 画像ダウンロード開始 ===")
    print(f"対象ページ数: {len(PAGES)}")
    print(f"保存先: {OUTPUT_DIR}")
    print()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    total_downloaded = 0
    total_found = 0

    for i, page in enumerate(PAGES, 1):
        folder, downloaded, found = process_page(page)
        total_downloaded += downloaded
        total_found += found
        if downloaded > 0:
            print(f"[{i:3d}/{len(PAGES)}] {folder}: {downloaded}/{found} images downloaded")
        elif i % 20 == 0:
            print(f"[{i:3d}/{len(PAGES)}] processing... (total: {total_downloaded} images)")
        # Be polite
        time.sleep(0.3)

    print()
    print(f"=== 完了 ===")
    print(f"総ページ数: {len(PAGES)}")
    print(f"発見画像数: {total_found}")
    print(f"ダウンロード数: {total_downloaded} (重複除外済み)")

    # Count folders
    folders = [f for f in OUTPUT_DIR.iterdir() if f.is_dir()]
    print(f"フォルダ数: {len(folders)}")

    # Summary per folder
    print()
    print("=== フォルダ別集計 ===")
    for folder in sorted(folders):
        files = list(folder.glob("*"))
        if files:
            print(f"  {folder.name}: {len(files)} files")


if __name__ == "__main__":
    main()
