#!/usr/bin/env python3
"""Render the public policy and synchronize its Android offline copy.

Uses only the Python standard library. Does not build or launch the app.
POLITICA_PRIVACIDAD.md is the content source; index.html supplies the existing style.
"""
import html
import re
from pathlib import Path

SITE = Path(__file__).resolve().parent
ROOT = SITE.parent
source = (SITE / "POLITICA_PRIVACIDAD.md").read_text(encoding="utf-8")
old_html = (SITE / "index.html").read_text(encoding="utf-8")
style = re.search(r"<style>(.*?)</style>", old_html, re.S).group(1)
logo = re.search(r"(<svg\b.*?</svg>)", old_html, re.S).group(1)
date = re.search(r"\*\*Vigencia y última actualización:\*\* ([^\n]+)", source).group(1).strip()
url = re.search(r"\*\*URL pública:\*\* (https://[^\s]+)", source).group(1)


def inline(value):
    value = html.escape(value, quote=True)
    value = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(
        r"https://[^\s<]+",
        lambda match: '<a href="' + match.group(0).rstrip('.') +
        '" rel="noopener noreferrer">' + match.group(0).rstrip('.') + '</a>' +
        ('.' if match.group(0).endswith('.') else ''), value
    )
    return re.sub(r"\bgabow95k@gmail\.com\b", '<a href="mailto:gabow95k@gmail.com">gabow95k@gmail.com</a>', value)


ids = ["responsable", "datos", "finalidad", "permisos", "respaldos", "google",
       "seguridad", "conservacion", "derechos", "menores", "sitio", "cambios"]
sections = []
for index, block in enumerate(re.split(r"(?m)^## ", source)[1:]):
    title, body = block.split("\n", 1)
    ident = ids[index]
    parts = []
    for paragraph in re.split(r"\n\s*\n", body.strip()):
        if paragraph.startswith("### "):
            heading = paragraph[4:].strip()
            anchor = ' id="eliminar-perfil"' if heading == "Eliminación del perfil de la nube" else ''
            parts.append(f"<h3{anchor}>{inline(heading)}</h3>")
        elif paragraph.startswith("- "):
            parts.append("<ul>" + "".join(f"<li>{inline(line[2:])}</li>" for line in paragraph.splitlines()) + "</ul>")
        else:
            parts.append(f"<p>{inline(paragraph)}</p>")
    sections.append((ident, title, "\n".join(parts)))

toc = "\n".join(f'<a href="#{ident}">{html.escape(title)}</a>' for ident, title, _ in sections)
article = "\n".join(
    f'<section id="{ident}" aria-labelledby="h-{ident}">\n<h2 id="h-{ident}">{html.escape(title)}</h2>\n{body}\n</section>'
    for ident, title, body in sections
)
page = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Política de privacidad de EspacioGo: datos locales, cuenta de Google, Drive, estadísticas opcionales, avisos, suscripciones y eliminación del perfil.">
<meta name="color-scheme" content="light">
<meta name="referrer" content="no-referrer">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; img-src 'self' data:; base-uri 'none'; form-action 'none'">
<title>Política de privacidad | EspacioGo</title>
<link rel="canonical" href="{html.escape(url, quote=True)}">
<style>{style}</style>
</head>
<body data-policy-revision="2026-11-22">
<header>
<a class="brand" href="#inicio">{logo}<span>EspacioGo</span></a>
<div class="hero" id="inicio">
<span class="eyebrow">Privacidad y datos</span>
<h1>Política de privacidad</h1>
<p>Conoce qué información utiliza EspacioGo para Android, qué se guarda en tu dispositivo y cómo funcionan los servicios de Google.</p>
<div class="meta"><span>Última actualización: {html.escape(date)}</span><span>Responsable: Gabriel Rodríguez</span></div>
</div>
</header>
<main class="layout">
<aside class="toc" aria-label="Contenido"><strong>Política de privacidad</strong><nav>{toc}</nav></aside>
<div>
<details class="mobile-toc"><summary>Ver contenido de la política</summary><nav aria-label="Contenido móvil">{toc}</nav></details>
<article aria-label="Política de privacidad de EspacioGo">
{article}
<div class="contact"><strong>¿Tienes una consulta de privacidad?</strong><p>Gabriel Rodríguez · <a href="mailto:gabow95k@gmail.com">gabow95k@gmail.com</a></p></div>
</article>
</div>
</main>
<footer><p>EspacioGo · Política de privacidad · Última actualización: {html.escape(date)}.</p></footer>
</body>
</html>
'''
(SITE / "index.html").write_text(page, encoding="utf-8")
if (ROOT / "app/src/main").is_dir():
    assets = ROOT / "app/src/main/assets"
    assets.mkdir(exist_ok=True)
    (assets / "privacy-policy.html").write_text(page, encoding="utf-8")
if (ROOT / "docs").is_dir():
    (ROOT / "docs/POLITICA_PRIVACIDAD.md").write_text(source, encoding="utf-8")
print(f"Política renderizada y copias disponibles sincronizadas: {date}.")
