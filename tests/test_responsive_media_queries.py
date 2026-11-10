import os
import glob
import re

SCREEN_FILES = [
    'css/screens/screen-320px.css',
    'css/screens/screen-375px.css',
    'css/screens/screen-480px.css',
    'css/screens/screen-576px.css',
    'css/screens/screen-768px.css',
    'css/screens/screen-1024px.css',
    'css/screens/screen-1200px.css',
    'css/screens/screen-1440px.css',
    'css/screens/screen-wide.css',
    'css/screens/all-screens.css'
]

HTML_FILES = [
    'index.html',
    'work.html',
    'about.html',
    'services.html',
    'blog.html',
    'contact.html',
    '404.html',
    'thank-you.html'
]

REQUIRED_320_CLASSES = [
    'html', 'body', '.container', '.header', '.header-logo', '.menu-toggle',
    '.menu-drawer', '.menu-drawer-item', '.hero-title-giant', '.hero-desc',
    '.project-row-content', '.project-name', '.award-row', '.services-grid',
    '.process-grid', '.cta-box', '.footer-grid', '.footer-right',
    '.footer-newsletter-wrap', '.footer-newsletter-form', '.footer-social-btn',
    '.pricing-grid', '.matrix-grid', '.testimonials-grid', '.status-pill-grid',
    '.resources-grid', '.timeline-track', '.accordion-header',
    '.home-section-grid', '.work-spotlight-card', '.work-spotlight-metrics',
    '.work-archive-grid', '.about-profile-grid', '.about-gallery-grid',
    '.services-tools-grid', '.blog-featured-card', '.blog-posts-grid',
    '.blog-guides-grid', '.contact-layout-grid', '.utility-destinations-grid',
    '.utility-highlights-grid'
]

errors = 0

print("=== 1. CHECKING SCREEN CSS FILES EXISTENCE ===")
for fpath in SCREEN_FILES:
    if os.path.exists(fpath):
        size = os.path.getsize(fpath)
        print(f"  [OK] {fpath} exists ({size} bytes)")
    else:
        print(f"  [FAIL] Missing {fpath}")
        errors += 1

print("\n=== 2. CHECKING 320PX SCREEN COMPREHENSIVE COVERAGE ===")
with open('css/screens/screen-320px.css', 'r', encoding='utf-8') as f:
    css_320_content = f.read()

for cls in REQUIRED_320_CLASSES:
    if cls in css_320_content:
        print(f"  [OK] 320px coverage for {cls}")
    else:
        print(f"  [FAIL] Missing 320px styling for {cls}")
        errors += 1

print("\n=== 3. CHECKING HTML FILES LINK SEPARATE SCREEN CSS ===")
for html_page in HTML_FILES:
    with open(html_page, 'r', encoding='utf-8') as f:
        html = f.read()
    
    missing_links = []
    for screen_css in SCREEN_FILES[:9]: # first 9 screen files
        if screen_css not in html:
            missing_links.append(screen_css)
            
    if not missing_links:
        print(f"  [OK] {html_page} links all 9 separate screen media query stylesheets!")
    else:
        print(f"  [FAIL] {html_page} missing links: {missing_links}")
        errors += 1

print(f"\n==========================================")
print(f"TOTAL VALIDATION ERRORS: {errors}")
if errors == 0:
    print("ALL RESPONSIVE MEDIA QUERY TESTS PASSED PERFECTLY!")
else:
    print("SOME TESTS FAILED. PLEASE REVIEW.")

