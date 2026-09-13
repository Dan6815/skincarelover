with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_about_block = '''                <h2 class="section-title">
                    Who is <span class="gradient-text">Hilda Asamoah?</span> ✨
                </h2>
                <div class="alias-pill"><i class="fa-solid fa-sparkles"></i> Also known as <strong>Skincarelover (@skincarelover325)</strong></div>
                
                <p class="about-text">
                    <strong>Hilda Asamoah</strong>, also known as <strong>Skincarelover (@skincarelover325)</strong>, is a passionate skincare and K-Beauty content creator known for her glowing skin routines, honest product reviews, and aesthetic short videos, helping beauty lovers discover effective skincare solutions.
                </p>

                <p class="about-text">
                    Partnering with major beauty platforms like <strong>YesStyle (Code: HILDA124E)</strong> and <strong>STYLEVANA (Code: SV15HILDA)</strong>, Skincarelover creates authentic UGC content that builds viewer confidence and drives direct product sales.
                </p>'''

new_about_block = '''                <h2 class="section-title">
                    Hi, I'm <span class="gradient-text">Hilda Asamoah!</span> ✨
                </h2>
                <div class="alias-pill"><i class="fa-solid fa-sparkles"></i> Also known as <strong>Skincarelover (@skincarelover325)</strong></div>
                
                <p class="about-text">
                    Hey there! I’m <strong>Hilda Asamoah</strong>, but you probably know me online as <strong>Skincarelover (@skincarelover325)</strong>. I’m truly obsessed with all things skincare and K-Beauty — from achieving that dream glass skin glow to testing viral barrier care routines. My goal is simple: share real, honest product reviews and aesthetic vlogs that help everyday beauty lovers feel confident in their own skin.
                </p>

                <p class="about-text">
                    Over the years, I’ve built a tight-knit community of skincare lovers who trust my authentic recommendations. Partnering with top global beauty platforms like <strong>YesStyle (Code: HILDA124E)</strong> and <strong>STYLEVANA (Code: SV15HILDA)</strong>, I create engaging short-form UGC videos that don't just look stunning — they educate, build community trust, and drive real campaign conversions for brands I genuinely love.
                </p>'''

if old_about_block in html:
    html = html.replace(old_about_block, new_about_block)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('index.html updated with first-person human bio!')
else:
    print('Target block not found, checking alternatives...')
