# Imperial Jewelry — Tema "Aurart"

Tema de Shopify (Online Store 2.0) para **Imperial Jewelry**, construido sobre
[Dawn](https://github.com/Shopify/dawn) v15.5.0 y personalizado por completo.

## Idioma

La tienda está **únicamente en español de México**. No existe versión en inglés
ni en ningún otro idioma:

- `locales/es.default.json` — todos los textos del storefront (menús, botones,
  buscador, filtros, carrito, formularios, mensajes de error, cuenta y pedidos).
- `locales/es.default.schema.json` — toda la configuración visible del tema en el
  editor de Shopify, incluidos los valores predeterminados de cada sección.

Se eliminaron `en.default.json`, `en.default.schema.json` y los archivos de los
demás idiomas que traía Dawn.

### Reglas de redacción

Se usa vocabulario mexicano: *aretes* y *arracadas* (nunca "pendientes"),
*dije*, *cadena*, *pulsera*, *anillo*, *oro amarillo*, *plata esterlina .925*,
*agregar al carrito*, *comprar ahora*, *envío gratis*, *costos de envío* (nunca
"gastos de envío"), *métodos de pago*, *cambios y devoluciones*, *meses sin
intereses*, *número de rastreo*, *paquetería*, *IVA incluido*, *Estado* (no
"Provincia") y *finalizar compra*.

**Ningún texto editable va escrito en el código.** Las secciones propias leen sus
textos con claves de traducción (`t:` dentro de `{% schema %}` y el filtro `| t`
en Liquid). Si necesitas cambiar una palabra, edítala en `locales/`, no en el
archivo `.liquid`.

## Identidad de marca
- Azul imperial `#2A3871`, oro `#D9BF55`, blanco y negro `#1C1C1C`.
- Títulos en serif elegante (Playfair Display) + cuerpo legible (Assistant).
- Logo `imperial-logo.png` y favicon de iniciales.

## Personalizaciones propias
- `sections/hero-imperial.liquid` — portada de marca con foto, velo azul, texto
  alternativo configurable y dos botones.
- `sections/trust-bar.liquid` — barra de confianza (oro y plata de verdad, envío
  gratis, meses sin intereses, WhatsApp).
- `snippets/whatsapp-float.liquid` — botón flotante de WhatsApp (se configura en
  Ajustes del tema › Imperial Jewelry).
- `assets/imperial-custom.css` y `assets/section-imperial.css` — estilos de marca.
- `templates/index.json` — página de inicio: portada, confianza, categorías,
  novedades en oro, historia de marca, plata esterlina .925, preguntas frecuentes
  y suscripción.
- Encabezado, pie de página y esquemas de color adaptados a la marca.

## Material visual

El material visual debe salir **exclusivamente** de la carpeta de Dropbox
**"fotos meli"** (391 SKUs, 4,571 imágenes y 1,924 videos).

El inventario y el cruce con el catálogo viven en `deploy/`:

- `deploy/inventario-fotos-meli.csv` — un renglón por archivo.
- `deploy/inventario-fotos-meli-resumen.json` — totales, duplicados y huérfanos.
- `deploy/catalogo-shopify.csv` — catálogo por variante.
- `deploy/cruce-sku-archivos.csv` — relación SKU ↔ archivos.

**Importante:** el nombre de cada carpeta de Dropbox (por ejemplo `78198ML`) es el
SKU de una **variante**, no de un producto. Varias variantes del mismo producto
(medidas o tallas distintas) comparten las mismas fotos, byte por byte. Por eso
las fotos se cargan a nivel de producto, sin duplicar.

## Configuración pendiente (1 minuto)
En **Ajustes del tema › Imperial Jewelry**, escribe tu número de WhatsApp
(con clave de país, ej. `5215512345678`) para activar el botón flotante.
