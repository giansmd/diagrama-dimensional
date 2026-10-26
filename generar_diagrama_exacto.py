"""
generar_diagrama_exacto.py
===========================
Genera el diagrama 'ANÁLISIS DIMENSIONAL CONFORMADO DE BUYERS'
con los 7 ejes dimensionales, niveles claramente separados del eje
(sin superposición en DimFecha, DimAnuncio ni DimCampaña) y panel de medidas.
"""

import math
import os

def generar_diagrama_svg(ruta_svg="diagrama_exacto.svg"):
    """Genera el diagrama como archivo SVG vectorial puro, nítido y editable."""
    w = 985
    h = 523
    cx = 313.0
    cy = 293.0
    axis_len = 195.0
    
    # 7 ejes dimensionales calibrados
    axes = [
        {
            "name": "DimFecha",
            "angle": 98,
            "title_x": cx + 215 * math.cos(math.radians(98)),
            "title_y": cy - 215 * math.sin(math.radians(98)) - 14,
            "title_anchor": "middle",
            "ticks": [
                {"r": 62, "text": "Día", "tx": 318, "ty": 232, "anchor": "start"},
                {"r": 102, "text": "Mes", "tx": 312, "ty": 192, "anchor": "start"},
                {"r": 142, "text": "Trimestre", "tx": 307, "ty": 152, "anchor": "start"},
                {"r": 182, "text": "Año", "tx": 302, "ty": 113, "anchor": "start"},
            ]
        },
        {
            "name": "DimBuyer",
            "angle": 50,
            "title_x": cx + 220 * math.cos(math.radians(50)),
            "title_y": cy - 220 * math.sin(math.radians(50)) - 8,
            "title_anchor": "start",
            "ticks": [
                {"r": 62, "text": "Nombre", "tx": 366, "ty": 248, "anchor": "start"},
                {"r": 102, "text": "Plato favorito", "tx": 392, "ty": 218, "anchor": "start"},
                {"r": 142, "text": "Tipo Buyer", "tx": 418, "ty": 187, "anchor": "start"},
                {"r": 182, "text": "Red Social", "tx": 443, "ty": 157, "anchor": "start"},
            ]
        },
        {
            "name": "DimProducto",
            "angle": 0,
            "title_x": cx + axis_len + 28,
            "title_y": cy + 1,
            "title_anchor": "start",
            "ticks": [
                {"r": 62, "text": "Pertene_combo", "tx": 375, "ty": 311, "anchor": "middle"},
                {"r": 102, "text": "Categoria", "tx": 415, "ty": 311, "anchor": "middle"},
                {"r": 142, "text": "Precio_base", "tx": 455, "ty": 311, "anchor": "middle"},
                {"r": 182, "text": "Nombre", "tx": 495, "ty": 311, "anchor": "middle"},
            ]
        },
        {
            "name": "DimCampaña",
            "angle": 299,
            "title_x": cx + 220 * math.cos(math.radians(299)) + 4,
            "title_y": cy - 220 * math.sin(math.radians(299)) + 14,
            "title_anchor": "start",
            "ticks": [
                {"r": 62, "text": "Fuente UTM", "tx": 358, "ty": 345, "anchor": "start"},
                {"r": 102, "text": "Plato Gancho", "tx": 378, "ty": 380, "anchor": "start"},
                {"r": 142, "text": "Tipo Buyer Objetivo", "tx": 398, "ty": 415, "anchor": "start"},
                {"r": 182, "text": "Nombre", "tx": 418, "ty": 450, "anchor": "start"},
            ]
        },
        {
            "name": "DimPersonal",
            "angle": 250,
            "title_x": cx + 220 * math.cos(math.radians(250)),
            "title_y": cy - 220 * math.sin(math.radians(250)) + 14,
            "title_anchor": "middle",
            "ticks": [
                {"r": 62, "text": "Nombres", "tx": 278, "ty": 351, "anchor": "end"},
                {"r": 102, "text": "Apellidos", "tx": 264, "ty": 389, "anchor": "end"},
                {"r": 142, "text": "Cargo", "tx": 250, "ty": 427, "anchor": "end"},
                {"r": 182, "text": "Área", "tx": 236, "ty": 464, "anchor": "end"},
            ]
        },
        {
            "name": "DimRedSocial",
            "angle": 201,
            "title_x": cx + 220 * math.cos(math.radians(201)) - 8,
            "title_y": cy - 220 * math.sin(math.radians(201)) + 6,
            "title_anchor": "end",
            "ticks": [
                {"r": 45, "text": "URL", "tx": 271, "ty": 298, "anchor": "middle"},
                {"r": 95, "text": "Nombre de Página", "tx": 224, "ty": 315, "anchor": "middle"},
                {"r": 145, "text": "Plataforma", "tx": 178, "ty": 333, "anchor": "middle"},
                {"r": 182, "text": "Personal", "tx": 143, "ty": 346, "anchor": "middle"},
            ]
        },
        {
            "name": "DimAnuncio",
            "angle": 151,
            "title_x": cx + 220 * math.cos(math.radians(151)) - 6,
            "title_y": cy - 220 * math.sin(math.radians(151)) - 8,
            "title_anchor": "end",
            "ticks": [
                {"r": 62, "text": "Nombre", "tx": 244, "ty": 259, "anchor": "end"},
                {"r": 102, "text": "Hora Inicio", "tx": 209, "ty": 239, "anchor": "end"},
                {"r": 142, "text": "Horario Fin", "tx": 174, "ty": 220, "anchor": "end"},
                {"r": 182, "text": "Campaña", "tx": 139, "ty": 201, "anchor": "end"},
            ]
        }
    ]

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">')
    svg.append('  <style>')
    svg.append('    .title { font-family: "Arial", sans-serif; font-size: 14.5px; font-weight: bold; fill: #000; letter-spacing: 0.5px; }')
    svg.append('    .dim-name { font-family: "Arial", sans-serif; font-size: 10.5px; font-weight: bold; fill: #000; }')
    svg.append('    .tick-label { font-family: "Arial", sans-serif; font-size: 8.5px; fill: #111; paint-order: stroke fill; stroke: #ffffff; stroke-width: 3.5px; stroke-linejoin: round; stroke-linecap: round; }')
    svg.append('    .box-title { font-family: "Arial", sans-serif; font-size: 13.5px; font-weight: bold; fill: #000; }')
    svg.append('    .medida-group { font-family: "Arial", sans-serif; font-size: 9px; font-weight: bold; fill: #000; }')
    svg.append('    .medida-item { font-family: "Arial", sans-serif; font-size: 8.5px; fill: #222; }')
    svg.append('    .axis-line { stroke: #000; stroke-width: 1.4; stroke-linecap: round; }')
    svg.append('    .tick-line { stroke: #000; stroke-width: 1.3; }')
    svg.append('  </style>')

    # Fondo blanco
    svg.append(f'  <rect width="{w}" height="{h}" fill="#ffffff" />')

    # Marcadores de flechas
    svg.append('  <defs>')
    svg.append('    <marker id="arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">')
    svg.append('      <path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#000000" />')
    svg.append('    </marker>')
    svg.append('  </defs>')

    # 1. TÍTULO PRINCIPAL
    svg.append('  <!-- Título principal -->')
    svg.append(f'  <text x="518" y="36" text-anchor="middle" class="title">ANÁLISIS DIMENSIONAL CONFORMADO DE BUYERS</text>')

    # 2. EJES Y MARCAS
    svg.append('  <!-- Ejes radiales -->')
    for ax in axes:
        rad = math.radians(ax["angle"])
        ux = math.cos(rad)
        uy = -math.sin(rad)
        px = -uy
        py = ux

        tip_x = cx + axis_len * ux
        tip_y = cy + axis_len * uy

        # Línea de eje con flecha
        svg.append(f'  <line x1="{cx}" y1="{cy}" x2="{tip_x:.1f}" y2="{tip_y:.1f}" class="axis-line" marker-end="url(#arrow)" />')

        # Nombre de dimensión
        svg.append(f'  <text x="{ax["title_x"]:.1f}" y="{ax["title_y"]:.1f}" text-anchor="{ax["title_anchor"]}" dominant-baseline="middle" class="dim-name">{ax["name"]}</text>')

        # Marcas y textos
        for t in ax["ticks"]:
            tx = cx + t["r"] * ux
            ty = cy + t["r"] * uy
            t_half = 5.5
            x1 = tx + t_half * px
            y1 = ty + t_half * py
            x2 = tx - t_half * px
            y2 = ty - t_half * py

            svg.append(f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="tick-line" />')
            svg.append(f'  <text x="{t["tx"]}" y="{t["ty"]}" text-anchor="{t["anchor"]}" dominant-baseline="middle" class="tick-label">{t["text"]}</text>')

    # 3. CAJA DE MEDIDAS
    bx = 649
    by = 138
    bw = 290
    bh = 294
    title_center_x = bx + bw / 2

    svg.append('  <!-- Caja de Medidas -->')
    svg.append(f'  <rect x="{bx}" y="{by}" width="{bw}" height="{bh}" fill="#fff9c4" stroke="#000000" stroke-width="1.6" />')
    svg.append(f'  <text x="{title_center_x}" y="{by + 26}" text-anchor="middle" class="box-title">Medidas</text>')
    svg.append(f'  <line x1="{title_center_x - 35}" y1="{by + 34}" x2="{title_center_x + 35}" y2="{by + 34}" stroke="#000000" stroke-width="1.3" />')

    grupos = [
        {
            "titulo": "• Costo por BUYER:",
            "items": [
                "- Gasto en anuncios",
                "- N° de buyers que llenan el formulario"
            ]
        },
        {
            "titulo": "• Tasa de interés en menú digital:",
            "items": [
                "- N° de personas que hicieron clic en el menú",
                "- N° de personas que visitan la página"
            ]
        },
        {
            "titulo": "• Tasa de Conversión BUYER a LEAD:",
            "items": [
                "- N° leads",
                "- N° buyers"
            ]
        }
    ]

    curr_y = by + 58
    left_titulo = bx + 22
    left_item = bx + 34

    for g in grupos:
        svg.append(f'  <text x="{left_titulo}" y="{curr_y}" class="medida-group">{g["titulo"]}</text>')
        curr_y += 15
        for item in g["items"]:
            svg.append(f'  <text x="{left_item}" y="{curr_y}" class="medida-item">{item}</text>')
            curr_y += 13.5
        curr_y += 9

    svg.append('</svg>')

    with open(ruta_svg, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg))
    print(f"SVG generado: {ruta_svg}")


def generar_diagrama_png(ruta_png="diagrama_exacto.png"):
    """Genera el PNG de alta fidelidad con matplotlib, nítido y con halo blanco anti-solapamiento."""
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    import matplotlib.patheffects as path_effects

    w = 985
    h = 523
    dpi = 150
    fig = plt.figure(figsize=(w / 100, h / 100), dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, w)
    ax.set_ylim(h, 0)
    ax.axis('off')

    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    font = 'Arial'

    # Título principal
    ax.text(518, 36, "ANÁLISIS DIMENSIONAL CONFORMADO DE BUYERS", fontsize=13, fontweight='bold', fontfamily=font, color='#000000', ha='center', va='center')

    cx = 313.0
    cy = 293.0
    axis_len = 195.0
    tick_half = 5.5

    axes = [
        {
            "name": "DimFecha", "angle": 98,
            "title_pos": (cx + 215 * math.cos(math.radians(98)), cy - 215 * math.sin(math.radians(98)) - 14),
            "ha": "center", "va": "center",
            "ticks": [
                {"r": 62, "text": "Día", "offset": (12, 0), "ha": "left"},
                {"r": 102, "text": "Mes", "offset": (12, 0), "ha": "left"},
                {"r": 142, "text": "Trimestre", "offset": (12, 0), "ha": "left"},
                {"r": 182, "text": "Año", "offset": (12, 0), "ha": "left"},
            ]
        },
        {
            "name": "DimBuyer", "angle": 50,
            "title_pos": (cx + 220 * math.cos(math.radians(50)), cy - 220 * math.sin(math.radians(50)) - 8),
            "ha": "left", "va": "center",
            "ticks": [
                {"r": 62, "text": "Nombre", "offset": (12, 2), "ha": "left"},
                {"r": 102, "text": "Plato favorito", "offset": (12, 2), "ha": "left"},
                {"r": 142, "text": "Tipo Buyer", "offset": (12, 2), "ha": "left"},
                {"r": 182, "text": "Red Social", "offset": (12, 2), "ha": "left"},
            ]
        },
        {
            "name": "DimProducto", "angle": 0,
            "title_pos": (cx + axis_len + 28, cy + 1),
            "ha": "left", "va": "center",
            "ticks": [
                {"r": 62, "text": "Pertene_combo", "offset": (0, 16), "ha": "center"},
                {"r": 102, "text": "Categoria", "offset": (0, 16), "ha": "center"},
                {"r": 142, "text": "Precio_base", "offset": (0, 16), "ha": "center"},
                {"r": 182, "text": "Nombre", "offset": (0, 16), "ha": "center"},
            ]
        },
        {
            "name": "DimCampaña", "angle": 299,
            "title_pos": (cx + 220 * math.cos(math.radians(299)) + 4, cy - 220 * math.sin(math.radians(299)) + 14),
            "ha": "left", "va": "center",
            "ticks": [
                {"r": 62, "text": "Fuente UTM", "offset": (14, -2), "ha": "left"},
                {"r": 102, "text": "Plato Gancho", "offset": (14, -2), "ha": "left"},
                {"r": 142, "text": "Tipo Buyer Objetivo", "offset": (14, -2), "ha": "left"},
                {"r": 182, "text": "Nombre", "offset": (14, -2), "ha": "left"},
            ]
        },
        {
            "name": "DimPersonal", "angle": 250,
            "title_pos": (cx + 220 * math.cos(math.radians(250)), cy - 220 * math.sin(math.radians(250)) + 14),
            "ha": "center", "va": "center",
            "ticks": [
                {"r": 62, "text": "Nombres", "offset": (-14, 0), "ha": "right"},
                {"r": 102, "text": "Apellidos", "offset": (-14, 0), "ha": "right"},
                {"r": 142, "text": "Cargo", "offset": (-14, 0), "ha": "right"},
                {"r": 182, "text": "Área", "offset": (-14, 0), "ha": "right"},
            ]
        },
        {
            "name": "DimRedSocial", "angle": 201,
            "title_pos": (cx + 220 * math.cos(math.radians(201)) - 8, cy - 220 * math.sin(math.radians(201)) + 6),
            "ha": "right", "va": "center",
            "ticks": [
                {"r": 45, "text": "URL", "offset": (-10, -12), "ha": "center"},
                {"r": 95, "text": "Nombre de Página", "offset": (-4, -12), "ha": "center"},
                {"r": 145, "text": "Plataforma", "offset": (0, -12), "ha": "center"},
                {"r": 182, "text": "Personal", "offset": (0, -12), "ha": "center"},
            ]
        },
        {
            "name": "DimAnuncio", "angle": 151,
            "title_pos": (cx + 220 * math.cos(math.radians(151)) - 6, cy - 220 * math.sin(math.radians(151)) - 8),
            "ha": "right", "va": "center",
            "ticks": [
                {"r": 62, "text": "Nombre", "offset": (-14, -4), "ha": "right"},
                {"r": 102, "text": "Hora Inicio", "offset": (-14, -4), "ha": "right"},
                {"r": 142, "text": "Horario Fin", "offset": (-14, -4), "ha": "right"},
                {"r": 182, "text": "Campaña", "offset": (-14, -4), "ha": "right"},
            ]
        }
    ]

    for a in axes:
        rad = math.radians(a["angle"])
        ux = math.cos(rad)
        uy = -math.sin(rad)
        px = -uy
        py = ux

        tip_x = cx + axis_len * ux
        tip_y = cy + axis_len * uy

        # Flecha del eje
        ax.annotate(
            '',
            xy=(tip_x, tip_y),
            xytext=(cx, cy),
            arrowprops=dict(
                arrowstyle='->, head_width=0.35, head_length=0.45',
                color='#000000',
                lw=1.3,
                shrinkA=0,
                shrinkB=0
            )
        )

        # Título del eje
        ax.text(a["title_pos"][0], a["title_pos"][1], a["name"], fontsize=9.5, fontweight='bold', fontfamily=font, color='#000000', ha=a["ha"], va=a["va"])

        # Ticks y etiquetas
        for t in a["ticks"]:
            tx = cx + t["r"] * ux
            ty = cy + t["r"] * uy
            ax.plot([tx + tick_half * px, tx - tick_half * px], [ty + tick_half * py, ty - tick_half * py], color='#000000', lw=1.2)
            
            lbl_x = tx + t["offset"][0]
            lbl_y = ty + t["offset"][1]
            txt = ax.text(lbl_x, lbl_y, t["text"], fontsize=7.8, fontfamily=font, color='#111111', ha=t["ha"], va='center')
            txt.set_path_effects([path_effects.withStroke(linewidth=3, foreground='white')])

    # Caja de Medidas
    bx, by, bw, bh = 649.0, 138.0, 290.0, 294.0
    rect = patches.Rectangle((bx, by), bw, bh, facecolor='#fff9c4', edgecolor='#000000', linewidth=1.5, zorder=2)
    ax.add_patch(rect)

    tc_x = bx + bw / 2.0
    ax.text(tc_x, by + 24, "Medidas", fontsize=11.5, fontweight='bold', fontfamily=font, color='#000000', ha='center', va='center', zorder=3)
    ax.plot([tc_x - 34, tc_x + 34], [by + 33, by + 33], color='#000000', lw=1.2, zorder=3)

    grupos = [
        ("• Costo por BUYER:", ["- Gasto en anuncios", "- N° de buyers que llenan el formulario"]),
        ("• Tasa de interés en menú digital:", ["- N° de personas que hicieron clic en el menú", "- N° de personas que visitan la página"]),
        ("• Tasa de Conversión BUYER a LEAD:", ["- N° leads", "- N° buyers"])
    ]

    cy_box = by + 58
    for g_title, g_items in grupos:
        ax.text(bx + 22, cy_box, g_title, fontsize=8.5, fontweight='bold', fontfamily=font, color='#000000', ha='left', va='center', zorder=3)
        cy_box += 15.0
        for item in g_items:
            ax.text(bx + 34, cy_box, item, fontsize=7.8, fontfamily=font, color='#111111', ha='left', va='center', zorder=3)
            cy_box += 13.5
        cy_box += 9.0

    plt.savefig(ruta_png, dpi=dpi, facecolor='#ffffff', edgecolor='none')
    plt.close()
    print(f"PNG generado: {ruta_png}")


if __name__ == '__main__':
    generar_diagrama_svg()
    generar_diagrama_png()
