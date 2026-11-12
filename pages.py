# -*- coding: utf-8 -*-
import re, sys, os
sys.path.insert(0, "/home/claude/site/build")
from base import page, ba_slider, TERRAIN_PAIR, MAISON_BA, SIM, TEAM, FINAL_CTA, PARTNER, faq_block

P = {}

# ---------- EXPERTISE (accueil + méthode) ----------
METIERS = """<div class="grid3">
      <div class="card"><span class="k">1 · Urbanisme</span><h3>Lire le règlement, pas seulement la carte</h3><p class="hint">Emprise au sol, retraits, pleine terre, stationnement, hauteur. Une règle mal lue, et l'autorisation est refusée.</p></div>
      <div class="card"><span class="k">2 · Droit</span><h3>Sécuriser chaque acte</h3><p class="hint">Servitudes, mitoyenneté, copropriété, conditions suspensives. Un montage mal préparé se rattrape difficilement chez le notaire.</p></div>
      <div class="card"><span class="k">3 · Architecture</span><h3>Vérifier que le bâtiment s'y prête</h3><p class="hint">Murs porteurs, accès indépendants, réseaux, compteurs séparés, isolation entre logements, plans de chaque lot.</p></div>
      <div class="card"><span class="k">4 · Travaux</span><h3>Chiffrer avant de s'engager</h3><p class="hint">Devis d'entreprises, budget, calendrier. Un projet dessiné sans devis est un projet qui dérape.</p></div>
      <div class="card"><span class="k">5 · Marché</span><h3>Créer des lots qui se vendent</h3><p class="hint">Ventes réelles du quartier, surfaces recherchées, budgets des acheteurs. Un lot mal dimensionné reste en vitrine.</p></div>
      <div class="card"><span class="k">6 · Finance et pilotage</span><h3>Tenir pendant des mois</h3><p class="hint">Avancer les frais, coordonner géomètre, architecte, mairie, notaire et agence, dans le bon ordre.</p></div>
    </div>"""
RISQUES = """<div class="case">
      <h3>Ce qui arrive quand une division est mal préparée</h3>
      <ul>
        <li>L'autorisation est refusée, ou attaquée par un voisin : des mois perdus, et le dossier à refaire.</li>
        <li>Un logement créé ne respecte pas les minimums légaux (14 m² et 33 m³, équipements propres) : la division est interdite et l'amende peut atteindre 15 000 € (Code de la construction et de l'habitation, art. L126-17 et L183-14).</li>
        <li>Le lot détaché n'a pas l'accès ou la largeur exigés : il n'est pas constructible, donc pas vendable comme terrain à bâtir.</li>
        <li>Les frais de géomètre, d'architecte et de dossier sont payés, et le projet ne se fait pas.</li>
        <li>La vente bloque au dernier moment, sur un défaut de conformité que la banque de l'acheteur refuse.</li>
      </ul>
    </div>"""
EXPERTISE = f"""  <section aria-labelledby="h-exp">
    <span class="eyebrow">Notre savoir-faire</span>
    <h2 id="h-exp">Diviser un bien paraît simple. Le faire bien demande six métiers.</h2>
    <p class="lead">Une division touche à l'urbanisme, au droit, à l'architecture, aux travaux, au marché et à la finance. Chaque étape coûte de l'argent et du temps, et une erreur sur l'une d'elles peut faire tomber toutes les autres.</p>
    {METIERS}
    {RISQUES}
    <p class="note"><b>Pourquoi nous avons intérêt à bien faire :</b> nous engageons nos propres moyens dans les projets que nous retenons. Un dossier mal exécuté, c'est d'abord notre argent et notre temps qui sont perdus. Notre intérêt est le même que le vôtre. <a href="/notre-methode">Voir notre méthode</a></p>
  </section>
"""

# ---------- FAQ commune ----------
FAQ = [
 ("Est-ce que PLU Value achète ma maison ?", "Pas nécessairement. Notre approche principale est un partenariat de valorisation : vous restez propriétaire et nous engageons nos moyens dans la préparation du projet. Dans certains dossiers, une acquisition peut être étudiée, toujours sous conditions suspensives."),
 ("Est-ce que je reste propriétaire de mon bien ?", "Oui, dans le cadre du partenariat de valorisation, selon les modalités du contrat. Vous restez maître des décisions : rien ne se signe sans votre accord."),
 ("Qui paie les études ?", "L'étude préalable est gratuite. Pour les projets que nous sélectionnons, PLU Value finance les études et les intervenants prévus au contrat (architecte, géomètre-expert, avocat, mise en copropriété le cas échéant). Les frais engagés sont récupérés lors de la vente du premier lot, selon les conditions écrites au contrat."),
 ("Que se passe-t-il si la division est impossible ?", "Si notre étude préalable conclut qu'aucune solution n'est réaliste, nous vous le disons, avec la raison, et vous ne devez rien. Si un obstacle apparaît après la signature, par exemple un refus d'autorisation, les conséquences sont prévues noir sur blanc dans le contrat, avant toute signature."),
 ("Quels professionnels interviennent ?", "Selon le projet : architecte, géomètre-expert, avocat en droit de l'urbanisme, notaire, entreprises pour les devis de travaux, et l'agence immobilière chargée de la vente. Nous les coordonnons pour vous."),
 ("Qui réalise les travaux ?", "PLU Value ne réalise pas de travaux. Nous faisons chiffrer les travaux nécessaires par des entreprises et nous les intégrons à l'étude. Leur réalisation et leur prise en charge sont précisées au contrat ; en règle générale, les lots sont vendus en l'état et les aménagements reviennent aux acquéreurs."),
 ("Qui commercialise les futurs logements ?", "La vente est assurée par des professionnels habilités : l'agence qui vous accompagne déjà, ou une agence partenaire. PLU Value ne vend pas et ne publie pas d'annonces : nous transmettons à l'agence les plans et les documents techniques des lots."),
 ("Quels délais prévoir ?", "Ils varient selon le dossier. À titre indicatif, l'instruction d'une déclaration préalable dure en principe un mois et celle d'un permis d'aménager trois mois, auxquels s'ajoutent les délais de recours des tiers après affichage et la préparation des dossiers. Nous vous présentons un calendrier propre à votre projet."),
 ("Une division est-elle toujours possible ?", "Non. Elle dépend du PLU, des servitudes, de la configuration du terrain et du bâtiment, des réseaux et de l'intérêt économique de l'opération. C'est précisément ce que notre étude préalable vérifie."),
 ("Un agent immobilier peut-il nous présenter un bien sans perdre son mandat ?", "Oui. Le dépôt est horodaté et couvert par notre charte de confidentialité et de non-contournement : nous ne contactons pas le propriétaire sans l'agent, pendant 24 mois, et sa rémunération est due si une opération se fait."),
 ("Comment PLU Value est-il rémunéré ?", "Notre rémunération est liée à la valorisation obtenue : nous sommes payés quand le projet réussit, selon les modalités écrites au contrat. Nous n'avons donc aucun intérêt à engager des dépenses dans un projet qui ne fonctionne pas."),
]
FAQ_HTML, FAQ_LD = faq_block(FAQ)

SOLUTIONS3 = f"""<div class="grid3">
      <a class="card" href="/division-maison-logements"><span class="k">1 · Le bâtiment</span><h3>Diviser une maison</h3><p class="hint">Étudier la création de plusieurs logements indépendants dans une construction existante.</p><em>Diviser une maison →</em></a>
      <a class="card" href="/division-terrain"><span class="k">2 · Le terrain</span><h3>Valoriser le terrain</h3><p class="hint">Étudier le détachement d'une parcelle ou une construction complémentaire.</p><em>Division de terrain →</em></a>
      <a class="card" href="/nos-solutions#immeuble"><span class="k">3 · L'immeuble</span><h3>Réorganiser un immeuble</h3><p class="hint">Étudier la création de lots indépendants destinés à une vente séparée.</p><em>En savoir plus →</em></a>
    </div>"""

TIMELINE = """<ol class="steps">
      <li><div><h3>Analyse du bien</h3><p>Lecture du PLU, du cadastre, des servitudes et des ventes réelles du secteur.</p></div></li>
      <li><div><h3>Étude des scénarios</h3><p>Division du bâtiment, du terrain, ou les deux : chaque scénario est chiffré.</p></div></li>
      <li><div><h3>Validation de la faisabilité</h3><p>Nous vous présentons ce qui est réaliste, ce qui ne l'est pas, et pourquoi.</p></div></li>
      <li><div><h3>Préparation juridique et technique</h3><p>Architecte, géomètre-expert, avocat, devis de travaux, mise en copropriété si nécessaire.</p></div></li>
      <li><div><h3>Autorisations et division</h3><p>Dépôt des dossiers d'urbanisme, suivi de l'instruction, division juridique avec le notaire.</p></div></li>
      <li><div><h3>Préparation de la remise en vente</h3><p>Plans et documents techniques transmis à l'agence habilitée, qui commercialise les lots.</p></div></li>
    </ol>"""

# ---------- ACCUEIL ----------
P[""] = ("PLU Value | Valorisation et division immobilière",
 "Maison trop grande, vente bloquée ou succession ? PLU Value étudie la division de maisons et de terrains et investit dans la préparation des projets retenus.",
 f"""  <section aria-labelledby="h-hero">
    <div class="hero-grid">
      <div style="display:grid;gap:18px">
        <span class="eyebrow">Partenariat de valorisation immobilière</span>
        <h1 id="h-hero">Avant de vendre votre maison, découvrez tout son potentiel.</h1>
        <p class="lead">Division de maison, création de logements indépendants, valorisation de terrain : PLU Value étudie les possibilités de votre patrimoine et investit dans la préparation des projets qu'elle sélectionne.</p>
        <div class="cta"><a class="btn primary" href="/deposer-un-bien">Faire étudier mon bien</a><a class="btn ghost" href="/nos-solutions">Découvrir nos solutions</a></div>
        <p class="reassure"><span>Étude préalable gratuite</span><span>Accompagnement technique et juridique</span><span>Montage juridique et financier</span></p>
      </div>
      <figure class="shot"><img src="/media/maison-avant.webp" alt="Pavillon des années 1970 avec garage et jardin" width="439" height="439"></figure>
    </div>
  </section>

  <section aria-labelledby="h-sit">
    <h2 id="h-sit">Votre bien mérite peut-être une autre stratégie.</h2>
    <div class="grid4">
      <a class="card" href="/valoriser-maison-familiale"><h3>« Ma maison est devenue trop grande. »</h3><em>Découvrir ses possibilités →</em></a>
      <a class="card" href="/succession-maison-familiale"><h3>« J'ai hérité d'une maison familiale. »</h3><em>Avant de décider →</em></a>
      <a class="card" href="/valoriser-maison-familiale#vente"><h3>« Mon bien ne trouve pas d'acheteur. »</h3><em>Une autre approche →</em></a>
      <a class="card" href="/division-terrain"><h3>« Je souhaite valoriser une partie de mon terrain. »</h3><em>Division de terrain →</em></a>
    </div>
  </section>

  <section aria-labelledby="h-sol">
    <span class="eyebrow">Une maison. Plusieurs possibilités.</span>
    <h2 id="h-sol">Une propriété peut offrir plusieurs possibilités.</h2>
    {SOLUTIONS3}
    {TERRAIN_PAIR}
    {SIM}
  </section>

  <section aria-labelledby="h-acc">
    <h2 id="h-acc">Nous nous occupons de la complexité du projet.</h2>
    <p>Urbanisme, architecture, géomètre, juridique, copropriété, devis de travaux : nous coordonnons les compétences nécessaires aux opérations retenues, pour que vous preniez vos décisions avec une vision claire.</p>
    {TIMELINE}
    <div><a class="btn ghost" href="/notre-methode">Voir notre méthode en détail</a></div>
  </section>

  <section class="dark" aria-labelledby="h-inv">
    <span class="eyebrow">Notre modèle</span>
    <h2 id="h-inv">Un accompagnement dans lequel nous investissons aussi.</h2>
    {PARTNER}
    <p>Vous apportez votre bien. Nous investissons dans son potentiel : pour les projets que nous sélectionnons, nous engageons nos moyens dans les études et mobilisons les professionnels nécessaires. Notre rémunération est liée à la valorisation prévue au contrat.</p>
    <p><b>Nous n'avons pas intérêt à engager des dépenses dans un projet qui ne fonctionne pas.</b> C'est pourquoi chaque dossier est étudié avec rigueur avant toute proposition.</p>
    <div><a class="btn gold" href="/nos-engagements">Comprendre nos engagements</a></div>
  </section>

  <section aria-labelledby="h-off">
    <h2 id="h-off">Trois façons de travailler ensemble</h2>
    <div class="grid3">
      <div class="card"><span class="k">Partenariat de valorisation</span><h3>Vous restez propriétaire</h3><p class="hint">Nous engageons nos moyens dans la préparation du projet ; la valeur créée est partagée selon le contrat.</p></div>
      <div class="card"><span class="k">Acquisition</span><h3>Une offre d'achat, quand c'est pertinent</h3><p class="hint">Étudiée au cas par cas, toujours sous conditions suspensives, notamment d'autorisation d'urbanisme.</p></div>
      <div class="card"><span class="k">Grands projets</span><h3>Un montage avec des partenaires</h3><p class="hint">Pour les terrains et immeubles plus importants, avec des investisseurs ou promoteurs partenaires.</p></div>
    </div>
    <p class="hint">Ces approches ne s'appliquent pas automatiquement à tous les biens : elles dépendent de l'étude. <a href="/nos-engagements">Conditions et engagements</a>.</p>
  </section>

{EXPERTISE}
  <section aria-labelledby="h-eq">
    <h2 id="h-eq">Les personnes derrière PLU Value</h2>
    {TEAM}
    <p class="hint">Nous travaillons avec des architectes, des géomètres-experts, des notaires et des agences immobilières habilitées. <a href="/equipe">Découvrir l'équipe</a>.</p>
  </section>

  <section aria-labelledby="h-mis">
    <h2 id="h-mis">Créer les logements de demain à partir de ceux d'aujourd'hui.</h2>
    <figure class="shot"><img src="/media/site-accueil.webp" alt="Vue aérienne d'un quartier pavillonnaire au coucher du soleil" width="1536" height="864" loading="lazy"></figure>
    <p>Partout, on manque de logements, et le parc existant est une ressource sous-utilisée : de grandes maisons occupées par une ou deux personnes, de grands jardins difficiles à entretenir. Les transformer intelligemment, sans artificialiser de nouveaux terrains, c'est une contribution concrète, à notre échelle, au besoin de logements.</p>
  </section>
{FAQ_HTML}{FINAL_CTA}""", FAQ_LD)

# ---------- NOS SOLUTIONS ----------
P["nos-solutions"] = ("Nos solutions : diviser une maison, un terrain, un immeuble | PLU Value",
 "Division de maison en plusieurs logements, division de terrain, réorganisation de petits immeubles : les solutions de valorisation immobilière étudiées par PLU Value.",
 f"""  <section aria-labelledby="h1">
    <span class="eyebrow">Nos solutions</span>
    <h1 id="h1">Une maison. Plusieurs possibilités.</h1>
    <p class="lead">Chaque bien est différent. Nous étudions toutes les pistes que le PLU, le bâtiment et le marché permettent, et nous ne retenons que celles qui tiennent.</p>
  </section>
  <section id="maison" aria-labelledby="h-m">
    <span class="k">1 · Le bâtiment</span>
    <h2 id="h-m">Diviser une maison en plusieurs logements</h2>
    <div class="grid2"><div style="display:grid;gap:14px"><p>Une maison familiale devenue trop grande peut, quand la configuration le permet, accueillir deux logements autonomes, chacun avec son entrée. Deux logements de taille moyenne rencontrent souvent une demande différente de celle d'une grande maison unique.</p><a class="btn ghost" href="/division-maison-logements">Diviser une maison en 2 logements</a></div>{MAISON_BA}</div>
    {SIM}
  </section>
  <section id="terrain" aria-labelledby="h-t">
    <span class="k">2 · Le terrain</span>
    <h2 id="h-t">Détacher un lot à bâtir</h2>
    <p>Une maison sur un terrain généreux peut garder un jardin à sa mesure, tandis qu'une partie devient un terrain constructible, recherché par les familles qui veulent faire construire.</p>
    {TERRAIN_PAIR}
    <div><a class="btn ghost" href="/division-terrain">Division de terrain</a></div>
    {SIM}
  </section>
  <section id="immeuble" aria-labelledby="h-i">
    <span class="k">3 · L'immeuble</span>
    <h2 id="h-i">Réorganiser une maison de ville ou un petit immeuble</h2>
    <p>Une grande maison de ville ou un immeuble ancien peut parfois être réorganisé en plusieurs appartements vendus séparément, avec une mise en copropriété. Nous étudions la faisabilité réglementaire, technique et économique avant toute proposition.</p>
    <p class="note">Nous préparons des exemples documentés pour cette solution : ils seront publiés dès qu'un dossier réel pourra l'être.</p>
  </section>
  <section aria-labelledby="h-c">
    <h2 id="h-c">Et si plusieurs solutions se combinent ?</h2>
    <p>C'est fréquent : une maison divisée en deux logements et un lot à bâtir détaché du jardin, par exemple. L'étude compare les scénarios et retient celui qui crée le plus de valeur pour un risque raisonnable.</p>
    <div class="cta"><a class="btn primary" href="/deposer-un-bien">Faire étudier mon bien</a><a class="btn ghost" href="/exemples-valorisation">Voir des exemples</a></div>
  </section>
{FINAL_CTA}""")

# ---------- PROPRIÉTAIRES ----------
P["valoriser-maison-familiale"] = ("Valoriser une maison familiale avant de la vendre | PLU Value",
 "Maison devenue trop grande, vente qui traîne, transmission à préparer : PLU Value étudie les possibilités de votre maison familiale et investit dans les projets retenus.",
 f"""  <section aria-labelledby="h1">
    <div class="hero-grid">
      <div style="display:grid;gap:18px">
        <span class="eyebrow">Propriétaires de maisons familiales</span>
        <h1 id="h1">Votre maison a accompagné une grande partie de votre vie.</h1>
        <p class="lead">Avant de la vendre ou de la transmettre, découvrez toutes ses possibilités. Nous étudions ce qu'elle permet, et nous coordonnons les professionnels nécessaires pour les projets que nous retenons.</p>
        <div class="cta"><a class="btn primary" href="/deposer-un-bien?profil=proprietaire">Faire étudier ma maison</a></div>
      </div>
      <figure class="shot"><img src="/media/maison-avant.webp" alt="Pavillon des années 1970 avec garage et jardin" width="439" height="439"></figure>
    </div>
  </section>
  <section aria-labelledby="h-s">
    <h2 id="h-s">Vous vous reconnaissez peut-être</h2>
    <div class="grid2">
      <div class="card"><ul><li>La maison est devenue trop grande depuis le départ des enfants.</li><li>Le jardin est devenu difficile à entretenir.</li><li>Vous préparez un déménagement ou un changement de vie.</li></ul></div>
      <div class="card"><ul><li>Vous souhaitez anticiper la transmission de votre patrimoine.</li><li>Votre maison est en vente depuis trop longtemps.</li><li>Vous cherchez une solution pour mieux la valoriser.</li></ul></div>
    </div>
  </section>
  <section aria-labelledby="h-p">
    <h2 id="h-p">Ce que votre maison peut permettre</h2>
    {SOLUTIONS3}
  </section>
  <section id="vente" aria-labelledby="h-v">
    <h2 id="h-v">Votre maison ne trouve pas d'acheteur ?</h2>
    <p>Une grande maison peut être difficile à vendre parce que son prix global dépasse le budget d'une partie des acheteurs, même quand le prix au mètre carré est juste. Avant de baisser votre prix, il existe peut-être une autre manière de la valoriser : deux biens plus accessibles au lieu d'un seul. Cela ne vaut pas pour toutes les maisons, et c'est ce que l'étude vérifie.</p>
  </section>
  <section class="dark" aria-labelledby="h-m">
    <h2 id="h-m">Vous apportez votre bien. Nous investissons dans son potentiel.</h2>
    <ul class="steps">
      <li><div><h3>Vous restez propriétaire</h3><p>Dans le partenariat de valorisation, vous gardez votre bien et vos décisions.</p></div></li>
      <li><div><h3>Nous engageons nos moyens</h3><p>Études, architecte, géomètre-expert, avocat : financés par PLU Value pour les projets retenus, selon le contrat.</p></div></li>
      <li><div><h3>Nous réussissons quand vous réussissez</h3><p>Notre rémunération est liée à la valorisation obtenue.</p></div></li>
    </ul>
    <div><a class="btn gold" href="/nos-engagements">Nos engagements en détail</a></div>
  </section>
{FAQ_HTML.replace('h-faq','h-faq2')}{FINAL_CTA}""")

# ---------- DIVISION MAISON ----------
P["division-maison-logements"] = ("Diviser une maison en 2 logements | PLU Value",
 "Peut-on diviser une maison en deux logements ? Règles du PLU, accès, copropriété, travaux, vente séparée : PLU Value étudie et prépare la division de maisons.",
 f"""  <section aria-labelledby="h1">
    <span class="eyebrow">Division de maison</span>
    <h1 id="h1">Diviser une maison en plusieurs logements</h1>
    <p class="lead">Une maison familiale devenue trop grande peut, dans certains cas, accueillir deux logements indépendants vendus séparément. Nous étudions si c'est possible, et à quelles conditions.</p>
    {MAISON_BA}
    {SIM}
  </section>
  <section aria-labelledby="h-q">
    <h2 id="h-q">Ce qu'il faut vérifier</h2>
    <div class="grid2">
      <div class="card"><h3>Les règles d'urbanisme</h3><p class="hint">Le PLU peut encadrer la création de logements : stationnement exigé par logement, surfaces minimales, destination. Certaines divisions demandent une autorisation d'urbanisme, et certaines communes imposent une autorisation préalable de division.</p></div>
      <div class="card"><h3>Le bâtiment</h3><p class="hint">Accès séparés, répartition des pièces, réseaux (eau, électricité, assainissement), isolation phonique et sécurité incendie entre les deux logements.</p></div>
      <div class="card"><h3>Le cadre juridique</h3><p class="hint">Pour vendre deux logements séparément dans un même bâtiment, une mise en copropriété est généralement nécessaire : état descriptif de division et règlement de copropriété, établis avec un géomètre-expert et un notaire.</p></div>
      <div class="card"><h3>L'intérêt économique</h3><p class="hint">Deux logements ne valent pas toujours plus qu'une maison. Nous comparons les prix réels du secteur, les coûts de division et les travaux à prévoir avant de proposer quoi que ce soit.</p></div>
    </div>
    <p class="sources">À consulter : <a href="https://www.service-public.gouv.fr/particuliers/vosdroits/N319">service-public.gouv.fr, autorisations d'urbanisme</a> ; <a href="https://www.geoportail-urbanisme.gouv.fr/">Géoportail de l'urbanisme</a> pour le PLU de votre commune.</p>
  </section>
  <section aria-labelledby="h-r">
    <h2 id="h-r">Ce que PLU Value prend en charge</h2>
    {TIMELINE}
    <p class="note">PLU Value ne réalise pas les travaux : nous les faisons chiffrer et les intégrons à l'étude. Leur prise en charge est précisée au contrat.</p>
  </section>
{FINAL_CTA}""")

# ---------- DIVISION TERRAIN ----------
P["division-terrain"] = ("Division de terrain | PLU Value",
 "Détacher un lot à bâtir de son terrain : constructibilité, PLU, géomètre, déclaration préalable ou permis d'aménager. PLU Value étudie et prépare la division de terrains.",
 f"""  <section aria-labelledby="h1">
    <span class="eyebrow">Division de terrain</span>
    <h1 id="h1">Valoriser une partie de votre terrain</h1>
    <p class="lead">Une maison sur un grand terrain peut garder un jardin à sa mesure, tandis qu'une partie devient un lot à bâtir. Nous étudions la constructibilité et nous préparons la division pour les projets retenus.</p>
    {TERRAIN_PAIR}
    {SIM}
  </section>
  <section aria-labelledby="h-v">
    <h2 id="h-v">Les points clés d'une division de terrain</h2>
    <div class="grid2">
      <div class="card"><h3>La constructibilité</h3><p class="hint">Zone du PLU, emprise au sol, distances aux limites, hauteur, espaces verts à conserver, prescriptions (espaces boisés, cœurs d'îlot).</p></div>
      <div class="card"><h3>L'accès et les réseaux</h3><p class="hint">Le nouveau lot doit être desservi : façade sur rue ou servitude de passage, raccordements possibles.</p></div>
      <div class="card"><h3>L'autorisation</h3><p class="hint">Selon les cas, une déclaration préalable ou un permis d'aménager, préparés avec un géomètre-expert qui établit le plan de division et le bornage.</p></div>
      <div class="card"><h3>Le prix de sortie</h3><p class="hint">Valeur des terrains à bâtir et des maisons du secteur, d'après les ventes réellement enregistrées (DVF).</p></div>
    </div>
    <p class="sources">À consulter : <a href="https://www.service-public.gouv.fr/particuliers/vosdroits/F17578">service-public.gouv.fr, déclaration préalable</a> ; <a href="https://www.geoportail-urbanisme.gouv.fr/">Géoportail de l'urbanisme</a> ; <a href="https://www.georisques.gouv.fr/">Géorisques</a> pour les risques naturels.</p>
  </section>
  <section aria-labelledby="h-o">
    <h2 id="h-o">Votre jardin cache peut-être un terrain à bâtir</h2>
    <p>Présentez-nous l'adresse : nous vous disons sous 72 heures, une fois le dossier complet, si une division paraît réaliste.</p>
    <div><a class="btn primary" href="/deposer-un-bien?profil=proprietaire">Faire étudier mon terrain</a></div>
  </section>
{FINAL_CTA}""")

# ---------- SUCCESSION ----------
P["succession-maison-familiale"] = ("Maison héritée : vente et valorisation | PLU Value",
 "Vous avez hérité d'une maison ? Avant de la vendre en l'état, PLU Value étudie si d'autres possibilités peuvent mieux valoriser ce patrimoine familial, en lien avec votre notaire.",
 f"""  <section aria-labelledby="h1">
    <span class="eyebrow">Succession et patrimoine familial</span>
    <h1 id="h1">Vous avez hérité d'une maison ?</h1>
    <p class="lead">Avant de la vendre en l'état, découvrez si d'autres possibilités peuvent mieux valoriser ce patrimoine. Une étude claire aide aussi plusieurs héritiers à décider ensemble.</p>
    <div class="cta"><a class="btn primary" href="/deposer-un-bien?profil=heritier">Faire étudier la maison</a></div>
  </section>
  <section aria-labelledby="h-s">
    <h2 id="h-s">Les situations que nous rencontrons</h2>
    <div class="grid2">
      <div class="card"><ul><li>La maison est trop grande pour les besoins de chacun.</li><li>Elle est difficile à vendre au prix espéré.</li><li>Son entretien pèse en attendant la décision.</li></ul></div>
      <div class="card"><ul><li>Plusieurs héritiers doivent prendre une décision commune.</li><li>Vous voulez connaître toutes les possibilités avant de vendre.</li><li>Il faut l'accord de chacun pour avancer.</li></ul></div>
    </div>
  </section>
  <section aria-labelledby="h-a">
    <h2 id="h-a">Ce que nous apportons</h2>
    <p>Une étude chiffrée de chaque scénario (vente en l'état, division de la maison, lot à bâtir), sur laquelle chacun peut s'appuyer. Pour les projets retenus, nous engageons nos moyens dans leur préparation. Un premier lot vendu peut aussi donner de la trésorerie, tandis que le reste se vend au bon prix.</p>
    <div class="case"><span class="k">Cas réel</span><p>Des héritiers devaient vendre vite. Le premier lot s'est vendu en moins de deux mois, ce qui a laissé le temps de vendre le reste au bon prix.</p></div>
    <p class="note">PLU Value ne se substitue ni au notaire chargé de la succession, ni aux décisions des héritiers. Nous travaillons avec votre notaire, et rien ne se fait sans l'accord des personnes concernées.</p>
  </section>
{FINAL_CTA}""")

# ---------- MÉTHODE ----------
P["notre-methode"] = ("Notre méthode de valorisation immobilière | PLU Value",
 "Du premier contact à la remise en vente : analyse, scénarios, faisabilité, préparation juridique et technique, autorisations, commercialisation. La méthode PLU Value.",
 f"""  <section aria-labelledby="h1">
    <span class="eyebrow">Notre méthode</span>
    <h1 id="h1">Du premier contact à la remise en vente</h1>
    <p class="lead">Une méthode conçue avec Me Pierre-Henry Blanc, avocat en droit de l'urbanisme depuis 30 ans, et appliquée à chaque dossier.</p>
  </section>
  <section aria-labelledby="h-e">
    <h2 id="h-e">Les étapes</h2>
    <ol class="steps">
      <li><div><h3>Vous nous présentez le bien</h3><p>Quelques informations suffisent pour commencer. Accusé de réception rapide, en journée.</p></div></li>
      <li><div><h3>Étude préalable gratuite</h3><p>PLU, cadastre, servitudes, risques, ventes réelles du secteur. Réponse sous 72 heures une fois le dossier complet : le bien est retenu, ou nous expliquons pourquoi il ne l'est pas.</p></div></li>
      <li><div><h3>Sélection et proposition</h3><p>Pour les dossiers retenus, nous présentons les scénarios chiffrés et les conditions du partenariat, par écrit.</p></div></li>
      <li><div><h3>Préparation juridique et technique</h3><p>Architecte, géomètre-expert, avocat, devis de travaux, état descriptif de division et copropriété si nécessaire.</p></div></li>
      <li><div><h3>Autorisations et division</h3><p>Dépôt des dossiers d'urbanisme, suivi de l'instruction, division juridique avec le notaire.</p></div></li>
      <li><div><h3>Remise en vente</h3><p>Plans et documents techniques transmis à l'agence habilitée, qui seule commercialise les lots. Les actes se signent chez le notaire.</p></div></li>
    </ol>
  </section>
{EXPERTISE.replace('<a href="/notre-methode">Voir notre méthode</a>', '<a href="/nos-engagements">Voir nos engagements</a>')}
{FINAL_CTA}""")

# ---------- ENGAGEMENTS ----------
P["nos-engagements"] = ("Notre modèle et nos engagements | PLU Value",
 "Partenariat de valorisation immobilière : ce que PLU Value finance, comment il est rémunéré, ce que perçoit le propriétaire, la confidentialité et les risques présentés en toute transparence.",
 f"""  <section aria-labelledby="h1">
    <span class="eyebrow">Notre modèle</span>
    <h1 id="h1">Un partenariat fondé sur la création de valeur</h1>
    {PARTNER}
    <p class="lead">Certains biens possèdent un potentiel qui ne se révèle pas dans une vente classique. Plutôt que de vous vendre une étude, nous pouvons nous associer à votre projet de valorisation.</p>
  </section>
  <section aria-labelledby="h-c">
    <h2 id="h-c">Ce qui change avec PLU Value</h2>
    <table class="cmp"><thead><tr><th>Un prestataire classique</th><th>PLU Value</th></tr></thead><tbody>
      <tr><td>Vous vend une étude</td><td>Investit dans le potentiel de votre bien</td></tr>
      <tr><td>Vous accompagne</td><td>Devient partenaire de sa valorisation</td></tr>
      <tr><td>Vous facture ses prestations</td><td>Engage ses moyens dans le projet</td></tr>
      <tr><td>Vous laisse les démarches</td><td>Pilote la préparation jusqu'à la remise en vente</td></tr>
    </tbody></table>
  </section>
  <section class="dark" aria-labelledby="h-w">
    <h2 id="h-w">Nous n'avons pas intérêt à engager des dépenses dans un projet qui ne fonctionne pas.</h2>
    <p>Pour les projets que nous sélectionnons, nous finançons les études et les intervenants prévus au contrat. Notre rémunération est liée à la valorisation obtenue. Nos intérêts sont donc alignés avec les vôtres : c'est ce qui nous oblige à étudier chaque dossier avec rigueur.</p>
    <p>Aligner nos intérêts ne veut pas dire qu'il n'y a aucun risque : délais, autorisations, marché. Nous les présentons avant toute signature.</p>
  </section>
  <section id="remuneration" aria-labelledby="h-r">
    <h2 id="h-r">Comment fonctionne notre rémunération ?</h2>
    <div class="grid2">
      <div class="card"><span class="k">Partenariat de valorisation</span><ul>
        <li>Vous restez propriétaire.</li>
        <li>Un prix de référence est fixé ensemble au départ.</li>
        <li>La valeur créée au-delà de ce prix est partagée entre vous et PLU Value, selon une répartition écrite au contrat.</li>
        <li>Les frais engagés par PLU Value et sa part sont réglés chez le notaire, lors des ventes, à partir du premier lot vendu.</li>
        <li>La durée du contrat est fixée à l'avance.</li></ul></div>
      <div class="card"><span class="k">Acquisition</span><ul>
        <li>Une offre d'achat à un prix convenu.</li>
        <li>Toujours sous conditions suspensives, notamment l'obtention de l'autorisation d'urbanisme.</li>
        <li>Réalisée directement ou par un investisseur partenaire, ce qui vous est indiqué dès l'offre.</li></ul></div>
    </div>
    <p class="note">Les montants, la répartition, la durée et les cas de sortie sont propres à chaque projet et figurent dans le contrat que vous recevez avant toute signature. Nous ne promettons ni vente garantie, ni plus-value garantie.</p>
  </section>
  <section aria-labelledby="h-e">
    <h2 id="h-e">Nos engagements</h2>
    <div class="grid2">
      <div class="card"><ul><li>Transparence sur le déroulement du projet.</li><li>Explication écrite des conditions financières.</li><li>Prise en charge des études selon le contrat.</li><li>Présentation des risques, délais et conditions de faisabilité.</li></ul></div>
      <div class="card"><ul><li>Respect des intérêts du vendeur et de ses décisions.</li><li>Respect des mandats immobiliers existants.</li><li>Protection des agents apporteurs (charte de 24 mois).</li><li>Confidentialité des informations communiquées.</li></ul></div>
    </div>
  </section>
{FAQ_HTML.replace('h-faq','h-faq3')}{FINAL_CTA}""", FAQ_LD)

# ---------- EXEMPLES ----------
P["exemples-valorisation"] = ("Exemples de valorisation immobilière | PLU Value",
 "Comprendre le raisonnement d'une valorisation : bien de départ, contraintes, scénarios étudiés. Simulations clairement identifiées et cas réels lorsqu'ils peuvent être publiés.",
 f"""  <section aria-labelledby="h1">
    <span class="eyebrow">Exemples</span>
    <h1 id="h1">Comprendre une valorisation, étape par étape</h1>
    <p class="lead">Nous ne publions que des cas réels autorisés et des simulations présentées comme telles. Aucun témoignage ni résultat n'est inventé.</p>
  </section>
  <section aria-labelledby="h-c1">
    <span class="k">Cas réel · succession</span>
    <h2 id="h-c1">Des héritiers qui devaient vendre vite</h2>
    <div class="grid2">
      <div class="card"><h3>La situation</h3><p class="hint">Des héritiers devaient réunir rapidement la somme nécessaire au règlement de la succession.</p></div>
      <div class="card"><h3>Le résultat constaté</h3><p class="hint">Le bien a été divisé ; le premier lot s'est vendu en moins de deux mois, ce qui a laissé le temps de vendre le reste au bon prix.</p></div>
    </div>
    <p class="note">Le détail chiffré de ce dossier sera publié avec l'accord des personnes concernées.</p>
  </section>
  <section aria-labelledby="h-s1">
    <span class="k">Simulation de principe · terrain</span>
    <h2 id="h-s1">Une maison sur 1 100 m² de terrain</h2>
    {TERRAIN_PAIR}
    <ul class="steps">
      <li><div><h3>Le bien de départ</h3><p>Une maison sur un terrain de 1 100 m², en vente depuis plusieurs mois.</p></div></li>
      <li><div><h3>La difficulté</h3><p>Le prix total dépasse le budget de la plupart des acheteurs du quartier.</p></div></li>
      <li><div><h3>Le scénario étudié</h3><p>La maison conservée sur 620 m² ; un lot à bâtir de 480 m² détaché.</p></div></li>
      <li><div><h3>Ce qu'il faut vérifier</h3><p>Constructibilité du lot, accès, réseaux, prix des terrains à bâtir du secteur, coût du géomètre et des autorisations.</p></div></li>
    </ul>
    {SIM}
  </section>
  <section aria-labelledby="h-s2">
    <span class="k">Simulation de principe · bâtiment</span>
    <h2 id="h-s2">Un pavillon divisé en deux logements</h2>
    {MAISON_BA}
    <p>Un pavillon des années 1970 sur sous-sol, devenu trop grand. Scénario étudié : deux logements indépendants avec deux entrées, mise en copropriété, vente séparée. À vérifier : règles du PLU (stationnement notamment), réseaux, isolation entre logements, prix des appartements du secteur.</p>
    {SIM}
  </section>
{FINAL_CTA}""")

# ---------- ÉQUIPE ----------
P["equipe"] = ("Les fondateurs de PLU Value | PLU Value",
 "Me Pierre-Henry Blanc, avocat en droit de l'urbanisme depuis 30 ans, et Yannis Amallah, entrepreneur : les fondateurs de PLU Value et les professionnels avec lesquels ils travaillent.",
 f"""  <section aria-labelledby="h1">
    <span class="eyebrow">Qui sommes-nous ?</span>
    <h1 id="h1">Une équipe engagée dans chaque projet</h1>
    <p class="lead">Notre conviction : les logements de demain existent déjà. Ils dorment dans des maisons trop grandes et des terrains trop vastes. Notre métier est de les révéler.</p>
  </section>
  <section aria-labelledby="h-f">
    <h2 id="h-f">Les fondateurs</h2>
    {TEAM}
  </section>
  <section aria-labelledby="h-p">
    <h2 id="h-p">Nos partenaires</h2>
    <p>Nous travaillons avec des architectes, des géomètres-experts, des notaires, des agences immobilières et, pour les projets plus importants, des investisseurs et promoteurs partenaires.</p>
    <p class="hint">PLU Value est une marque exploitée par LATULIPE SAS, RCS Nîmes 921 470 951.</p>
  </section>
{FINAL_CTA}""")

with open("/home/claude/v2/_pages_a.py.done", "w") as f:
    f.write("ok")
