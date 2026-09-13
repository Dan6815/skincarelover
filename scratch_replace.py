import re

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replacements for index.html
html = html.replace('Hilda Rose', 'Skincarelover')
html = html.replace('hilda rose', 'skincarelover')
html = html.replace('<span class="logo-mark">H</span>', '<span class="logo-mark">S</span>')
html = html.replace('Hilda <span class="accent-text">Rose</span>', 'Skincare<span class="accent-text">lover</span>')
html = html.replace('Hi, I\'m <span class="gradient-text glow-title">Hilda Asamoah</span>', 'Hi, I\'m <span class="gradient-text glow-title">Skincarelover</span>')
html = html.replace('Hilda is a passionate skincare', 'Skincarelover is a passionate skincare')
html = html.replace('Hilda creates authentic UGC', 'Skincarelover creates authentic UGC')
html = html.replace('Hilda\'s team will reach out', 'Skincarelover\'s team will reach out')
html = html.replace('Hilda\'s skincare unboxing', 'Skincarelover\'s skincare unboxing')
html = html.replace('Hilda\'s Holy Grail', 'Skincarelover\'s Holy Grail')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Successfully updated index.html')

# Replacements for style.css & script.js
for fname in ['style.css', 'script.js']:
    with open(fname, 'r', encoding='utf-8') as f:
        txt = f.read()
    txt = txt.replace('HILDA ROSE', 'SKINCARELOVER')
    txt = txt.replace('Hilda Rose', 'Skincarelover')
    txt = txt.replace('hilda rose', 'skincarelover')
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(txt)
    print(f'Successfully updated {fname}')
