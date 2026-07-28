# Reporte de la tienda Imperial Jewelry

Tienda: **Imperial Jewelry** · imperialjewelry.com.mx · MXN · México
Rama de trabajo: `claude/tienda-espanol-mexico-yudekf`

---

## 1. Idioma — terminado

La tienda quedó **únicamente en español de México**. Se eliminó por completo la
posibilidad de que el tema muestre otro idioma.

| Concepto | Resultado |
|---|---|
| Archivos de idioma eliminados | 50 (incluidos `en.default.json` y `en.default.schema.json`) |
| Idioma predeterminado del tema | `es.default.json` + `es.default.schema.json` |
| Cadenas del storefront en español | 398 |
| Cadenas del editor de tema en español | 1,211 |
| Texto en inglés visible al cliente | 0 |
| Texto editable escrito en el código | 0 |

### Qué se cubrió

Menús y navegación, botones, buscador y filtros, carrito y paso previo al pago,
formularios, mensajes de confirmación y error, páginas informativas, preguntas
frecuentes, avisos promocionales, configuración visible del tema, textos
alternativos de imágenes y la página de contraseña.

### Correcciones de español de España o traducción literal

| Antes | Ahora | Por qué |
|---|---|---|
| "gastos de envío" | **costos de envío** | Término de España |
| "Provincia" | **Estado** | Formato de dirección mexicano |
| "Impuestos incluidos" | **IVA incluido** | Término fiscal mexicano |
| "Pagar pedido" | **Finalizar compra** | Uso común en México |
| "Formas de pago" | **Métodos de pago** | Terminología pedida |
| "Hacer seguimiento del envío" | **Rastrear mi envío** | En México se rastrea, no se sigue |
| "Número de seguimiento" | **Número de rastreo** | Idem |
| "Empresa de transporte" | **Paquetería** | Término mexicano |
| "Proveedor" | **Marca** | "Proveedor" suena a mayorista |
| "Precio habitual" | **Precio normal** | Uso común en México |
| "Retiro disponible" | **Disponible para recoger** | Uso común en México |
| "Dirección 1 / Dirección 2" | **Calle y número / Interior, colonia o referencias** | Formato mexicano |

### Errores del español base de Shopify que se corrigieron

- `Pagina anterior` → **Página anterior** (faltaba el acento).
- `Tu carrito esta vacío` → **Tu carrito está vacío** (faltaba el acento).
- Filtro de rango de precios: la etiqueta `Para` era una traducción literal de
  "To"; ahora dice **A** (De … A …).
- `¿Está seguro/a de que deseas eliminar esta dirección?` mezclaba usted y tú;
  ahora dice **¿Seguro que quieres eliminar esta dirección?**
- Faltaba un punto en el mensaje de "sin resultados" de búsqueda.

### Vocabulario de joyería aplicado

Aretes y arracadas (nunca "pendientes"), dije, cadena, pulsera, anillo,
oro amarillo, plata esterlina .925, agregar al carrito, comprar ahora,
envío gratis, meses sin intereses, cambios y devoluciones.

### Textos fuera del código

Ninguna palabra editable quedó escrita en un archivo `.liquid`:

- `sections/hero-imperial.liquid` y `sections/trust-bar.liquid` leen etiquetas,
  opciones y valores predeterminados con claves `t:` desde
  `locales/es.default.schema.json`.
- `snippets/whatsapp-float.liquid` toma su etiqueta de accesibilidad y su
  mensaje predeterminado desde `locales/es.default.json`.
- `config/settings_schema.json` usa claves `t:` en el apartado Imperial Jewelry.
- La portada dejó de tener una imagen fija incrustada en el código y ahora tiene
  un campo de **texto alternativo** configurable.

Se verificó que las 1,609 claves de traducción usadas por el tema existen; no
falta ninguna.

---

## 2. Material visual — inventario terminado

Carpeta de Dropbox: **"fotos meli"** (`/fotos meli`, 391 carpetas de SKU).

| Concepto | Cantidad |
|---|---|
| Archivos totales | 6,505 |
| Imágenes | 4,571 |
| — fotos reales de producto (`_01` a `_12`, jpg) | 4,180 |
| — infografías generadas (`_infografia.png`) | 391 |
| Videos | 1,924 |
| Otros archivos (scripts `.ps1`, `.txt`, `.csv`) | 10 |
| Carpetas de SKU | 391 |
| Peso total | 5.82 GB |

Extensiones encontradas: `jpg` 4,180 · `mp4` 1,924 · `png` 391 · `ps1` 7 ·
`txt` 2 · `csv` 1.

### Estructura de cada SKU

372 SKUs traen exactamente 17 archivos, con esta forma:

- 11 fotos numeradas `_01` … `_11`
- 1 infografía `_infografia.png`
- 5 videos: `_video`, `_vertical_v1`, `_vertical_v2`, `_cuadrado_v1`, `_cuadrado_v2`

4 SKUs traen 19 archivos y 4 traen 21 (versiones `_v3` y `_v4` adicionales).

### Hallazgo importante: el SKU de Dropbox es de VARIANTE, no de producto

Se verificó con hashes de contenido, no solo por tamaño. Ejemplo comprobado:

- `78198ML_01.jpg`, `78200ML_01.jpg` y `78201ML_01.jpg` tienen el mismo hash
  `13199bec…` → son el mismo archivo byte por byte.
- En Shopify, `78200ML`, `78201ML`, `78198ML` y `78202ML` son las variantes
  **50, 55, 60 y 65 cm** del mismo producto: *Cadena De Plata 925 Estilo 3x1
  Figaro*.

Es decir, las fotos repetidas **no son un error**: son la misma joya en distinta
medida o talla. Por eso las fotos deben cargarse **a nivel de producto**, no una
copia por variante.

Agrupando los 391 SKUs por su juego de fotos quedan **102 juegos distintos**:

- 101 juegos con 11 fotos reales cada uno.
- 1 juego sin ninguna foto real (solo infografía), que abarca 11 SKUs.

### Archivos duplicados

| Tipo de duplicado | Detalle |
|---|---|
| `_video.mp4` = `_vertical_v1.mp4` | Idénticos en 287 de 380 SKUs (distintos en 93) |
| Juegos de fotos compartidos entre SKUs | 359 de 391 SKUs comparten fotos con otro SKU |
| SKUs con fotos únicas | 32 |

En cambio, `_vertical_v1` vs `_vertical_v2` y `_cuadrado_v1` vs `_cuadrado_v2`
**siempre** son distintos: son cortes de video diferentes, no duplicados.

### SKUs sin material fotográfico real

Estos 11 SKUs solo tienen la infografía generada, sin una sola foto del producto:

`78654ML` · `79612ML` · `79615ML` · `79634ML` · `80936ML` · `80937ML` ·
`80938ML` · `80948ML` · `80967ML` · `81101ML` · `81117ML`

**Requieren fotografía nueva.** No se publican automáticamente.

### Archivos que no corresponden a ningún SKU

10 archivos sueltos en la raíz de "fotos meli", ninguno es material visual:

`Agregar_fotos_CUADRADAS_MELI.ps1` · `Agregar_fotos_CUADRADAS_v2_MELI.ps1` ·
`Agregar_fotos_infografias_MELI.ps1` · `Agregar_infografias_CanvaBulk.ps1` ·
`Agregar_videos_Ficha.ps1` · `Agregar_videos_Ficha_v2.ps1` ·
`Descargar_fotos_meli.ps1` · `_fallos.txt` · `_fallos_infografias.txt` ·
`_links.csv`

Son scripts de automatización y bitácoras. **No se publican.**

### Plan de carga sin duplicar

| | Archivos |
|---|---|
| Si se subiera archivo por archivo | 6,505 |
| Subiendo un juego por producto | **1,212** (1,111 fotos + 101 videos) |
| Ahorro | **82 %** |

Orden propuesto dentro de cada galería, como pediste: foto principal `_01`,
después ángulos y acercamientos `_02`–`_09`, al final medidas y detalle de uso
`_10`–`_11`, y el video integrado en la misma galería (se recomienda
`_cuadrado_v1`, que es el formato que mejor encuadra en la ficha de producto).

---

## 3. Relación entre SKU y archivos

Se cruzó el catálogo real de Shopify (259 productos, 587 variantes) contra las
391 carpetas de "fotos meli".

| Concepto | Cantidad |
|---|---|
| Productos en Shopify | 259 |
| Variantes en Shopify | 587 |
| — con SKU asignado | 518 |
| — **sin SKU asignado** | **69** |
| Carpetas de SKU en "fotos meli" | 391 |
| — que sí corresponden a una variante de Shopify | 348 |
| — **que no corresponden a ningún producto** | **42** |
| Productos con material visual en "fotos meli" | 164 |
| — cubiertos por completo | 145 |
| — **cubiertos solo en parte** | **19** |
| **Productos sin ninguna foto en "fotos meli"** | **95** |
| Variantes con SKU pero sin carpeta en Dropbox | 164 |

El detalle renglón por renglón está en `deploy/cruce-sku-archivos.csv`.

### 42 SKUs de Dropbox que no existen en Shopify

`78193ML` · `78285ML` · `78330ML` · `78343ML` · `78344ML` · `78434ML` ·
`78581ML` · `78582ML` · `78589ML` · `78590ML` · `78596ML` · `78604ML` ·
`78617ML` · `78622ML` · `78629ML` · `78642ML` · `79266ML` · `79267ML` ·
`79268ML` · `79269ML` · `79270ML` · `79271ML` · `79273ML` · `79275ML` ·
`79276ML` · `79302ML` · `79303ML` · `79304ML` · `79315ML` · `79613ML` ·
`79633ML` · `79635ML` · `80196ML` · `80882ML` · `80936ML` · `80937ML` ·
`80938ML` · `80948ML` · `80967ML` · `81117ML` · `81158ML` · `81159ML`

Son fotos de piezas que están en MercadoLibre pero **no están dadas de alta en
Shopify**. No se inventó ninguna relación: quedan en espera de que confirmes si
hay que crear esos productos o si son piezas descontinuadas.

Vale la pena notar que la foto que hoy usa la portada de la tienda
(`020_78285_00005_…jpg`) corresponde justamente a `78285ML`, uno de estos SKUs
huérfanos.

### 19 productos cubiertos solo en parte

Tienen fotos para algunas medidas o tallas pero no para todas. Ejemplos:

| Producto | Variantes con foto | Sin foto |
|---|---|---|
| Cadena De Plata 925 Estilo 3x1 Figaro De 60 Cm Calibre 4.1mm | 8 | `79668ML`, `79669ML`, `79667ML` |
| Arete Arracada Diamantada De Oro 10k Estilo Dominó | 3 | `78280ML`, `78281ML` |
| Cadena De Plata 925 Torsal Figaro 3x1 De 55cm Calibre 7.5mm | 1 | `78207ML`, `78208ML` |
| Arete Arracada De Oro De 14k Diamantada Estilo Torsal | 4 | `78370ML` |
| Arete Arracada Para Mujer De Oro Puro De 14k Medida 20mm | 2 | `79088ML` |

Como las variantes del mismo producto comparten fotos, en la práctica estos
productos **sí quedan cubiertos**: la galería se arma a nivel de producto.

### 95 productos de Shopify sin nada de material visual

Más de un tercio del catálogo no tiene fotos en "fotos meli". Los primeros:

- Pulso Torsal Hueco Oro Italiano 10k, Calibre 1.9mm
- Set Para Mujer De Cadena, Pulsera Y Aretes De Oro De 14k
- Aretes Para Mujer De Oro De 14k, 42 Mm Con Piedra Zirconia
- Arete Arracada Con Tubos Lisos Torcidos De Oro 10k, 35Mm
- Pulsera Para Mujer De Oro De 14k Con Piedra De 18cm
- Arracadas con tubos torcidos de Oro Amarillo y Blanco de 14K
- Pulsera Italiana Cubana Hueca De 10 Quilates 4.5mm, 18.5 Cm
- Pulsera Esclava De Plata Ley 925 Para Niña
- Collar Para Mujer De Oro De 14k Con Piedra De 45 Cm, 1mm
- Medalla De Virgen Italiana De Oro De 14k Dije De Oro Mujer
- Cadena Ancla Italiana De 14k Medida 55 Cm
- Dije De Virgen De Guadalupe De Plata 925 Con Zirconita

La lista completa está en `deploy/cruce-resumen.json`.

**Estos 95 productos no se pueden armar solo con "fotos meli".** Si la regla de
usar únicamente esa carpeta se mantiene tal cual, estos productos se quedarían
sin foto. Hay que decidir entre fotografiarlos o despublicarlos.

---

## 4. Lo que falta y por qué

### 4.1 No se pudo descargar ni un archivo de Dropbox

El entorno donde corro tiene la salida a internet restringida. Se comprobó:

```
https://www.dropbox.com            -> bloqueado
https://api.dropboxapi.com         -> bloqueado
https://content.dropboxapi.com     -> bloqueado
*.dl.dropboxusercontent.com        -> 403 del proxy
https://cdn.shopify.com            -> bloqueado
```

La conexión de Dropbox sí permite **leer nombres, rutas, tamaños y hashes** —por
eso el inventario y el cruce están completos y verificados— pero **no permite
bajar el contenido de los archivos**.

Como consecuencia, en esta sesión **no fue posible**: descargar las fotos,
comprimirlas, convertirlas a WebP, ni subirlas a Shopify.

Para poder hacerlo se necesita una de estas dos cosas:

1. Que la carpeta "fotos meli" esté **sincronizada en la computadora** donde
   corra Claude Code, y me digas la ruta local (ej. `~/Dropbox/fotos meli`).
2. Que se **habilite el acceso de red** a `dropboxusercontent.com` y
   `cdn.shopify.com` en el entorno.

### 4.2 La tienda todavía tiene inglés publicado

Consultando Shopify directamente:

| Idioma | Principal | Publicado |
|---|---|---|
| Español | sí | sí |
| **Inglés** | no | **sí** |

El tema ya no puede mostrar inglés: se borraron sus archivos de idioma. Pero
mientras el inglés siga publicado en Shopify, siguen existiendo las URLs `/en/…`
y el checkout y los correos pueden salir en inglés, porque eso lo controla
Shopify, no el tema.

**No lo despubliqué por mi cuenta**: es un cambio en la tienda en vivo que
afecta URLs ya indexadas por Google. Se hace en
**Configuración › Idiomas › Inglés › Despublicar**. Dime si quieres que lo haga.

### 4.3 Meta títulos y meta descripciones

El tema los toma de lo que esté capturado en el panel de Shopify por producto,
colección y página (`page_title` y `page_description`). No hay texto fijo en el
código. Redactar los ~259 metatítulos y metadescripciones en español es trabajo
de contenido sobre el catálogo, y conviene hacerlo junto con la carga de fotos.

### 4.4 Otros pendientes

- **69 variantes sin SKU** en Shopify: sin SKU no se pueden ligar a su foto.
  Hay que capturárselos. Se concentran en productos multicolor o multitalla
  (cadenas de plata en 4 colores, arracadas de plata, cubanas archivadas).
- **2 SKUs mal capturados en Shopify** que impiden el cruce automático:
  `78383ML_29235957_D_UPLICATED` (parece un duplicado mal nombrado) y una
  variante cuyo SKU dice `Amarillo` en lugar de una clave. Conviene corregirlos.
- **11 SKUs sin fotografía real** (solo infografía): requieren sesión de fotos.
- **Textos alternativos**: el campo ya existe y el tema lo respeta; se redactan
  al momento de cargar cada foto, con tipo de joya, material y medida tomados
  del título del producto (nada que no esté respaldado por la ficha).
- **Infografías**: las 391 son de estilo MercadoLibre. Recomiendo **no** subirlas
  a la tienda propia o dejarlas al final de la galería; le restan elegancia a una
  ficha de joyería fina. Dime qué prefieres.

---

## 5. Archivos generados

| Archivo | Contenido |
|---|---|
| `deploy/inventario-fotos-meli.csv` | Un renglón por archivo (6,505) |
| `deploy/inventario-fotos-meli-resumen.json` | Totales, duplicados, huérfanos |
| `deploy/plan-carga-deduplicado.json` | Los 102 juegos de fotos y su SKU representativo |
| `deploy/catalogo-shopify.csv` | Catálogo de Shopify por variante |
| `deploy/cruce-sku-archivos.csv` | Relación SKU ↔ archivos |
| `deploy/cruce-resumen.json` | Productos sin material, SKUs huérfanos |
