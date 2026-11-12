import os, shutil
from pages2 import P, FORMS_JS
from base import page
import blog

OUT = 'out'
for f in os.listdir(OUT):
    if f.endswith('.html'): os.remove(os.path.join(OUT, f))
shutil.rmtree(OUT + '/blog', ignore_errors=True); os.makedirs(OUT + '/blog')

def write(slug, html):
    fp = OUT + '/' + ('index.html' if slug == '' else slug + 'index.html' if slug.endswith('/') else slug if slug.endswith('.html') else slug + '.html')
    open(fp, 'w', encoding='utf-8').write(html); print(f'{slug or "index":60s}{len(html)}')

for slug, v in P.items():
    write(slug, page(slug, v[0], v[1], v[2], v[4] if len(v) > 4 else "", v[3] if len(v) > 3 else None))
s, t, d, b = blog.PROMO
write(s, page(s, t, d, b, FORMS_JS))
for s, t, d, b in blog.LEGAL: write(s, page(s, t, d, b))
s, t, d, b, ld = blog.blog_index(); write(s, page(s, t, d, b, "", ld))
for a in blog.ARTICLES:
    s, t, d, b, ld = blog.article_page(a); write(s, page(s, t, d, b, "", ld, og="article"))

red = """/proprietaires  /valoriser-maison-familiale  301
/proprietaires.html  /valoriser-maison-familiale  301
/agents  /agents-immobiliers  301
/agents.html  /agents-immobiliers  301
/conseils  /blog/  301
/conseils/  /blog/  301
/blog.html  /blog/  301
/blog  /blog/  301
"""
open(OUT + '/_redirects', 'w').write(red)
open(OUT + '/robots.txt', 'w').write('User-agent: *\nAllow: /\nSitemap: https://plu-value.fr/sitemap.xml\n')
main = ['', 'nos-solutions', 'valoriser-maison-familiale', 'division-maison-logements', 'division-terrain', 'succession-maison-familiale', 'agents-immobiliers', 'notaires', 'investisseurs', 'promoteurs', 'notre-methode', 'nos-engagements', 'exemples-valorisation', 'equipe', 'deposer-un-bien', 'blog/']
x = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u in main: x += f'  <url><loc>https://plu-value.fr/{u}</loc><lastmod>2026-11-12</lastmod></url>\n'
for a in blog.ARTICLES: x += f'  <url><loc>https://plu-value.fr/blog/{a["slug"]}.html</loc><lastmod>{max(a["date"], "2026-11-12")}</lastmod></url>\n'
for u in ['mentions-legales.html', 'confidentialite.html']: x += f'  <url><loc>https://plu-value.fr/{u}</loc><lastmod>2026-11-12</lastmod></url>\n'
open(OUT + '/sitemap.xml', 'w').write(x + '</urlset>\n')
llms = """# PLU Value

> PLU Value, marque exploitée par LATULIPE SAS (RCS Nîmes 921 470 951) : partenariat de valorisation immobilière. Étude gratuite de ce que le PLU permet sur une maison ou un terrain (division de terrain, lot à bâtir, division d'une maison en logements). Pour les projets retenus, PLU Value finance les études et les démarches et partage avec le propriétaire la valeur créée au-dessus d'un prix de référence. PLU Value ne vend pas et ne publie pas d'annonces : la vente est confiée à une agence immobilière. Aucun résultat n'est garanti.

## Pour qui
- Propriétaires : maison devenue trop grande, grand terrain, succession, vente bloquée.
- Agents immobiliers : mandats qui ne se vendent pas ; l'agent garde son client et vend les lots (charte de non-contournement).
- Notaires : successions et indivisions portant sur un bien difficile à vendre en l'état.
- Investisseurs, marchands de biens, promoteurs : opérations et fonciers déjà étudiés.

## Pages clés
- [Accueil](https://plu-value.fr/)
- [Nos solutions](https://plu-value.fr/nos-solutions)
- [Diviser une maison en logements](https://plu-value.fr/division-maison-logements)
- [Division de terrain](https://plu-value.fr/division-terrain)
- [Succession et maison familiale](https://plu-value.fr/succession-maison-familiale)
- [Nos engagements](https://plu-value.fr/nos-engagements)
- [Faire étudier un bien](https://plu-value.fr/deposer-un-bien)

## Conseils
""" + "".join(f"- [{a['title']}](https://plu-value.fr/blog/{a['slug']}.html)\n" for a in blog.ARTICLES) + """
## Contact
- E-mail : contact@plu-value.fr
- Téléphone et WhatsApp : 07 56 98 67 00
- Instagram : @plu_value
"""
open(OUT + '/llms.txt', 'w').write(llms)
