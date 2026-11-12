# -*- coding: utf-8 -*-
import json

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..100,500..800&family=Public+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">')

GROUPS = [
    ("Nos solutions", "/nos-solutions", [("/nos-solutions", "Toutes nos solutions"), ("/division-maison-logements", "Diviser une maison"),
                                        ("/division-terrain", "Diviser un terrain"), ("/succession-maison-familiale", "Succession")]),
    ("Propriétaires", "/valoriser-maison-familiale", []),
    ("Professionnels", None, [("/agents-immobiliers", "Agents immobiliers"), ("/notaires", "Notaires"),
                              ("/investisseurs", "Investisseurs"), ("/promoteurs", "Promoteurs")]),
    ("Méthode et engagements", "/notre-methode", [("/notre-methode", "Notre méthode"), ("/nos-engagements", "Nos engagements"),
                                                  ("/exemples-valorisation", "Exemples"), ("/equipe", "Qui sommes-nous ?")]),
    ("Conseils", "/blog/", []),
]


def _nav(cur):
    blog = cur.startswith("/blog/")
    desk, mob = "", ""
    for label, href, subs in GROUPS:
        active = cur == href or any(cur == h for h, _ in subs) or (href == "/blog/" and blog)
        ac = ' aria-current="page"' if active else ""
        if not subs:
            desk += f'<a href="{href}"{ac}>{label}</a>'
            mob += f'<a href="{href}"{ac}>{label}</a>'
            continue
        links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == cur else ""}>{t}</a>' for h, t in subs)
        head = f'<a href="{href}"{ac}>{label} <span aria-hidden="true">▾</span></a>' if href else f'<span class="ddl" tabindex="0"{ac}>{label} <span aria-hidden="true">▾</span></span>'
        desk += f'<div class="dd">{head}<div class="sub">{links}</div></div>'
        mob += f'<span class="grp">{label}</span>{links}'
    return desk, mob


WA = "https://wa.me/33756986700?text=Bonjour%2C%20je%20vous%20contacte%20depuis%20le%20site%20PLU%20Value."

ORG = {"@context": "https://schema.org", "@type": "Organization", "name": "PLU Value", "url": "https://plu-value.fr/",
       "email": "contact@plu-value.fr", "telephone": "+33756986700",
       "description": "Partenariat de valorisation immobilière : division de maisons en logements, division de terrains et création de lots.",
       "founder": [{"@type": "Person", "name": "Yannis Amallah"}, {"@type": "Person", "name": "Pierre-Henry Blanc"}],
       "parentOrganization": {"@type": "Organization", "name": "LATULIPE SAS"}}


def page(slug, title, desc, body, script="", extra_ld=None, og="website"):
    url = "https://plu-value.fr/" + ("" if slug == "" else slug)
    cur = "/" + slug
    nav_d, nav_m = _nav(cur)
    ld = [ORG] if slug == "" else []
    if extra_ld:
        ld += extra_ld if isinstance(extra_ld, list) else [extra_ld]
    ld_html = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="{og}">
<meta property="og:locale" content="fr_FR">
<meta property="og:image" content="https://plu-value.fr/media/maison-avant.webp">
<meta name="theme-color" content="#123D33">
{FONTS}
<link rel="stylesheet" href="/site.css">
{ld_html}
</head>
<body>
<div class="wrap">
  <header>
    <div class="top">
      <a class="brand" href="/" aria-label="PLU Value, accueil"><i aria-hidden="true"></i>PLU Value</a>
      <div class="top-actions">
        <a class="btn primary small" href="/deposer-un-bien">Faire étudier un bien</a>
        <details class="menu"><summary aria-label="Ouvrir le menu">Menu ☰</summary><nav aria-label="Navigation principale"><a href="/">Accueil</a>{nav_m}<hr><a href="/deposer-un-bien">Contact et dépôt d'un bien</a></nav></details>
      </div>
    </div>
    <nav class="desk" aria-label="Navigation principale">{nav_d}</nav>
  </header>
  <main>
{body}
  </main>
  <footer>
    <div class="cols">
      <div><b>PLU Value</b><span>Révélez le potentiel de votre patrimoine.</span><span>Une maison. Plusieurs possibilités. Un accompagnement complet.</span></div>
      <div><b>Plan du site</b><a href="/nos-solutions">Nos solutions</a><a href="/valoriser-maison-familiale">Propriétaires</a><a href="/agents-immobiliers">Agents immobiliers</a><a href="/notaires">Notaires</a><a href="/investisseurs">Investisseurs</a><a href="/promoteurs">Promoteurs</a><a href="/exemples-valorisation">Exemples</a><a href="/equipe">Qui sommes-nous ?</a><a href="/blog/">Conseils</a></div>
      <div><b>Contact</b><a href="mailto:contact@plu-value.fr">contact@plu-value.fr</a><a href="tel:+33756986700">07 56 98 67 00</a><a href="{WA}">WhatsApp</a><a href="/mentions-legales.html">Mentions légales</a><a href="/confidentialite.html">Politique de confidentialité</a></div>
    </div>
    <div>PLU Value est une marque exploitée par LATULIPE SAS, RCS Nîmes 921 470 951. Aucune donnée n'est revendue ni publiée.</div>
  </footer>
  <a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="Écrire sur WhatsApp">WhatsApp</a>
</div>
<script>
(function(){{
  document.querySelectorAll('.ba input').forEach(function(r){{var b=r.closest('.ba');function u(){{b.style.setProperty('--pos',r.value+'%')}}r.addEventListener('input',u);u()}});
}})();
</script>
{script}
</body>
</html>
"""


def ba_slider(before, after, alt_b, alt_a, lb="Aujourd'hui", la="Simulation"):
    return f"""<div class="ba">
      <img src="/media/{before}" alt="{alt_b}" width="439" height="439" loading="lazy">
      <img class="after" src="/media/{after}" alt="{alt_a}" width="439" height="439" loading="lazy">
      <span class="bar" aria-hidden="true"></span><span class="lbl l">{lb}</span><span class="lbl r">{la}</span>
      <input type="range" min="0" max="100" value="50" aria-label="Comparer avant et après : faites glisser">
    </div>"""


G = "var(--green)"
GD = "var(--gold)"

def _house(x, doors):
    d = "".join(f'<rect x="{x+dx}" y="150" width="20" height="36" rx="2" fill="none" stroke="{G}" stroke-width="2.5"/>' for dx in doors)
    return (f'<path d="M{x+20} 186 V96 L{x+110} 44 L{x+200} 96 V186 Z" fill="none" stroke="{G}" stroke-width="3" stroke-linejoin="round"/>'
            f'<rect x="{x+42}" y="108" width="28" height="24" fill="none" stroke="{G}" stroke-width="2.5"/><rect x="{x+150}" y="108" width="28" height="24" fill="none" stroke="{G}" stroke-width="2.5"/>' + d)

def _panel(title, inner):
    return f'<figure class="schema"><svg viewBox="0 0 240 210" role="img" aria-label="{title}"><line x1="6" y1="186" x2="234" y2="186" stroke="{G}" stroke-width="2" opacity=".35"/>{inner}</svg><figcaption>{title}</figcaption></figure>'

MAISON_BA = '<div class="pair">' + _panel("Aujourd'hui · une grande maison, un seul acheteur possible", _house(10, [96])) + \
    _panel("Possibilité étudiée · deux logements, deux entrées", _house(10, [62, 132]) + f'<line x1="120" y1="40" x2="120" y2="194" stroke="{GD}" stroke-width="3" stroke-dasharray="9 7"/><text x="64" y="80" font-size="13" fill="{G}" font-family="var(--body)" font-weight="700">A</text><text x="168" y="80" font-size="13" fill="{G}" font-family="var(--body)" font-weight="700">B</text>') + '</div>'

def _plot(split):
    out = (f'<rect x="20" y="14" width="200" height="164" fill="var(--green-soft)" stroke="{G}" stroke-width="3"/>'
           f'<rect x="20" y="178" width="200" height="18" fill="none" stroke="{G}" stroke-width="1.5" opacity=".4"/>'
           f'<text x="120" y="191" text-anchor="middle" font-size="10" fill="{G}" font-family="var(--body)">rue</text>'
           f'<rect x="50" y="118" width="70" height="44" fill="var(--sheet)" stroke="{G}" stroke-width="2.5"/>')
    if split:
        out += (f'<line x1="20" y1="92" x2="220" y2="92" stroke="{GD}" stroke-width="3" stroke-dasharray="9 7"/>'
                f'<rect x="140" y="96" width="12" height="82" fill="none" stroke="{GD}" stroke-width="2" stroke-dasharray="4 4"/>'
                f'<text x="120" y="56" text-anchor="middle" font-size="13" font-weight="700" fill="{G}" font-family="var(--body)">Lot à bâtir</text>'
                f'<text x="185" y="150" text-anchor="middle" font-size="11" fill="{G}" font-family="var(--body)">Maison</text>')
    else:
        out += f'<text x="120" y="60" text-anchor="middle" font-size="12" fill="{G}" font-family="var(--body)" opacity=".7">grand jardin</text>'
    return out

TERRAIN_PAIR = '<div class="pair">' + _panel("Aujourd'hui · une maison sur un grand terrain", _plot(False)) + \
    _panel("Possibilité étudiée · la maison garde son jardin, un lot à bâtir est détaché, avec son accès", _plot(True)) + '</div>'

SIM = '<p class="sim">Schéma de principe · chaque projet dépend du PLU, du bâtiment et des autorisations obtenues</p>'

TEAM = """<div class="team">
      <div class="person"><img src="/media/portrait-pierre-henry.webp" alt="Portrait de Me Pierre-Henry Blanc" width="150" height="150" loading="lazy"><span class="k">Associé · Urbanisme et juridique</span><b>Me Pierre-Henry Blanc</b><p>Avocat en droit de l'urbanisme depuis 30 ans, à l'origine de la méthode PLU Value. Il revoit chaque étude de faisabilité : règles du PLU, servitudes, autorisations, montage juridique.</p></div>
      <div class="person"><img src="/media/portrait-yannis.webp" alt="Portrait de Yannis Amallah" width="150" height="150" loading="lazy"><span class="k">Associé fondateur · Développement et opérations</span><b>Yannis Amallah</b><p>Entrepreneur, diplômé en commerce international. Il sélectionne les biens, coordonne géomètres, architectes et notaires, et pilote la préparation de la remise en vente avec les agences.</p></div>
    </div>"""

FINAL_CTA = """  <section class="dark" aria-labelledby="h-final">
    <h2 id="h-final">Et si votre propriété avait plus de potentiel que vous ne l'imaginiez ?</h2>
    <p>Présentez-nous votre bien. Nous étudions s'il correspond à nos critères et quelles solutions peuvent être envisagées. Réponse sous 72 heures une fois le dossier complet.</p>
    <div class="cta"><a class="btn gold" href="/deposer-un-bien">Présenter mon bien à PLU Value</a><a class="btn ghost" style="color:#F7F4EC;border-color:#F7F4EC" href="/nos-engagements">Comprendre nos engagements</a></div>
  </section>"""

PARTNER = """<p class="quote">Votre patrimoine. Notre investissement. Une valeur à créer ensemble.</p>"""


def faq_block(items, hid="h-faq", title="Questions fréquentes"):
    html = f'  <section aria-labelledby="{hid}">\n    <h2 id="{hid}">{title}</h2>\n    <div>\n'
    for q, a in items:
        html += f'      <details class="q"><summary>{q}</summary><p>{a}</p></details>\n'
    html += '    </div>\n  </section>\n'
    ld = {"@context": "https://schema.org", "@type": "FAQPage",
          "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}
    return html, ld
