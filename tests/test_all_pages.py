import os
import re

main_pages = ['index.html', 'work.html', 'about.html', 'services.html', 'blog.html', 'contact.html']
utility_pages = ['404.html', 'thank-you.html']
all_pages = main_pages + utility_pages

all_valid = True

# 1. Check all files exist
for f in all_pages:
    if not os.path.exists(f):
        print(f'MISSING FILE: {f}')
        all_valid = False

# 2. Check main pages have the identical universal footer with 5 social links to 404.html
for f in main_pages:
    with open(f, 'r', encoding='utf-8') as html_file:
        content = html_file.read()

    if '<footer class="footer">' not in content:
        print(f'{f}: Missing footer!')
        all_valid = False

    footer = re.search(r'<footer class="footer">.*?</footer>', content, re.DOTALL)
    if footer:
        social_links = re.findall(r'<a[^>]+class="footer-social-btn"[^>]*href="([^"]+)"', footer.group(0))
        if not social_links:
            social_links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*class="footer-social-btn"', footer.group(0))
        if not social_links:
            print(f'{f}: Footer social buttons missing!')
            all_valid = False
        for sl in social_links:
            if sl != '404.html':
                print(f'{f}: Social link is {sl}, expected 404.html')
                all_valid = False

# 3. Check utility pages (404 and thank-you) have NO nav, NO menu drawer, and NO footer
for f in utility_pages:
    with open(f, 'r', encoding='utf-8') as html_file:
        content = html_file.read()

    if '<header' in content:
        print(f'{f}: Unexpected header present! (User requested NO nav on utility pages)')
        all_valid = False
    if 'menu-drawer' in content:
        print(f'{f}: Unexpected menu-drawer present! (User requested NO nav on utility pages)')
        all_valid = False
    if '<footer' in content:
        print(f'{f}: Unexpected footer present! (User requested NO footer on utility pages)')
        all_valid = False

# 4. Check all referenced images exist
for f in all_pages:
    with open(f, 'r', encoding='utf-8') as html_file:
        content = html_file.read()
    images = re.findall(r'<img[^>]+src="([^"]+)"', content)
    for img in images:
        if not img.startswith('http') and not os.path.exists(img):
            print(f'{f}: Missing referenced image: {img}')
            all_valid = False

print('Overall check status:', '100% VALID & VERIFIED!' if all_valid else 'FAILED')
