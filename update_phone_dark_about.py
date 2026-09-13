import re

# ==============================================================================
# 1. UPDATE INDEX.HTML
# ==============================================================================
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add theme toggle button in navbar actions if not present
theme_btn_html = '''            <div class="nav-actions">
                <button class="theme-toggle" id="themeToggle" onclick="toggleTheme()" aria-label="Toggle light/dark mode" title="Toggle Light/Dark Mode">
                    <i class="fa-solid fa-moon"></i>
                </button>
                <button class="btn btn-primary btn-glow" onclick="openContactModal()">'''

if 'id="themeToggle"' not in html:
    html = html.replace('            <div class="nav-actions">\n                <button class="btn btn-primary btn-glow"', theme_btn_html)

# Add theme toggle link in mobile menu
mobile_theme_html = '''                <a href="#testimonials" class="nav-link">Reviews</a>
                <button class="mobile-theme-btn" onclick="toggleTheme()"><i class="fa-solid fa-moon"></i> Switch Theme</button>'''

if 'class="mobile-theme-btn"' not in html:
    html = html.replace('                <a href="#testimonials" class="nav-link">Reviews</a>', mobile_theme_html)

# Update About Me section heading & bio text
old_about_part = '''            <!-- About Content Side -->
            <div class="about-content">
                <div class="section-subtitle">
                    <span class="dash">—</span> About Me
                </div>
                <h2 class="section-title">
                    Who is <span class="gradient-text">Skincarelover?</span> ✨
                </h2>
                
                <p class="about-text">
                    Skincarelover is a passionate skincare and K-Beauty content creator known on TikTok as <strong>@skincarelover325</strong>. Known for her glowing skin routines, honest product reviews, and aesthetic short videos, she helps beauty lovers discover effective skincare solutions.
                </p>'''

new_about_part = '''            <!-- About Content Side -->
            <div class="about-content">
                <div class="section-subtitle">
                    <span class="dash">—</span> About Me
                </div>
                <h2 class="section-title">
                    Who is <span class="gradient-text">Hilda Asamoah?</span> ✨
                </h2>
                <div class="alias-pill"><i class="fa-solid fa-sparkles"></i> Also known as <strong>Skincarelover (@skincarelover325)</strong></div>
                
                <p class="about-text">
                    <strong>Hilda Asamoah</strong>, also known as <strong>Skincarelover (@skincarelover325)</strong>, is a passionate skincare and K-Beauty content creator known for her glowing skin routines, honest product reviews, and aesthetic short videos, helping beauty lovers discover effective skincare solutions.
                </p>'''

html = html.replace(old_about_part, new_about_part)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('index.html updated successfully!')


# ==============================================================================
# 2. UPDATE STYLE.CSS FOR DARK MODE & MOBILE OPTIMIZATIONS
# ==============================================================================
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

dark_mode_and_mobile_css = '''
/* ==========================================================================
   THEME TOGGLE BUTTON & DARK MODE SYSTEM
   ========================================================================== */
.theme-toggle {
    width: 44px;
    height: 44px;
    border-radius: 50%;
    background: var(--pink-soft);
    color: var(--pink-primary);
    border: 1px solid var(--border-light);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.15rem;
    cursor: pointer;
    transition: var(--transition);
}
.theme-toggle:hover {
    background: var(--pink-primary);
    color: var(--white);
    transform: rotate(15deg) scale(1.08);
}

.mobile-theme-btn {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 12px 18px;
    border-radius: 16px;
    background: var(--pink-soft);
    color: var(--pink-primary);
    font-weight: 700;
    font-size: 0.95rem;
    margin-top: 10px;
    cursor: pointer;
    border: 1px solid var(--border-light);
    width: 100%;
    justify-content: center;
}

.alias-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: var(--pink-soft);
    color: var(--pink-primary);
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 0.88rem;
    font-weight: 700;
    margin-bottom: 18px;
    border: 1px solid var(--border-light);
}

/* Dark Mode Theme Variables & Overrides */
[data-theme="dark"] {
    --pink-blush: #0a0208;
    --pink-subtle: #1a0416;
    --pink-soft: #2c0824;
    --dark-luxury: #ffffff;
    --dark-body: #f3e8f0;
    --text-muted: #c8b0c0;
    --white: #160312;
    --white-glass: rgba(28, 4, 23, 0.85);
    --border-light: rgba(255, 42, 109, 0.28);
    --border-hover: rgba(255, 42, 109, 0.65);
    --shadow-soft: 0 12px 36px rgba(0, 0, 0, 0.6);
    --shadow-hover: 0 24px 50px rgba(255, 42, 109, 0.4);
}

[data-theme="dark"] .navbar {
    background: rgba(16, 3, 14, 0.88);
    border-bottom-color: rgba(255, 42, 109, 0.2);
}
[data-theme="dark"] .glass-card {
    background: rgba(28, 4, 23, 0.78);
    border: 1px solid rgba(255, 42, 109, 0.28);
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.6);
}
[data-theme="dark"] .brands-section {
    background: #10020d;
}
[data-theme="dark"] .brand-item {
    background: #1b0416;
    color: #e6d4e2;
    border-color: rgba(255, 42, 109, 0.25);
}
[data-theme="dark"] .holy-grail-section {
    background: linear-gradient(180deg, #0a0208 0%, #160413 100%);
}
[data-theme="dark"] .theme-toggle {
    background: rgba(255, 42, 109, 0.25);
    color: #FFD700;
    border-color: rgba(255, 42, 109, 0.5);
}
[data-theme="dark"] .nav-link {
    color: #e6d4e2;
}
[data-theme="dark"] .nav-link:hover,
[data-theme="dark"] .nav-link.active {
    color: var(--pink-primary);
}
[data-theme="dark"] .footer {
    background: #060105;
}
[data-theme="dark"] .code-box {
    background: #0f020c;
}
[data-theme="dark"] .accordion-header {
    background: rgba(36, 5, 30, 0.6);
}
[data-theme="dark"] .accordion-item.active .accordion-header {
    background: rgba(255, 42, 109, 0.18);
}

/* Mobile & Small Screen Optimizations */
@media (max-width: 600px) {
    .container {
        padding: 0 16px;
    }
    .hero {
        padding-top: 100px;
    }
    .hero-title {
        font-size: 2.3rem;
        line-height: 1.15;
    }
    .hero-subtitle {
        font-size: 0.98rem;
    }
    .hero-arch-wrapper {
        width: 270px;
        height: 370px;
    }
    .tag-pill {
        font-size: 0.72rem;
        padding: 6px 12px;
    }
    .tag-unboxing { top: -15px; left: -10px; }
    .tag-1 { top: 30px; right: -10px; }
    .tag-2 { bottom: 80px; left: -10px; }
    .tag-3 { bottom: 20px; right: -10px; }
    .tag-4 { display: none; }
    .tag-5 { display: none; }

    .tiktok-stats-bar {
        grid-template-columns: repeat(3, 1fr);
        gap: 8px;
    }
    .t-stat-item {
        padding: 10px 6px;
    }
    .t-stat-num {
        font-size: 1.1rem;
    }
    .t-stat-lbl {
        font-size: 0.7rem;
    }

    .code-box {
        flex-direction: column;
        align-items: flex-start;
        gap: 10px;
    }
    .btn-copy {
        width: 100%;
        text-align: center;
    }

    .section-title {
        font-size: 1.85rem;
    }

    .reel-modal-card {
        padding: 16px;
        max-height: 92vh;
        overflow-y: auto;
    }
    .reel-video-frame {
        height: 420px;
    }

    .contact-form input,
    .contact-form select,
    .contact-form textarea {
        font-size: 16px; /* Prevents auto zoom on iOS */
    }

    .toast-notification {
        left: 16px;
        right: 16px;
        bottom: 20px;
        justify-content: center;
    }
}
'''

if '.theme-toggle' not in css:
    css += dark_mode_and_mobile_css
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print('style.css updated successfully!')


# ==============================================================================
# 3. UPDATE SCRIPT.JS FOR DARK MODE TOGGLE & PERSISTENCE
# ==============================================================================
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

js_theme_logic = '''
// --- DARK MODE THEME TOGGLE LOGIC ---
function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    
    updateThemeToggleIcon(newTheme);
    if (typeof showToast === 'function') {
        showToast(newTheme === 'dark' ? '🌙 Dark Mode Activated' : '☀️ Light Mode Activated');
    }
}

function updateThemeToggleIcon(theme) {
    const toggles = document.querySelectorAll('.theme-toggle i, .mobile-theme-btn i');
    toggles.forEach(icon => {
        if (theme === 'dark') {
            icon.className = 'fa-solid fa-sun';
        } else {
            icon.className = 'fa-solid fa-moon';
        }
    });
}

// Auto-initialize theme on load
(function initTheme() {
    const savedTheme = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    document.documentElement.setAttribute('data-theme', savedTheme);
    document.addEventListener('DOMContentLoaded', () => {
        updateThemeToggleIcon(savedTheme);
    });
})();
'''

if 'function toggleTheme()' not in js:
    js += js_theme_logic
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print('script.js updated successfully!')
