# -*- coding: utf-8 -*-
# DAP ATLAS — Sidebar SaaS (logo grande + abas CSS + scroll interno + EXPORT SVG/PDF via atalhos)
# Obs.: As abas "Principais Achados" e "Mancha & Embarcação" abrem JUNTAS por padrão.

from datetime import datetime
from base64 import b64encode
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="DAP ATLAS — Sidebar SaaS", page_icon="🛰️", layout="wide")

# ======= Tema
PRIMARY   = "#00E3A5"
BG_DARK   = "#0b1221"
CARD_DARK = "#10182b"
TEXT      = "#FFFFFF"
MUTED     = "#9fb0c9"
BORDER    = "rgba(255,255,255,.10)"

PANEL_W_PX   = 560
PANEL_GAP_PX = 24

# ======= Logo (png com fundo branco) — opcional
logo_uri = ""
p = Path("dapatlas_fundo_branco.png")
if p.exists() and p.stat().st_size > 0:
    logo_uri = "data:image/png;base64," + b64encode(p.read_bytes()).decode("ascii")

# ======= Dados
AOI_ID       = "BR-PA-2025-01"
confianca    = "92%"
extensao_km  = "5 km"
area_km2     = "25 km²"
resolucao    = "35 cm"
local        = "Cena 5 × 5 km"
data_hora    = "07/06/2025 – 09:25"
sensor       = "BlackSky Global-16 (Sensor: Global-16)"
agora        = datetime.now().strftime("%d/%m %H:%M")

# ======= Achados (ajustados para derramamento de óleo)
achados = [
    "Anomalia extensa compatível com mancha de óleo detectada em imagem SAR, com ~25 km de comprimento.",
    "Indícios apontam para origem em embarcação em movimento — navio-tanque (LPG) Grajau — ao largo da costa brasileira.",
    "Estado do mar calmo no momento da aquisição, favorecendo contraste e visibilidade da feição.",
    "Ponto de detecção localizado a ~20 km da linha de costa.",
    "Próximo passe de satélite previsto em X horas, permitindo acompanhamento e confirmação da evolução."
]

# ======= TABELAS: Mancha & Embarcação
def _rows(d: dict) -> str:
    return "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in d.items())

dados_mancha = {
    "Código da Ocorrência": "A005",
    "Data do Passe": "19/07/2019",
    "Hora Local": "04:53",
    "Latitude": "-7.1055",
    "Longitude": "-34.605",
    "Comprimento da Mancha (km)": "25",
    "Distância à Costa (km)": "20",
    "Estado do Mar": "Calmo",
    "Contraste (SAR)": "Forte",
    "Sensor": "SAR",
    "Instrumento": "Sentinel-1",
}

dados_navio = {
    "Fonte Suspeita": "Embarcação em movimento",
    "Tipo de Embarcação": "Navio-tanque (LPG)",
    "Nome do Navio": "Grajau",
    "Bandeira": "Brasil",
    "Status": "Em movimento",
    "MMSI": "—",
    "Direção do Vento": "Noroeste",
    "Velocidade do Vento (nós)": "5",
}

rows_mancha = _rows(dados_mancha)
rows_navio  = _rows(dados_navio)

# ======= HTML
html = f"""
<!doctype html>
<html><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<style>
:root {{
  --panel-w:{PANEL_W_PX}px; --gap:{PANEL_GAP_PX}px;
  --primary:{PRIMARY}; --bg:{BG_DARK}; --card:{CARD_DARK};
  --text:{TEXT}; --muted:{MUTED}; --border:{BORDER};
}}
*{{box-sizing:border-box}}
body{{margin:0;height:100vh;width:100vw;background:var(--bg);color:var(--text);
  font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Inter,Helvetica Neue,Arial,Noto Sans,sans-serif}}
.stage{{height:100vh;width:100vw;position:relative;
  background:radial-gradient(1000px 600px at 70% 40%,rgba(255,255,255,.04),transparent 60%),
             radial-gradient(800px 500px at 30% 70%,rgba(255,255,255,.03),transparent 60%)}}
.side-panel{{
  position:absolute; top:var(--gap); right:var(--gap); bottom:var(--gap);
  width:var(--panel-w); background:var(--card); border:1px solid var(--border);
  border-radius:18px; box-shadow:0 18px 44px rgba(0,0,0,.45);
  padding:16px; display:flex; flex-direction:column; gap:12px;
  overflow:auto;
}}
.panel-header{{display:flex;align-items:center;justify-content:space-between;gap:18px}}
.brand{{display:flex;align-items:center;gap:18px}}
.logo-wrap{{width:80px;height:80px;border-radius:18px;overflow:hidden;background:#fff;
  border:1px solid var(--border);display:flex;align-items:center;justify-content:center}}
.logo-wrap img{{width:100%;height:100%;object-fit:contain;display:block}}
.name{{font-weight:800;letter-spacing:.2px;line-height:1.1;font-size:1.1rem}}
.sub{{font-size:.82rem;color:var(--muted);margin-top:2px}}
.badge{{background:rgba(0,227,165,.12);color:var(--primary);border:1px solid rgba(0,227,165,.25);
  padding:6px 10px;border-radius:999px;font-weight:700;font-size:.85rem;white-space:nowrap}}
.metrics{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-top:6px}}
.metric{{background:rgba(255,255,255,.04);border:1px solid var(--border);border-radius:14px;padding:12px}}
.metric .k{{font-size:1.15rem;font-weight:800}}
.metric .l{{font-size:.85rem;color:var(--muted)}}

/* ======= Abas ======= */
.tabs{{margin-top:6px}}
.tabs input{{display:none}}
.tabs label{{
  display:inline-block; padding:8px 12px; margin-right:8px; border:1px solid var(--border);
  border-bottom:none; border-top-left-radius:10px; border-top-right-radius:10px;
  color:var(--muted); background:rgba(255,255,255,.02); cursor:pointer; font-weight:700; font-size:.92rem
}}
.tabs input:checked + label{{color:#08121f; background:var(--primary); border-color:var(--primary)}}
.tab-content{{border:1px solid var(--border); border-radius:0 12px 12px 12px; padding:12px; margin-top:-1px}}

ul.bullets{{margin:6px 0 0 0; padding-left:1.1rem}}
ul.bullets li{{margin:8px 0}}
.section-title{{font-weight:800; margin: 2px 0 8px}}

table.minimal{{width:100%;border-collapse:collapse;margin-top:2px}}
table.minimal th, table.minimal td{{border-bottom:1px solid var(--border);padding:9px 6px;text-align:left;font-size:.95rem}}
table.minimal th{{color:var(--muted);font-weight:600}}

.footer{{margin-top:auto;display:flex;justify-content:space-between;align-items:center;gap:10px}}
.small{{font-size:.85rem}}

/* Grid para as duas tabelas lado a lado */
.grid-two{{display:grid;grid-template-columns:1fr 1fr;gap:12px}}
@media(max-width:860px){{.grid-two{{grid-template-columns:1fr}}}}
.box{{background:rgba(255,255,255,.03);border:1px solid var(--border);border-radius:10px;padding:10px}}
.box h4{{margin:0 0 8px;color:#fff;font-size:1rem;font-weight:800}}
</style>
</head>
<body>
  <div class="stage">
    <div class="side-panel" id="panel">
      <div class="panel-header">
        <div class="brand">
          <div class="logo-wrap">
            {"<img src='"+logo_uri+"' alt='DAP ATLAS'/>" if logo_uri else "<div style='color:#000;font-weight:900'>DA</div>"}
          </div>
          <div>
            <div class="name">Relatório de Situação</div>
            <div class="sub">Imagem Óptica + IA</div>
          </div>
        </div>
        <div class="badge">AOI {AOI_ID} • Live 24/7</div>
      </div>

      <div class="metrics">
        <div class="metric"><div class="k">{confianca}</div><div class="l">Confiança</div></div>
        <div class="metric"><div class="k">{extensao_km}</div><div class="l">Extensão</div></div>
        <div class="metric"><div class="k">{area_km2}</div><div class="l">Área</div></div>
        <div class="metric"><div class="k">{resolucao}</div><div class="l">Resolução</div></div>
      </div>

      <!-- Abas -->
      <div class="tabs">
        <input type="radio" name="tab" id="tab-achados" checked>
        <label for="tab-achados">Principais Achados</label>

        <input type="radio" name="tab" id="tab-dados">
        <label for="tab-dados">Mancha & Embarcação</label>

        <input type="radio" name="tab" id="tab-meta">
        <label for="tab-meta">Metadados</label>

        <input type="radio" name="tab" id="tab-resumo">
        <label for="tab-resumo">Resumo</label>

        <!-- ACHADOS -->
        <div class="tab-content" id="content-achados">
          <ul class="bullets">
            {''.join(f'<li>{a}</li>' for a in achados)}
          </ul>
        </div>

        <!-- DADOS (abre junto com os Achados) -->
        <div class="tab-content" id="content-dados">
          <div class="grid-two">
            <div class="box">
              <h4>Dados da Mancha (SAR)</h4>
              <table class="minimal">{rows_mancha}</table>
            </div>
            <div class="box">
              <h4>Dados da Embarcação</h4>
              <table class="minimal">{rows_navio}</table>
            </div>
          </div>
        </div>

        <!-- META / RESUMO (preenchidos via JS) -->
        <div class="tab-content" id="content-meta" style="display:none"></div>
        <div class="tab-content" id="content-resumo" style="display:none"></div>
      </div>

      <div class="footer">
        <div class="muted small">© {datetime.now().year} MAVIPE Sistemas Espaciais</div>
      </div>
    </div>
  </div>

  <!-- libs: dom-to-image-more (SVG) + jsPDF + svg2pdf -->
  <script src="https://cdn.jsdelivr.net/npm/dom-to-image-more@2.8.0/dist/dom-to-image-more.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/jspdf@2.5.1/dist/jspdf.umd.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/svg2pdf.js@2.2.3/dist/svg2pdf.umd.min.js"></script>

  <script>
    // Referências dos painéis
    const elAchados = document.getElementById('content-achados');
    const elDados   = document.getElementById('content-dados');
    const elMeta    = document.getElementById('content-meta');
    const elResumo  = document.getElementById('content-resumo');

    // Função de exibição:
    //  - 'a' (Achados)  => mostra Achados E Dados juntos
    //  - 'd' (Dados)    => mostra Achados E Dados juntos (comportamento solicitado)
    //  - 'm' (Metadados)=> esconde Achados/Dados e mostra Metadados
    //  - 'r' (Resumo)   => esconde Achados/Dados e mostra Resumo
    function show(which){
      const showAD = (which === 'a' || which === 'd');
      elAchados.style.display = showAD ? 'block' : 'none';
      elDados.style.display   = showAD ? 'block' : 'none';
      elMeta.style.display    = (which === 'm') ? 'block' : 'none';
      elResumo.style.display  = (which === 'r') ? 'block' : 'none';
    }

    // Troca das abas
    document.getElementById('tab-achados').onchange = ()=>show('a');
    document.getElementById('tab-dados').onchange   = ()=>show('d');
    document.getElementById('tab-meta').onchange    = ()=>show('m');
    document.getElementById('tab-resumo').onchange  = ()=>show('r');

    // Preenche conteúdo das abas Meta/Resumo
    const meta = elMeta, resumo = elResumo;
    meta.innerHTML = `
      <div class="section-title">Metadados</div>
      <table class="minimal">
        <tr><th>Local</th><td>{local}</td></tr>
        <tr><th>Data/Hora</th><td>{data_hora}</td></tr>
        <tr><th>Fonte</th><td>{sensor}</td></tr>
        <tr><th>Geração</th><td>{agora}</td></tr>
        <tr><th>Sistema</th><td>DAP ATLAS — SITREP</td></tr>
      </table>
    `;
    resumo.innerHTML = `
      <div class="section-title">Resumo</div>
      <p>
        Detecções sobrepostas à imagem base, com registro geométrico submétrico.
        Pipeline <b>Imagem Óptica + IA + fusão multi-sensor</b> com atualização em <b>tempo quase-real</b>.
      </p>
    `;

    // Exibe Achados + Dados logo de cara
    document.addEventListener('DOMContentLoaded', ()=> show('a'));

    // ===== Exportação Vetorial (somente atalhos) =====
    const PANEL = document.getElementById('panel');

    async function exportSVG() {
      const dataUrl = await domtoimage.toSvg(PANEL, { bgcolor: '{CARD_DARK}', quality: 1 });
      if (!safeDownload(dataUrl, 'SITREP_Painel.svg')) {
        window.open(dataUrl, '_blank', 'noopener');
      }
    }

    async function exportPDF() {
      const svgUrl  = await domtoimage.toSvg(PANEL, { bgcolor: '{CARD_DARK}', quality: 1 });
      const svgText = await (await fetch(svgUrl)).text();

      const { jsPDF } = window.jspdf;
      const pdf = new jsPDF({ unit: 'pt', format: 'a4', orientation: 'p' });

      // dimensões do SVG
      const parser = new DOMParser();
      const svgDoc = parser.parseFromString(svgText, 'image/svg+xml');
      const svgEl  = svgDoc.documentElement;
      const width  = parseFloat(svgEl.getAttribute('width'))  || PANEL.offsetWidth;
      const height = parseFloat(svgEl.getAttribute('height')) || PANEL.offsetHeight;

      // escala para caber na página mantendo proporção
      const pageW = pdf.internal.pageSize.getWidth();
      const pageH = pdf.internal.pageSize.getHeight();
      const scale = Math.min(pageW / width, pageH / height);

      window.svg2pdf(svgEl, pdf, {
        x: (pageW - width * scale) / 2,
        y: (pageH - height * scale) / 2,
        scale: scale
      });

      try {
        const blob = pdf.output('blob');
        const url = URL.createObjectURL(blob);
        if (!safeDownload(url, 'SITREP_Painel.pdf')) {
          window.open(url, '_blank', 'noopener');
        }
      } catch (e) {
        console.error(e);
      }
    }

    function safeDownload(url, filename) {
      try {
        const a = document.createElement('a');
        a.href = url;
        a.download = filename;
        a.rel = 'noopener';
        a.target = '_blank';
        document.body.appendChild(a);
        a.click();
        a.remove();
        return true;
      } catch (_) {
        return false;
      }
    }

    // Atalhos: S (SVG) e P (PDF)
    document.addEventListener('keydown', (e) => {
      if (e.key === 's' || e.key === 'S') exportSVG();
      if (e.key === 'p' || e.key === 'P') exportPDF();
    });
  </script>
</body></html>
"""

components.html(html, height=900, scrolling=False)


