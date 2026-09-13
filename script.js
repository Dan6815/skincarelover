/* ==========================================================================
   SKINCARELOVER — INFLUENCER PORTFOLIO JAVASCRIPT (V3 Upgraded)
   Interactive 9:16 Reel Simulator, Toast System, Spotlight & ROI Calculator
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {

    // --- 1. MOUSE CURSOR SPOTLIGHT AURA ---
    const spotlight = document.getElementById('cursorSpotlight');
    if (spotlight && window.innerWidth > 768) {
        document.addEventListener('mousemove', (e) => {
            spotlight.style.left = `${e.clientX}px`;
            spotlight.style.top = `${e.clientY}px`;
        });
    }

    // --- 2. FLOATING SPARKLE PARTICLES GENERATOR ---
    const particlesContainer = document.getElementById('particlesBg');
    if (particlesContainer) {
        const particleCount = 20;
        for (let i = 0; i < particleCount; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            const size = Math.random() * 6 + 4;
            particle.style.width = `${size}px`;
            particle.style.height = `${size}px`;
            particle.style.left = `${Math.random() * 100}%`;
            particle.style.animationDuration = `${Math.random() * 10 + 8}s`;
            particle.style.animationDelay = `${Math.random() * 5}s`;
            particlesContainer.appendChild(particle);
        }
    }

    // --- 3. NAVBAR SCROLL GLASS EFFECT ---
    const navbar = document.getElementById('mainNavbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 40) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // --- 4. ACCORDION CONTROLLER ---
    const accordionItems = document.querySelectorAll('.accordion-item');
    accordionItems.forEach(item => {
        const header = item.querySelector('.accordion-header');
        const toggleBtn = item.querySelector('.accordion-toggle');

        header.addEventListener('click', () => {
            const isActive = item.classList.contains('active');

            accordionItems.forEach(otherItem => {
                otherItem.classList.remove('active');
                const otherBtn = otherItem.querySelector('.accordion-toggle');
                if (otherBtn) {
                    otherBtn.innerHTML = '<i class="fa-solid fa-plus"></i>';
                }
            });

            if (!isActive) {
                item.classList.add('active');
                if (toggleBtn) {
                    toggleBtn.innerHTML = '<i class="fa-solid fa-minus"></i>';
                }
            }
        });
    });

    // --- 5. GALLERY CATEGORY FILTER ---
    const tabBtns = document.querySelectorAll('.tab-btn');
    const galleryCards = document.querySelectorAll('.gallery-card');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            tabBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filter = btn.getAttribute('data-filter');

            galleryCards.forEach(card => {
                const category = card.getAttribute('data-category');
                if (filter === 'all' || category === filter) {
                    card.style.display = 'block';
                    card.style.opacity = '1';
                    card.style.transform = 'scale(1)';
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'scale(0.9)';
                    setTimeout(() => {
                        if (card.style.opacity === '0') {
                            card.style.display = 'none';
                        }
                    }, 300);
                }
            });
        });
    });

    // --- 6. STATS NUMBER COUNTER ANIMATION ---
    const statValues = document.querySelectorAll('.stat-val, .stat-number, .t-stat-num');
    let hasAnimated = false;

    function animateStats() {
        const statsSection = document.getElementById('about');
        if (!statsSection) return;

        const rect = statsSection.getBoundingClientRect();
        if (rect.top <= window.innerHeight * 0.85 && !hasAnimated) {
            hasAnimated = true;
            
            statValues.forEach(element => {
                const targetText = element.getAttribute('data-target');
                if (!targetText) return;

                const targetNum = parseFloat(targetText);
                const isDecimal = targetText.includes('.');
                const suffix = element.textContent.replace(/[\d\.]/g, '');
                
                let current = 0;
                const duration = 1800;
                const steps = 40;
                const increment = targetNum / steps;
                const stepTime = duration / steps;

                const timer = setInterval(() => {
                    current += increment;
                    if (current >= targetNum) {
                        current = targetNum;
                        clearInterval(timer);
                    }
                    element.textContent = (isDecimal ? current.toFixed(1) : Math.floor(current)) + suffix;
                }, stepTime);
            });
        }
    }

    window.addEventListener('scroll', animateStats);
    animateStats();

    // --- 7. MOBILE MENU TOGGLE ---
    const mobileToggle = document.getElementById('mobileToggle');
    const navMenu = document.getElementById('navMenu');

    if (mobileToggle && navMenu) {
        mobileToggle.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            const icon = mobileToggle.querySelector('i');
            if (navMenu.classList.contains('active')) {
                icon.className = 'fa-solid fa-xmark';
                document.body.style.overflow = 'hidden'; // Lock scroll
            } else {
                icon.className = 'fa-solid fa-bars-staggered';
                document.body.style.overflow = ''; // Unlock scroll
            }
        });

        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
                document.body.style.overflow = ''; // Unlock scroll
                if (mobileToggle.querySelector('i')) {
                    mobileToggle.querySelector('i').className = 'fa-solid fa-bars-staggered';
                }
            });
        });
    }

    // --- 8. HERO 3D TILT EFFECT ---
    const heroArch = document.getElementById('heroArchWrapper');
    if (heroArch && window.innerWidth > 992) {
        heroArch.addEventListener('mousemove', (e) => {
            const rect = heroArch.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;

            heroArch.style.transform = `rotateY(${x * 0.05}deg) rotateX(${-y * 0.05}deg) scale(1.02)`;
        });

        heroArch.addEventListener('mouseleave', () => {
            heroArch.style.transform = 'rotateY(0deg) rotateX(0deg) scale(1)';
        });
    }

    updateCampaignEstimate();
});

// --- 9. TOAST NOTIFICATION SYSTEM ---
function showToast(message) {
    const toast = document.getElementById('toastNotification');
    const toastMsg = document.getElementById('toastMsg');
    if (toast && toastMsg) {
        toastMsg.textContent = message;
        toast.classList.add('show');
        setTimeout(() => {
            toast.classList.remove('show');
        }, 3200);
    }
}

// --- 10. COPY AFFILIATE DISCOUNT CODE LOGIC ---
function copyDiscountCode(codeText, element) {
    if (navigator.clipboard) {
        navigator.clipboard.writeText(codeText).then(() => {
            showToast(`✨ Promo Code ${codeText} copied to clipboard!`);

            const btn = element ? (element.querySelector('.btn-copy') || element.querySelector('.btn-hg-copy')) : null;
            if (btn) {
                const originalText = btn.innerHTML;
                btn.innerHTML = '<i class="fa-solid fa-check"></i> Copied!';
                btn.style.background = '#27ae60';
                btn.style.color = '#fff';

                setTimeout(() => {
                    btn.innerHTML = originalText;
                    btn.style.background = '';
                    btn.style.color = '';
                }, 2000);
            }
        });
    }
}

// --- 11. INTERACTIVE 9:16 VIDEO REEL MODAL ---
let currentReelCode = '';

function openReelModal(title, brand, code, views, imageSrc) {
    const modal = document.getElementById('reelModal');
    const img = document.getElementById('reelModalImg');
    const titleEl = document.getElementById('reelModalTitle');
    const titleRight = document.getElementById('reelModalTitleRight');
    const brandEl = document.getElementById('reelModalBrand');
    const codeEl = document.getElementById('reelModalCode');
    const viewsEl = document.getElementById('reelModalViews');

    currentReelCode = code;

    if (img) img.src = imageSrc;
    if (titleEl) titleEl.textContent = title;
    if (titleRight) titleRight.textContent = title;
    if (brandEl) brandEl.textContent = brand;
    if (codeEl) codeEl.textContent = code;
    if (viewsEl) viewsEl.innerHTML = `<i class="fa-solid fa-eye"></i> ${views} Views`;

    if (modal) {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
}

function closeReelModal() {
    const modal = document.getElementById('reelModal');
    if (modal) {
        modal.classList.remove('active');
        document.body.style.overflow = 'auto';
    }
}

function toggleReelLike(btn) {
    if (!btn) return;
    const icon = btn.querySelector('i');
    const countSpan = btn.querySelector('span');
    if (icon) {
        if (icon.style.color === 'rgb(255, 42, 109)' || icon.style.color === '#ff2a6d') {
            icon.style.color = '';
            if (countSpan) countSpan.textContent = '14.2K';
        } else {
            icon.style.color = '#FF2A6D';
            if (countSpan) countSpan.textContent = '14.3K';
            showToast('❤️ Saved to favorites!');
        }
    }
}

function copyReelCode() {
    if (currentReelCode) {
        copyDiscountCode(currentReelCode, null);
    }
}

// --- 12. CAMPAIGN ROI CALCULATOR LOGIC ---
function updateCampaignEstimate() {
    const packageSelect = document.getElementById('calcPackage');
    const reachSlider = document.getElementById('reachSlider');
    const resImpressions = document.getElementById('resImpressions');
    const resEngagement = document.getElementById('resEngagement');

    if (!packageSelect || !reachSlider) return;

    const reachTier = parseInt(reachSlider.value, 10);
    const packageType = packageSelect.value;

    let baseImpressions = 50000;
    if (reachTier === 1) baseImpressions = 25000;
    if (reachTier === 2) baseImpressions = 50000;
    if (reachTier === 3) baseImpressions = 100000;
    if (reachTier === 4) baseImpressions = 250000;
    if (reachTier === 5) baseImpressions = 500000;

    let multiplier = 1.0;
    if (packageType === 'ugc-pack') multiplier = 2.2;
    if (packageType === 'ig-dedicated') multiplier = 1.5;
    if (packageType === 'multi-platform') multiplier = 3.4;
    if (packageType === 'ambassador') multiplier = 5.0;

    const totalImpressions = Math.round(baseImpressions * multiplier);
    const totalEngagement = Math.round(totalImpressions * 0.124); // 12.4% avg engagement

    if (resImpressions) {
        resImpressions.textContent = `${(totalImpressions / 1000).toFixed(0)}K+ Impressions`;
    }
    if (resEngagement) {
        resEngagement.textContent = `${(totalEngagement / 1000).toFixed(1)}K+ Interactions`;
    }
}

// --- 13. CONTACT MODAL LOGIC ---
function openContactModal() {
    const modal = document.getElementById('contactModal');
    if (modal) {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
}

function closeContactModal() {
    const modal = document.getElementById('contactModal');
    if (modal) {
        modal.classList.remove('active');
        document.body.style.overflow = 'auto';
    }
}

document.addEventListener('click', (e) => {
    const modal = document.getElementById('contactModal');
    const reelModal = document.getElementById('reelModal');
    if (e.target === modal) {
        closeContactModal();
    }
    if (e.target === reelModal) {
        closeReelModal();
    }
});

document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeContactModal();
        closeReelModal();
    }
});

function handleFormSubmit(event) {
    event.preventDefault();
    const btn = event.target.querySelector('button[type="submit"]');
    const originalText = btn.innerHTML;

    btn.disabled = true;
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Sending Request...';

    setTimeout(() => {
        btn.innerHTML = '<i class="fa-solid fa-check-circle"></i> Request Sent! ✨';
        btn.style.background = '#27ae60';

        showToast('✨ Partnership request sent to asamoahhilda21@gmail.com!');

        setTimeout(() => {
            closeContactModal();
            event.target.reset();
            btn.disabled = false;
            btn.innerHTML = originalText;
            btn.style.background = '';
        }, 1200);
    }, 1500);
}

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
