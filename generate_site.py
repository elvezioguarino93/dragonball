from pathlib import Path
from textwrap import dedent

base = Path('/mnt/data/dragonball-affiliate-site')
(base/'assets/css').mkdir(parents=True, exist_ok=True)
(base/'assets/js').mkdir(parents=True, exist_ok=True)
(base/'pages').mkdir(parents=True, exist_ok=True)

site_name = 'DragonBall Picks'
base_url = 'https://example.com'
aff_tag = 'YOURTAG-21'

def amazon_search(query):
    from urllib.parse import quote_plus
    return f"https://www.amazon.it/s?k={quote_plus(query)}&tag={aff_tag}"

css = dedent('''
:root {
  --bg: #0a0a0f;
  --card: #12121a;
  --muted: #a7adbb;
  --text: #f3f5f7;
  --line: #232634;
  --accent: #ff9f1c;
  --accent-2: #f94144;
  --max: 1180px;
  --radius: 18px;
  --shadow: 0 12px 30px rgba(0,0,0,.22);
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: linear-gradient(180deg, #0a0a0f 0%, #10131b 100%);
  color: var(--text);
  line-height: 1.65;
}
a { color: inherit; text-decoration: none; }
img { max-width: 100%; display: block; }
.container { width: min(var(--max), calc(100% - 32px)); margin: 0 auto; }
.topbar {
  position: sticky; top: 0; z-index: 30;
  backdrop-filter: blur(10px);
  background: rgba(10,10,15,.75); border-bottom: 1px solid rgba(255,255,255,.06);
}
.nav {
  display: flex; align-items: center; justify-content: space-between; gap: 20px; padding: 14px 0;
}
.logo { font-weight: 800; letter-spacing: .2px; }
.logo span { color: var(--accent); }
.nav-links { display: flex; gap: 18px; flex-wrap: wrap; }
.nav-links a { color: var(--muted); font-size: .95rem; }
.nav-links a:hover { color: var(--text); }
.hero { padding: 84px 0 46px; }
.hero-grid { display: grid; grid-template-columns: 1.2fr .8fr; gap: 24px; align-items: center; }
.eyebrow {
  display: inline-flex; gap: 8px; align-items: center; background: rgba(255,159,28,.12);
  color: #ffbe5c; padding: 7px 12px; border-radius: 999px; font-size: .84rem; border: 1px solid rgba(255,159,28,.18);
}
h1, h2, h3 { line-height: 1.15; margin: 0 0 14px; }
h1 { font-size: clamp(2.3rem, 4vw, 4.2rem); }
h2 { font-size: clamp(1.8rem, 2.8vw, 2.9rem); margin-top: 0; }
h3 { font-size: 1.25rem; }
.lead { font-size: 1.1rem; color: #d7dbe3; max-width: 65ch; }
.hero-card, .card, .stat, .product, .faq, .content-box, .table-wrap, .mini-card {
  background: rgba(18,18,26,.9); border: 1px solid rgba(255,255,255,.06); box-shadow: var(--shadow); border-radius: var(--radius);
}
.hero-card { padding: 22px; }
.hero-card ul { margin: 0; padding-left: 18px; color: var(--muted); }
.cta-row { display: flex; gap: 12px; flex-wrap: wrap; margin-top: 24px; }
.btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 10px;
  padding: 13px 18px; border-radius: 999px; font-weight: 700; transition: transform .15s ease, opacity .15s ease;
}
.btn:hover { transform: translateY(-1px); opacity: .95; }
.btn-primary { background: linear-gradient(135deg, var(--accent), #ffb703); color: #161616; }
.btn-secondary { border: 1px solid rgba(255,255,255,.09); color: var(--text); }
section { padding: 38px 0; }
.section-head { display:flex; justify-content: space-between; gap: 16px; align-items: end; margin-bottom: 18px; }
.section-head p { color: var(--muted); margin: 0; max-width: 72ch; }
.grid { display: grid; gap: 18px; }
.grid-3 { grid-template-columns: repeat(3, minmax(0,1fr)); }
.grid-2 { grid-template-columns: repeat(2, minmax(0,1fr)); }
.card { padding: 20px; }
.card p, .mini-card p, .product p, .faq p, .content-box p, .content-box li { color: var(--muted); }
.badge { display: inline-block; padding: 6px 10px; border-radius: 999px; background: rgba(249,65,68,.12); color: #ff8f92; font-size: .78rem; margin-bottom: 10px; }
.list-clean { list-style: none; padding: 0; margin: 0; }
.list-clean li { padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,.06); }
.list-clean li:last-child { border-bottom: 0; }
.pillars a, .related a { display: block; }
.stats { display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 16px; }
.stat { padding: 18px; }
.stat strong { display: block; font-size: 1.5rem; margin-bottom: 6px; }
.table-wrap { overflow: auto; }
table { width: 100%; border-collapse: collapse; min-width: 760px; }
th, td { padding: 14px 16px; text-align: left; border-bottom: 1px solid rgba(255,255,255,.06); }
th { color: #fff; font-size: .95rem; background: rgba(255,255,255,.03); }
td { color: var(--muted); }
.product { padding: 22px; display: grid; grid-template-columns: 1fr auto; gap: 20px; align-items: start; }
.product .actions { display: flex; flex-direction: column; gap: 10px; min-width: 180px; }
.note { color: #c7ced9; font-size: .93rem; }
.faq { padding: 18px 20px; }
.faq + .faq { margin-top: 12px; }
.content-box { padding: 24px; }
.content-box ul { padding-left: 18px; }
.footer { padding: 42px 0 56px; color: var(--muted); }
.footer-grid { display:grid; grid-template-columns: 1.3fr .7fr .7fr; gap: 18px; }
.small { font-size: .9rem; color: var(--muted); }
.breadcrumbs { color: var(--muted); font-size: .92rem; margin-bottom: 18px; }
.kicker { text-transform: uppercase; letter-spacing: .12em; color: #ffbe5c; font-size: .82rem; }
.mini-card { padding: 16px; }
.article-grid { display: grid; grid-template-columns: 1fr 320px; gap: 24px; }
.sidebar-sticky { position: sticky; top: 90px; }
.notice { padding: 14px 16px; border-left: 4px solid var(--accent); background: rgba(255,159,28,.08); border-radius: 12px; color: #f2d3a0; }
.hr { height: 1px; background: rgba(255,255,255,.06); margin: 24px 0; }
@media (max-width: 950px) {
  .hero-grid, .article-grid, .grid-3, .grid-2, .footer-grid, .stats, .product { grid-template-columns: 1fr; }
  .product .actions { min-width: auto; }
}
@media (max-width: 680px) {
  h1 { font-size: 2.1rem; }
  .nav { flex-direction: column; align-items: flex-start; }
  .hero { padding-top: 58px; }
}
''')
(base/'assets/css/styles.css').write_text(css, encoding='utf-8')

js = dedent('''
const yearEl = document.querySelector('[data-year]');
if (yearEl) yearEl.textContent = new Date().getFullYear();
''')
(base/'assets/js/main.js').write_text(js, encoding='utf-8')

pillars = [
    {
        'slug': 'migliori-figure-dragon-ball',
        'title': 'Migliori Figure Dragon Ball',
        'meta': 'Guida completa alle migliori figure Dragon Ball da comprare su Amazon: economiche, premium, Banpresto, SH Figuarts e idee per collezionisti.',
        'hero': 'Le migliori figure Dragon Ball da comprare online',
        'intro': 'Questa guida raccoglie le migliori figure Dragon Ball per qualità, resa estetica, popolarità tra i fan e rapporto qualità prezzo. È pensata per chi vuole comprare in modo più consapevole, senza perdere ore tra risultati confusi.',
        'keyword': 'figure Dragon Ball',
        'products': [
            ('Figure Banpresto Goku', 'Ottimo equilibrio tra prezzo, qualità e resa visiva. Ideale per chi inizia una collezione.', 'Entry level', 'Banpresto', 'amazon.it search'),
            ('Figure Vegeta Battle Pose', 'Perfetta per una mensola a tema Saiyan. Una delle più ricercate nelle collezioni medie.', 'Miglior design', 'Vegeta', 'amazon.it search'),
            ('SH Figuarts Goku', 'Più costosa ma molto più posabile. Adatta a chi vuole qualità premium.', 'Premium', 'SH Figuarts', 'amazon.it search'),
            ('Figure Broly Oversize', 'Scelta ideale per chi cerca una statua scenica e d’impatto.', 'Best statement piece', 'Broly', 'amazon.it search'),
            ('Figure Trunks Future', 'Una scelta forte per variare la collezione oltre ai personaggi principali.', 'Alternativa fan favorite', 'Trunks', 'amazon.it search'),
        ],
        'faq': [
            ('Quali sono le migliori marche di figure Dragon Ball?', 'Per chi punta al prezzo convengono spesso Banpresto e linee similari. Per articolazioni, finiture e posabilità avanzata di solito si sale verso SH Figuarts e statue premium.'),
            ('Conviene comprare figure economiche o premium?', 'Dipende dall’obiettivo. Se vuoi volume e varietà, ha senso partire da figure economiche. Se vuoi pochi pezzi ma d’impatto, meglio una selezione premium.'),
            ('Come scegliere una figure Dragon Ball?', 'Guarda dimensioni, materiale, fedeltà al personaggio, marca, base inclusa e recensioni foto reali. Evita acquisti impulsivi senza confronti.'),
        ],
        'related': [
            ('Figure di Goku', '#'), ('Figure di Vegeta', '#'), ('Figure economiche sotto 30 euro', '#'), ('Banpresto vs SH Figuarts', '#')
        ]
    },
    {
        'slug': 'migliori-gadget-dragon-ball',
        'title': 'Migliori Gadget Dragon Ball',
        'meta': 'I migliori gadget Dragon Ball su Amazon: lampade, accessori, tazze, portachiavi, zaini e idee regalo perfette per ogni fan.',
        'hero': 'I gadget Dragon Ball più belli per fan e collezionisti',
        'intro': 'I gadget giusti trasformano una passione in esperienza quotidiana. In questa pagina trovi una selezione ragionata di idee utili, decorative o regalo, con un occhio alla convenienza e uno all’effetto wow.',
        'keyword': 'gadget Dragon Ball',
        'products': [
            ('Lampada sfera del drago', 'Arreda bene scrivania e camera. Uno dei gadget più regalabili.', 'Best regalo', 'Lampada', 'amazon.it search'),
            ('Tazza Dragon Ball', 'Idea economica ma sempre efficace per fan casual e regali rapidi.', 'Budget', 'Tazza', 'amazon.it search'),
            ('Portachiavi 4 stelle', 'Piccolo, iconico e facile da abbinare a un regalo principale.', 'Piccolo pensiero', 'Portachiavi', 'amazon.it search'),
            ('Zaino Dragon Ball', 'Perfetto per scuola, palestra o uso quotidiano con richiamo fanservice evidente.', 'Più utile', 'Zaino', 'amazon.it search'),
            ('Set scrivania Dragon Ball', 'Per chi vuole un angolo tema anime senza andare sul costoso.', 'Home office', 'Accessorio', 'amazon.it search'),
        ],
        'faq': [
            ('Qual è il miglior gadget Dragon Ball da regalare?', 'Per andare sul sicuro, lampade, tazze premium e portachiavi iconici sono tra le scelte più trasversali.'),
            ('Quali gadget Dragon Ball costano poco?', 'Le categorie più economiche in genere sono portachiavi, adesivi, tazze e piccoli accessori da scrivania.'),
            ('Meglio gadget utili o decorativi?', 'Per conversione e soddisfazione spesso i migliori sono quelli che uniscono entrambe le cose, come lampade, tazze e zaini.'),
        ],
        'related': [('Lampade Dragon Ball', '#'), ('Zaini Dragon Ball', '#'), ('Idee regalo economiche', '#'), ('Portachiavi Dragon Ball', '#')]
    },
    {
        'slug': 'migliori-funko-pop-dragon-ball',
        'title': 'Migliori Funko Pop Dragon Ball',
        'meta': 'Scopri i migliori Funko Pop Dragon Ball da acquistare: Goku, Vegeta, versioni rare, edizioni da collezione e consigli per comprare meglio.',
        'hero': 'I migliori Funko Pop Dragon Ball da collezionare',
        'intro': 'I Funko Pop di Dragon Ball uniscono forte riconoscibilità del brand e buona capacità di attrarre fan casual, collezionisti e chi compra regali. Questa guida ti aiuta a capire cosa cercare e quali modelli osservare.',
        'keyword': 'Funko Pop Dragon Ball',
        'products': [
            ('Funko Pop Goku', 'Il personaggio più facile da convertire e da consigliare a chi entra nella nicchia.', 'Best seller', 'Goku', 'amazon.it search'),
            ('Funko Pop Vegeta', 'Molto richiesto da chi vuole una coppia iconica con Goku.', 'Fan favorite', 'Vegeta', 'amazon.it search'),
            ('Funko Pop Gohan', 'Perfetto per ampliare la collezione senza essere troppo scontati.', 'Buona varietà', 'Gohan', 'amazon.it search'),
            ('Funko Pop Shenron', 'Più scenico e particolare, ottimo come pezzo distintivo.', 'Statement piece', 'Shenron', 'amazon.it search'),
            ('Funko Pop Ultra Instinct', 'Uno dei concept più forti per appeal moderno e ricerche ad alta intenzione.', 'High intent', 'Ultra Instinct', 'amazon.it search'),
        ],
        'faq': [
            ('I Funko Pop Dragon Ball aumentano di valore?', 'Alcune edizioni limitate o fuori produzione possono crescere, ma chi compra dovrebbe sempre partire dal gusto personale e non dalla sola speculazione.'),
            ('Come capire se un Funko Pop è adatto al regalo?', 'Punta su personaggi iconici, confezione integra e venditori affidabili, soprattutto se il destinatario è un collezionista.'),
            ('Meglio acquistare versioni comuni o rare?', 'Le versioni comuni convertono meglio e sono più facili da consigliare in guide affiliate. Le rare hanno appeal, ma prezzo e disponibilità cambiano più spesso.'),
        ],
        'related': [('Funko di Goku', '#'), ('Funko rari Dragon Ball', '#'), ('Funko economici', '#'), ('Dove comprare Funko Pop', '#')]
    },
    {
        'slug': 'migliori-manga-dragon-ball',
        'title': 'Migliori Manga Dragon Ball',
        'meta': 'Guida ai manga Dragon Ball più interessanti da comprare: serie classica, Dragon Ball Super, box set, edizioni e consigli per iniziare.',
        'hero': 'I manga Dragon Ball da comprare per iniziare o completare la collezione',
        'intro': 'I manga sono una delle aree più forti per una nicchia Dragon Ball perché uniscono ricerca informativa e intenzione d’acquisto. Qui trovi le scelte migliori per lettura, collezione e regali.',
        'keyword': 'manga Dragon Ball',
        'products': [
            ('Dragon Ball manga volumi singoli', 'Ideale per iniziare senza investimento alto e capire se vuoi completare la serie.', 'Per iniziare', 'Volumi', 'amazon.it search'),
            ('Box manga Dragon Ball', 'Scelta perfetta per chi vuole ordine, regalo importante e collezione completa.', 'Best box', 'Box set', 'amazon.it search'),
            ('Dragon Ball Super manga', 'Consigliato a chi ha già amato la serie principale e vuole continuare.', 'Continuazione', 'Super', 'amazon.it search'),
            ('Guida illustrata Dragon Ball', 'Ottima per fan storici e collezionisti che vogliono materiale extra.', 'Extra lore', 'Guidebook', 'amazon.it search'),
            ('Edizione deluxe o speciale', 'Più costosa ma interessante per posizionamento premium e regalo.', 'Premium', 'Speciale', 'amazon.it search'),
        ],
        'faq': [
            ('Da dove conviene iniziare a leggere Dragon Ball?', 'Per la maggior parte delle persone la serie classica resta il punto di partenza migliore. Dragon Ball Super è più adatto a chi conosce già l’opera base.'),
            ('Meglio box set o volumi singoli?', 'Il box set è spesso migliore come regalo e ordine estetico; i volumi singoli sono più flessibili per chi vuole spendere meno all’inizio.'),
            ('I manga Dragon Ball sono un buon prodotto affiliato?', 'Sì, perché rispondono a ricerche molto chiare: ordine di lettura, regalo, collezione completa, differenze tra edizioni.'),
        ],
        'related': [('Ordine di lettura', '#'), ('Dragon Ball Super', '#'), ('Box manga', '#'), ('Differenze anime e manga', '#')]
    },
    {
        'slug': 'migliori-regali-dragon-ball',
        'title': 'Migliori Regali Dragon Ball',
        'meta': 'Idee regalo Dragon Ball per bambini, adulti e collezionisti: prodotti economici, premium e ad alto impatto da comprare su Amazon.',
        'hero': 'Le migliori idee regalo Dragon Ball per ogni budget',
        'intro': 'Le keyword regalo sono perfette per l’affiliazione perché intercettano persone già pronte all’acquisto. Questa pagina organizza i prodotti per fascia di prezzo, tipo di fan e utilità percepita.',
        'keyword': 'regali Dragon Ball',
        'products': [
            ('Regalo sotto 20 euro', 'Piccoli accessori iconici e facili da convertire in periodi regalo.', 'Low budget', 'Sotto 20€', 'amazon.it search'),
            ('Figure regalo Dragon Ball', 'La scelta più semplice per chi vuole un effetto visivo immediato.', 'Scelta sicura', 'Figure', 'amazon.it search'),
            ('Box manga regalo', 'Più adatto a chi vuole fare un regalo importante e memorabile.', 'Regalo premium', 'Manga', 'amazon.it search'),
            ('Lampada decorativa', 'Unisce utilità e impatto, ottima conversione anche per non super fan.', 'Best utility', 'Decorazione', 'amazon.it search'),
            ('Set regalo misto Dragon Ball', 'Buona opzione per compleanni e ricorrenze con budget medio.', 'Bundle idea', 'Set', 'amazon.it search'),
        ],
        'faq': [
            ('Qual è il miglior regalo Dragon Ball per un adulto?', 'Spesso funzionano meglio figure curate, manga box, lampade decorative e oggetti da esposizione.'),
            ('Che regalo Dragon Ball scegliere per un bambino?', 'Meglio prodotti robusti, riconoscibili e non troppo delicati: zaini, tazze resistenti, accessori o figure semplici.'),
            ('Quali regali Dragon Ball convertono meglio in affiliazione?', 'Le categorie più forti in genere sono figure, gadget decorativi, manga box e prodotti facili da regalare con budget chiaro.'),
        ],
        'related': [('Regali sotto 20 euro', '#'), ('Regali per adulti', '#'), ('Regali per bambini', '#'), ('Regali per collezionisti', '#')]
    },
    {
        'slug': 'poster-dragon-ball',
        'title': 'Poster e Decorazioni Dragon Ball',
        'meta': 'I migliori poster e decorazioni Dragon Ball per camera, studio e gaming room: quadri, tele, LED e accessori da parete.',
        'hero': 'Poster e decorazioni Dragon Ball per una stanza davvero iconica',
        'intro': 'Questa pillar è ideale per intercettare chi cerca ispirazione d’arredo a tema anime. Ha grande potenziale Pinterest, ricerca visuale e ottime opportunità di monetizzazione con accessori e bundle decorativi.',
        'keyword': 'poster Dragon Ball',
        'products': [
            ('Poster Goku e Vegeta', 'Il duo iconico resta la scelta più semplice e universale.', 'Iconico', 'Poster', 'amazon.it search'),
            ('Tela Dragon Ball premium', 'Più elegante del poster classico, ideale per setup gaming o studio.', 'Più premium', 'Tela', 'amazon.it search'),
            ('Set poster multipli', 'Ottimo per chi vuole riempire la parete con un solo acquisto.', 'Best value', 'Set', 'amazon.it search'),
            ('Neon LED tema Dragon Ball', 'Un prodotto di forte impatto visivo e ottimo CTR in pagina.', 'High impact', 'LED', 'amazon.it search'),
            ('Tappeto camera Dragon Ball', 'Completa l’angolo tema e aiuta a costruire articoli bundle.', 'Complemento', 'Decor', 'amazon.it search'),
        ],
        'faq': [
            ('Meglio poster, tela o quadro Dragon Ball?', 'Dipende dallo stile della stanza. I poster costano meno, le tele risultano più pulite, i quadri premium sono più d’impatto.'),
            ('Come decorare una camera Dragon Ball?', 'Parti da un elemento principale a parete, poi abbina luce LED, oggetti da scrivania e una o due figure per coerenza visiva.'),
            ('Le decorazioni Dragon Ball sono adatte a guide affiliate?', 'Sì, soprattutto se unisci intento ispirazionale e shopping, con gallery, bundle e consigli pratici per setup completi.'),
        ],
        'related': [('Poster camera', '#'), ('Luci LED Dragon Ball', '#'), ('Tappeti Dragon Ball', '#'), ('Set decorativi', '#')]
    }
]


def layout(title, meta, content, canonical):
    return f'''<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{meta}" />
  <meta name="robots" content="index,follow,max-image-preview:large" />
  <link rel="canonical" href="{canonical}" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{meta}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:site_name" content="{site_name}" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="stylesheet" href="{'../' if '/pages/' in canonical else ''}assets/css/styles.css" />
  <script type="application/ld+json">{{
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "{site_name}",
    "url": "{base_url}"
  }}</script>
</head>
<body>
  {content}
  <script src="{'../' if '/pages/' in canonical else ''}assets/js/main.js" defer></script>
</body>
</html>'''


def build_nav(prefix=''):
    return f'''
<div class="topbar">
  <div class="container nav">
    <a class="logo" href="{prefix}index.html">Dragon<span>Ball</span> Picks</a>
    <div class="nav-links">
      <a href="{prefix}pages/migliori-figure-dragon-ball.html">Figure</a>
      <a href="{prefix}pages/migliori-gadget-dragon-ball.html">Gadget</a>
      <a href="{prefix}pages/migliori-funko-pop-dragon-ball.html">Funko Pop</a>
      <a href="{prefix}pages/migliori-manga-dragon-ball.html">Manga</a>
      <a href="{prefix}pages/migliori-regali-dragon-ball.html">Regali</a>
      <a href="{prefix}pages/poster-dragon-ball.html">Poster</a>
    </div>
  </div>
</div>
'''


home_cards = ''.join([
    f'''<a href="pages/{p['slug']}.html" class="card">
      <div class="badge">Pillar page</div>
      <h3>{p['title']}</h3>
      <p>{p['meta']}</p>
      <div class="small">Vai alla guida completa →</div>
    </a>''' for p in pillars
])

latest_cards = ''.join([
    f'''<a href="pages/{p['slug']}.html" class="mini-card"><h3>{p['title']}</h3><p>{p['intro']}</p></a>''' for p in pillars[:4]
])

home_content = f'''
{build_nav()}
<header class="hero">
  <div class="container hero-grid">
    <div>
      <span class="eyebrow">Sito SEO + Affiliazione Amazon • nicchia Dragon Ball</span>
      <h1>Guide essenziali per comprare i migliori prodotti Dragon Ball.</h1>
      <p class="lead">Home minimale, struttura interna forte e pillar page progettate per posizionarsi su keyword commerciali come figure, gadget, manga, regali e decorazioni Dragon Ball.</p>
      <div class="cta-row">
        <a class="btn btn-primary" href="#pillar">Esplora le pillar page</a>
        <a class="btn btn-secondary" href="#struttura">Vedi struttura SEO</a>
      </div>
    </div>
    <aside class="hero-card">
      <h3>Come usare questa home</h3>
      <ul>
        <li>Trasferisce autorevolezza alle pagine principali.</li>
        <li>Riduce distrazioni e disperde meno link juice.</li>
        <li>Aiuta Google a capire subito la mappa editoriale.</li>
        <li>Fa arrivare l’utente alle guide con intento d’acquisto.</li>
      </ul>
    </aside>
  </div>
</header>

<section id="pillar">
  <div class="container">
    <div class="section-head">
      <div>
        <div class="kicker">Pillar architecture</div>
        <h2>Le pagine che devono salire di rank</h2>
      </div>
      <p>Ogni guida è pensata come hub commerciale: intro SEO, tabella comparativa, selezione prodotti, FAQ, consigli d’acquisto e linking interno verso future sottopagine satellite.</p>
    </div>
    <div class="grid grid-3 pillars">{home_cards}</div>
  </div>
</section>

<section id="struttura">
  <div class="container">
    <div class="section-head">
      <div>
        <div class="kicker">SEO foundation</div>
        <h2>Struttura semplice, veloce e scalabile</h2>
      </div>
      <p>Questa base è pronta per GitHub Pages, Netlify o Vercel. Puoi aggiungere articoli satellite, aggiornare le tabelle e sostituire i link Amazon con il tuo tag affiliato.</p>
    </div>
    <div class="stats">
      <div class="stat"><strong>6</strong><span>Pillar page commerciali già pronte</span></div>
      <div class="stat"><strong>1</strong><span>Home minimale che distribuisce autorevolezza</span></div>
      <div class="stat"><strong>100%</strong><span>Statico e semplice da pubblicare su GitHub</span></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <div>
        <div class="kicker">Guide in evidenza</div>
        <h2>Le sezioni da spingere subito</h2>
      </div>
      <p>Queste sono le prime pagine da rafforzare con contenuti satellite, anchor text interni coerenti e aggiornamenti periodici.</p>
    </div>
    <div class="grid grid-2">{latest_cards}</div>
  </div>
</section>

<section>
  <div class="container content-box">
    <h2>Checklist rapida prima di andare online</h2>
    <ul>
      <li>Sostituisci tutti i tag <strong>YOURTAG-21</strong> con il tuo codice Amazon Affiliates.</li>
      <li>Cambia <strong>https://example.com</strong> nel file sitemap.xml e nei canonical con il tuo dominio reale.</li>
      <li>Aggiungi una pagina privacy/cookie policy e la disclosure affiliazione secondo le tue esigenze legali.</li>
      <li>Pubblica almeno 10-20 articoli satellite collegati alle pillar page entro il primo mese.</li>
      <li>Carica immagini ottimizzate WebP e alt text descrittivi per ogni categoria o prodotto.</li>
    </ul>
    <div class="notice">Nota: i prodotti presenti in queste pagine sono impostati come esempi SEO e commerciali. Prima di pubblicare, personalizza copy, immagini e posizionamento in base al tuo stile editoriale.</div>
  </div>
</section>

<footer class="footer">
  <div class="container footer-grid">
    <div>
      <div class="logo">Dragon<span>Ball</span> Picks</div>
      <p class="small">Sito editoriale orientato a recensioni, classifiche e guide all’acquisto. Alcuni link possono generare una commissione senza costi aggiuntivi per l’utente.</p>
    </div>
    <div>
      <h3>Guide principali</h3>
      <ul class="list-clean">
        <li><a href="pages/migliori-figure-dragon-ball.html">Figure Dragon Ball</a></li>
        <li><a href="pages/migliori-gadget-dragon-ball.html">Gadget Dragon Ball</a></li>
        <li><a href="pages/migliori-funko-pop-dragon-ball.html">Funko Pop Dragon Ball</a></li>
      </ul>
    </div>
    <div>
      <h3>Altre sezioni</h3>
      <ul class="list-clean">
        <li><a href="pages/migliori-manga-dragon-ball.html">Manga Dragon Ball</a></li>
        <li><a href="pages/migliori-regali-dragon-ball.html">Regali Dragon Ball</a></li>
        <li><a href="pages/poster-dragon-ball.html">Poster Dragon Ball</a></li>
      </ul>
    </div>
  </div>
  <div class="container small" style="margin-top:20px;">© <span data-year></span> DragonBall Picks</div>
</footer>
'''

(base/'index.html').write_text(layout(f'{site_name} | Guide all\'acquisto Dragon Ball', 'Home minimale SEO per un sito Dragon Ball in affiliazione Amazon con pillar page orientate al ranking.', home_content, f'{base_url}/index.html'), encoding='utf-8')

for p in pillars:
    rows = ''.join([
        f'<tr><td>{name}</td><td>{why}</td><td>{fit}</td><td><a class="btn btn-secondary" href="{amazon_search(name + " " + p["keyword"])}" rel="nofollow sponsored">Vedi su Amazon</a></td></tr>'
        for name, why, fit, _, _ in p['products']
    ])

    product_cards = ''.join([
        f'''<article class="product">
          <div>
            <div class="badge">{label}</div>
            <h3>{name}</h3>
            <p>{why}</p>
            <p><strong>Per chi è adatto:</strong> {fit}.</p>
          </div>
          <div class="actions">
            <a class="btn btn-primary" href="{amazon_search(name + ' ' + p['keyword'])}" rel="nofollow sponsored">Vedi prezzo su Amazon</a>
            <a class="btn btn-secondary" href="../index.html">Torna alla home</a>
          </div>
        </article>'''
        for name, why, label, fit, _ in p['products']
    ])

    faqs = ''.join([f'<div class="faq"><h3>{q}</h3><p>{a}</p></div>' for q,a in p['faq']])
    related = ''.join([f'<li><a href="{href}">{label}</a></li>' for label,href in p['related']])

    jsonld_items = ','.join([
        '{"@type":"ListItem","position":%d,"name":"%s","url":"%s"}' % (i+1, item[0].replace('"','\\"'), amazon_search(item[0] + ' ' + p['keyword']))
        for i,item in enumerate(p['products'])
    ])

    content = f'''
    {build_nav('../')}
    <main class="container" style="padding-top:40px; padding-bottom:56px;">
      <div class="breadcrumbs"><a href="../index.html">Home</a> / {p['title']}</div>
      <div class="article-grid">
        <article>
          <header>
            <div class="kicker">Pillar page commerciale</div>
            <h1>{p['hero']}</h1>
            <p class="lead">{p['intro']}</p>
            <div class="cta-row">
              <a class="btn btn-primary" href="#tabella">Vai alla tabella comparativa</a>
              <a class="btn btn-secondary" href="#faq">Leggi le FAQ</a>
            </div>
          </header>

          <section>
            <div class="content-box">
              <h2>Panoramica veloce</h2>
              <p>{p['title']} è una keyword ad alto potenziale perché unisce ricerca informativa e intenzione d’acquisto. Questa pagina è costruita per intercettare utenti che vogliono confrontare prodotti, trovare idee regalo o scegliere un acquisto in modo più rapido.</p>
              <p>Per migliorare il ranking nel tempo, aggiungi sottopagine dedicate ai singoli personaggi, alle fasce di prezzo e alle versioni premium. Tutte dovranno linkare questa pagina con anchor text naturali e coerenti.</p>
              <div class="notice">Disclosure affiliazione: alcuni link in questa pagina sono link affiliati Amazon e possono generare una commissione. Per la pubblicazione reale, personalizza il testo secondo la tua policy.</div>
            </div>
          </section>

          <section id="tabella">
            <div class="section-head">
              <div>
                <div class="kicker">Confronto rapido</div>
                <h2>Tabella comparativa</h2>
              </div>
              <p>Una tabella ben progettata aiuta l’utente a scansionare la pagina più velocemente e aumenta la probabilità di click sui link commerciali.</p>
            </div>
            <div class="table-wrap">
              <table>
                <thead>
                  <tr>
                    <th>Prodotto</th>
                    <th>Punto forte</th>
                    <th>Ideale per</th>
                    <th>Link</th>
                  </tr>
                </thead>
                <tbody>{rows}</tbody>
              </table>
            </div>
          </section>

          <section>
            <div class="section-head">
              <div>
                <div class="kicker">Selezione editoriale</div>
                <h2>I migliori prodotti da considerare</h2>
              </div>
              <p>Usa questa sezione per approfondire vantaggi, limiti, prezzo percepito e scenario d’uso. È una delle aree più utili sia per il lettore sia per la conversione.</p>
            </div>
            <div class="grid">{product_cards}</div>
          </section>

          <section>
            <div class="content-box">
              <h2>Come scegliere bene</h2>
              <ul>
                <li>Controlla brand, materiali, dimensioni e presenza di componenti ufficiali o licenziati.</li>
                <li>Leggi recensioni con foto reali per verificare differenze tra immagini promozionali e prodotto ricevuto.</li>
                <li>Confronta fascia prezzo e utilità percepita: non sempre il prodotto più costoso è il più adatto.</li>
                <li>Valuta se stai acquistando per te, per collezione o come regalo: il criterio cambia molto.</li>
                <li>Aggiorna periodicamente la pagina con nuovi prodotti e rimuovi quelli non più interessanti.</li>
              </ul>
            </div>
          </section>

          <section id="faq">
            <div class="section-head">
              <div>
                <div class="kicker">FAQ SEO</div>
                <h2>Domande frequenti</h2>
              </div>
              <p>Le FAQ aiutano a coprire query secondarie e migliorano la completezza percepita della guida.</p>
            </div>
            {faqs}
          </section>
        </article>

        <aside class="sidebar-sticky">
          <div class="card">
            <h3>Keyword target</h3>
            <p class="small">{p['title']}</p>
            <div class="hr"></div>
            <h3>Espansioni consigliate</h3>
            <ul class="list-clean related">{related}</ul>
          </div>
          <div class="card" style="margin-top:18px;">
            <h3>Da fare dopo la pubblicazione</h3>
            <ul class="list-clean">
              <li>Aggiungi immagini WebP ottimizzate.</li>
              <li>Inserisci link interni da articoli satellite.</li>
              <li>Aggiorna prodotti e CTA almeno ogni 30-45 giorni.</li>
              <li>Sostituisci i placeholder con il tuo tag affiliato.</li>
            </ul>
          </div>
        </aside>
      </div>
    </main>
    <footer class="footer">
      <div class="container footer-grid">
        <div>
          <div class="logo">Dragon<span>Ball</span> Picks</div>
          <p class="small">Guida editoriale indipendente dedicata a prodotti, manga, gadget e collezionabili Dragon Ball.</p>
        </div>
        <div>
          <h3>Home</h3>
          <ul class="list-clean"><li><a href="../index.html">Torna alla home</a></li></ul>
        </div>
        <div>
          <h3>Altre pillar</h3>
          <ul class="list-clean">
            <li><a href="migliori-figure-dragon-ball.html">Figure</a></li>
            <li><a href="migliori-gadget-dragon-ball.html">Gadget</a></li>
            <li><a href="migliori-manga-dragon-ball.html">Manga</a></li>
          </ul>
        </div>
      </div>
      <div class="container small" style="margin-top:20px;">© <span data-year></span> DragonBall Picks</div>
    </footer>
    <script type="application/ld+json">{{
      "@context":"https://schema.org",
      "@type":"ItemList",
      "name":"{p['title']}",
      "itemListElement":[{jsonld_items}]
    }}</script>
    '''
    (base/'pages'/f"{p['slug']}.html").write_text(layout(f"{p['title']} | {site_name}", p['meta'], content, f"{base_url}/pages/{p['slug']}.html"), encoding='utf-8')

robots = dedent(f'''
User-agent: *
Allow: /

Sitemap: {base_url}/sitemap.xml
''')
(base/'robots.txt').write_text(robots, encoding='utf-8')

sitemap_entries = ['<url><loc>%s/index.html</loc></url>' % base_url] + [f'<url><loc>{base_url}/pages/{p["slug"]}.html</loc></url>' for p in pillars]
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + '\n'.join(sitemap_entries) + '\n</urlset>'
(base/'sitemap.xml').write_text(sitemap, encoding='utf-8')

readme = dedent('''
# DragonBall Picks

Sito statico SEO-oriented per affiliazione Amazon nella nicchia Dragon Ball.

## Cosa include

- Home minimale che distribuisce link juice alle pillar page
- 6 pillar page commerciali già pronte
- CSS e JS leggeri
- robots.txt e sitemap.xml
- Link Amazon con tag placeholder `YOURTAG-21`

## Pubblicazione su GitHub

1. Crea un nuovo repository su GitHub.
2. Carica tutti i file di questa cartella nel repository.
3. Vai su **Settings > Pages**.
4. In **Build and deployment**, scegli **Deploy from a branch**.
5. Seleziona il branch principale e la root `/`.
6. Salva e attendi la pubblicazione.

## Prima di andare online

- Sostituisci `YOURTAG-21` con il tuo vero tag affiliato Amazon.
- Cambia `https://example.com` in `sitemap.xml` e nei file HTML con il tuo dominio o URL GitHub Pages.
- Aggiungi privacy policy, cookie policy e disclosure affiliazione definitiva.
- Inserisci immagini ottimizzate e personalizza i contenuti.

## Struttura

- `index.html`
- `pages/`
- `assets/css/styles.css`
- `assets/js/main.js`
- `robots.txt`
- `sitemap.xml`

## Suggerimento SEO

Aggiungi presto articoli satellite come:

- migliori figure Goku
- migliori figure Vegeta
- gadget Dragon Ball sotto 20 euro
- migliori regali Dragon Ball per adulti
- box manga Dragon Ball completo
- poster Dragon Ball per camera gaming
''')
(base/'README.md').write_text(readme, encoding='utf-8')
