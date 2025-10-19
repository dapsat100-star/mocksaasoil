# -*- coding: utf-8 -*-
# DAP ATLAS — Sidebar SaaS (Key Findings + Slick & Vessel open together by default)
# Export: S = SVG, P = PDF

from datetime import datetime
from base64 import b64encode
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="DAP ATLAS — Sidebar SaaS", page_icon="🛰️", layout="wide")

# ======= Theme
PRIMARY   = "#00E3A5"
BG_DARK   = "#0b1221"
CARD_DARK = "#10182b"
TEXT      = "#FFFFFF"
MUTED     = "#9fb0c9"
BORDER    = "rgba(255,255,255,.10)"

PANEL_W_PX   = 560
PANEL_GAP_PX = 24

# ======= Logo (optional)
logo_uri = ""
p = Path("dapatlas_fundo_branco.png")
if p.exists() and p.stat().st_size > 0:
    logo_uri = "data:image/png;base64," + b64encode(p.read_bytes()).decode("ascii")

# Prebuilt logo HTML (avoids if inside the HTML)
logo_html = f"<img src='{logo_uri}' alt='DAP ATLAS'/>" if logo_uri else "<div style='color:#000;font-weight:900'>DA</div>"

# ======= ISR Offering (short text for About/overlay if needed)
ABOUT_HTML = """
<p><b>DAP ATLAS</b> is a geospatial analytics platform that fuses optical and SAR satellite data, ground sensors,
and AI to support <b>Intelligence, Surveillance, and Reconnaissance (ISR)</b> operations.</p>
<ul>
  <li><b>Technology transfer</b> of the platform</li>
  <li><b>Hands-on training</b> for operators and analysts</li>
  <li><b>Theoretical courses</b> on satellite employment for Defense & Security</li>
  <li><b>Design & setup of an ISR Cell</b> (space operations center for sea/land ISR)</li>
</ul>
<p>Backed by eight years of experience of <b>Márcio Perassoli</b> at the Brazilian Air Force <b>COPE</b> (Space Operations Center),
and consulting roles with <b>SAR satellite providers</b>.</p>
"""

# ======= Data (example)
AOI_ID       = "BR-PA-2025-01"
confidence   = "92%"
extent_km    = "100 km"
area_km2     = "10,000 km²"
resolution   = "20 m"
location     = "Scene 250 × 250 km"
acq_datetime = "2025-06-07 – 09:25"
sensor       = "Sentinel-1"
now_label    = datetime.now().strftime("%d/%m %H:%M")

# ======= Findings (oil)
findings = [
    "Extended anomaly consistent with an oil slick detected in SAR imagery, ~25 km in length.",
    "Indicators suggest a moving vessel as the source — tanker (LPG) Grajau — off the Brazilian coast.",
    "Calm sea state at acquisition time, improving slick contrast and visibility.",
    "Detection point located ~20 km from the shoreline.",
    "Next satellite pass expected in X hours, enabling tracking and confirmation of evolution."
]
findings_html = "".join(f"<li>{a}</li>" for a in findings)

# ======= Tables: Slick & Vessel
def _rows(d: dict) -> str:
    return "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in d.items())

slick_data = {
    "Occurrence Code": "A005",
    "Pass Date": "2019-07-19",
    "Local Time": "04:53",
    "Latitude": "-7.1055",
    "Longitude": "-34.605",
    "Slick Length (km)": "25",
    "Distance to Coast (km)": "20",
    "Sea State": "Calm",
    "SAR Contrast": "Strong",
    "Sensor Type": "SAR",
    "Instrument": "Sentinel-1",
}
vessel_data = {
    "Suspected Source": "Moving vessel",
    "Vessel Type": "Tanker (LPG)",
    "Vessel Name": "Grajau",
    "Flag": "Brazil",
    "Status": "Under way",
    "MMSI": "—",
    "Wind Direction": "Northwest",
    "Wind Speed (knots)": "5",
}
rows_slick  = _rows(slick_data)
rows_vessel = _rows(vessel_data)

# ======= HTML (all JS/CSS inside; note {{ }} escaping literal braces)
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

/* ======= Sections & Metrics (reordered) ======= */
.section-head{{font-weight:900;letter-spacing:.2px;margin:8px 0 6px;color:#fff}}
.metrics{{display:grid;gap:10px;margin-top:6px}}
.metrics.three{{grid-template-columns:repeat(3,minmax(0,1fr))}}
.metrics.one{{grid-template-columns:repeat(1,minmax(0,1fr))}}
@media(max-width:860px){{
  .metrics.three{{grid-template-columns:1fr 1fr}}
}}
.metric{{background:rgba(255,255,255,.04);border:1px solid var(--border);border-radius:14px;padding:12px}}
.metric .k{{font-size:1.15rem;font-weight:800}}
.metric .l{{font-size:.85rem;color:var(--muted)}}

/* ======= Tabs ======= */
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

/* Grid: two tables side by side */
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
          <div class="logo-wrap">{logo_html}</div>
          <div>
            <div class="name">Situation Report</div>
            <div class="sub">SAR Imagery + AI</div>
          </div>
        </div>
        <div class="badge">AOI {AOI_ID} • Live 24/7</div>
      </div>

      <!-- Scene Characteristics first -->
      <div class="section-head">Scene Characteristics</div>
      <div class="metrics three">
        <div class="metric"><div class="k">{extent_km}</div><div class="l">Extent</div></div>
        <div class="metric"><div class="k">{area_km2}</div><div class="l">Area</div></div>
        <div class="metric"><div class="k">{resolution}</div><div class="l">Resolution</div></div>
      </div>

      <!-- Detection after -->
      <div class="section-head">Detection</div>
      <div class="metrics one">
        <div class="metric"><div class="k">{confidence}</div><div class="l">Confidence</div></div>
      </div>

      <!-- Tabs -->
      <div class="tabs">
        <input type="radio" name="tab" id="tab-findings" checked>
        <label for="tab-findings">Key Findings</label>

        <input type="radio" name="tab" id="tab-data">
        <label for="tab-data">Slick & Vessel</label>

        <input type="radio" name="tab" id="tab-meta">
        <label for="tab-meta">Metadata</label>

        <input type="radio" name="tab" id="tab-summary">
        <label for="tab-summary">Summary</label>

        <!-- FINDINGS -->
        <div class="tab-content" id="content-findings">
          <ul class="bullets">
            {findings_html}
          </ul>
        </div>

        <!-- DATA (opens together with Findings) -->
        <div class="tab-content" id="content-data">
          <div class="grid-two">
            <div class="box">
              <h4>Oil Slick Data (SAR)</h4>
              <table class="minimal">{rows_slick}</table>
            </div>
            <div class="box">
              <h4>Vessel Data</h4>
              <table class="minimal">{rows_vessel}</table>
            </div>
          </div>
        </div>

        <!-- META / SUMMARY (filled via JS) -->
        <div class="tab-content" id="content-meta" style="display:none"></div>
        <div class="tab-content" id="content-summary" style="display:none"></div>
      </div>

      <div class="footer">
        <div class="muted small">© {datetime.now().year} MAVIPE Space Systems</div>
      </div>
    </div>
  </div>

  <!-- libs: dom-to-image-more (SVG) + jsPDF + svg2pdf -->
  <script src="https://cdn.jsdelivr.net/npm/dom-to-image-more@2.8.0/dist/dom-to-image-more.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/jspdf@2.5.1/dist/jspdf.umd.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/svg2pdf.js@2.2.3/dist/svg2pdf.umd.min.js"></script>

  <script>
    // Panel refs
    const elFindings = document.getElementById('content-findings');
    const elData     = document.getElementById('content-data');
    const elMeta     = document.getElementById('content-meta');
    const elSummary  = document.getElementById('content-summary');

    // Show Findings + Data together ('f' or 'd'); Meta ('m'); Summary ('s')
    function show(which){{
      const showFD = (which === 'f' || which === 'd');
      elFindings.style.display = showFD ? 'block' : 'none';
      elData.style.display     = showFD ? 'block' : 'none';
      elMeta.style.display     = (which === 'm') ? 'block' : 'none';
      elSummary.style.display  = (which === 's') ? 'block' : 'none';
    }}

    // Tab switching
    document.getElementById('tab-findings').onchange = ()=>show('f');
    document.getElementById('tab-data').onchange     = ()=>show('d');
    document.getElementById('tab-meta').onchange     = ()=>show('m');
    document.getElementById('tab-summary').onchange  = ()=>show('s');

    // Fill Meta/Summary content
    const meta = elMeta, summary = elSummary;
    meta.innerHTML = `
      <div class="section-title">Metadata</div>
      <table class="minimal">
        <tr><th>Location</th><td>{location}</td></tr>
        <tr><th>Acquisition Time</th><td>{acq_datetime}</td></tr>
        <tr><th>Source</th><td>{sensor}</td></tr>
        <tr><th>Generated</th><td>{now_label}</td></tr>
        <tr><th>System</th><td>DAP ATLAS — SITREP</td></tr>
      </table>
    `;
    summary.innerHTML = `
      <div class="section-title">Summary</div>
      <p>
        Detections overlaid on base imagery with sub-meter geometric registration.
        <b>Optical Imagery + AI + multi-sensor fusion</b> pipeline with <b>near-real-time</b> updates.
      </p>
      <div style="margin-top:8px;border:1px solid var(--border);padding:10px;border-radius:10px;background:rgba(255,255,255,.03)">
        {ABOUT_HTML}
      </div>
    `;

    // Show Findings + Data by default
    document.addEventListener('DOMContentLoaded', ()=> show('f'));

    // ===== Vector Export (keyboard shortcuts only) =====
    const PANEL = document.getElementById('panel');

    async function exportSVG() {{
      const dataUrl = await domtoimage.toSvg(PANEL, {{ bgcolor: '{CARD_DARK}', quality: 1 }});
      if (!safeDownload(dataUrl, 'SITREP_Panel.svg')) {{
        window.open(dataUrl, '_blank', 'noopener');
      }}
    }}

    async function exportPDF() {{
      const svgUrl  = await domtoimage.toSvg(PANEL, {{ bgcolor: '{CARD_DARK}', quality: 1 }});
      const svgText = await (await fetch(svgUrl)).text();

      const {{ jsPDF }} = window.jspdf;
      const pdf = new jsPDF({{ unit: 'pt', format: 'a4', orientation: 'p' }});

      // SVG dimensions
      const parser = new DOMParser();
      const svgDoc = parser.parseFromString(svgText, 'image/svg+xml');
      const svgEl  = svgDoc.documentElement;
      const width  = parseFloat(svgEl.getAttribute('width'))  || PANEL.offsetWidth;
      const height = parseFloat(svgEl.getAttribute('height')) || PANEL.offsetHeight;

      // scale to fit page while preserving aspect ratio
      const pageW = pdf.internal.pageSize.getWidth();
      const pageH = pdf.internal.pageSize.getHeight();
      const scale = Math.min(pageW / width, pageH / height);

      window.svg2pdf(svgEl, pdf, {{
        x: (pageW - width * scale) / 2,
        y: (pageH - height * scale) / 2,
        scale: scale
      }});

      try {{
        const blob = pdf.output('blob');
        const url = URL.createObjectURL(blob);
        if (!safeDownload(url, 'SITREP_Panel.pdf')) {{
          window.open(url, '_blank', 'noopener');
        }}
      } catch (e) {{
        console.error(e);
      }}
    }}

    function safeDownload(url, filename) {{
      try {{
        const a = document.createElement('a');
        a.href = url;
        a.download = filename;
        a.rel = 'noopener';
        a.target = '_blank';
        document.body.appendChild(a);
        a.click();
        a.remove();
        return true;
      }} catch (_) {{
        return false;
      }}
    }}

    // Shortcuts: S (SVG) and P (PDF)
    document.addEventListener('keydown', (e) => {{
      if (e.key === 's' || e.key === 'S') exportSVG();
      if (e.key === 'p' || e.key === 'P') exportPDF();
    }});
  </script>
</body></html>
"""

components.html(html, height=900, scrolling=False)
