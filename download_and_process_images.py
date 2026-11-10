import os
import io
import urllib.request
from PIL import Image

IMAGES_DIR = os.path.abspath("images")

# 1. Map of filename -> Unsplash direct high-resolution image URL
PROJECT_IMAGES = {
    # Personal Author Avatar
    "author.webp": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800&q=80",
    
    # Hero Visual Displays
    "home-hero-03.webp": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1200&q=80",
    "home-hero-06.webp": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1200&q=80",
    
    # Project 1: FinTech Dashboard & Banking UI
    "project-01-preview-01.webp": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1200&q=80",
    "project-01-preview-02.webp": "https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=1200&q=80",
    
    # Project 2: E-commerce & Luxury Fashion UI
    "project-02-preview-01.webp": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=1200&q=80",
    "project-02-preview-02.webp": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1200&q=80",
    
    # Project 3: AI Platform & Developer SaaS
    "project-03-preview-01.webp": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200&q=80",
    "project-03-preview-02.webp": "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?w=1200&q=80",
    
    # Project 4: HealthTech & Telemedicine App
    "project-04-preview-01.webp": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=1200&q=80",
    "project-04-preview-02.webp": "https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=1200&q=80",
    
    # About Gallery: Studio, Sketching, Code, Architecture
    "about-01.webp": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1200&q=80",
    "about-02.webp": "https://images.unsplash.com/photo-1581291518857-4e27b48ff24e?w=1200&q=80",
    "about-03.webp": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=1200&q=80",
    "about-04.webp": "https://images.unsplash.com/photo-1497366216548-37526070297c?w=1200&q=80",
    
    # Blog Previews: Design Tokens, Motion, Frontend Architecture, Conversion
    "post-01-preview.webp": "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=1200&q=80",
    "post-02-preview.webp": "https://images.unsplash.com/photo-1634017839464-5c339ebe3cb4?w=1200&q=80",
    "post-03-preview.webp": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=1200&q=80",
    "post-04-preview.webp": "https://images.unsplash.com/photo-1551836022-d5d88e9218df?w=1200&q=80",
    
    # Services Showcase
    "home-services-01.webp": "https://images.unsplash.com/photo-1542744094-3a31f272c490?w=1200&q=80",
    "services-01.webp": "https://images.unsplash.com/photo-1542744094-3a31f272c490?w=1200&q=80",
    "home-services-02.webp": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=1200&q=80",
    "services-02.webp": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=1200&q=80",
    "home-services-03.webp": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1200&q=80",
    "services-03.webp": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1200&q=80",
    
    # Call to Action Banner
    "cta.webp": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1200&q=80",
}

# Protected files to NOT delete
KEEP_FILES = {
    "logo.webp",
    "logo.svg",
    "headline-footer.svg",
    "client-logo-01.svg",
    "client-logo-02.svg",
    "client-logo-03.svg",
    "client-logo-04.svg",
    "client-logo-05.svg",
    "client-logo-06.svg",
    "client-01.svg",
    "client-02.svg",
    "client-03.svg",
    "client-04.svg",
    "client-05.svg",
    "client-06.svg",
}

def clean_images_directory():
    print("--- 1. Cleaning images folder (preserving logos & svg vectors) ---")
    deleted_count = 0
    for filename in os.listdir(IMAGES_DIR):
        if filename in KEEP_FILES:
            print(f"  [PRESERVED] {filename}")
            continue
        file_path = os.path.join(IMAGES_DIR, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            deleted_count += 1
    print(f"Total old files removed: {deleted_count}")

def optimize_image_webp(img_bytes, max_dim=1200, target_max_kb=92):
    img = Image.open(io.BytesIO(img_bytes))
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    
    # Scale down if larger than max_dim
    w, h = img.size
    if max(w, h) > max_dim:
        scale = max_dim / max(w, h)
        img = img.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
    
    # Adaptive quality search to guarantee under target_max_kb (and under 100 KB)
    for quality in (82, 76, 70, 64, 58, 50, 42, 35):
        buf = io.BytesIO()
        img.save(buf, format="WEBP", quality=quality, method=6)
        size_kb = len(buf.getvalue()) / 1024
        if size_kb <= target_max_kb:
            return buf.getvalue(), size_kb, quality
            
    # Fallback scale reduction if quality reduction alone isn't enough
    w, h = img.size
    img = img.resize((int(w * 0.75), int(h * 0.75)), Image.Resampling.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="WEBP", quality=60, method=6)
    size_kb = len(buf.getvalue()) / 1024
    return buf.getvalue(), size_kb, 60

def download_and_save_all():
    print("\n--- 2. Downloading & Optimizing Project Images (< 100KB WebP) ---")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    # Cache downloaded bytes for duplicates (e.g. services-01 and home-services-01)
    url_cache = {}
    
    success_count = 0
    for filename, url in PROJECT_IMAGES.items():
        dest_path = os.path.join(IMAGES_DIR, filename)
        
        if url in url_cache:
            raw_bytes = url_cache[url]
        else:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=20) as resp:
                raw_bytes = resp.read()
            url_cache[url] = raw_bytes
            
        max_dim = 800 if filename == "author.webp" else 1200
        webp_bytes, size_kb, quality = optimize_image_webp(raw_bytes, max_dim=max_dim, target_max_kb=90)
        
        with open(dest_path, "wb") as f:
            f.write(webp_bytes)
            
        print(f"  [SAVED] {filename:<26} -> {size_kb:6.2f} KB (Q: {quality}) [Under 100KB: {size_kb < 100}]")
        assert size_kb < 100, f"Error: {filename} exceeded 100 KB ({size_kb} KB)"
        success_count += 1
        
    print(f"\nAll {success_count} project images saved successfully in WebP under 100 KB!")

if __name__ == "__main__":
    clean_images_directory()
    download_and_save_all()

