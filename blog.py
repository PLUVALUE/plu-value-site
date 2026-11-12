# -*- coding: utf-8 -*-
"""Blog, pages légales et page promoteurs du site PLU Value (v4)."""
import re, html as H
from base import WA

MOIS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']


def fdate(d):
    y, m, dd = d.split('-')
    return f"{int(dd)}{'er' if int(dd) == 1 else ''} {MOIS[int(m) - 1]} {y}"


CTA = f"""<aside class="help" aria-label="Faire étudier un bien">
      <h2>Votre bien a peut-être plus de potentiel que vous ne le pensez</h2>
      <p>PLU Value étudie gratuitement ce que votre maison ou votre terrain permet. Pour les projets que nous retenons, nous finançons les études et les démarches, et nous partageons avec vous la valeur créée au-dessus d'un prix de référence fixé ensemble. Aucun résultat n'est garanti : chaque bien est étudié au cas par cas.</p>
      <div class="cta"><a class="btn gold" href="/deposer-un-bien">Faire étudier mon bien</a><a class="btn ghost" href="{WA}" target="_blank" rel="noopener">Écrire sur WhatsApp</a></div>
    </aside>"""

ARTICLES = []

# ---------------------------------------------------------------- articles d'origine (7 octobre), remis au positionnement actuel
ARTICLES.append(dict(
    slug="diviser-son-terrain-plu", date="2026-10-07", cat="Urbanisme · Division", read="7 min",
    title="Diviser son terrain : ce que le PLU autorise vraiment",
    desc="Division de terrain : zones du PLU, accès, emprise au sol, déclaration préalable ou permis d'aménager. Les règles à vérifier avant de vendre un lot à bâtir.",
    body="""
<p class="answer">Un grand jardin peut cacher un deuxième lot constructible. Mais diviser un terrain ne dépend ni de la surface seule ni de l'envie du propriétaire : c'est le plan local d'urbanisme (PLU) de la commune qui fixe ce qui est possible. Voici les points que nous vérifions à chaque étude.</p>

<h2>1. Dans quelle zone du PLU se trouve la parcelle ?</h2>
<p>Chaque parcelle est classée dans une zone : zones urbaines (U), zones à urbaniser (AU), zones agricoles (A) ou naturelles (N). Une division en vue de construire n'a de sens qu'en zone U, ou en zone AU ouverte à l'urbanisation. Le règlement de la zone, souvent découpé en sous-secteurs (UA, UB, UC…), contient les règles qui décident de tout le reste.</p>
<p>On consulte le zonage sur le <a href="https://www.geoportail-urbanisme.gouv.fr/" rel="noopener">Géoportail de l'urbanisme</a> ou en mairie, puis on lit le règlement écrit de la zone concernée.</p>

<h2>2. Les règles qui comptent pour créer un lot</h2>
<ul>
<li><strong>L'accès</strong> : le futur lot doit être desservi par une voie ou un passage. Beaucoup de PLU imposent une largeur minimale d'accès, et un lot « en drapeau » derrière la maison n'est possible que si cette largeur existe sur le côté.</li>
<li><strong>L'emprise au sol</strong> : la part maximale du terrain qui peut être couverte par des constructions. Après division, la maison existante doit encore respecter cette règle sur son nouveau lot, plus petit.</li>
<li><strong>La pleine terre et les espaces verts</strong> : de nombreux PLU imposent une part minimale de terrain non bâti et non imperméabilisé.</li>
<li><strong>L'implantation</strong> : les distances à respecter par rapport à la rue et aux limites séparatives réduisent la zone réellement constructible.</li>
<li><strong>La hauteur et le stationnement</strong> : nombre de places exigé par logement, hauteur maximale, qui conditionnent le type de maison réalisable.</li>
<li><strong>Les servitudes et les risques</strong> : plan de prévention des risques (inondation, mouvements de terrain), périmètre de monument historique, emplacements réservés. Ils peuvent rendre un projet impossible ou allonger son instruction.</li>
</ul>

<h2>3. Déclaration préalable ou permis d'aménager ?</h2>
<p>Une division en vue de construire relève en principe d'une <strong>déclaration préalable</strong>. Elle passe à un <strong>permis d'aménager</strong> lorsque le projet crée des voies, des espaces ou des équipements communs à plusieurs lots, ou lorsqu'il se situe dans certains périmètres protégés. Le délai d'instruction de droit commun est d'un mois pour une déclaration préalable et de trois mois pour un permis d'aménager, sauf majoration.</p>
<p>Avant même de déposer, un <strong>certificat d'urbanisme opérationnel</strong> permet d'interroger la mairie sur la faisabilité d'un projet précis et de figer les règles applicables pendant 18 mois.</p>

<h2>4. Le rôle du géomètre-expert</h2>
<p>Le géomètre établit le plan de division, procède au bornage et prépare le document qui crée les nouvelles parcelles au cadastre. C'est lui qui transforme une intuition (« il y a la place pour une maison ») en lots réels, aux surfaces exactes.</p>

<h2>5. Ce qu'on ne voit pas sur une annonce</h2>
<p>Deux terrains de même surface peuvent avoir des potentiels très différents : largeur de façade, position de la maison existante, pente, arbres protégés, réseaux disponibles. C'est pour cela qu'une étude au cas par cas reste indispensable avant de parler de prix.</p>
<p>Pour la suite des démarches, voir <a href="/blog/etapes-division-parcellaire.html">Division parcellaire : les étapes, du premier avis au lot vendu</a>.</p>
"""))

ARTICLES.append(dict(
    slug="maison-qui-ne-se-vend-pas", date="2026-10-07", cat="Vendre · Propriétaires", read="6 min",
    title="Maison qui ne se vend pas : les raisons fréquentes et les solutions",
    desc="Votre maison reste en vente depuis des mois ? Prix global trop élevé, surface inadaptée, trop de terrain : les causes fréquentes et les solutions, dont la division.",
    body="""
<p class="answer">Les visites s'enchaînent, les retours sont polis, mais personne ne signe. Le prix baisse une fois, deux fois. Quand une maison reste en vitrine pendant des mois, le problème n'est pas toujours le prix au mètre carré : c'est souvent le bien lui-même qui ne correspond plus au budget des acheteurs du quartier.</p>

<h2>Les causes que l'on rencontre le plus souvent</h2>
<h3>Un montant total trop élevé</h3>
<p>Une grande maison peut être affichée à un prix au m² raisonnable et rester hors de portée, simplement parce que le montant total dépasse ce que les ménages du secteur peuvent emprunter. Les familles achètent dans une fourchette de budget ; au-dessus, les acheteurs se raréfient.</p>
<h3>Trop de terrain</h3>
<p>Un très grand jardin plaît en photo, mais il a un coût (entretien, taxe foncière) et pèse sur le prix. Beaucoup d'acheteurs ne veulent pas payer des mètres carrés qu'ils n'utiliseront pas.</p>
<h3>Une surface ou une configuration atypique</h3>
<p>Maison trop grande, plusieurs niveaux, dépendances sans autorisation claire, gros travaux à prévoir : chaque particularité réduit le nombre d'acheteurs capables de se projeter et d'obtenir leur prêt.</p>
<h3>Des diagnostics ou une situation administrative qui inquiètent</h3>
<p>Un DPE défavorable, une extension non déclarée, une servitude mal comprise : autant de points qui font reculer un acheteur ou sa banque au dernier moment.</p>

<h2>Baisser le prix n'est pas la seule option</h2>
<p>La réponse classique consiste à réduire le prix jusqu'à trouver preneur. Elle coûte directement au vendeur. Avant d'en arriver là, il vaut la peine de se demander si le bien ne pourrait pas être <strong>présenté autrement</strong> :</p>
<ul>
<li><strong>Diviser le terrain</strong> pour vendre d'un côté une maison avec un jardin plus raisonnable, de l'autre un terrain à bâtir. Deux biens à des budgets plus accessibles touchent deux publics différents. Voir <a href="/division-terrain">la division de terrain</a>.</li>
<li><strong>Découper une grande maison</strong> en plusieurs logements quand le PLU et la configuration le permettent. Voir <a href="/division-maison-logements">la division de maison</a>.</li>
<li><strong>Régulariser</strong> une dépendance ou une extension pour lever un doute qui bloque les acheteurs.</li>
</ul>
<p>Ces solutions demandent une étude d'urbanisme, un géomètre, parfois un architecte, et des autorisations. C'est ce qui décourage la plupart des propriétaires.</p>

<h2>Ce que propose PLU Value</h2>
<p>Nous étudions gratuitement le potentiel de votre bien au regard du PLU. Si une valorisation est possible et que nous retenons le projet, nous vous proposons un <strong>partenariat de valorisation</strong> : vous restez propriétaire, nous finançons et pilotons les études et les démarches, et la valeur créée est partagée selon un contrat écrit. Si votre agent immobilier vous accompagne, il reste dans la boucle et garde son mandat.</p>
<p>Si vous cherchez plutôt à vendre vite, lisez aussi <a href="/blog/vendre-une-partie-de-son-terrain-maison-trop-grande.html">Maison devenue trop grande : peut-on vendre une partie de son terrain ?</a></p>
"""))

ARTICLES.append(dict(
    slug="contrat-de-valorisation-immobiliere", date="2026-10-07", cat="Notre modèle · Valorisation", read="6 min",
    title="Contrat de valorisation immobilière : rester propriétaire et partager la valeur créée", seo="Contrat de valorisation immobilière : comment ça marche",
    desc="Le contrat de valorisation permet à un propriétaire de rester maître de son bien pendant qu'un opérateur finance et pilote division, autorisations et démarches. Fonctionnement et points de vigilance.",
    body="""
<p class="answer">Entre « vendre en l'état » et « tout faire soi-même », il existe une troisième voie : confier la valorisation de son bien à un opérateur qui en assume le coût et le pilotage, tout en restant propriétaire jusqu'à la vente. C'est le principe du contrat de valorisation proposé par PLU Value.</p>

<h2>Le principe</h2>
<p>Le propriétaire conserve son bien. PLU Value étudie ce que le PLU permet (division, création d'un lot, découpe en logements), puis <strong>finance et pilote</strong> les démarches : géomètre, architecte si nécessaire, conseil juridique, dépôt des autorisations. Une fois les autorisations obtenues, le bien est vendu, en un ou plusieurs lots, par l'agence choisie avec le propriétaire. La valeur créée au-delà d'un prix de référence fixé ensemble au départ est partagée selon les conditions du contrat.</p>

<h2>Les étapes</h2>
<ol>
<li><strong>Analyse du bien</strong> : parcelle, zone du PLU, contraintes, marché local.</li>
<li><strong>Avis du comité</strong> : nous ne nous engageons que si nous pensons pouvoir réellement créer de la valeur. Nous n'avons aucun intérêt à engager des dépenses dans un projet qui ne fonctionne pas.</li>
<li><strong>Proposition écrite</strong> : prix de référence, répartition, calendrier, frais pris en charge, sortie si les autorisations sont refusées.</li>
<li><strong>Démarches</strong> : plan de division, dossiers d'urbanisme, purge des recours.</li>
<li><strong>Vente</strong> : par une agence immobilière, de préférence celle qui suit déjà le bien et qui garde ses mandats. PLU Value ne vend pas et ne publie pas d'annonces.</li>
</ol>

<h2>Pour qui ?</h2>
<ul>
<li>Le propriétaire qui ne veut pas brader un bien qui ne trouve pas preneur.</li>
<li>Les héritiers qui veulent vendre dans de bonnes conditions sans avancer de frais. Voir <a href="/succession-maison-familiale">succession et maison familiale</a>.</li>
<li>L'agent immobilier dont le mandat stagne et qui cherche une solution concrète à proposer à son vendeur.</li>
</ul>

<h2>Les points de vigilance</h2>
<p>Un contrat de valorisation se lit attentivement, de préférence avec son notaire : définition du prix de référence, durée, ce qui se passe si l'autorisation d'urbanisme est refusée, répartition des frais, conditions de sortie. Aucune plus-value n'est garantie : elle dépend des règles d'urbanisme et du marché au moment de la vente.</p>

<h2>Et si le vendeur préfère vendre ?</h2>
<p>Dans certains cas, une promesse d'achat peut être étudiée, directement ou par un investisseur partenaire. Elle est toujours assortie de conditions suspensives, notamment l'obtention des autorisations d'urbanisme. Le détail de ce que nous nous engageons à faire, et à ne pas faire, figure dans <a href="/nos-engagements">nos engagements</a>.</p>
"""))

ARTICLES.append(dict(
    slug="agent-immobilier-mandat-qui-stagne", date="2026-10-07", cat="Agents · Partenariat", read="5 min",
    title="Agents immobiliers : comment débloquer un mandat qui stagne",
    desc="Mandat en vente depuis des mois, vendeur qui refuse de baisser : une solution de valorisation par le PLU pour débloquer la vente, en gardant votre client et vos mandats.",
    body="""
<p class="answer">Tout agent connaît ce mandat : un bien trop grand ou trop cher au total, des visites sans suite, un vendeur qui ne veut pas entendre parler d'une nouvelle baisse. Le temps passe, l'annonce s'use, et la relation avec le vendeur se tend.</p>

<h2>Pourquoi certains biens bloquent</h2>
<p>Ce n'est pas toujours une question de prix au m². Grandes maisons, grands terrains, propriétés avec dépendances : leur <strong>montant total</strong> les sort du budget de la majorité des acheteurs du secteur. Le bien est bien placé, mais il n'est pas adapté à la demande.</p>

<h2>Changer le bien plutôt que le prix</h2>
<p>Quand le PLU le permet, un même bien peut devenir deux biens plus faciles à vendre : une maison avec un jardin raisonnable et un terrain à bâtir, ou plusieurs logements. Deux produits, deux budgets accessibles, deux publics d'acheteurs.</p>

<h2>Ce que PLU Value apporte à l'agent</h2>
<ul>
<li><strong>Une étude gratuite</strong> du potentiel du bien, à présenter à votre vendeur.</li>
<li><strong>Le financement et le pilotage</strong> des démarches (géomètre, autorisations) pour les projets retenus, sans frais avancés par le vendeur.</li>
<li><strong>Vos intérêts protégés</strong> : vous gardez votre client, et c'est vous qui vendez les lots créés. Nous vous transmettons les plans et les documents techniques ; nous ne publions pas d'annonces.</li>
<li><strong>Une charte de non-contournement</strong> : nous ne contactons jamais votre vendeur sans vous.</li>
</ul>

<h2>Comment ça se passe</h2>
<ol>
<li>Vous déposez le bien en quelques minutes, sous charte de confidentialité.</li>
<li>Nous analysons le bien et les règles du PLU.</li>
<li>Notre comité étudie la faisabilité.</li>
<li>Nous vous répondons : si nous pouvons apporter de la valeur, nous vous disons si nous nous engageons, et à quelles conditions.</li>
</ol>
<p>Le détail du partenariat est sur la page <a href="/agents-immobiliers">agents immobiliers</a>. Pour déposer un mandat : <a href="/deposer-un-bien?profil=agent">dépôt d'un bien par un agent</a>.</p>
"""))

ARTICLES.append(dict(
    slug="etapes-division-parcellaire", date="2026-10-07", cat="Urbanisme · Méthode", read="6 min",
    title="Division parcellaire : les étapes, du premier avis au lot vendu",
    desc="Les étapes d'une division parcellaire : étude du PLU, certificat d'urbanisme, géomètre, déclaration préalable ou permis d'aménager, purge des recours, viabilisation et vente.",
    body="""
<p class="answer">Diviser une parcelle pour créer un terrain à bâtir suit un enchaînement assez précis. Connaître les étapes permet d'anticiper les délais et d'éviter les mauvaises surprises au moment de vendre.</p>

<h2>1. L'étude préalable</h2>
<p>Lecture du règlement du PLU de la zone, vérification de l'accès, des servitudes, des risques, des réseaux disponibles. C'est à ce stade qu'on sait si un lot est envisageable et quelle maison pourrait y être construite. Voir <a href="/blog/diviser-son-terrain-plu.html">ce que le PLU autorise vraiment</a>.</p>

<h2>2. Le certificat d'urbanisme opérationnel (facultatif mais utile)</h2>
<p>Il interroge la mairie sur un projet précis et fige les règles d'urbanisme applicables pendant 18 mois. Il sécurise la suite, notamment si le PLU venait à être modifié.</p>

<h2>3. Le plan de division et le bornage</h2>
<p>Le géomètre-expert mesure, propose le découpage, borne les limites et prépare les documents qui serviront au dossier d'urbanisme, puis au cadastre.</p>

<h2>4. L'autorisation d'urbanisme</h2>
<p>En principe une <strong>déclaration préalable</strong> (instruction d'un mois en droit commun), ou un <strong>permis d'aménager</strong> si le projet crée des voies ou des espaces communs, ou se trouve dans certains secteurs protégés (trois mois en droit commun). Les délais peuvent être majorés, par exemple en périmètre de monument historique.</p>

<h2>5. L'affichage et la purge des recours</h2>
<p>L'autorisation doit être affichée sur le terrain. Les tiers disposent de deux mois à compter du premier jour d'affichage continu pour former un recours. Une fois ce délai passé sans recours, l'autorisation est dite « purgée » : c'est ce qui rassure les acheteurs et leurs banques.</p>

<h2>6. Le document d'arpentage et la viabilisation</h2>
<p>Le géomètre fait enregistrer les nouvelles parcelles au cadastre. Selon le cas, le lot est viabilisé (raccordements à l'eau, à l'électricité, à l'assainissement) avant la vente, ou l'acquéreur s'en charge.</p>

<h2>7. La vente</h2>
<p>Le terrain à bâtir et la maison existante peuvent être vendus séparément, à des acheteurs différents : deux biens adaptés à la demande plutôt qu'un seul qui ne trouve pas preneur.</p>
<p>Chaque étape a un coût et un délai. Dans le cadre d'un <a href="/blog/contrat-de-valorisation-immobiliere.html">contrat de valorisation</a>, PLU Value finance et pilote ces étapes pour les projets qu'elle retient ; la vente est confiée à une agence immobilière.</p>
"""))


# ---------------------------------------------------------------- brouillons SEO (27/10, 03/11, 10/11) repris tels quels, sans l'ancien encadré d'offre
def _draft(folder, slug, date, cat, read, kind, fallback_desc=None):
    s = open(f'drafts/{folder}/index.html', encoding='utf-8').read()
    title = H.unescape(re.search(r'<h1>(.*?)</h1>', s, re.S).group(1))
    m = re.search(r'<meta name="description" content="(.*?)">', s)
    desc = H.unescape(m.group(1)) if m else fallback_desc
    if kind == 'article':
        body = re.search(r'<article>(.*?)</article>', s, re.S).group(1)
    else:
        body = re.search(r'</h1>(.*?)</main>', s, re.S).group(1)
    body = re.sub(r'<h1>.*?</h1>', '', body, count=1, flags=re.S)
    body = re.sub(r'<p class="meta">.*?</p>', '', body, count=1, flags=re.S)
    body, n = re.subn(r'<aside class="help".*?</aside>|<div class="aide">.*?</div>', '', body, flags=re.S)
    assert n == 1, (folder, n)
    body = body.replace('https://plu-value.fr/#deposer', '/deposer-un-bien').replace('https://plu-value.fr/', '/')
    assert '20 km' not in body and '18 mois, le vendeur' not in body and 'Zéro frais' not in body, folder
    ARTICLES.append(dict(slug=slug, date=date, cat=cat, read=read, title=title, desc=desc, body=body))


_draft('champigny', 'diviser-son-terrain-champigny-sur-marne', '2026-10-27', 'Par commune · Champigny-sur-Marne', '8 min', 'article',
       "Zone UP, bande de 20 m, emprise 40 %, retraits : ce que le PLU de Champigny-sur-Marne impose pour diviser un terrain, et les démarches à suivre.")
_draft('densification', 'densification-douce-pavillonnaire-commune', '2026-11-03', 'Communes · Urbanisme', '7 min', 'main')
_draft('vendre', 'vendre-une-partie-de-son-terrain-maison-trop-grande', '2026-11-10', 'Propriétaires · Maison trop grande', '8 min', 'article')

SEO = {'densification-douce-pavillonnaire-commune': 'Densification douce du pavillonnaire : le rôle de la commune', 'vendre-une-partie-de-son-terrain-maison-trop-grande': 'Vendre une partie de son terrain : maison trop grande ?', 'diviser-son-terrain-champigny-sur-marne': 'Diviser son terrain à Champigny-sur-Marne : le PLU'}
for a in ARTICLES:
    if a['slug'] in SEO: a['seo'] = SEO[a['slug']]
ARTICLES.sort(key=lambda a: a['date'], reverse=True)

ORG_LD = {"@type": "Organization", "name": "PLU Value", "url": "https://plu-value.fr/"}


def article_page(a):
    """Renvoie (slug, title, desc, body, ld) pour base.page()."""
    path = f"blog/{a['slug']}.html"
    url = "https://plu-value.fr/" + path
    others = [o for o in ARTICLES if o is not a][:3]
    cards = "".join(f'<a class="card" href="/blog/{o["slug"]}.html"><span class="k">{o["cat"]}</span><h3>{o["title"]}</h3><em>Lire l\'article →</em></a>' for o in others)
    body = f"""  <nav class="crumbs" aria-label="Fil d'Ariane"><a href="/">Accueil</a> › <a href="/blog/">Conseils</a> › {a['cat'].split(' · ')[-1]}</nav>
  <article class="post">
    <span class="eyebrow">{a['cat']}</span>
    <h1>{a['title']}</h1>
    <p class="meta">Publié le {fdate(a['date'])} · {a['read']} de lecture · PLU Value</p>
{a['body']}
    {CTA}
  </article>
  <section aria-labelledby="h-lire"><h2 id="h-lire">À lire aussi</h2><div class="postlist">{cards}</div></section>"""
    ld = [{"@context": "https://schema.org", "@type": "Article", "headline": a['title'], "description": a['desc'], "datePublished": a['date'],
           "dateModified": a['date'], "inLanguage": "fr-FR", "author": ORG_LD, "publisher": ORG_LD, "mainEntityOfPage": url},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://plu-value.fr/"},
              {"@type": "ListItem", "position": 2, "name": "Conseils", "item": "https://plu-value.fr/blog/"},
              {"@type": "ListItem", "position": 3, "name": a['title'], "item": url}]}]
    faq = re.findall(r'<details[^>]*><summary>(.*?)</summary>\s*<p>(.*?)</p></details>', a['body'], re.S)
    if faq:
        strip = lambda t: H.unescape(re.sub(r'<[^>]+>', '', t)).strip()
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(r)}} for q, r in faq]})
    t = a.get('seo') or (a['title'] if len(a['title']) > 48 else a['title'] + " | PLU Value")
    return path, t, a['desc'], body, ld


def blog_index():
    cards = "".join(f'<a class="card" href="/blog/{a["slug"]}.html"><span class="k">{a["cat"]}</span><h2>{a["title"]}</h2><p>{a["desc"]}</p>'
                    f'<span class="hint">{fdate(a["date"])} · {a["read"]} de lecture</span></a>' for a in ARTICLES)
    body = f"""  <section aria-labelledby="h1">
    <span class="eyebrow">Conseils</span>
    <h1 id="h1">Division, PLU et maisons difficiles à vendre</h1>
    <p class="lead">Ce que le PLU permet vraiment, comment débloquer une vente, comment fonctionne un partenariat de valorisation. Des guides sourcés, pour les propriétaires, les agents immobiliers et les communes.</p>
    <div class="postlist">{cards}</div>
  </section>
  <section class="dark" aria-labelledby="h-b"><h2 id="h-b">Une question sur votre bien ?</h2><p>Présentez-le nous : l'étude préalable est gratuite.</p><div class="cta"><a class="btn gold" href="/deposer-un-bien">Faire étudier mon bien</a></div></section>"""
    ld = {"@context": "https://schema.org", "@type": "Blog", "name": "Conseils PLU Value", "url": "https://plu-value.fr/blog/",
          "blogPost": [{"@type": "BlogPosting", "headline": a['title'], "url": f"https://plu-value.fr/blog/{a['slug']}.html", "datePublished": a['date']} for a in ARTICLES]}
    return ("blog/", "Conseils : division de terrain, PLU, vente bloquée | PLU Value",
            "Guides pratiques et sourcés sur la division de terrain, la division de maison, le PLU et les biens qui ne trouvent pas preneur.", body, ld)


# ---------------------------------------------------------------- pages légales
MAJ = "12 novembre 2026"
ML = f"""  <article class="post">
    <span class="eyebrow">Informations légales</span>
    <h1>Mentions légales</h1>
    <p class="meta">Dernière mise à jour : {MAJ}</p>
    <h2>Éditeur du site</h2>
    <p>Le site plu-value.fr est édité par <strong>LATULIPE</strong>, société par actions simplifiée au capital de 1 000 €, dont le siège est situé 81 impasse de la Tulipe, 30900 Nîmes, immatriculée au RCS de Nîmes sous le numéro 921 470 951. PLU Value est une marque exploitée par LATULIPE SAS.</p>
    <p>Contact : <a href="mailto:contact@plu-value.fr">contact@plu-value.fr</a> · 07 56 98 67 00</p>
    <h2>Directeur de la publication</h2>
    <p>Rattarin Dowling, président de LATULIPE SAS.</p>
    <h2>Hébergement</h2>
    <p>Netlify, Inc., 101 2nd Street, San Francisco, CA 94105, États-Unis, <a href="https://www.netlify.com" rel="noopener">www.netlify.com</a>.</p>
    <h2>Activité</h2>
    <p>PLU Value étudie le potentiel d'urbanisme de biens immobiliers et propose des partenariats de valorisation. Les analyses publiées ou transmises sont indicatives : elles ne constituent ni une offre d'achat, ni un engagement, ni un conseil juridique, fiscal ou financier. Toute opération fait l'objet d'un accord écrit distinct, assorti de conditions suspensives.</p>
    <p>PLU Value n'exerce pas l'activité d'agent immobilier : elle ne vend pas de biens, ne publie pas d'annonces et ne perçoit pas d'honoraires de transaction. Les biens confiés par des professionnels le sont dans le respect de leurs mandats et de la <a href="/deposer-un-bien?profil=agent">charte de confidentialité et de non-contournement</a>.</p>
    <h2>Propriété intellectuelle</h2>
    <p>L'ensemble des contenus du site (textes, visuels, schémas, logo, charte) est la propriété de l'éditeur, sauf mention contraire. Toute reproduction ou réutilisation sans autorisation écrite est interdite.</p>
    <h2>Responsabilité</h2>
    <p>L'éditeur s'efforce de fournir des informations exactes et à jour, notamment sur les règles d'urbanisme, mais ne peut garantir leur exhaustivité : les règles applicables dépendent du PLU en vigueur dans chaque commune et de la situation précise de chaque parcelle. Les schémas du site sont des schémas de principe.</p>
    <h2>Données personnelles</h2>
    <p>Voir notre <a href="/confidentialite.html">politique de confidentialité</a>.</p>
    <h2>Droit applicable</h2>
    <p>Le présent site est soumis au droit français.</p>
  </article>"""

PC = f"""  <article class="post">
    <span class="eyebrow">Données personnelles</span>
    <h1>Politique de confidentialité</h1>
    <p class="meta">Dernière mise à jour : {MAJ}</p>
    <p>Cette politique explique quelles données nous collectons via plu-value.fr et nos échanges par e-mail et WhatsApp, pourquoi, et quels sont vos droits au titre du Règlement général sur la protection des données (RGPD) et de la loi Informatique et Libertés.</p>
    <h2>Responsable du traitement</h2>
    <p>LATULIPE SAS, exploitant la marque PLU Value, 81 impasse de la Tulipe, 30900 Nîmes, RCS Nîmes 921 470 951. Contact : <a href="mailto:contact@plu-value.fr">contact@plu-value.fr</a>.</p>
    <h2>Données collectées</h2>
    <ul>
      <li><strong>Formulaires du site</strong> (dépôt d'un bien, demande d'étude, transmission par un notaire, critères d'investisseur ou de promoteur) : nom, société ou agence, téléphone, e-mail, numéro de carte professionnelle pour les agents ; informations sur le bien (adresse, surfaces, prix, historique de commercialisation) ; documents transmis (photos, diagnostics, plans).</li>
      <li><strong>Échanges</strong> : contenu de vos e-mails et de vos messages WhatsApp.</li>
      <li><strong>Prospection professionnelle</strong> : nom, structure et coordonnées professionnelles publiquement accessibles des professionnels de l'immobilier et des études notariales que nous contactons.</li>
    </ul>
    <p>Nous ne demandons aucune donnée sensible. Ne transmettez pas de données personnelles de vos clients au-delà de ce qui est nécessaire à l'étude du bien.</p>
    <h2>Finalités et bases légales</h2>
    <ul>
      <li>Étudier le bien présenté et vous répondre : mesures précontractuelles prises à votre demande.</li>
      <li>Assurer le suivi d'un partenariat ou d'une opération et respecter la charte de non-contournement : exécution du contrat.</li>
      <li>Contacter des professionnels pour leur présenter notre activité : intérêt légitime, avec possibilité de s'opposer à tout moment (réponse « STOP »).</li>
    </ul>
    <h2>Destinataires</h2>
    <p>Les données sont accessibles uniquement à l'équipe PLU Value et à nos prestataires techniques, dans la limite de leurs missions : Netlify (hébergement du site et réception des formulaires), Titan (messagerie), Make (automatisation des échanges), Google (tableurs de suivi), WhatsApp (messagerie instantanée), ainsi que des outils d'analyse assistée par intelligence artificielle utilisés pour préparer nos études. Certains prestataires sont situés hors de l'Union européenne, notamment aux États-Unis ; les transferts sont encadrés par les garanties prévues par le RGPD.</p>
    <p>Nous ne vendons ni ne louons vos données. Nous ne contactons jamais un vendeur confié par un agent sans l'accord de celui-ci.</p>
    <h2>Durées de conservation</h2>
    <ul>
      <li>Dossiers de biens et échanges associés : 3 ans après le dernier contact, ou la durée de l'opération augmentée des délais de prescription légaux si une opération est réalisée.</li>
      <li>Données de prospection : 3 ans après le dernier contact, ou jusqu'à votre opposition.</li>
    </ul>
    <h2>Cookies et mesure d'audience</h2>
    <p>Le site ne dépose ni cookies publicitaires ni cookies de mesure d'audience. Les polices de caractères sont chargées depuis Google Fonts, ce qui transmet techniquement votre adresse IP à Google.</p>
    <h2>Vos droits</h2>
    <p>Vous disposez d'un droit d'accès, de rectification, d'effacement, de limitation, d'opposition et de portabilité de vos données. Pour les exercer, écrivez à <a href="mailto:contact@plu-value.fr">contact@plu-value.fr</a>. Vous pouvez aussi introduire une réclamation auprès de la CNIL (<a href="https://www.cnil.fr" rel="noopener">www.cnil.fr</a>).</p>
  </article>"""

LEGAL = [("mentions-legales.html", "Mentions légales | PLU Value", "Mentions légales du site plu-value.fr : éditeur, hébergeur, activité, propriété intellectuelle.", ML),
         ("confidentialite.html", "Politique de confidentialité | PLU Value", "Données collectées par PLU Value, finalités, destinataires, durées de conservation et droits RGPD.", PC)]

# ---------------------------------------------------------------- promoteurs
PROMO_FORM = """<form name="criteres-promoteur" method="POST" data-netlify="true" netlify-honeypot="site-web" data-simple data-ok="ok-promo" novalidate>
      <input type="hidden" name="form-name" value="criteres-promoteur">
      <p class="hp"><label>Ne pas remplir <input name="site-web" tabindex="-1" autocomplete="off"></label></p>
      <div class="row two"><div class="f"><label for="p-nom">Nom *</label><input id="p-nom" name="nom" required autocomplete="name"></div><div class="f"><label for="p-soc">Société *</label><input id="p-soc" name="societe" required autocomplete="organization"></div></div>
      <div class="row two"><div class="f"><label for="p-email">E-mail *</label><input id="p-email" name="email" type="email" required autocomplete="email"></div><div class="f"><label for="p-tel">Téléphone</label><input id="p-tel" name="telephone" type="tel" autocomplete="tel"></div></div>
      <div class="f"><label for="p-zone">Communes ou secteurs recherchés *</label><input id="p-zone" name="zones" required></div>
      <div class="f"><span id="p-type-l" style="font-weight:600">Types d'opération</span>
        <div class="chips" role="group" aria-labelledby="p-type-l">
          <label><input type="checkbox" name="type-operation" value="maisons individuelles">Maisons individuelles</label>
          <label><input type="checkbox" name="type-operation" value="petit collectif">Petit collectif</label>
          <label><input type="checkbox" name="type-operation" value="lots à bâtir">Lots à bâtir</label>
          <label><input type="checkbox" name="type-operation" value="résidence gérée">Résidence gérée</label>
        </div></div>
      <div class="row two"><div class="f"><label for="p-min">Surface de plancher minimale (m²)</label><input id="p-min" name="sdp-min" type="number" min="0"></div><div class="f"><label for="p-max">Surface de plancher maximale (m²)</label><input id="p-max" name="sdp-max" type="number" min="0"></div></div>
      <div class="f"><label for="p-msg">Précisions</label><textarea id="p-msg" name="message"></textarea></div>
      <label class="check"><input type="checkbox" name="accord" value="oui" required><span>J'accepte d'être recontacté par PLU Value au sujet de fonciers. *</span></label>
      <p class="err" role="alert" hidden></p><div><button class="btn primary" type="submit">Envoyer mes critères</button></div>
    </form>
    <div class="okbox" id="ok-promo" hidden tabindex="-1" role="status"><b>Critères bien reçus.</b><p>Nous vous présenterons les fonciers qui correspondent.</p></div>"""

PROMO = ("promoteurs", "Promoteurs et constructeurs : fonciers étudiés | PLU Value",
         "Promoteurs et constructeurs : PLU Value vous présente des fonciers dont l'urbanisme a été étudié, avec des vendeurs informés. Indiquez vos critères.",
         f"""  <section aria-labelledby="h1">
    <span class="eyebrow">Promoteurs · Constructeurs</span>
    <h1 id="h1">Des fonciers étudiés avant de vous être présentés.</h1>
    <p class="lead">Nous repérons des terrains et des propriétés sous-exploités, nous vérifions ce que le PLU permet, et nous vous présentons ceux qui correspondent à vos critères.</p>
    <div class="cta"><a class="btn primary" href="#criteres">Indiquer mes critères</a><a class="btn ghost" href="/notre-methode">Notre méthode</a></div>
    <figure class="shot"><img src="/media/site-promoteurs.webp" alt="Plan de masse d'un terrain avec plusieurs lots à bâtir" width="1536" height="864"></figure>
  </section>
  <section aria-labelledby="h-a">
    <h2 id="h-a">Ce que contient un dossier</h2>
    <div class="grid3">
      <div class="card"><span class="k">Le foncier</span><ul><li>Adresse, parcelles, surfaces</li><li>Zone du PLU, règles d'implantation et de hauteur</li><li>Servitudes et risques connus</li></ul></div>
      <div class="card"><span class="k">Le cadre</span><ul><li>Analyse d'urbanisme revue par Me Pierre-Henry Blanc, avocat en urbanisme</li><li>Un vendeur informé, qui a accepté l'étude</li></ul></div>
      <div class="card"><span class="k">Le montage</span><ul><li>Promesse sous conditions suspensives, dont l'obtention des autorisations</li><li>Conditions convenues par écrit, dossier par dossier</li></ul></div>
    </div>
    <p class="note">Nous ne présentons un foncier qu'après l'avoir étudié. Chaque projet reste soumis au PLU en vigueur et aux autorisations obtenues.</p>
  </section>
  <section id="criteres" aria-labelledby="h-f"><h2 id="h-f">Indiquer vos critères</h2>{PROMO_FORM}</section>""")
