# CAMBIOS — Imperial Jewelry · Revisión ES-MX

Auditoría y mejora del tema publicado **"Julio 31 copia de onwrd"** (ID 155530625210).
Todo el trabajo se aplicó sobre una **copia no publicada** llamada **"Imperial - Revisión ES-MX"**.
**El tema publicado (live) no fue modificado en ningún momento.**

Fecha: 3 de agosto de 2026.

---

## 1. Idioma: español de México como único idioma del tema

### Archivos de idioma
- **Nuevo `locales/es.default.json`** (en esta carpeta) — la traducción completa en español de México (365 claves + 16 nuevas, cobertura 100% de las claves que tenía `en.default.json`, cero huecos). Es la fuente única de todos los textos del tema.
- **En el tema subido a Shopify**: la herramienta de subida usada en esta sesión **no permite borrar archivos de temas** (política de seguridad), por lo que en el tema "Imperial - Revisión ES-MX" el contenido es-MX se aplicó **sobrescribiendo `locales/es.json` Y `locales/en.default.json` con el mismo contenido en español**. Resultado práctico: el idioma default/fallback del tema es español y **no queda ningún texto en inglés**, aunque los nombres de archivo se conserven.
- **Paso manual opcional (1 minuto, cosmético)** en el editor de código del tema copia: eliminar `locales/es.json`, renombrar/recrear `locales/en.default.json` como `locales/es.default.json` (el contenido es el de esta carpeta), y borrar los 26 locales de otros idiomas (ar, cs, da, …, zh-TW) y `fr.schema.json`. Mientras no se haga, esos archivos extra son inertes: solo se usarían si publicaras esos idiomas en la tienda.
- **Conservado `locales/en.default.schema.json`** — es el archivo de etiquetas del **editor de temas** (no lo ve el cliente); el tema lo requiere como schema default. No existía `es.schema.json` en el tema original.

### Reescritura completa de la traducción (España → México)
El `es.json` original era una traducción de España. Se reescribió íntegro. Ejemplos clave (antes → después):

| Antes (es-ES) | Después (es-MX) |
|---|---|
| Cesta / La cesta está vacía | Carrito / Tu carrito está vacío |
| Añadir a la cesta | **Agregar al carrito** |
| Añadido a la cesta | Agregado al carrito |
| Gastos de envío (en carrito, pedido y estimador) | Envío / Calcular envío |
| Los impuestos y gastos de envío se calculan en la pantalla de pago | Los impuestos y el envío se calculan al finalizar la compra. |
| ¡Gasta {{ monto }} más y consigue envío gratuito! | Te faltan {{ monto }} para obtener **envío gratis** |
| Tu pedido cumple los requisitos de envío gratuito. | ¡Tu pedido tiene **envío gratis**! |
| Aceptamos (íconos de pago) | **Métodos de pago** |
| Pedido previo | Reservar |
| Sin existencias | Agotado |
| Recogida disponible | Disponible para recoger en tienda |
| Provincia | Estado |
| Apellidos | Apellido |
| Línea 1 / Línea 2 de dirección | Calle y número / Colonia, interior (opcional) |
| Importe disponible / Importe reembolsado | Saldo disponible / Monto reembolsado |
| Caduca el / ha caducado | Vence el / venció |
| Tasas de aduanas | Impuestos de importación |
| Introduce un código de descuento válido | Ingresa un código de descuento válido |
| Registro | Crear cuenta |
| vídeo | video |
| No puedes añadir más | Ya no puedes agregar más |
| Comprobar la disponibilidad en otras tiendas | Consultar disponibilidad en otras tiendas |
| comillas «…» | comillas "…" |

Trato al cliente: **"tú" consistente** en todo el archivo. Tono ajustado a joyería fina (p. ej. "Quedan pocas piezas" en inventario).

---

## 2. Correcciones de contenido en templates y grupos de secciones (97 cambios)

### Portada (`templates/index.json`)
- `Joyería de oro y plata  que  dura toda la vida` → `Joyería de oro y plata que dura toda la vida` (dobles espacios en el hero).
- `Envios a todo mexico` → `Envíos a todo México`.
- `clientes satisfechos` → `Clientes satisfechos` (2 lugares).
- `View all` → `Ver todo` (3 bloques de colecciones destacadas, estaban en inglés).
- CTAs inconsistentes `Comprar` / `Ver todos` → unificados a `Ver todo`.
- `fundicion de presición` → `fundición de precisión`; `las mejores talleres… reconocidas` → `los mejores talleres… reconocidos`; `europa` → `Europa`; espacios alrededor de `<strong>` y `<br/>` de relleno eliminados.
- `También De venta en` → `También de venta en`, y su encabezado pasó de `h1` a `h2` (había dos h1 en la portada — mejora SEO/semántica).
- `mercado libre` → `Mercado Libre` (también corregido en `product.json`, `productpage`, `product-page-v2`, `collection.json` y `footer-group.json`).

### Barra de anuncios (`sections/header-group.json`)
- `3 MSI en toda la tienda` → `3 meses sin intereses en toda la tienda` (glosario).
- `GARANTÍA DE ORO REAL` → `Garantía de oro real` (consistencia con los otros mensajes).

### Carrito y overlays (`sections/overlay-group.json`)
- Cross-sell del carrito: `Acompleta con` → `Complementa tu compra con`.
- Popup de newsletter (estaba íntegro en inglés): `Signup for our newsletter` → `Suscríbete a nuestras novedades`; descripción → `Recibe antes que nadie lanzamientos, promociones y meses sin intereses.`; `Subscribe` → `Suscribirme`.
- Banner de cookies (estaba en inglés): `🍪 Cookie policy` → `🍪 Política de cookies` + contenido traducido.

### Preguntas frecuentes (`templates/page.faq.json`)
La página FAQ era **el demo del tema en inglés** ("Do you ship overseas?"…). Se reescribió con datos reales de la tienda (tomados de la FAQ verdadera de la ficha de producto):
- `Order` → `Pedidos`.
- `Do you ship overseas?` → `¿Hacen envíos a todo México?` + respuesta real (envío calculado al pagar, gratis desde $999).
- `How long will it take to get my orders?` → `¿Cuánto tarda en llegar mi pedido?` + tiempos reales (Express 2–3 días hábiles, Terrestre 5–7).
- `Any question?` → `¿Tienes otra duda?` + invitación a la página de contacto.

### Fichas de producto (`product.json`, `product.productpage.json`, `product.product-page-v2.json`)
- Botón del acordeón `FAQ` → `Preguntas frecuentes`.
- `¿Expides factura fiscal?` → `¿Expiden factura fiscal?` (voz consistente) y `Si expedimos factura fiscal, mándanos tus datos.` → `Sí, expedimos factura fiscal. Envíanos tus datos después de tu compra.` (el "Si" sin acento se leía como condicional).
- `envío seguro` / `facturación disponible` / `compra protegida` / `preguntas frecuentes` / `¿necesitas ayuda?` → capitalización inicial.
- `Solícitala` → `Solicítala` (acento mal colocado, detectado durante la verificación de subida).
- `Pairs well with` → `Combina bien con`; `Productos Similares` → `Productos similares`; `Dudas del Producto` → `Dudas del producto`.
- Testimonios placeholder en inglés → placeholder en español (bloque desactivado).
- Encabezado decorativo `h1` → `h2` en productpage (evita h1 duplicado con el título del producto).
- Los mensajes de envío/pagos/meses sin intereses quedan visibles: barra de anuncios (envío gratis desde $999 + 3 meses sin intereses), franja de beneficios en ficha de producto y "Métodos de pago" en el carrito.

### Página Nosotros (`templates/page.nosotros.json`)
- **Bug de CSS**: `rgba(NaN, NaN, NaN, 0)` en el gradiente del hero → `rgba(0, 0, 0, 0)`.
- `plata ley 925` → `Plata Ley .925`; `calidad internacional` → `Calidad internacional`; `el valor de lo auténtico` → `El valor de lo auténtico`; `El Valor de los Metales Preciosos` → `El valor de los metales preciosos` (Title Case anglosajón).
- `ORO`/`Plata` inconsistentes → `Oro`/`Plata`; punto final faltante agregado.

### Página default (`templates/page.json`)
- Tres bloques con **todo el párrafo en `<strong>`** → negrita global eliminada.
- Espacios faltantes tras punto corregidos en 6 lugares (`nobles.A` → `nobles. A`, `Asia.Nuestra` → `Asia. Nuestra`, etc.).

### Contacto y footer (`page.contact.json`, `page.contacto-v1-owd.json`, `footer-group.json`)
- `Mayoreo!` → `¡Mayoreo!` (4 archivos).
- Placeholders demo en inglés (bloques desactivados) traducidos: `Customer service` → `Atención a clientes`, `Secure payment` → `Pago seguro`, con sus contenidos.
- Sección demo `Heading`/`Subheading`/"Use this text…" traducida.

---

## 3. Textos hardcoded extraídos a `locales/` (requisito técnico)

El tema base ya estaba bien localizado con `| t`; los defectos estaban en archivos generados por apps (EComposer y bloques AI). Se extrajeron **45 textos** a claves de idioma:

### `sections/ecom-default-template-quickview.liquid` (vista rápida — estaba TODO en inglés)
- Botón de compra y sus estados JS: `Add to cart`, `Pre Order`, `Unavailable`, `Out stock`, `Added to cart` → `{{ 'product.general.*' | t }}` (Agregar al carrito, Reservar, No disponible, Agotado, Agregado al carrito).
- Badges: `Sold out` → clave `sold_out_badge`; ` {price}% OFF` → nueva clave `percent_off_badge` ("-{{ price }}%").
- Estado de inventario: `In stock`, `Outstock`, `{quantity} items left in stock`, `Preorder text` (placeholder roto), `Unavailable`, `Variant is out of stock. The product will available at:…` (inglés roto) → claves de `product.inventory.*` y `product.general.*`.
- `Quantity` (label), `control minus`/`control plus` (aria) → `product.quantity.*`.
- `Guarantee safe & secure checkout` → nueva clave `secure_checkout` ("Compra 100% segura y protegida"); `Share:` → `general.social.share`.
- Mensajes del wrapper de reseñas (Ryviu) → nuevas claves `sections.quickview.*`.
- `Play video` (texto de lector de pantalla) → `general.accessibility.play_video`.

### `sections/ecom-predictive-search.liquid` (buscador predictivo — estaba en inglés)
- `Suggestions`, `Pages` (×2), `Products` → `search.general.*`.
- `Search for "…"` → nueva clave `search.general.search_for`.

### Otros
- `sections/main-collection.liquid`: 5 `aria-label` en inglés de los botones de densidad de cuadrícula → nuevas claves `collection.general.{larger,smaller,compact}_images`.
- `sections/newsletter-popup.liquid`: `title="Newsletter popup"` → nueva clave `general.newsletter.popup_title`.
- `sections/contact.liquid`: label de respaldo `Custom field N` → nueva clave `contact.form.custom_field`.
- `snippets/product-card-horizontal.liquid`: `LOADING` visible en el modal de compra rápida → nueva clave `general.loading` ("Cargando…").
- `blocks/ai_gen_block_c8d7a6e.liquid`: `Go to slide {{ i }}` / `Previous slide` / `Next slide` → nuevas claves `general.accessibility.*`.
- `blocks/ai_gen_block_49e48d5.liquid`: badge `Sale` → `on_sale_badge` ("Oferta"); botón `Agotado` hardcoded → clave `sold_out_button`.
- `blocks/ai_gen_block_38a5b20.liquid` y `ai_gen_block_def05ab.liquid`: los avisos "agrega una imagen/video de fondo" se **envolvieron en `{% if request.design_mode %}`** — eran instrucciones para el comerciante que se mostraban a los clientes cuando faltaba la imagen.

**Claves nuevas agregadas a `es.default.json`** (16): `general.loading`, `general.accessibility.{go_to_slide,previous_slide,next_slide}`, `general.newsletter.popup_title`, `collection.general.{larger,smaller,compact}_images`, `search.general.search_for`, `contact.form.custom_field`, `product.general.{percent_off_badge,secure_checkout}`, `product.inventory.items_left`, `sections.quickview.{rating_placeholder,rating_select_platform,rating_not_supported}`.

---

## 4. Correcciones de código y accesibilidad

- `config/settings_schema.json`: **coma colgante** eliminada (JSON inválido en parsers estrictos; Shopify lo toleraba).
- `templates/page.nosotros.json`: gradiente `rgba(NaN,…)` corregido.
- `alt="trus"` (nombre de archivo truncado) en imagen decorativa de confianza del quick-view → `alt=""`.
- Dos `h1` duplicados degradados a `h2` (portada y ficha de producto).
- Aria-labels sin sentido ("control minus/plus") y en inglés → descriptivos y localizados.

---

## 5. Problemas encontrados que decidí NO tocar (y por qué)

1. **128 `default` en inglés dentro de `{% schema %}`** de secciones del tema base (p. ej. `"Announce something here"`, `"Frequently Asked Questions"`). Solo aparecen si el comerciante **agrega una sección nueva** y no edita el texto; el contenido real de la tienda ya los sobreescribe. Cambiarlos masivamente toca 40+ archivos del tema base con beneficio nulo para el cliente final. Lista completa disponible si se quiere una segunda pasada.
2. **`<link>`/`<style>` con `id` duplicados** en `ecom-default-template-quickview.liquid` y `ecom_theme_helper.liquid` — código generado por EComposer; eliminarlos podría romper la lógica interna de la app.
3. **Alertas en inglés** en `ecom_theme_helper.liquid` (`Please create Ecomposer quickview template first!`) — solo se muestran a personal logueado en el admin, no a clientes.
4. **Encabezado "Pages" del buscador predictivo** agrupa páginas y artículos con una condición imperfecta (si solo hay artículos, lista vacía) — bug menor de la app; se tradujo el encabezado pero no se cambió la lógica.
5. **Tarjetas placeholder "Producto de ejemplo/$99.00"** en `ai_gen_block_49e48d5.liquid` cuando no hay colección seleccionada — ya están en español; ocultarlas cambiaría el comportamiento del bloque.
6. **Enlaces a `diflor.com`** en los bloques "¡Mayoreo!" (contacto, footer, página default) — dominio externo; **verifica que sea intencional**.
7. **Backups de GemPages** (`*.gp-template-bk-default.json`, con placeholders en inglés) y `index.ecomposer.liquid` (workspace vacío) — solo renderizables con `?view=`; si ya no usas GemPages/EComposer, se pueden borrar.
8. **`templates/page.json`**: dos bloques tienen tono de ensayo interno de procesos ("pérdida de control sobre la manejabilidad de la materia prima") — corregí ortografía y formato, pero la reescritura comercial de fondo es decisión de marca.
9. **Color #D5AF17**: ese tono **no existe en ningún archivo del tema**. El dorado de la marca en este tema es **#D9BF55** (con azul #2A3871), usado de forma consistente. No lo introduje para no alterar el diseño.
10. **Assets minificados** (`theme.js`, `theme.css`, `vendor.min.js`, `photoswipe.min.js`, `gp-global.css`) — no se tocaron; los textos que muestran vienen de `js-variables.liquid`, que ya usa claves de idioma.

## 6. Pendientes que están fuera del tema (ajustes de la tienda, no del código)

- **La tienda tiene el idioma "Inglés" publicado** a nivel tienda (Configuración → Idiomas). El tema ya no tiene inglés, así que las URLs `/en` mostrarán español; para eliminarlo del todo, **despublica el inglés en el admin**.
- Los **nombres de colecciones, productos y páginas** viven en el admin (no en el tema); revisa que sigan el glosario (aretes, arracadas, dije, cadena, pulsera, anillo, oro amarillo, plata esterlina .925).
- Hay 7 temas antiguos sin publicar en la tienda ("ONW WIP", "DO NOT USE…", etc.); considera limpiar.
