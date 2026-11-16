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

# ---------------------------------------------------------------- 12/11/2026
ARTICLES.append(dict(
    slug="diviser-une-maison-en-plusieurs-logements", date="2026-11-12", cat="Urbanisme · Division de maison", read="8 min",
    title="Diviser une maison en plusieurs logements : règles et démarches",
    seo="Diviser une maison en plusieurs logements : les règles",
    desc="Autorisations d'urbanisme, surface minimale de 14 m², PLU, stationnement, mise en copropriété : ce qu'il faut vérifier avant de diviser une maison en logements.",
    body="""
<p class="answer">Oui, une grande maison peut souvent devenir deux ou trois logements, mais trois filtres décident : le PLU de la commune, le Code de la construction (chaque logement créé doit faire au moins 14 m² et 33 m³ et avoir ses propres équipements) et, si les logements sont vendus séparément, la mise en copropriété. L'ordre compte : on vérifie les règles avant de dessiner les lots, pas après.</p>

<h2>Pourquoi diviser une maison plutôt que la vendre entière ?</h2>
<p>Parce que beaucoup de grandes maisons ne correspondent plus à ceux qui les habitent, ni au budget de ceux qui cherchent. Selon l'Insee, un quart des ménages vivent dans une résidence principale en sous-occupation très accentuée, et 79 % de ces logements sont occupés par une ou deux personnes (recensement 2022, Insee Première n° 2064).</p>
<p>Une maison de sept pièces trouve peu d'acheteurs à son prix. Deux logements plus petits s'adressent à des budgets plus courants. Ce n'est pas vrai partout, ni pour toutes les maisons : c'est ce que l'étude doit établir. Voir aussi <a href="/blog/maison-qui-ne-se-vend-pas.html">Maison qui ne se vend pas : les raisons fréquentes et les solutions</a>.</p>

<h2>Faut-il une autorisation d'urbanisme ?</h2>
<p>Pas toujours pour la division elle-même, mais souvent pour les travaux qu'elle demande. Le ministère de la Justice le résume ainsi : diviser un bâtiment en lots ne donne pas forcément lieu à une formalité d'urbanisme ; ce sont les travaux qui peuvent exiger une déclaration préalable ou un permis de construire, par exemple quand un changement de destination s'accompagne de travaux sur la structure ou la façade.</p>
<p>En pratique, créer une seconde entrée, ouvrir une fenêtre ou aménager des combles touche presque toujours à l'aspect extérieur ou à la surface. Demandez à la mairie quelle autorisation s'applique à votre projet avant de commencer.</p>
<div class="table">
  <table>
    <thead><tr><th>Autorisation</th><th>Délai d'instruction de droit commun</th><th>Source</th></tr></thead>
    <tbody>
      <tr><td>Déclaration préalable</td><td>1 mois</td><td>Code de l'urbanisme, art. R*423-23</td></tr>
      <tr><td>Permis de construire, maison individuelle</td><td>2 mois</td><td>service-public.gouv.fr</td></tr>
      <tr><td>Permis de construire, autres projets</td><td>3 mois</td><td>service-public.gouv.fr</td></tr>
    </tbody>
  </table>
</div>
<p>Ces délais courent à partir d'un dossier complet et sont allongés en secteur protégé.</p>

<h2>Que dit le PLU de votre commune ?</h2>
<p>C'est le premier filtre, et il change d'une commune à l'autre. Trois points sont à lire dans le règlement de votre zone :</p>
<ul>
  <li><strong>Le stationnement.</strong> Beaucoup de règlements exigent des places par logement. Un logement de plus peut donc demander une place de plus sur le terrain. C'est le blocage le plus fréquent sur une petite parcelle.</li>
  <li><strong>La taille minimale des logements.</strong> Le Code de l'urbanisme (art. L151-14) permet au PLU de délimiter des secteurs où les programmes doivent comporter une proportion de logements d'une taille minimale.</li>
  <li><strong>L'autorisation préalable de division.</strong> Dans ces secteurs, la commune ou l'intercommunalité peut soumettre à autorisation les travaux qui créent plusieurs logements dans un immeuble existant, et la refuser si les logements ne respectent pas les proportions et tailles fixées par le PLU (Code de la construction et de l'habitation, art. L126-19).</li>
</ul>
<p class="callout"><strong>Limite de cette page :</strong> un régime voisin, souvent appelé « permis de diviser », existe aussi dans les zones d'habitat dégradé (art. L126-18). Nous n'avons pas pu lire le texte officiel de cet article pour cette page : seule la mairie vous dira si votre adresse est concernée.</p>

<h2>Quelle taille et quels équipements pour chaque logement ?</h2>
<p>Le Code de la construction et de l'habitation (art. L126-17) interdit trois types de division :</p>
<ul>
  <li>celle d'un immeuble frappé d'une interdiction d'habiter, d'un arrêté de péril ou déclaré insalubre ;</li>
  <li>celle qui crée des logements de <strong>moins de 14 m² et de moins de 33 m³</strong> habitables ;</li>
  <li>celle qui crée des logements sans alimentation en eau potable, sans évacuation des eaux usées ou sans accès à l'électricité, ou sans constat de risque d'exposition au plomb et recherche d'amiante.</li>
</ul>
<p>Diviser sans respecter ces règles expose à une amende qui peut atteindre 15 000 €, et 25 000 € en cas de nouveau manquement dans les trois ans (art. L183-14).</p>
<p>Si les logements sont loués, ils doivent en plus être décents : au moins une pièce principale de 9 m² avec 2,20 m sous plafond, ou un volume habitable de 20 m³ (décret n° 2002-120, art. 4). Le règlement sanitaire départemental peut être plus exigeant.</p>

<h2>Vendre les logements séparément : la copropriété</h2>
<p>Vendre deux logements d'une même maison à deux acheteurs revient en général à créer une copropriété : un état descriptif de division, qui définit les lots, et un règlement de copropriété, qui fixe les parties communes et la répartition des charges.</p>
<p>Si la maison a plus de dix ans, la mise en copropriété doit être précédée d'un diagnostic technique global (Code de la construction et de l'habitation, art. L731-4). L'ANIL précise qu'il se fait avant la rédaction du règlement et de l'état descriptif.</p>
<p>C'est le notaire qui rédige ces actes. Les questions d'impôt et de taxe dépendent de votre situation : faites-les chiffrer par lui, nous ne publions pas de montant.</p>

<h2>Dans quel ordre s'y prendre ?</h2>
<ol>
  <li><strong>Lire le PLU</strong> de la zone : stationnement, taille des logements, autorisation préalable éventuelle. Le <a href="https://www.geoportail-urbanisme.gouv.fr/" rel="noopener">Géoportail de l'urbanisme</a> donne la zone de votre adresse.</li>
  <li><strong>Vérifier la maison</strong> : peut-on créer deux entrées, deux cuisines, deux salles d'eau, et séparer les compteurs sans toucher aux murs porteurs ?</li>
  <li><strong>Faire dessiner le projet</strong> par un architecte ou un maître d'œuvre, avec les surfaces de chaque logement.</li>
  <li><strong>Déposer l'autorisation</strong> d'urbanisme adaptée et attendre la fin des délais de recours.</li>
  <li><strong>Préparer la copropriété</strong> avec le géomètre et le notaire.</li>
  <li><strong>Vendre</strong>, par une agence immobilière.</li>
</ol>
<p>Notre page <a href="/division-maison-logements">division de maison</a> présente la façon dont PLU Value conduit ces étapes, et <a href="/nos-engagements">nos engagements</a> ce que nous prenons à notre charge.</p>

<h2>Peut-on le faire soi-même ?</h2>
<p>En théorie, oui. En pratique, une division de maison réunit plusieurs métiers : un urbaniste ou un avocat pour lire le règlement, un architecte pour vérifier que le bâtiment s'y prête, des entreprises pour chiffrer les travaux, un géomètre et un notaire pour la copropriété, et une bonne connaissance du marché pour créer des logements qui se vendent. Chacun se paie, et le tout prend des mois.</p>
<p>Le vrai risque n'est pas de ne pas y arriver : c'est d'y arriver mal. Un logement trop petit, une place de stationnement manquante, une autorisation refusée, et les frais sont engagés pour rien. C'est pour cela que PLU Value ne retient que les projets qu'elle peut mener au bout, et y engage ses propres moyens. Voir <a href="/notre-methode">notre méthode</a>.</p>

<h2>Questions fréquentes</h2>
<details><summary>Quelle surface minimale pour un logement issu d'une division ?</summary><p>Le Code de la construction et de l'habitation (art. L126-17) interdit la division qui crée des logements de moins de 14 m² et de moins de 33 m³ habitables. Le PLU de la commune peut fixer des tailles plus grandes dans certains secteurs.</p></details>
<details><summary>Faut-il un permis de construire pour diviser une maison en deux logements ?</summary><p>Cela dépend des travaux. La division en lots ne demande pas toujours de formalité, mais les travaux peuvent exiger une déclaration préalable ou un permis de construire, par exemple en cas de changement de destination avec travaux sur la structure ou la façade. La mairie confirme le cas de votre projet.</p></details>
<details><summary>Combien de temps prend l'instruction ?</summary><p>En droit commun, un mois pour une déclaration préalable, deux mois pour un permis de construire portant sur une maison individuelle et trois mois pour les autres projets, à partir d'un dossier complet. Ces délais sont plus longs en secteur protégé, et il faut y ajouter les délais de recours.</p></details>
<details><summary>Faut-il créer une copropriété ?</summary><p>Oui en général si les logements sont vendus à des acheteurs différents : il faut un état descriptif de division et un règlement de copropriété, rédigés par un notaire. Si la maison a plus de dix ans, un diagnostic technique global doit précéder la mise en copropriété.</p></details>
<details><summary>Le PLU peut-il empêcher la division ?</summary><p>Oui, de fait : s'il exige des places de stationnement par logement que le terrain ne peut pas accueillir, ou s'il impose une taille minimale de logement que la maison ne permet pas d'atteindre. C'est pourquoi le PLU se lit en premier.</p></details>

<h2>Sources</h2>
<ol class="sources">
  <li>Ministère de la Justice, « Faut-il une autorisation pour diviser un bâtiment en plusieurs lots ? » : https://www.justice.fr/fiche/faut-autorisation-diviser-batiment-plusieurs-lots (consulté le 12/11/2026).</li>
  <li>Code de l'urbanisme, art. R*423-23 (délais d'instruction) : https://legifrance.gouv.fr/codes/section_lc/LEGITEXT000006074075/LEGISCTA000006158835/2026-02-03 (consulté le 12/11/2026).</li>
  <li>Service-public.gouv.fr, permis de construire (délais) : https://www.service-public.gouv.fr/particuliers/vosdroits/F1986 (consulté le 12/11/2026).</li>
  <li>Code de la construction et de l'habitation, art. L126-17 (divisions interdites) : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000041565257 ; art. L126-19 (autorisation préalable) : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000041565261 ; art. L183-14 (amende) : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000041570625 (consultés le 12/11/2026). Art. L126-18 : texte non lu.</li>
  <li>Code de l'urbanisme, art. L151-14 (taille minimale des logements) : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031211187 (consulté le 12/11/2026, extrait).</li>
  <li>Décret n° 2002-120 du 30 janvier 2002, art. 4 (logement décent) : https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000043842463 ; ministère de la Justice, « Logement à louer décent » : https://www.justice.fr/fiche/logement-decent (consultés le 12/11/2026).</li>
  <li>Code de la construction et de l'habitation, art. L731-4 (diagnostic technique global) : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000028779366 ; ANIL, « Diagnostic technique global de la copropriété » : https://anil.org/aj-copropriete-diagnostic-technique-global (consultés le 12/11/2026).</li>
  <li>Insee Première n° 2064, « Un quart des ménages vivent dans un logement en sous-occupation très accentuée », juillet 2025 : https://www.insee.fr/fr/statistiques/8606928 (consulté le 12/11/2026).</li>
</ol>
<p class="meta">Cette page est une information générale, pas un conseil juridique ni fiscal. Consultez la mairie de votre commune et un notaire avant toute décision.</p>
"""))

ARTICLES.append(dict(
    slug="maison-en-indivision-qui-ne-se-vend-pas", date="2026-11-15", cat="Succession · Indivision", read="7 min",
    title="Maison en indivision qui ne se vend pas : que peuvent faire les héritiers ?",
    seo="Maison en indivision qui ne se vend pas : que faire ?",
    desc="Maison des parents héritée à plusieurs, sans accord ou sans acheteur : règles de l'indivision, frais qui courent, options avant de baisser le prix.",
    body="""
<p class="answer">Une maison en indivision qui ne se vend pas bloque souvent pour deux raisons qui se cumulent : il faut l'accord de tous les héritiers pour la vendre, et une grande maison de famille trouve peu d'acheteurs à son prix. Avant de baisser le prix ou d'aller au tribunal, une troisième voie mérite d'être étudiée : vérifier si le bien peut se vendre autrement, en plusieurs lots. Ce n'est pas possible partout, et cela se vérifie.</p>

<h2>La maison des parents est vide, et rien ne bouge : pourquoi ?</h2>
<p>La situation est fréquente. Les parents sont partis, vous êtes deux, trois ou quatre à hériter, et la maison où vous avez grandi est en vente depuis des mois. L'un veut vendre vite, l'autre refuse de « brader », un troisième habite loin et ne répond plus. Pendant ce temps, la maison reste fermée.</p>
<p>Juridiquement, vous êtes en indivision : tant que le partage n'est pas fait, les biens du défunt appartiennent ensemble à tous les héritiers, explique le ministère de la Justice [1]. Personne ne possède « sa » chambre ou « sa » moitié de jardin : chacun détient une part de l'ensemble.</p>

<h2>Faut-il que tous les héritiers soient d'accord pour vendre ?</h2>
<p>Oui, en principe. Pour les actes les plus importants, dont la vente d'un bien immobilier, la décision doit être prise à l'unanimité [1]. Un seul héritier qui refuse le prix, ou qui ne signe pas, suffit à tout arrêter.</p>
<p>Il existe des exceptions. Le tribunal peut autoriser la vente à la demande d'héritiers qui détiennent au moins les deux tiers des droits indivis ; cette dérogation ne joue pas si le bien est démembré (usufruit et nue-propriété) ou si l'un des héritiers fait l'objet d'une mesure de protection [1][2]. En cas de mésentente, le tribunal peut aussi nommer un mandataire chargé de gérer provisoirement [1].</p>
<p>Nous n'avons pas pu lire, dans une source officielle, le détail des étapes et des délais de cette procédure des deux tiers : demandez-le à votre notaire avant de vous y engager.</p>

<h2>Peut-on vous obliger à rester dans l'indivision ?</h2>
<p>Non. Les notaires le rappellent : nul ne peut être contraint à demeurer dans l'indivision, et chaque héritier peut demander le partage à tout moment [2]. Si le partage amiable est impossible, il se demande au tribunal ; les autres héritiers peuvent alors demander à rester en indivision entre eux, en attribuant sa part à celui qui veut sortir [1].</p>
<p>Deux autres points utiles :</p>
<ul>
  <li>Les héritiers peuvent signer une convention d'indivision pour organiser la gestion du bien, pour une durée déterminée de cinq ans au maximum [2][3].</li>
  <li>Un héritier peut céder sa part à un tiers ; les autres ne peuvent pas s'y opposer, mais ils disposent d'un droit de préemption sur cette part [2].</li>
</ul>
<p>La voie judiciaire existe donc, mais elle abîme les relations familiales et ne règle pas la question de fond : pourquoi cette maison ne trouve-t-elle pas preneur ?</p>

<h2>Qui paie pendant que la maison ne se vend pas ?</h2>
<p>Tout le monde. Chaque héritier doit régler les dettes de l'indivision à proportion de sa part [2]. Pour la taxe foncière, chacun paie sa quote-part ; celui qui a tout avancé peut se faire rembourser par les autres [4].</p>
<p>Le calendrier fiscal, lui, n'attend pas la vente. La déclaration de succession doit être déposée dans les six mois du décès, et les droits se règlent au même moment [5][6]. Un paiement fractionné peut être demandé : sur un an au plus en trois versements, ou sur trois ans en sept versements si au moins la moitié des biens ne sont pas liquides, avec l'accord de tous les héritiers et des intérêts [7]. Votre notaire vous dira ce qui s'applique à votre succession : nous ne chiffrons aucun cas particulier.</p>
<p>Nous n'avons pas trouvé de source officielle qui précise qui paie l'entretien et l'assurance d'une maison restée vide : c'est une question à poser au notaire, et un sujet à mettre par écrit entre héritiers.</p>

<h2>Baisser le prix, attendre, ou vendre autrement ?</h2>
<p>Quand une maison héritée ne se vend pas, les héritiers ont en général quatre options.</p>
<div class="table"><table>
  <thead><tr><th>Option</th><th>Ce que cela règle</th><th>Ce que cela ne règle pas</th></tr></thead>
  <tbody>
    <tr><td>Ne rien faire</td><td>Rien à décider aujourd'hui</td><td>Les charges courent, la maison vide se dégrade, le désaccord s'installe</td></tr>
    <tr><td>Baisser le prix</td><td>Peut déclencher une offre</td><td>Chaque héritier reçoit moins ; celui qui refusait le prix refusera encore</td></tr>
    <tr><td>Aller au tribunal</td><td>Met fin au blocage d'un héritier</td><td>La maison reste difficile à vendre telle quelle</td></tr>
    <tr><td>Étudier une vente en plusieurs lots</td><td>S'adresse à d'autres acheteurs, à d'autres budgets</td><td>N'est pas possible partout : il faut le vérifier</td></tr>
  </tbody>
</table></div>
<p>La quatrième option est la moins connue. Une maison de famille avec un grand jardin, ou une maison de sept ou huit pièces, coûte trop cher au total pour la plupart des acheteurs du quartier. Selon les règles de la commune, il est parfois possible de détacher un terrain à bâtir, ou de créer plusieurs logements dans la maison. Chaque lot vise alors un budget plus courant. Le désaccord sur le prix change aussi de nature : on ne discute plus d'une baisse, mais d'un projet.</p>
<p>Rien n'est automatique. Tout dépend du plan local d'urbanisme, du terrain, du bâtiment et du marché local. Pour comprendre les deux pistes, voir <a href="/blog/vendre-une-partie-de-son-terrain-maison-trop-grande.html">vendre une partie de son terrain</a> et <a href="/blog/diviser-une-maison-en-plusieurs-logements.html">diviser une maison en plusieurs logements</a>. Notre page <a href="/succession-maison-familiale">succession et maison familiale</a> décrit la façon dont nous travaillons avec les héritiers et leur notaire.</p>

<h2>Pourquoi ne pas le faire seuls ?</h2>
<p>Parce qu'une division demande plusieurs métiers à la fois : lire le règlement d'urbanisme, vérifier que le bâtiment ou le terrain s'y prête, faire chiffrer les travaux, faire borner, obtenir les autorisations, connaître les prix du secteur, et avancer les frais pendant des mois. À plusieurs héritiers, il faut en plus que tous décident ensemble à chaque étape.</p>
<p>Mal préparé, un projet peut être refusé par la mairie, ou coûter des frais sans résultat. Dans une indivision déjà tendue, c'est le scénario à éviter.</p>
<p>PLU Value réunit ces métiers. L'étude préalable est gratuite ; si rien n'est réaliste, nous vous le disons, avec la raison. Pour les projets que nous retenons, nous engageons nos propres moyens dans les études et les démarches : nous avons donc le même intérêt que vous à ce que le projet aboutisse. La vente reste confiée à une agence immobilière, et les actes à votre notaire. Voir <a href="/nos-engagements">nos engagements</a>, ou <a href="/deposer-un-bien">présentez-nous le bien</a>.</p>

<h2>Questions fréquentes</h2>
<details><summary>Un seul héritier peut-il bloquer la vente de la maison ?</summary><p>Oui, en principe : la vente d'un bien immobilier en indivision se décide à l'unanimité. Le tribunal peut toutefois autoriser la vente à la demande d'héritiers détenant au moins les deux tiers des droits indivis, sauf si le bien est démembré ou si un héritier est sous mesure de protection.</p></details>
<details><summary>Peut-on sortir de l'indivision sans l'accord des autres ?</summary><p>Oui. Nul ne peut être contraint à demeurer dans l'indivision : chaque héritier peut demander le partage, à l'amiable ou, à défaut, devant le tribunal. Il peut aussi céder sa part, les autres héritiers disposant d'un droit de préemption.</p></details>
<details><summary>Qui paie la taxe foncière d'une maison en indivision ?</summary><p>Chaque héritier paie sa quote-part. Celui qui a réglé la totalité peut demander aux autres de lui rembourser leur part.</p></details>
<details><summary>Combien de temps a-t-on pour régler la succession auprès des impôts ?</summary><p>La déclaration de succession doit être déposée dans les six mois du décès, douze mois si le décès a eu lieu à l'étranger, et les droits sont dus au même moment. Un paiement fractionné peut être demandé sous conditions. Le notaire vous indiquera votre situation exacte.</p></details>
<details><summary>Diviser la maison ou le terrain, est-ce toujours possible ?</summary><p>Non. Cela dépend du plan local d'urbanisme, des servitudes, de la configuration du terrain et du bâtiment, et de l'intérêt économique de l'opération. C'est ce qu'une étude préalable permet de savoir avant toute décision.</p></details>

<h2>Sources</h2>
<ol class="sources">
  <li>Ministère de la Justice, « Succession : indivision entre les héritiers » : https://www.justice.fr/fiche/succession-indivision-entre-heritiers (consulté le 15/11/2026).</li>
  <li>Notaires de France, « Acheter en indivision (règles générales) » : https://www.notaires.fr/fr/immobilier-fiscalite/achat-et-vente-cas-particuliers/le-regime-de-lindivision (consulté le 15/11/2026).</li>
  <li>Code civil, convention d'indivision à durée déterminée (cinq ans au plus) : https://www.legifrance.gouv.fr/codes/id/LEGIARTI000006444603/2007-01-01 (consulté le 15/11/2026).</li>
  <li>Service-public.gouv.fr, « Impôts locaux : qui doit payer la taxe foncière en cas d'indivision ? » : https://www.service-public.gouv.fr/particuliers/vosdroits/F263 (consulté le 15/11/2026, version anglaise de la fiche).</li>
  <li>Service-public.gouv.fr, « Déclaration de succession » : https://www.service-public.gouv.fr/particuliers/vosdroits/R10279 (consulté le 15/11/2026).</li>
  <li>Ministère de la Justice, « Droits de succession - Déclaration » : https://www.justice.fr/fiche/droits-succession-declaration (consulté le 15/11/2026).</li>
  <li>Ministère de la Justice, « Paiement des droits de succession » : https://www.justice.fr/fiche/paiement-droits-succession (consulté le 15/11/2026).</li>
</ol>
<p class="meta">Cette page est une information générale, pas un conseil juridique ni fiscal. Consultez votre notaire avant toute décision.</p>
"""))

ARTICLES.append(dict(
    slug="vendre-sa-maison-residence-senior-ehpad", date="2026-11-15", cat="Propriétaires · Résidence senior et EHPAD", read="7 min",
    title="Vendre sa maison pour aller en résidence senior ou payer l'EHPAD : faut-il tout vendre ?",
    seo="Vendre sa maison pour aller en résidence senior",
    desc="Résidence senior ou EHPAD à financer : ce que coûte un EHPAD selon la CNSA, les aides, la règle fiscale à connaître et les options avant de vendre la maison.",
    body="""
<p class="answer">Vendre sa maison pour aller en résidence senior, ou pour payer l'EHPAD d'un conjoint ou d'un parent, est souvent la bonne décision. Mais « vendre la maison » ne veut pas forcément dire la vendre d'un seul bloc, au premier prix proposé. Avant de signer, trois vérifications valent la peine : ce que le séjour coûtera vraiment, les aides et la règle fiscale qui s'appliquent, et la façon de vendre qui correspond le mieux à votre bien.</p>

<h2>La maison est devenue trop grande : à quel moment faut-il se décider ?</h2>
<p>Les enfants sont partis, il reste quatre chambres vides, un escalier qui fatigue et un jardin qu'on n'arrive plus à entretenir. Selon l'Insee, 34,4 % des personnes de 65 ans ou plus vivent seules dans leur logement, et 43,4 % des femmes de cet âge (chiffres 2023) [1]. Vous n'êtes pas un cas isolé.</p>
<p>Le plus souvent, la décision se prend dans l'urgence : une chute, une hospitalisation, une place qui se libère. C'est le pire moment pour vendre, parce qu'on accepte alors la première offre. Y réfléchir avant, quand rien ne presse, laisse le choix.</p>

<h2>Résidence autonomie, résidence services, EHPAD : quelle différence ?</h2>
<p>Les résidences autonomie et les résidences services s'adressent à des personnes âgées autonomes qui veulent vivre de façon indépendante avec des services. L'EHPAD, lui, est un établissement médicalisé : il héberge des personnes, en général âgées d'au moins 60 ans, qui ont besoin de soins et d'aide au quotidien [2].</p>
<p>Nous n'avons pas pu ouvrir la page officielle qui compare résidences autonomie et résidences services (pour-les-personnes-agees.gouv.fr), et nous n'avons trouvé aucun chiffre officiel sur le coût d'une résidence services : demandez un devis complet à chaque résidence, services compris.</p>

<h2>Combien coûte un EHPAD ?</h2>
<p>La Caisse nationale de solidarité pour l'autonomie (CNSA) publie les prix. En 2024, pour une chambre seule en hébergement permanent, le prix médian était de 2 138 € par mois dans une chambre habilitée à l'aide sociale, et de 3 016 € par mois dans une chambre non habilitée [3]. Ce montant additionne l'hébergement et le tarif dépendance minimal, avant aides.</p>
<div class="table"><table>
  <thead><tr><th>Statut de l'établissement</th><th>Chambre habilitée à l'aide sociale</th><th>Chambre non habilitée</th></tr></thead>
  <tbody>
    <tr><td>Public</td><td>2 109 €</td><td>2 250 €</td></tr>
    <tr><td>Privé non lucratif</td><td>2 200 €</td><td>2 527 €</td></tr>
    <tr><td>Privé commercial</td><td>2 064 €</td><td>3 186 €</td></tr>
  </tbody>
</table></div>
<p class="hint">Prix médians mensuels 2024, chambre seule, hébergement permanent. Source : CNSA [3].</p>
<p>Les écarts entre départements sont importants : pour une chambre non habilitée, la CNSA relève 5 106 € par mois à Paris et 4 186 € dans les Hauts-de-Seine, contre 2 055 € en Lozère [3]. Sur plusieurs années, la somme à réunir est donc élevée, et c'est ce qui conduit beaucoup de familles à vendre la maison.</p>

<h2>Quelles aides, et que deviennent-elles à la succession ?</h2>
<p>L'aide sociale à l'hébergement (ASH) paie tout ou partie des frais d'hébergement quand les revenus ne suffisent pas, dans les établissements qui ont des places réservées à l'aide sociale : EHPAD, résidences autonomie, unités de soins de longue durée [4]. Deux points sont à connaître avant de la demander :</p>
<ul>
  <li>le département peut tenir compte des revenus des enfants, gendres et belles-filles pour fixer son montant [4] ;</li>
  <li>c'est une avance : le département peut la récupérer au décès sur la succession, et sur une donation faite dans les dix ans avant la demande ou après celle-ci [4].</li>
</ul>
<p>Autrement dit, garder la maison en demandant l'aide sociale ne la protège pas toujours pour les enfants. C'est une question à poser au notaire et au conseil départemental, pas à trancher seul.</p>

<h2>Y a-t-il un impôt quand on vend la maison ?</h2>
<p>La plus-value sur la vente de la résidence principale est exonérée. Si vous avez déjà quitté le logement, l'exonération reste possible lorsque vous l'avez occupé jusqu'à sa mise en vente et que la vente a lieu dans un délai normal, en principe un an [5].</p>
<p>Une règle particulière existe pour la personne entrée en maison de retraite médicalisée : la vente doit intervenir dans les deux ans qui suivent l'entrée, le logement doit être resté libre de toute occupation depuis, et des conditions de revenus et de patrimoine s'appliquent [5].</p>
<p>Ces délais comptent pour la suite : un projet qui prend du temps doit être calé avec le notaire dès le départ. Nous ne chiffrons aucune situation personnelle.</p>

<h2>Faut-il vendre toute la maison, d'un seul bloc ?</h2>
<p>Pas forcément. Une grande maison sur un grand terrain coûte cher au total, et peu d'acheteurs ont ce budget. Selon l'Insee, un quart des ménages vivent dans un logement en sous-occupation très accentuée [6] : beaucoup de grandes maisons cherchent preneur en même temps. Vous avez en général quatre options.</p>
<ul>
  <li><strong>Ne rien décider.</strong> La maison reste, les charges aussi, et la décision se prendra plus tard, dans l'urgence.</li>
  <li><strong>Vendre en l'état.</strong> C'est le plus simple. Le prix dépend du nombre d'acheteurs capables d'acheter l'ensemble.</li>
  <li><strong>Baisser le prix</strong> si la maison ne part pas : c'est autant de moins pour financer le séjour.</li>
  <li><strong>Vérifier si le bien peut se vendre autrement</strong> : détacher une partie du terrain, ou créer plusieurs logements dans la maison. Chaque lot s'adresse à un budget plus courant.</li>
</ul>
<p>La dernière option n'est pas possible partout. Elle dépend des règles d'urbanisme de la commune, du terrain et du bâtiment, et elle demande plus de temps qu'une vente simple : elle ne convient donc pas à toutes les situations, en particulier quand il faut payer un établissement tout de suite. Elle mérite d'être étudiée quand la décision se prépare à l'avance. Pour comprendre, voir <a href="/blog/vendre-une-partie-de-son-terrain-maison-trop-grande.html">vendre une partie de son terrain</a> et <a href="/blog/diviser-une-maison-en-plusieurs-logements.html">diviser une maison en plusieurs logements</a>, ou notre page <a href="/valoriser-maison-familiale">valoriser une maison familiale</a>.</p>

<h2>Pourquoi ne pas le faire seul ?</h2>
<p>Parce qu'une division réunit plusieurs métiers : lire le plan local d'urbanisme, vérifier que le terrain ou la maison s'y prête, faire chiffrer les travaux, faire borner, obtenir les autorisations, connaître les prix du secteur, et avancer les frais pendant des mois. À 75 ou 80 ans, ou pour des enfants qui gèrent déjà l'entrée d'un parent en établissement, c'est beaucoup.</p>
<p>Mal préparé, un projet peut être refusé par la mairie, ou coûter des frais sans résultat, au moment où chaque euro compte.</p>
<p>PLU Value réunit ces métiers. L'étude préalable est gratuite ; si rien n'est réaliste, ou si une vente simple est préférable dans votre cas, nous vous le disons. Pour les projets que nous retenons, nous engageons nos propres moyens dans les études et les démarches : nous avons donc le même intérêt que vous à bien faire. La vente reste confiée à une agence immobilière, et les actes à votre notaire. Voir <a href="/nos-engagements">nos engagements</a>, ou <a href="/deposer-un-bien">présentez-nous votre bien</a>.</p>

<h2>Questions fréquentes</h2>
<details><summary>Combien coûte un EHPAD par mois ?</summary><p>Selon la CNSA, en 2024, le prix médian d'une chambre seule en hébergement permanent était de 2 138 € par mois en chambre habilitée à l'aide sociale et de 3 016 € en chambre non habilitée, avant aides. Les prix varient fortement selon le département et le statut de l'établissement.</p></details>
<details><summary>L'aide sociale à l'hébergement est-elle reprise sur la succession ?</summary><p>Oui, elle peut l'être : le département peut récupérer les sommes versées au décès du bénéficiaire sur sa succession, et sur une donation faite dans les dix ans avant la demande ou après celle-ci.</p></details>
<details><summary>Paie-t-on un impôt sur la vente de sa résidence principale quand on part en établissement ?</summary><p>La plus-value sur la résidence principale est exonérée. Après un départ, la vente doit intervenir dans un délai normal, en principe un an. Pour une entrée en maison de retraite médicalisée, une règle particulière prévoit un délai de deux ans, sous conditions. Faites vérifier votre situation par le notaire.</p></details>
<details><summary>Peut-on vendre seulement une partie de son terrain pour financer une résidence senior ?</summary><p>Parfois. Cela dépend des règles d'urbanisme de la commune et de la configuration du terrain, et cela demande des autorisations et un bornage. Une étude préalable permet de le savoir avant toute décision.</p></details>
<details><summary>Les enfants doivent-ils participer aux frais d'EHPAD ?</summary><p>Pour l'aide sociale à l'hébergement, le département peut tenir compte des revenus des enfants, gendres et belles-filles. Les petits-enfants en sont dispensés.</p></details>

<h2>Sources</h2>
<ol class="sources">
  <li>Insee, « Personnes vivant seules dans leur logement selon l'âge et le sexe » (données 2023) : https://www.insee.fr/fr/statistiques/2381512 (consulté le 15/11/2026).</li>
  <li>Ministère de la Justice, « Éhpad : établissement d'hébergement pour personnes âgées dépendantes » : https://www.justice.fr/fiche/ehpad-etablissement-hebergement-personnes-agees-dependantes (extrait lu le 15/11/2026) ; pour-les-personnes-agees.gouv.fr, « Résidence autonomie et résidence services : quelle différence ? » (extrait lu le 15/11/2026, page complète non ouverte).</li>
  <li>CNSA, Repères statistiques n° 27, « En 2024, un écart moyen de 1 000 euros par mois entre les chambres habilitées à l'aide sociale en EHPAD et les autres », mars 2026 : https://www.cnsa.fr/sites/default/files/2026-04/PUB_RS-n27_Prix-EHPAD_2024_vf.pdf (consulté le 15/11/2026).</li>
  <li>Ministère de la Justice, « Aide sociale à l'hébergement (ASH) d'une personne âgée » : https://www.justice.fr/fiche/aide-sociale-hebergementash-personne-agee (consulté le 15/11/2026).</li>
  <li>impots.gouv.fr, « Plus-values exonérées » : https://www.impots.gouv.fr/particulier/plus-values-exonerees (consulté le 15/11/2026).</li>
  <li>Insee Première n° 2064, « Un quart des ménages vivent dans un logement en sous-occupation très accentuée », juillet 2025 : https://www.insee.fr/fr/statistiques/8606928 (consulté le 12/11/2026).</li>
</ol>
<p class="meta">Cette page est une information générale, pas un conseil juridique, fiscal ou médical. Consultez votre notaire et le conseil départemental avant toute décision.</p>
"""))

# ---------------------------------------------------------------- 16/11/2026
ARTICLES.append(dict(
    slug="faut-il-baisser-le-prix-de-sa-maison", date="2026-11-16", cat="Vendre · Maison en vente depuis longtemps", read="7 min",
    title="Faut-il baisser le prix de sa maison quand elle ne se vend pas ?",
    seo="Faut-il baisser le prix de sa maison qui ne se vend pas ?",
    desc="Des visites, pas d'offre, un mandat qui arrive à échéance : avant de baisser le prix de sa maison, ce qu'il faut vérifier, et les autres façons de vendre.",
    body="""
<p class="answer">Faut-il baisser le prix de sa maison quand elle ne se vend pas ? Parfois oui : si des maisons comparables se vendent moins cher autour de chez vous, le marché a déjà répondu. Mais quand la maison est grande ou posée sur un grand terrain, ce n'est pas toujours le prix au mètre carré qui bloque : c'est le montant total, que peu d'acheteurs peuvent emprunter. Dans ce cas, baisser encore ne règle rien, et il existe d'autres façons de vendre à étudier avant.</p>

<h2>Des mois de visites et toujours pas d'offre : que se passe-t-il ?</h2>
<p>L'annonce est en ligne depuis le printemps. Il y a eu des visites, des compliments sur le jardin, puis plus de nouvelles. L'agence a proposé une baisse, puis une autre, et le mandat arrive à échéance.</p>
<p>Le marché, lui, n'est pas à l'arrêt. Les notaires comptent 949 000 ventes de logements anciens sur douze mois à fin mai 2026, en progression de 5,7 % sur un an. Mais ils notent aussi que « les acquéreurs prennent plus de temps » pour concrétiser et que « les négociations retrouvent une place plus importante » [1]. En Île-de-France, les prix des maisons baissaient encore légèrement au premier trimestre 2026 (-0,4 %) [1].</p>

<h2>Pourquoi ma maison ne part pas alors que le prix au m² est correct ?</h2>
<p>Parce qu'un acheteur n'achète pas un prix au mètre carré : il achète avec une mensualité. Le Haut Conseil de stabilité financière a demandé aux banques, dans sa recommandation de janvier 2021, que le taux d'effort des emprunteurs n'excède pas 35 % et que la durée du crédit n'excède pas 25 ans, avec une marge de souplesse limitée à 20 % des crédits accordés [2]. Et le taux moyen des nouveaux crédits à l'habitat était de 3,32 % en septembre 2026, selon la Banque de France [3].</p>
<p><strong>Exemple.</strong> Un ménage qui gagne 5 000 € par mois ne peut pas, en principe, dépasser 1 750 € de mensualités (35 %). Si le prix total de votre maison demande une mensualité plus élevée, ce ménage ne peut pas faire d'offre, même s'il a adoré la visite.</p>
<p>Plus le prix total est haut, moins il reste de ménages capables de suivre. C'est le cas typique de la grande maison familiale : selon l'Insee, 41 % des maisons individuelles sont en sous-occupation très accentuée, c'est-à-dire qu'elles comptent au moins trois pièces de plus que ce dont le ménage a besoin [4]. Beaucoup de grandes maisons, peu de grands budgets.</p>

<h2>Comment savoir si c'est vraiment le prix qui bloque ?</h2>
<p>Avant de baisser, posez-vous trois questions simples, et posez-les à votre agent immobilier.</p>
<ul>
  <li><strong>Y a-t-il des visites ?</strong> Peu ou pas de visites : le prix affiché, les photos ou l'annonce écartent les acheteurs avant même qu'ils se déplacent.</li>
  <li><strong>Que disent ceux qui ont visité ?</strong> « Trop de travaux », « trop grand pour nous », « trop de terrain à entretenir », « la banque ne suit pas » : ce ne sont pas des remarques sur le prix au m², ce sont des remarques sur le bien lui-même ou sur son montant total.</li>
  <li><strong>À quel prix se sont vendues les maisons voisines, et lesquelles ?</strong> Si les ventes récentes du quartier concernent surtout des maisons plus petites, la vôtre n'a peut-être pas de vrai point de comparaison.</li>
</ul>
<p>Nous n'avons trouvé aucune statistique officielle sur « la bonne baisse » ou sur le nombre de visites sans offre à partir duquel il faudrait réagir. Les seuils que l'on lit sur les sites d'annonces sont des règles de pratique, pas des mesures.</p>

<h2>Quelles sont mes options, honnêtement ?</h2>
<div class="table"><table>
  <thead><tr><th>Option</th><th>Quand elle a du sens</th><th>Sa limite</th></tr></thead>
  <tbody>
    <tr><td>Ne rien changer et attendre</td><td>Vous n'êtes pas pressé et les visites sont régulières.</td><td>Les charges continuent, et une annonce ancienne finit par inquiéter les acheteurs.</td></tr>
    <tr><td>Baisser le prix</td><td>Des maisons comparables se vendent moins cher près de chez vous.</td><td>Chaque baisse est perdue pour vous. Si c'est le montant total qui bloque, il faut baisser beaucoup pour changer de catégorie d'acheteurs.</td></tr>
    <tr><td>Changer l'annonce ou d'agence</td><td>Peu de visites, photos ou description faibles.</td><td>Ne change rien si le bien lui-même ne correspond pas aux budgets du quartier.</td></tr>
    <tr><td>Vendre autrement : en plusieurs lots</td><td>Grande maison ou grand terrain, et des règles d'urbanisme qui le permettent.</td><td>Pas possible partout. Demande des études, des autorisations et du temps.</td></tr>
  </tbody>
</table></div>
<p>Si vous devez vendre vite, une baisse franche reste souvent la voie la plus simple.</p>

<h2>Et si le problème n'était pas le prix, mais la taille du bien ?</h2>
<p>C'est la question que presque personne ne pose. Une maison de sept pièces sur un grand terrain s'adresse à très peu d'acheteurs. La même propriété, présentée en deux biens, peut en intéresser beaucoup plus :</p>
<ul>
  <li><strong>détacher une partie du terrain</strong> : d'un côté la maison avec un jardin plus facile à vivre, de l'autre un terrain à bâtir. Voir <a href="/division-terrain">la division de terrain</a> et notre article <a href="/blog/vendre-une-partie-de-son-terrain-maison-trop-grande.html">vendre une partie de son terrain</a> ;</li>
  <li><strong>créer deux ou trois logements dans la maison</strong>, quand le bâtiment et les règles le permettent. Voir <a href="/blog/diviser-une-maison-en-plusieurs-logements.html">diviser une maison en plusieurs logements</a>.</li>
</ul>
<p>Chaque lot coûte moins cher au total que l'ensemble, et s'adresse donc à des budgets plus courants. Cela ne veut pas dire que la somme des lots dépassera votre prix actuel : cela dépend de la commune, du terrain, des travaux et du marché, et seule une étude peut le dire.</p>
<p>Car tout n'est pas permis. C'est le plan local d'urbanisme de la commune qui décide : reculs par rapport à la rue et aux voisins, part du terrain qui peut être construite, accès, stationnement. Une division de terrain passe au minimum par une déclaration préalable en mairie, dont le délai d'instruction est d'un mois, deux mois en général en secteur protégé [5], sans compter les études à mener avant. Ce n'est donc pas une solution rapide.</p>

<h2>Mon mandat arrive à échéance : que puis-je faire ?</h2>
<p>Un mandat de vente doit avoir une durée limitée. Le plus souvent, il est irrévocable pendant trois mois ; ensuite, vous pouvez y mettre fin en prévenant l'agent quinze jours à l'avance par lettre recommandée avec accusé de réception [6]. Relisez votre mandat : la durée et les conditions exactes y figurent.</p>
<p>La fin d'un mandat n'oblige pas à se fâcher avec son agent. Il connaît votre bien et les objections des visiteurs : c'est souvent lui qui peut dire si le blocage vient du prix ou de la taille du bien. Voir aussi <a href="/blog/maison-qui-ne-se-vend-pas.html">maison qui ne se vend pas : les raisons fréquentes et les solutions</a>.</p>

<h2>Pourquoi ne pas le faire seul ?</h2>
<p>Parce que « couper en deux » ne se résume pas à tracer un trait sur un plan. Il faut lire le règlement d'urbanisme, vérifier les accès et les réseaux, faire intervenir un géomètre, parfois un architecte, faire chiffrer les travaux, déposer les bonnes demandes en mairie, connaître les prix réels du secteur pour chaque lot, et avancer tous ces frais pendant des mois.</p>
<p>Mal préparé, le projet peut être refusé par la mairie, ou coûter des frais sans résultat, pendant que la maison reste invendue.</p>
<p>PLU Value réunit ces métiers. L'étude préalable est gratuite ; si rien n'est réaliste, ou si une baisse de prix est la réponse la plus raisonnable, nous vous le disons. Pour les projets que nous retenons, nous engageons nos propres moyens dans les études et les démarches : nous avons donc le même intérêt que vous à bien faire. Nous ne vendons pas et ne publions pas d'annonces : la vente reste confiée à une agence immobilière, la vôtre si vous en avez une. Voir <a href="/nos-engagements">nos engagements</a>, ou <a href="/deposer-un-bien">présentez-nous votre bien</a>.</p>

<h2>Questions fréquentes</h2>
<details><summary>De combien faut-il baisser le prix d'une maison qui ne se vend pas ?</summary><p>Il n'existe pas de pourcentage officiel. La bonne référence, ce sont les ventes récentes de maisons comparables dans votre quartier, que votre agent ou votre notaire peut vous montrer. Si aucune maison comparable ne s'est vendue, le problème vient peut-être de la taille du bien plus que de son prix.</p></details>
<details><summary>Au bout de combien de temps faut-il s'inquiéter ?</summary><p>Nous n'avons pas trouvé de délai de vente officiel qui serve de repère. Les notaires constatent en 2026 que les acquéreurs prennent plus de temps pour concrétiser et négocient davantage. Plus que la durée, regardez le nombre de visites et ce que disent les visiteurs.</p></details>
<details><summary>Peut-on changer d'agence quand la maison ne se vend pas ?</summary><p>Oui, à la fin de la période d'irrévocabilité prévue au mandat, le plus souvent trois mois, en respectant un préavis de quinze jours par lettre recommandée avec accusé de réception. Vérifiez les clauses de votre propre mandat.</p></details>
<details><summary>Une grande maison se vend-elle mieux en plusieurs lots ?</summary><p>Pas toujours. Des lots plus petits s'adressent à plus d'acheteurs, mais la division dépend des règles d'urbanisme de la commune, de la configuration du terrain et du bâtiment, et elle demande des études, des autorisations et du temps. Une étude préalable permet de le savoir avant toute décision.</p></details>

<h2>Sources</h2>
<ol class="sources">
  <li>Notaires de France (Conseil supérieur du notariat), Note de conjoncture immobilière n° 72, juillet 2026 : https://acte3.notaires.fr/wp-content/uploads/2026/09/Note-de-conjoncture-n°72-Juillet-2026.pdf (consulté le 16/11/2026).</li>
  <li>Haut Conseil de stabilité financière, recommandation n° R-HCSF-2021-1 du 27 janvier 2021 relative à l'octroi de crédits immobiliers résidentiels en France : https://www.economie.gouv.fr/files/files/directions_services/hcsf/HCSF_Recommandation_R-HCSF-2021-1.pdf (consulté le 16/11/2026). Nous n'avons pas pu confirmer sur une page officielle les textes qui l'ont suivie ; votre banque ou votre courtier vous indiquera les règles appliquées aujourd'hui.</li>
  <li>Banque de France, « Crédits aux particuliers », septembre 2026, mis en ligne le 5 novembre 2026 (chiffre provisoire) : https://www.banque-france.fr/fr/statistiques/credit/credits-aux-particuliers-2026-09 (consulté le 16/11/2026).</li>
  <li>Insee Première n° 2064, « Un quart des ménages vivent dans un logement en sous-occupation très accentuée », juillet 2025 : https://www.insee.fr/fr/statistiques/8606928 (consulté le 16/11/2026).</li>
  <li>Service-public, « Déclaration préalable (DP) », fiche F17578 : https://www.service-public.gouv.fr/particuliers/vosdroits/F17578 (consulté le 16/11/2026).</li>
  <li>Ministère de la Justice, « Quel mandat de vente peut-on confier à un agent immobilier ? », mise à jour du 19 septembre 2025 : https://www.justice.fr/fiche/mandat-vente-on-confier-agent-immobilier (consulté le 16/11/2026).</li>
</ol>
<p class="meta">Cette page est une information générale, pas un conseil juridique, fiscal ou financier. Chaque bien est étudié au cas par cas ; consultez votre notaire et votre agent immobilier avant toute décision.</p>
"""))

SEO = {'densification-douce-pavillonnaire-commune': 'Densification douce du pavillonnaire : le rôle de la commune', 'vendre-une-partie-de-son-terrain-maison-trop-grande': 'Vendre une partie de son terrain : maison trop grande ?', 'diviser-son-terrain-champigny-sur-marne': 'Diviser son terrain à Champigny-sur-Marne : le PLU'}
for a in ARTICLES:
    if a['slug'] in SEO: a['seo'] = SEO[a['slug']]
ARTICLES.sort(key=lambda a: a['date'], reverse=True)

# Vidéo associée à un article (numéro d'épisode dans base.VIDEOS), placée après le premier paragraphe.
ARTICLE_VIDEO = {'vendre-une-partie-de-son-terrain-maison-trop-grande': 12, 'agent-immobilier-mandat-qui-stagne': 4,
                 'maison-qui-ne-se-vend-pas': 8, 'maison-en-indivision-qui-ne-se-vend-pas': 9, 'vendre-sa-maison-residence-senior-ehpad': 3, 'contrat-de-valorisation-immobiliere': 5}

ORG_LD = {"@type": "Organization", "name": "PLU Value", "url": "https://plu-value.fr/"}


def article_page(a):
    """Renvoie (slug, title, desc, body, ld) pour base.page()."""
    path = f"blog/{a['slug']}.html"
    url = "https://plu-value.fr/" + path
    others = [o for o in ARTICLES if o is not a][:3]
    cards = "".join(f'<a class="card" href="/blog/{o["slug"]}.html"><span class="k">{o["cat"]}</span><h3>{o["title"]}</h3><em>Lire l\'article →</em></a>' for o in others)
    art_body, vld = a['body'], None
    if a['slug'] in ARTICLE_VIDEO:
        from base import video_inline
        vh, vld = video_inline(ARTICLE_VIDEO[a['slug']])
        assert '</p>' in art_body, a['slug']
        art_body = art_body.replace('</p>', '</p>\n' + vh, 1)
    body = f"""  <nav class="crumbs" aria-label="Fil d'Ariane"><a href="/">Accueil</a> › <a href="/blog/">Conseils</a> › {a['cat'].split(' · ')[-1]}</nav>
  <article class="post">
    <span class="eyebrow">{a['cat']}</span>
    <h1>{a['title']}</h1>
    <p class="meta">Publié le {fdate(a['date'])} · {a['read']} de lecture · PLU Value</p>
{art_body}
    {CTA}
  </article>
  <section aria-labelledby="h-lire"><h2 id="h-lire">À lire aussi</h2><div class="postlist">{cards}</div></section>"""
    ld = [{"@context": "https://schema.org", "@type": "Article", "headline": a['title'], "description": a['desc'], "datePublished": a['date'],
           "dateModified": a['date'], "inLanguage": "fr-FR", "author": ORG_LD, "publisher": ORG_LD, "mainEntityOfPage": url},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://plu-value.fr/"},
              {"@type": "ListItem", "position": 2, "name": "Conseils", "item": "https://plu-value.fr/blog/"},
              {"@type": "ListItem", "position": 3, "name": a['title'], "item": url}]}]
    if vld: ld.append(vld)
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
