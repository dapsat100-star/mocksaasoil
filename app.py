# ---------- BLOCO HTML: SITREP OIL SPILL (img esquerda, tabela meio, narrativa direita) ----------
# assets
logo_uri = ""
lp = Path("dapatlas.png")
if lp.exists() and lp.stat().st_size > 0:
    logo_uri = "data:image/png;base64," + b64encode(lp.read_bytes()).decode("ascii")

img_uri = ""
ip = Path("sar_base.png")
if ip.exists() and ip.stat().st_size > 0:
    img_uri = "data:image/png;base64," + b64encode(ip.read_bytes()).decode("ascii")

# dados do relatório (edite à vontade)
SITREP = {
    "occ_code": "A005",
    "pass_date": "July 19th, 2019",
    "pass_hour": "04h53 (Local time)",
    "lat": "-7.1055",
    "lon": "-34.605",
    "confidence": "High",
    "source": "Ship",
    "ship_name": "—",
    "flag": "Brazil",
    "ship_status": "Moving",
    "vessel_type": "LPG Tanker",
    "mmsi": "—",
    "wind_dir": "Northwest",
    "wind_spd": "5",
    "contrast": "Strong",
    "sea_state": "Calm",
    "slick_len_km": "25",
    "dist_shore_km": "20",
    "sensor": "SAR",
    "instrument": "Sentinel-1"
}

narrative = (
    "The oil spill detection process has identified a large anomaly, potentially associated with an oil slick, "
    f"measuring {SITREP['slick_len_km']} kilometers in length. It is suspected to have originated from a moving "
    f"{SITREP['vessel_type']} named {SITREP['ship_name']} off the Brazilian coast. With a calm sea state, the "
    f"anomaly was detected just {SITREP['dist_shore_km']} km from shore. The next satellite pass is scheduled "
    "for 6 hours, providing an opportunity for further monitoring and assessment."
)

html2 = f"""
<!doctype html>
<html><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<style>
  :root {{
    --bg:#0b1221; --panel:#10182b; --border:rgba(255,255,255,.12);
    --ink:#e6eefc; --muted:#9fb0c9; --accent:#24d3a7;
  }}
  *{{box-sizing:border-box}} body{{margin:0;background:var(--bg);color:var(--ink);
  font:14px/1.45 -apple-system,BlinkMacSystemFont,'Segoe UI',Inter,Roboto,Helvetica,Arial,sans-serif}}

  .wrap{{display:grid;grid-template-columns:1.2fr .9fr 1fr;gap:0;border-left:0;min-height:900px}}
  .pane{{padding:16px 18px}}
  .pane--img{{position:relative;overflow:hidden}}
  .imgbox{{position:relative;border-right:1px solid var(--border)}}
  .imgbox img{{width:100%;height:100%;object-fit:cover;display:block;filter:grayscale(.1) contrast(1.05)}}

  /* overlays (setinhas/retângulos do exemplo) */
  .overlay{{position:absolute;inset:0;pointer-events:none}}
  .slick{{position:absolute;left:12%;top:17%;width:3px;height:56%;background:transparent;
          border:3px dashed #ffd84a;transform:rotate(-14deg)}}
  .ship{{position:absolute;left:14%;top:63%;width:48px;height:48px;border-radius:50%;
         border:4px solid #ff4d4d}}
  .label{{position:absolute;background:#000; color:#fff; padding:6px 10px; border-radius:6px; font-weight:700}}
  .lbl-a{{left:20%;top:22%}} .lbl-ship{{left:19%;top:66%}}

  /* coluna do meio (tabela) */
  .mid{{background:var(--panel);border-left:1px solid var(--border);border-right:1px solid var(--border)}}
  .mid h3{{margin:0 0 10px;font-size:15px;letter-spacing:.2px;color:#fff;background:#0e1629;padding:10px;border-radius:8px}}
  table{{width:100%;border-collapse:collapse}}
  th,td{{padding:8px;border-bottom:1px solid var(--border);text-align:left}}
  th{{color:var(--muted);font-weight:600;width:48%}}
  td{{color:#e6eefc}}

  /* coluna direita (narrativa) */
  .right{{background:#0f1a2e;position:relative}}
  .brand{{position:absolute;top:18px;right:18px;display:flex;flex-direction:column;align-items:center;gap:6px}}
  .brand img{{width:92px;height:92px;object-fit:contain;display:block;filter:drop-shadow(0 4px 10px rgba(0,0,0,.4))}}
  .sr-title{{margin:130px 0 10px;background:#0e1629;color:#fff;padding:10px 12px;border:1px solid var(--border);
             font-size:22px;letter-spacing:.6px;font-weight:900;border-radius:6px;text-align:center}}
  .sr-body{{background:#0e1629;border:1px solid var(--border);border-radius:10px;color:#dfe8ff;padding:14px}}
  .footnote{{color:#cdd7f2;text-align:center;margin:14px 0 4px;font-size:12px;opacity:.9}}

  /* export area */
  #export-root{{margin:16px}}
</style>
</head>
<body>
  <div id="export-root" class="wrap">
    <!-- ESQUERDA: IMAGEM SAR -->
    <div class="pane pane--img">
      <div class="imgbox">{('<img src="'+img_uri+'" alt="SAR"/>') if img_uri else '<div style="background:#1a2744;height:100%"></div>'}</div>
      <div class="overlay">
        <div class="slick"></div>
        <div class="ship"></div>
        <div class="label lbl-a">A005</div>
        <div class="label lbl-ship">Ship</div>
      </div>
      <div class="footnote">Contains modified Copernicus Sentinel-1 data (2019), processed by MAVIPE Sistemas Espaciais</div>
    </div>

    <!-- MEIO: TABELA -->
    <div class="pane mid">
      <h3>Oil Spill Information</h3>
      <table>
        <tr><th>Occurrence Code</th><td>{SITREP['occ_code']}</td></tr>
        <tr><th>Satellite Pass Date</th><td>{SITREP['pass_date']}</td></tr>
        <tr><th>Satellite Pass Hour</th><td>{SITREP['pass_hour']}</td></tr>
        <tr><th>Lat</th><td>{SITREP['lat']}</td></tr>
        <tr><th>Long</th><td>{SITREP['lon']}</td></tr>
        <tr><th>Anomaly Confidence</th><td>{SITREP['confidence']}</td></tr>
        <tr><th>Potential Source of Pollution</th><td>{SITREP['source']}</td></tr>
        <tr><th>Ship's Name</th><td>{SITREP['ship_name']}</td></tr>
        <tr><th>Flag</th><td>{SITREP['flag']}</td></tr>
        <tr><th>Ship Status</th><td>{SITREP['ship_status']}</td></tr>
        <tr><th>Vessel Type</th><td>{SITREP['vessel_type']}</td></tr>
        <tr><th>MMSI</th><td>{SITREP['mmsi']}</td></tr>
        <tr><th>Wind Direction</th><td>{SITREP['wind_dir']}</td></tr>
        <tr><th>Wind Speed (knots)</th><td>{SITREP['wind_spd']}</td></tr>
        <tr><th>Contrast</th><td>{SITREP['contrast']}</td></tr>
        <tr><th>Sea State</th><td>{SITREP['sea_state']}</td></tr>
        <tr><th>Length of Slick (km)</th><td>{SITREP['slick_len_km']}</td></tr>
        <tr><th>Distance to Shore (km)</th><td>{SITREP['dist_shore_km']}</td></tr>
        <tr><th>Sensor</th><td>{SITREP['sensor']}</td></tr>
        <tr><th>Instrument</th><td>{SITREP['instrument']}</td></tr>
      </table>
    </div>

    <!-- DIREITA: NARRATIVA + LOGO -->
    <div class="pane right">
      <div class="brand">{('<img src="'+logo_uri+'" alt="DAP ATLAS"/>') if logo_uri else ''}<div></div></div>
      <div class="sr-title">SITUATION REPORT</div>
      <div class="sr-body">{narrative}</div>
    </div>
  </div>

  <!-- libs de exportação -->
  <script src="https://cdn.jsdelivr.net/npm/dom-to-image-more@2.8.0/dist/dom-to-image-more.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/jspdf@2.5.1/dist/jspdf.umd.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/svg2pdf.js@2.2.3/dist/svg2pdf.umd.min.js"></script>
  <script>
    const ROOT = document.getElementById('export-root');

    async function exportSVG() {{
      const dataUrl = await domtoimage.toSvg(ROOT, {{ quality: 1, bgcolor: '{BG_DARK}' }});
      const a = document.createElement('a'); a.href = dataUrl; a.download = 'SITREP_OilSpill.svg'; a.click();
    }}

    async function exportPDF() {{
      const svgUrl  = await domtoimage.toSvg(ROOT, {{ quality: 1, bgcolor: '{BG_DARK}' }});
      const svgTxt  = await (await fetch(svgUrl)).text();
      const {{ jsPDF }} = window.jspdf; const pdf = new jsPDF({{ unit:'pt', format:'a4', orientation:'l' }});
      const parser = new DOMParser(); const svgDoc = parser.parseFromString(svgTxt,'image/svg+xml'); const svgEl = svgDoc.documentElement;
      const pageW = pdf.internal.pageSize.getWidth(); const pageH = pdf.internal.pageSize.getHeight();
      const width = ROOT.offsetWidth; const height = ROOT.offsetHeight; const scale = Math.min(pageW/width, pageH/height);
      window.svg2pdf(svgEl, pdf, {{ x:(pageW-width*scale)/2, y:(pageH-height*scale)/2, scale:scale }});
      pdf.save('SITREP_OilSpill.pdf');
    }}

    document.addEventListener('keydown', (e) => {{
      if (e.key === 's' || e.key === 'S') exportSVG();
      if (e.key === 'p' || e.key === 'P') exportPDF();
    }});
  </script>
</body></html>
"""

components.html(html2, height=920, scrolling=False)
