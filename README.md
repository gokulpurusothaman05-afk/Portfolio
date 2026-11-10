# STACKLY — Personal Portfolio

High-fidelity **personal portfolio** engineered in pure HTML5, CSS3, and modern JavaScript, capturing the authentic visual language, layout, and animation specifications of the **Yuki Template** (`https://yuki-template.webflow.io/`), customized for **Stackly** (Independent Digital Designer & Creative Developer based in India).

---

## 🎨 Personal Portfolio Architecture (Matching Yuki)

1. **Personal Identity & First-Person Voice:**
   - **Creator:** `Stackly` — Independent Digital Designer & Creative Developer
   - **Base:** Bengaluru & Mumbai, India &bull; Available worldwide
   - **Author Portrait:** Authentically displays [`images/author.webp`](images/author.webp) across the hero bar and the [About Me](about.html) page.

2. **Yuki Page Structure & Sections:**
   - **Hero:** Giant horizontal typography (`STACKLY`), circular portrait avatar, personal bio statement, and explore button.
   - **Client Logo Marquee:** Infinite continuous ticker ribbon with partner marks (Zerodha, Razorpay, Swiggy, Flipkart, Cred, Tata Digital).
   - **( About ):** *"Welcome! I’m Stackly, a dedicated independent specialist in Logo & Branding, Web Design, and Web Development based in Bengaluru & Mumbai, India..."*
   - **( What I do ):** (01) Logo & Branding, (02) Web & UI/UX Design, (03) Web Development.
   - **( Selected Work ):** Interactive project list featuring the signature Yuki **hover image strip reveal** (Pixel Perfect, Brand Fusion, Web Vision, Infinite Design).
   - **( How I work ):** 4-step creative process (Concept & Discovery, Design & Prototyping, Development, Launch & Support).
   - **( Testimonial ):** Quote from Akira Tanaka (ZenTech Innovations).
   - **( Work With Me ):** Editorial CTA banner leading directly to the contact page.

3. **5 Navigation Items (Desktop & Fullscreen Drawer):**
   - `(01) Work` &rarr; [`work.html`](work.html)
   - `(02) About` &rarr; [`about.html`](about.html)
   - `(03) Services` &rarr; [`services.html`](services.html)
   - `(04) Blog` &rarr; [`blog.html`](blog.html)
   - `(05) Contact` &rarr; [`contact.html`](contact.html)

4. **Identical Universal Footer on All Pages:**
   - Giant vector headline mark: [`images/headline-footer.svg`](images/headline-footer.svg) (`STACKLY`)
   - Personal branding: `© Made by Stackly • Personal Digital Portfolio, India`
   - **5 Footer Social Media Buttons** (`.footer-social-btn` for LinkedIn, Twitter/X, Instagram, GitHub, Dribbble) all redirecting to [`404.html`](404.html)
   - 3 Column links: `(Pages)`, `(CMS)`, `(Utility Pages)`
   - Working newsletter subscription form routing to [`thank-you.html`](thank-you.html)

5. **Signature Animations:**
   - **Text-Flip Buttons (`.btn-flip`):** Dual stacked text sliding upward on hover.
   - **Hover Image Ribbon (`.project-hover-ribbon`):** Gliding horizontal ribbon of screenshots appearing on project row hover.
   - **Slide-Down Menu Drawer (`.menu-drawer`):** Hamburger morphs into an X and triggers a full-screen blurred backdrop.
   - **Desktop Custom Magnetic Cursor:** Glowing dot and smooth trailing follower ring.

6. **Separately Written Media Queries (320px to 4K Displays):**
   - In [`css/style.css`](css/style.css), media queries are written explicitly across 9 screen ranges (320px, 375px, 480px, 576px, 768px, 1024px, 1200px, 1440px, 1441px+).

7. **Universal Redirection & Safety:**
   - All unmapped buttons, placeholder links, and footer social links route to [`404.html`](404.html).
   - All forms submit and route to [`thank-you.html`](thank-you.html).

---

## 📁 Directory Structure

```
Portfolio/
├── 404.html                 # Stylized 404 Error page
├── about.html               # Personal About Me page with author portrait
├── blog.html                # Personal Journal & Articles
├── contact.html             # Personal inquiry form with budget selector
├── index.html               # Personal portfolio homepage
├── services.html            # Services & "What I do" offerings
├── thank-you.html           # Message received confirmation
├── work.html                # Selected Work archive with filters
├── css/
│   └── style.css            # Responsive styles & Yuki animations
├── js/
│   └── main.js              # Interactive animations engine
├── fonts/                   # General Sans & Zodiak WOFF fonts
├── images/                  # Photography, author portrait, and SVGs
└── tests/                   # Automated validation test suite
```

---

## 💻 Local Preview

Open [`index.html`](index.html) in any browser, or run:
```bash
python -m http.server 8000
```
Visit `http://localhost:8000`.
