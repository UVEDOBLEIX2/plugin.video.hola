# plugin.video.hola

Addon de ejemplo para Kodi. Muestra 2 vídeos de demo.

## Estructura
- `addon.xml`: metadatos del addon
- `main.py`: código principal
- `resources/language/.../strings.po`: traducciones (opcional)
- `.github/workflows/release.yml`: crea el ZIP instalable al publicar una versión

## Instalación rápida en Kodi (ZIP ya listo)
Descarga el archivo `/plugin.video.hola-1.0.0.zip` y en Kodi ve a **Add-ons → Instalar desde un archivo .zip**.

## Publicar en GitHub
Sube esta carpeta a un repositorio llamado `plugin.video.hola` y crea un Release con tag `v1.0.0` para que GitHub Actions suba el ZIP automáticamente.
