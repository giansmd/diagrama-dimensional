# 🎯 Generador de Análisis Dimensional Conformado de Buyers

Aplicación interactiva y generador de gráficos vectoriales para reproducir y personalizar con **fidelidad visual exacta (pixel-perfect)** el diagrama radial de constelación dimensional y panel de medidas.

---

## 🚀 Cómo Iniciar la Aplicación

Puedes usar la aplicación de cualquiera de las siguientes 3 formas:

### Opción 1: Doble Clic Directo (Sin instalación ni consola)
Simplemente haz doble clic en el archivo **`index.html`** para abrirlo inmediatamente en Chrome, Edge, Firefox o tu navegador preferido. ¡Funciona 100% offline!

### Opción 2: Ejecutable de Windows
Haz doble clic en **`iniciar_app.bat`**. Se abrirá el servidor local y tu navegador en `http://localhost:8000`.

### Opción 3: Desde la Terminal / Consola
```bash
python server.py
```

---

## ⚡ Generación Inmediata por Script Python

Si solo deseas generar los archivos gráficos de alta resolución desde la consola:

```bash
python generar_diagrama_exacto.py
```

Esto generará automáticamente:
* 📄 **`diagrama_exacto.png`** (Imagen en alta definición, idéntica a la referencia).
* 📐 **`diagrama_exacto.svg`** (Vector editable en Illustrator, Figma, Inkscape o PowerPoint).

---

## 🎨 Características de la Aplicación

1. **Diseño Idéntico al 100%**:
   * Ejes a 45° exactos: `DimFecha` (90°), `DimBuyer` (45°), `DimTipoBuyer` (0°), `DimCampaña` (315°), `DimPersonal` (270°), `DimCanal` (225°), `DimRedSocial` (180°) y `DimAnuncio` (135°).
   * Marcas (ticks) transversales calibradas en posición y etiquetas.
   * Nota de rol superior (*"dimensión de rol — se reutiliza varias veces por hecho..."*).
   * Panel amarillo suave (`#fff9c4`) con borde negro y todas las medidas clasificadas por viñetas.

2. **Edición Interactiva en Tiempo Real**:
   * Modifica nombres de dimensiones, ángulos y longitudes.
   * Añade o elimina marcas/ticks con distancia milimétrica.
   * Añade nuevos ejes dimensionales según tus necesidades de modelado.
   * Edita el título principal, notas de rol y medidas.
   * Personaliza colores (fondo, ejes, panel de medidas).

3. **Herramienta de Calco y Verificación (Overlay Slider)**:
   * En la pestaña **Estilos**, activa el slider de opacidad para superponer la imagen original sobre el diagrama generado y verificar la coincidencia exacta de cada línea y texto.

4. **Exportación Profesional**:
   * 📋 **Copiar Imagen**: Copia el diagrama en alta resolución directamente al portapapeles con un clic para pegarlo con `Ctrl+V` en Word, PowerPoint o Slack.
   * 📥 **Descargar PNG**: Exporta en alta resolución (DPI escalado).
   * 📐 **Descargar SVG**: Exporta gráficos vectoriales sin pérdida de calidad.
   * 🔄 **Restablecer Plantilla**: Vuelve al diseño idéntico original en cualquier momento.

---

## 📁 Estructura del Proyecto

* **`index.html`**: Aplicación web completa con editor interactivo, motor de renderizado SVG y exportador Canvas.
* **`generar_diagrama_exacto.py`**: Script de Python con generadores en SVG y Matplotlib.
* **`diagrama_exacto.png`**: Archivo PNG generado idéntico a la imagen original.
* **`diagrama_exacto.svg`**: Archivo SVG generado idéntico a la imagen original.
* **`server.py`**: Servidor local Python con apertura automática de navegador.
* **`iniciar_app.bat`**: Lanzador para Windows.
* **`referencia_original.png`**: Imagen original de referencia utilizada para calibrar el diseño.
