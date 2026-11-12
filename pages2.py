# -*- coding: utf-8 -*-
import re
from base import page, ba_slider, TERRAIN_PAIR, MAISON_BA, SIM, TEAM, FINAL_CTA, PARTNER, faq_block
from pages import P

CHARTE = open("/home/claude/v2/_charte_details.html").read().replace('class="charter" id="charte-texte"', 'class="charter" id="charte-texte"')

# ---------- formulaire agent (repris à l'identique : mêmes noms de champs) ----------
dep = open("/home/claude/site/_deposer.html").read()
a = dep.find('<form enctype="multipart/form-data" method="post" name="documents-bien">')
b = dep.find('</section>')
dep = dep[a:b]
dep = dep.replace('<form enctype="multipart/form-data" method="post" name="documents-bien">',
                  '<form enctype="multipart/form-data" method="post" name="documents-bien" data-netlify="true" hidden>')
dep = dep.replace('<input type="file" name="document"></form>',
                  '<input type="file" name="document"><input name="form-name" value="documents-bien"></form>')
dep = dep.replace('<form enctype="multipart/form-data" id="depot" method="POST" name="depot-bien" novalidate="">',
                  '<form enctype="multipart/form-data" id="depot" method="POST" name="depot-bien" data-netlify="true" netlify-honeypot="bot-field" novalidate="">\n'
                  '      <input type="hidden" name="form-name" value="depot-bien">\n'
                  '      <input type="hidden" name="reference" id="reference">\n'
                  '      <input type="hidden" name="horodatage" id="horodatage">')
dep = re.sub(r'\n\s*\n\s*\n\s*\n', '\n', dep)
dep = dep.replace('https://plu-value.fr/#charte-texte', '#charte-texte')
dep = dep.replace('<div class="receipt" id="receipt" tabindex="-1">', '<div class="receipt" id="receipt" tabindex="-1" hidden>')
dep = dep.replace('<span class="error" id="err" role="alert"></span>', '<span class="error" id="err" role="alert" hidden></span>')
dep = dep.replace('<p class="hint" id="r-preview">', '<p class="hint" id="r-preview" hidden>')
dep = dep.replace('<legend><span class="mono">A</span> Vous</legend>', '<legend>Vous</legend>').replace('<legend><span class="mono">B</span> Le bien</legend>', '<legend>Le bien</legend>').replace('<legend><span class="mono">C</span> Le vendeur</legend>', '<legend>Le vendeur</legend>')
DEP_FORM = dep

FORMS_JS = """<script>
(function(){
  var isPreview=/claude|localhost|^$/.test(location.hostname)||location.protocol==='file:';
  function ref(){var d=new Date(),p=function(n){return String(n).padStart(2,'0')};return 'PLV-'+d.getFullYear()+p(d.getMonth()+1)+p(d.getDate())+'-'+Math.random().toString(36).slice(2,6).toUpperCase()}
  function stamp(){return new Date().toLocaleString('fr-FR',{dateStyle:'long',timeStyle:'short'})}
  /* profils */
  var radios=document.querySelectorAll('input[name=profil-choix]');
  function show(v){document.querySelectorAll('[data-for]').forEach(function(el){el.hidden=el.dataset.for.split(' ').indexOf(v)<0});
    var pf=document.getElementById('d-profil');if(pf)pf.value=v;}
  radios.forEach(function(r){r.addEventListener('change',function(){show(r.value)})});
  var q=new URLSearchParams(location.search).get('profil');
  if(q){var r=document.querySelector('input[name=profil-choix][value="'+q+'"]');if(r){r.checked=true;show(q)}}
  /* formulaires simples */
  document.querySelectorAll('form[data-simple]').forEach(function(f){
    var err=f.querySelector('.err'),btn=f.querySelector('button[type=submit]'),ok=document.getElementById(f.dataset.ok),label=btn.textContent;
    f.addEventListener('submit',function(e){
      e.preventDefault();err.hidden=true;
      var miss=[].filter.call(f.querySelectorAll('[required]'),function(el){return el.type==='checkbox'?!el.checked:!el.value.trim()});
      if(miss.length){miss[0].focus();err.textContent=miss[0].type==='checkbox'?'Cochez la case d’accord pour envoyer.':'Complétez les champs marqués *.';err.hidden=false;return}
      var em=f.querySelector('input[type=email]');if(em&&!em.checkValidity()){em.focus();err.textContent='L’adresse e-mail semble incomplète.';err.hidden=false;return}
      var rf=f.querySelector('input[name=reference]'),r=ref();if(rf)rf.value=r;
      btn.disabled=true;btn.textContent='Envoi…';
      var fd=new FormData(f),hasFile=f.querySelector('input[type=file]')&&f.querySelector('input[type=file]').files.length;
      var opts=hasFile?{method:'POST',body:fd}:{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:new URLSearchParams(fd).toString()};
      if(isPreview){err.textContent='Aperçu : l’envoi fonctionnera une fois la page en ligne.';err.hidden=false;btn.disabled=false;btn.textContent=label;return}
      fetch('/',opts).then(function(x){if(!x.ok)throw 0;f.hidden=true;var s=ok.querySelector('.ref');if(s)s.textContent=r;ok.hidden=false;ok.focus()})
        .catch(function(){btn.disabled=false;btn.textContent=label;err.textContent='L’envoi n’a pas abouti. Écrivez-nous à contact@plu-value.fr ou au 07 56 98 67 00.';err.hidden=false});
    });
  });
  /* dépôt agent (horodaté, pièces jointes) */
  var form=document.getElementById('depot');if(!form)return;
  var err=document.getElementById('err'),btn=document.getElementById('send'),receipt=document.getElementById('receipt');
  form.addEventListener('submit',async function(e){
    e.preventDefault();err.hidden=true;
    var missing=[].filter.call(form.querySelectorAll('[required]'),function(el){return el.type==='checkbox'?!el.checked:!el.value.trim()});
    if(missing.length){missing[0].focus();err.textContent=missing[0].type==='checkbox'?'Cochez les deux cases d’acceptation pour envoyer.':'Complétez les champs marqués * avant d’envoyer.';err.hidden=false;return}
    var em=document.getElementById('agent-email');if(!em.checkValidity()){em.focus();err.textContent='L’adresse e-mail semble incomplète.';err.hidden=false;return}
    var files=[].slice.call(document.getElementById('bien-fichiers').files);
    var big=files.filter(function(f){return f.size>8*1024*1024});
    if(big.length){err.textContent='« '+big[0].name+' » dépasse 8 Mo. Ajoutez plutôt un lien de téléchargement.';err.hidden=false;return}
    if(files.length>15){err.textContent='15 fichiers maximum par dépôt.';err.hidden=false;return}
    if(isPreview){err.textContent='Aperçu : l’envoi fonctionnera une fois la page en ligne.';err.hidden=false;return}
    var r=ref(),when=stamp();document.getElementById('reference').value=r;document.getElementById('horodatage').value=new Date().toISOString();
    btn.disabled=true;btn.textContent='Envoi…';
    try{
      var x=await fetch('/',{method:'POST',body:new FormData(form)});if(!x.ok)throw new Error(x.status);
      for(var i=0;i<files.length;i++){btn.textContent='Envoi des documents '+(i+1)+'/'+files.length+'…';
        var fd=new FormData();fd.append('form-name','documents-bien');fd.append('reference',r);fd.append('agent-email',em.value);
        fd.append('bien-ville',document.getElementById('bien-ville').value);fd.append('numero',(i+1)+'/'+files.length);fd.append('document',files[i],files[i].name);
        var d=await fetch('/',{method:'POST',body:fd});if(!d.ok)throw new Error('doc');}
      document.getElementById('r-ref').textContent=r;document.getElementById('r-date').textContent=when;form.hidden=true;receipt.hidden=false;receipt.focus();
    }catch(x){err.textContent='L’envoi n’a pas abouti. Réessayez, ou écrivez-nous à contact@plu-value.fr.';err.hidden=false}
    finally{btn.disabled=false;btn.textContent='Envoyer le bien'}
  });
  document.getElementById('again').addEventListener('click',function(){form.reset();receipt.hidden=true;form.hidden=false});
  document.querySelectorAll('a[href="#charte-texte"]').forEach(function(a){a.addEventListener('click',function(){document.getElementById('charte-texte').open=true})});
})();
</script>"""

OWNER_FORM = """<form id="f-etude" name="demande-etude" method="POST" data-netlify="true" netlify-honeypot="site-web" enctype="multipart/form-data" data-simple data-ok="ok-etude" novalidate>
      <input type="hidden" name="form-name" value="demande-etude">
      <input type="hidden" name="profil" id="d-profil" value="proprietaire">
      <input type="hidden" name="reference">
      <p class="hp"><label>Ne pas remplir <input name="site-web" tabindex="-1" autocomplete="off"></label></p>
      <fieldset><legend>Vous</legend>
        <div class="row two"><div class="f"><label for="e-nom">Nom et prénom *</label><input id="e-nom" name="nom" required autocomplete="name"></div>
        <div class="f"><label for="e-tel">Téléphone *</label><input id="e-tel" name="telephone" type="tel" required autocomplete="tel"></div></div>
        <div class="f"><label for="e-email">E-mail *</label><input id="e-email" name="email" type="email" required autocomplete="email"></div>
      </fieldset>
      <fieldset><legend>Le bien</legend>
        <div class="row two"><div class="f"><label for="e-ville">Commune du bien *</label><input id="e-ville" name="commune" required placeholder="Champigny-sur-Marne"></div>
        <div class="f"><label for="e-type">Type de propriété</label><select id="e-type" name="type"><option>Maison</option><option>Maison avec grand terrain</option><option>Terrain</option><option>Maison de ville ou petit immeuble</option><option>Autre</option></select></div></div>
        <div class="row two"><div class="f"><label for="e-surf">Surface habitable approximative (m²)</label><input id="e-surf" name="surface" type="number" inputmode="numeric" min="0"></div>
        <div class="f"><label for="e-ter">Surface du terrain approximative (m²)</label><input id="e-ter" name="terrain" type="number" inputmode="numeric" min="0"></div></div>
        <div class="f"><label for="e-sit">Votre situation</label><select id="e-sit" name="situation"><option>Je réfléchis à vendre</option><option>Mon bien est en vente</option><option>Succession en cours</option><option>Je prépare une transmission</option><option>Indivision</option><option>Autre</option></select></div>
        <div class="f"><label for="e-msg">Description <span class="hint">facultatif</span></label><textarea id="e-msg" name="message" placeholder="Ce que vous souhaitez, vos délais, ce qui bloque…"></textarea></div>
        <div class="f"><label for="e-files">Photos ou documents <span class="hint">facultatif, 8 Mo maximum au total</span></label><input id="e-files" name="documents" type="file" multiple accept="image/*,.pdf"></div>
      </fieldset>
      <div class="consent">
        <label><input type="checkbox" name="accord-traitement" value="oui" required><span>J'accepte que PLU Value utilise ces informations pour étudier mon bien et me recontacter à ce sujet. *</span></label>
        <label><input type="checkbox" name="accord-actualites" value="oui"><span>J'accepte de recevoir occasionnellement des informations de PLU Value (facultatif).</span></label>
      </div>
      <p class="err" role="alert" hidden></p>
      <div><button class="btn primary" type="submit">Envoyer ma demande</button></div>
    </form>
    <div class="okbox" id="ok-etude" hidden tabindex="-1" role="status"><b>Demande bien reçue.</b><p>Référence <span class="ref"></span>. Nous revenons vers vous rapidement, et sous 72 heures une fois le dossier complet.</p></div>"""

NOTAIRE_FORM = """<form id="f-notaire" name="transmission-notaire" method="POST" data-netlify="true" netlify-honeypot="site-web" data-simple data-ok="ok-not" novalidate>
      <input type="hidden" name="form-name" value="transmission-notaire">
      <input type="hidden" name="reference">
      <p class="hp"><label>Ne pas remplir <input name="site-web" tabindex="-1" autocomplete="off"></label></p>
      <div class="row two"><div class="f"><label for="n-etude">Étude *</label><input id="n-etude" name="etude" required autocomplete="organization"></div>
      <div class="f"><label for="n-nom">Votre nom *</label><input id="n-nom" name="nom" required autocomplete="name"></div></div>
      <div class="row two"><div class="f"><label for="n-email">E-mail *</label><input id="n-email" type="email" name="email" required autocomplete="email"></div>
      <div class="f"><label for="n-tel">Téléphone <span class="hint">facultatif</span></label><input id="n-tel" type="tel" name="telephone" autocomplete="tel"></div></div>
      <div class="f"><label for="n-adr">Adresse du bien *<span class="hint"> ou commune et référence cadastrale</span></label><input id="n-adr" name="adresse" required></div>
      <div class="row two"><div class="f"><label for="n-sit">Situation</label><select id="n-sit" name="situation"><option>Succession en cours</option><option>Indivision</option><option>Partage</option><option>Cession d'une maison familiale</option><option>Autre</option></select></div>
      <div class="f"><label for="n-del">Délai souhaité</label><select id="n-del" name="delai"><option>Moins de 3 mois</option><option>3 à 6 mois</option><option>Plus de 6 mois</option><option>Pas de contrainte</option></select></div></div>
      <div class="f"><label for="n-msg">Précisions <span class="hint">facultatif : surface, terrain, occupation</span></label><textarea id="n-msg" name="message"></textarea></div>
      <label class="check"><input type="checkbox" name="accord" value="oui" required><span>Je transmets uniquement des informations que mes clients m'autorisent à partager. Aucune donnée nominative sur les héritiers n'est nécessaire à ce stade. *</span></label>
      <p class="err" role="alert" hidden></p>
      <div><button class="btn primary" type="submit">Transmettre l'adresse</button></div>
    </form>
    <div class="okbox" id="ok-not" hidden tabindex="-1" role="status"><b>Adresse bien reçue.</b><p>Référence <span class="ref"></span>. Réponse sous 72 heures : piste ou pas, avec la raison.</p></div>"""

# ---------- DÉPOSER UN BIEN ----------
P["deposer-un-bien"] = ("Faire étudier un bien | PLU Value",
 "Présentez un bien à PLU Value : propriétaires, héritiers, agents immobiliers et notaires. Étude préalable gratuite, réponse sous 72 heures une fois le dossier complet.",
 f"""  <section aria-labelledby="h1">
    <span class="eyebrow">Faire étudier un bien</span>
    <h1 id="h1">Présentez-nous votre bien</h1>
    <p class="lead">L'étude préalable est gratuite et ne vous engage à rien. Réponse sous 72 heures une fois le dossier complet : le bien est retenu, ou nous vous expliquons pourquoi.</p>
    <fieldset><legend>Vous êtes</legend>
      <div class="profiles">
        <label><input type="radio" name="profil-choix" value="proprietaire" checked>Propriétaire</label>
        <label><input type="radio" name="profil-choix" value="heritier">Héritier ou famille</label>
        <label><input type="radio" name="profil-choix" value="agent">Agent immobilier</label>
        <label><input type="radio" name="profil-choix" value="notaire">Notaire</label>
        <label><input type="radio" name="profil-choix" value="autre">Autre professionnel</label>
      </div>
    </fieldset>
  </section>
  <section data-for="proprietaire heritier autre" aria-labelledby="h-o">
    <h2 id="h-o">Votre demande d'étude</h2>
    <p class="hint">Quelques informations suffisent pour commencer. Aucun dossier juridique n'est nécessaire à ce stade.</p>
    {OWNER_FORM}
  </section>
  <section data-for="agent" id="deposer" aria-labelledby="h-a" hidden>
    <span class="eyebrow">Dépôt confidentiel · charte de non-contournement</span>
    <h2 id="h-a">Déposer un bien en tant qu'agent</h2>
    <p class="hint">Dépôt horodaté avec une référence unique. Nous ne contactons jamais le propriétaire sans vous, pendant 24 mois.</p>
    {DEP_FORM}
    {CHARTE}
  </section>
  <section data-for="notaire" aria-labelledby="h-n" hidden>
    <h2 id="h-n">Transmission confidentielle d'un dossier patrimonial</h2>
    <p class="hint">Une adresse suffit pour une première lecture. Le secret professionnel s'applique : ne transmettez que ce que vos clients vous autorisent à partager.</p>
    {NOTAIRE_FORM}
  </section>
  <section aria-labelledby="h-c">
    <h2 id="h-c">Vous préférez nous parler ?</h2>
    <div class="cta"><a class="btn ghost" href="tel:+33756986700">07 56 98 67 00</a><a class="btn ghost" href="mailto:contact@plu-value.fr">contact@plu-value.fr</a><a class="btn ghost" href="https://wa.me/33756986700">WhatsApp</a></div>
  </section>""", None)
P["deposer-un-bien"] = P["deposer-un-bien"][:3] + (None, FORMS_JS)

# ---------- AGENTS ----------
P["agents-immobiliers"] = ("Valorisez vos mandats difficiles | PLU Value",
 "Agents immobiliers : avant de baisser le prix d'un mandat difficile, faites étudier son potentiel de division et de valorisation. Charte de non-contournement de 24 mois.",
 f"""  <section aria-labelledby="h1">
    <div class="hero-grid">
      <div style="display:grid;gap:18px">
        <span class="eyebrow">Agents immobiliers</span>
        <h1 id="h1">Votre mandat ne se vend pas ? Avant de baisser le prix, étudions son potentiel.</h1>
        <p class="lead">Division de la maison, lot à bâtir, découpe d'un immeuble : nous étudions gratuitement ce que le bien permet et nous investissons dans les projets retenus. Vous gardez votre client et votre mandat.</p>
        <div class="cta"><a class="btn primary" href="/deposer-un-bien?profil=agent">Déposer un bien</a><a class="btn ghost" href="#charte">La charte</a></div>
      </div>
      <figure class="shot"><img src="/media/site-agents.webp" alt="Plan cadastral sur lequel une parcelle est divisée, avec une maquette de maison" width="1536" height="864"></figure>
    </div>
  </section>
  <section aria-labelledby="h-p">
    <h2 id="h-p">Les mandats que nous débloquons</h2>
    <div class="grid2">
      <div class="card"><ul><li>Biens en vitrine depuis des mois.</li><li>Grandes maisons dont le budget total freine les acheteurs.</li><li>Propriétés avec grand terrain.</li></ul></div>
      <div class="card"><ul><li>Biens atypiques : ateliers, maisons de ville, petits immeubles.</li><li>Vendeurs qui refusent de baisser leur prix.</li><li>Projets trop techniques pour une agence classique.</li></ul></div>
    </div>
  </section>
  <section aria-labelledby="h-g">
    <h2 id="h-g">Ce que vous y gagnez</h2>
    <div class="grid3">
      <div class="card"><h3>Un dossier qui avance</h3><p class="hint">Une étude chiffrée à présenter à votre vendeur, plutôt qu'une énième baisse de prix.</p></div>
      <div class="card"><h3>Plusieurs biens à vendre</h3><p class="hint">Les lots créés vous sont proposés en mandat, avec une rémunération complémentaire convenue par écrit avant la signature avec le vendeur.</p></div>
      <div class="card"><h3>Zéro travail technique</h3><p class="hint">Urbanisme, géomètre, juridique et copropriété sont pris en charge.</p></div>
    </div>
  </section>
  <section id="charte" aria-labelledby="h-c">
    <span class="eyebrow">Charte partenaire, version d'octobre 2026</span>
    <h2 id="h-c">Votre relation client est protégée</h2>
    <div class="card"><ul>
      <li>Nous ne contactons jamais le propriétaire sans vous.</li>
      <li>Nous n'achetons ni ne valorisons le bien en dehors de vous, pendant 24 mois.</li>
      <li>Vos informations servent uniquement à l'étude du bien.</li>
      <li>Si une opération se fait, votre rémunération est due.</li>
      <li>La date et l'heure de votre dépôt font foi.</li></ul></div>
    {CHARTE}
    <div><a class="btn primary" href="/deposer-un-bien?profil=agent">Déposer un bien</a></div>
  </section>
{FINAL_CTA}""")

# ---------- NOTAIRES ----------
P["notaires"] = ("Notaires : potentiel immobilier des successions | PLU Value",
 "Successions, indivisions, partages : PLU Value offre à vos clients une analyse complémentaire du potentiel immobilier de leurs biens, avec Me Pierre-Henry Blanc, avocat en urbanisme. Réponse sous 72 h.",
 f"""  <section aria-labelledby="h1">
    <div class="hero-grid">
      <div style="display:grid;gap:18px">
        <span class="eyebrow">Notaires · Successions et indivisions</span>
        <h1 id="h1">Offrez à vos clients une analyse du potentiel de leurs biens.</h1>
        <p class="lead">Avant une décision de vente ou de partage, nous étudions ce que la maison ou le terrain permet. Pour les projets retenus, nous engageons nos moyens dans leur préparation. Les actes restent chez vous.</p>
        <div class="cta"><a class="btn primary" href="#transmettre">Transmettre une adresse</a><a class="btn ghost" href="/nos-engagements">Notre modèle</a></div>
      </div>
      <figure class="shot"><img src="/media/site-notaires.webp" alt="Bureau d'étude avec un dossier ouvert, vue sur une maison avec jardin" width="1536" height="864"></figure>
    </div>
    <ul class="facts"><li><b>72 h</b><span>pour vous dire s'il y a une piste, et pourquoi</span></li><li><b>0 €</b><span>d'étude à la charge de vos clients</span></li><li><b>30 ans</b><span>de droit de l'urbanisme derrière chaque étude</span></li></ul>
  </section>
  <section aria-labelledby="h-cas">
    <h2 id="h-cas">Les dossiers concernés</h2>
    <div class="grid2">
      <div class="card"><ul><li>Successions portant sur une maison trop grande pour le marché.</li><li>Indivisions qui ne s'accordent pas sur le prix.</li><li>Partages patrimoniaux.</li></ul></div>
      <div class="card"><ul><li>Cessions de maisons familiales.</li><li>Biens difficiles à valoriser en l'état.</li><li>Questions de division foncière ou immobilière.</li></ul></div>
    </div>
  </section>
  <section aria-labelledby="h-m">
    <h2 id="h-m">Comment nous travaillons avec votre étude</h2>
    <ol class="steps">
      <li><div><h3>Vous nous transmettez une adresse</h3><p>Aucune donnée nominative sur les héritiers n'est nécessaire au premier contact.</p></div></li>
      <li><div><h3>Nous étudions le bien sous 72 heures</h3><p>Scénarios chiffrés, revus par Me Pierre-Henry Blanc, avocat en urbanisme.</p></div></li>
      <li><div><h3>Nous présentons la solution, avec vous</h3><p>Vous restez l'interlocuteur de vos clients. Rien ne se fait sans leur accord.</p></div></li>
      <li><div><h3>Les ventes se signent chez vous</h3><p>Côté vendeurs, chaque acte passe par votre étude.</p></div></li>
    </ol>
    <p class="note"><b>Notre règle :</b> nous ne proposons ni ne versons aucune rémunération à votre étude. Nous ne nous substituons pas à vos missions.</p>
  </section>
  <section id="transmettre" aria-labelledby="h-t">
    <h2 id="h-t">Transmettre une adresse</h2>
    {NOTAIRE_FORM}
  </section>
{FINAL_CTA}""", None)
P["notaires"] = P["notaires"][:3] + (None, FORMS_JS)

# ---------- INVESTISSEURS ----------
INV_FORM = """<form name="criteres-investisseur" method="POST" data-netlify="true" netlify-honeypot="site-web" data-simple data-ok="ok-inv" novalidate>
      <input type="hidden" name="form-name" value="criteres-investisseur">
      <p class="hp"><label>Ne pas remplir <input name="site-web" tabindex="-1" autocomplete="off"></label></p>
      <div class="row two"><div class="f"><label for="i-nom">Nom *</label><input id="i-nom" name="nom" required autocomplete="name"></div><div class="f"><label for="i-soc">Société</label><input id="i-soc" name="societe" autocomplete="organization"></div></div>
      <div class="row two"><div class="f"><label for="i-email">E-mail *</label><input id="i-email" name="email" type="email" required autocomplete="email"></div><div class="f"><label for="i-tel">Téléphone</label><input id="i-tel" name="telephone" type="tel" autocomplete="tel"></div></div>
      <div class="f"><label for="i-zone">Zones recherchées *</label><input id="i-zone" name="zones" required></div>
      <div class="row two"><div class="f"><label for="i-min">Ticket minimum (€)</label><input id="i-min" name="ticket-min" type="number" min="0"></div><div class="f"><label for="i-max">Ticket maximum (€)</label><input id="i-max" name="ticket-max" type="number" min="0"></div></div>
      <div class="f"><label for="i-msg">Précisions</label><textarea id="i-msg" name="message"></textarea></div>
      <label class="check"><input type="checkbox" name="accord" value="oui" required><span>J'accepte d'être recontacté par PLU Value au sujet d'opérations. *</span></label>
      <p class="err" role="alert" hidden></p><div><button class="btn primary" type="submit">Envoyer mes critères</button></div>
    </form>
    <div class="okbox" id="ok-inv" hidden tabindex="-1" role="status"><b>Critères bien reçus.</b><p>Nous vous présenterons les dossiers qui correspondent.</p></div>"""
P["investisseurs"] = ("Investisseurs et marchands de biens : opérations étudiées | PLU Value",
 "Marchands de biens et investisseurs : PLU Value apporte des opérations de division avec la faisabilité, le montage juridique et la méthode.",
 f"""  <section aria-labelledby="h1">
    <span class="eyebrow">Investisseurs · Marchands de biens</span>
    <h1 id="h1">Des opérations déjà étudiées, montage juridique compris.</h1>
    <p class="lead">Nous repérons des biens sous-exploités, nous vérifions ce que le PLU permet, et nous apportons des dossiers prêts à décider.</p>
    <figure class="shot"><img src="/media/site-investisseurs.webp" alt="Plan cadastral avec une parcelle divisée et une maquette de maison" width="1536" height="864"></figure>
  </section>
  <section aria-labelledby="h-a">
    <h2 id="h-a">Ce que nous apportons</h2>
    <div class="grid2">
      <div class="card"><span class="k">Le dossier</span><ul><li>Lecture du PLU, cadastre, servitudes</li><li>Ventes réelles du secteur (DVF)</li><li>Scénarios chiffrés</li></ul></div>
      <div class="card"><span class="k">Le juridique</span><ul><li>Revu par Me Pierre-Henry Blanc, avocat en urbanisme</li><li>Promesses sous conditions suspensives</li><li>Aucune acquisition sans autorisation obtenue</li></ul></div>
      <div class="card"><span class="k">La méthode</span><ul><li>Géomètre, autorisations, copropriété</li><li>Commercialisation avec des agences partenaires</li></ul></div>
      <div class="card"><span class="k">Le flux</span><ul><li>Mandats apportés par notre réseau d'agents</li><li>Successions et indivisions</li><li>Veille quotidienne du marché</li></ul></div>
    </div>
    <p class="note">Les conditions de chaque opération sont convenues par écrit, dossier par dossier.</p>
  </section>
  <section id="criteres" aria-labelledby="h-f"><h2 id="h-f">Recevoir nos dossiers</h2>{INV_FORM}</section>""", None)
P["investisseurs"] = P["investisseurs"][:3] + (None, FORMS_JS)

HASH_JS = """<script>(function(){var h=location.hash;if(h==='#deposer'||h==='#charte'||h==='#charte-texte'){location.replace('/deposer-un-bien?profil=agent'+(h==='#deposer'?'':h));}if(h==='#contact'){location.replace('/deposer-un-bien');}})();</script>"""
v=P[""]; P[""]=(v[0],v[1],v[2],v[3],HASH_JS)
