/**
 * STACKLY — DIGITAL PRODUCT & ENGINEERING STUDIO
 * High-End Animation & Interaction Engine
 * Inspired by Yuki Webflow Template Animation Specs
 */

document.addEventListener('DOMContentLoaded', () => {
  initHeaderScroll();
  initMenuDrawer();
  initProjectHover();
  initAccordions();
  initWorkFilters();
  initUniversal404();
  initFormRedirects();
});

/* --------------------------------------------------------------------------
   1. HEADER SCROLL STATE
   -------------------------------------------------------------------------- */
function initHeaderScroll() {
  const header = document.querySelector('.header');
  if (!header) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });
}

/* --------------------------------------------------------------------------
   2. FULLSCREEN SLIDE-DOWN DRAWER MENU
   -------------------------------------------------------------------------- */
function initMenuDrawer() {
  const toggleBtn = document.querySelector('.menu-toggle');
  const drawer = document.querySelector('.menu-drawer');
  const closeBtn = document.querySelector('.drawer-close-btn');
  const navLinks = document.querySelectorAll('.menu-drawer-item');

  if (!drawer) return;

  function toggleMenu() {
    const isOpen = drawer.classList.contains('is-active');
    if (isOpen) {
      closeMenu();
    } else {
      openMenu();
    }
  }

  function openMenu() {
    drawer.classList.add('is-active');
    if (toggleBtn) toggleBtn.classList.add('is-active');
    document.body.classList.add('menu-open');
    document.body.style.overflow = 'hidden';
  }

  function closeMenu() {
    drawer.classList.remove('is-active');
    if (toggleBtn) toggleBtn.classList.remove('is-active');
    document.body.classList.remove('menu-open');
    document.body.style.overflow = '';
  }

  if (toggleBtn) {
    toggleBtn.addEventListener('click', (e) => {
      e.preventDefault();
      toggleMenu();
    });
  }

  if (closeBtn) {
    closeBtn.addEventListener('click', (e) => {
      e.preventDefault();
      closeMenu();
    });
  }

  navLinks.forEach((link) => {
    link.addEventListener('click', () => {
      closeMenu();
    });
  });

  // ESC key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer.classList.contains('is-active')) {
      closeMenu();
    }
  });
}

/* --------------------------------------------------------------------------
   3. SIGNATURE PROJECT ROW HOVER (IMAGE RIBBON REVEAL)
   -------------------------------------------------------------------------- */
function initProjectHover() {
  const projectRows = document.querySelectorAll('.project-row');

  projectRows.forEach((row) => {
    const ribbon = row.querySelector('.project-hover-ribbon');
    if (!ribbon) return;

    row.addEventListener('mouseenter', () => {
      ribbon.style.opacity = '1';
    });

    row.addEventListener('mouseleave', () => {
      ribbon.style.opacity = '0';
    });
  });
}

/* --------------------------------------------------------------------------
   4. ACCORDION (FAQ / SERVICES CAPABILITIES)
   -------------------------------------------------------------------------- */
function initAccordions() {
  const headers = document.querySelectorAll('.accordion-header');

  headers.forEach((header) => {
    header.addEventListener('click', () => {
      const item = header.closest('.accordion-item');
      const body = item.querySelector('.accordion-body');
      const isOpen = item.classList.contains('active');

      // Close all others
      document.querySelectorAll('.accordion-item').forEach((other) => {
        if (other !== item) {
          other.classList.remove('active');
          const otherBody = other.querySelector('.accordion-body');
          if (otherBody) otherBody.style.maxHeight = null;
        }
      });

      if (!isOpen) {
        item.classList.add('active');
        body.style.maxHeight = body.scrollHeight + 'px';
      } else {
        item.classList.remove('active');
        body.style.maxHeight = null;
      }
    });
  });
}

/* --------------------------------------------------------------------------
   5. WORK PORTFOLIO CATEGORY FILTERS
   -------------------------------------------------------------------------- */
function initWorkFilters() {
  const filterBtns = document.querySelectorAll('.filter-pill');
  const projectCards = document.querySelectorAll('.project-row, .work-card');

  if (!filterBtns.length) return;

  filterBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      filterBtns.forEach((b) => b.classList.remove('selected'));
      btn.classList.add('selected');

      const filter = btn.getAttribute('data-filter') || 'all';

      projectCards.forEach((card) => {
        const category = card.getAttribute('data-category') || '';
        if (filter === 'all' || category.includes(filter)) {
          card.style.display = '';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

/* --------------------------------------------------------------------------
   6. UNIVERSAL 404 REDIRECTION FOR UNMAPPED LINKS & BUTTONS
   -------------------------------------------------------------------------- */
function initUniversal404() {
  const allLinks = document.querySelectorAll('a');
  allLinks.forEach((link) => {
    const href = link.getAttribute('href');
    if (!href || href === '#' || href === '' || href.startsWith('javascript:')) {
      link.setAttribute('href', '404.html');
    }
  });

  const buttons = document.querySelectorAll('button:not([type="submit"]):not(.menu-toggle):not(.accordion-header)');
  buttons.forEach((btn) => {
    if (!btn.hasAttribute('onclick') && !btn.closest('form') && !btn.classList.contains('filter-pill')) {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        window.location.href = '404.html';
      });
    }
  });
}

/* --------------------------------------------------------------------------
   7. UNIVERSAL FORM SUBMISSION REDIRECTION (THANK-YOU.HTML)
   -------------------------------------------------------------------------- */
function initFormRedirects() {
  const forms = document.querySelectorAll('form');
  forms.forEach((form) => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const submitBtn = form.querySelector('[type="submit"], button');
      if (submitBtn) {
        submitBtn.disabled = true;
        const originalText = submitBtn.textContent;
        submitBtn.textContent = 'Processing...';

        setTimeout(() => {
          window.location.href = 'thank-you.html';
        }, 500);
      } else {
        window.location.href = 'thank-you.html';
      }
    });
  });
}
