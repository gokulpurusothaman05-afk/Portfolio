import os
import re

pages = ['index.html', 'work.html', 'about.html', 'services.html', 'blog.html', 'contact.html', '404.html', 'thank-you.html']

errors = []

for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Check all img src
    imgs = re.findall(r'<img[^>]+src="([^"]+)"', content)
    for src in imgs:
        if src.startswith('http') or src.startswith('data:'):
            continue
        clean_src = src.split('?')[0].split('#')[0]
        if not os.path.exists(clean_src):
            errors.append(f'{p}: Image not found on disk -> {clean_src}')

    # 2. Check all local a hrefs
    links = re.findall(r'<a[^>]+href="([^"]+)"', content)
    for href in links:
        if href.startswith('http') or href.startswith('mailto:') or href.startswith('tel:') or href.startswith('#'):
            continue
        clean_href = href.split('?')[0].split('#')[0]
        if not os.path.exists(clean_href):
            errors.append(f'{p}: Link target not found on disk -> {clean_href}')

    # 3. Check CSS links
    css_links = re.findall(r'<link[^>]+href="([^"]+)"', content)
    for href in css_links:
        if href.startswith('http'):
            continue
        clean_href = href.split('?')[0]
        if not os.path.exists(clean_href):
            errors.append(f'{p}: CSS file not found on disk -> {clean_href}')

    # 4. Check JS scripts
    scripts = re.findall(r'<script[^>]+src="([^"]+)"', content)
    for src in scripts:
        if src.startswith('http'):
            continue
        clean_src = src.split('?')[0]
        if not os.path.exists(clean_src):
            errors.append(f'{p}: Script file not found on disk -> {clean_src}')

print(f'Total validation errors: {len(errors)}')
for err in errors:
    print('  ERROR:', err)

if len(errors) == 0:
    print('SUCCESS: Every link, image, stylesheet, and script resolves with zero errors!')
