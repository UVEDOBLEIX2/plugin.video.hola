# -*- coding: utf-8 -*-
import sys
import urllib.parse
import requests  # para descargar la lista M3U

import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon

ADDON = xbmcaddon.Addon()
HANDLE = int(sys.argv[1])


M3U_URL = "https://raw.githubusercontent.com/UVEDOBLEIX2/uvedobletv/refs/heads/main/auto-ace"

def cargar_m3u(url):
    canales = []
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        lineas = resp.text.splitlines()
        nombre = None
        for linea in lineas:
            linea = linea.strip()
            if linea.startswith("#EXTINF"):
                # Extrae el nombre después de la coma
                partes = linea.split(",", 1)
                if len(partes) > 1:
                    nombre = partes[1].strip()
            elif linea and not linea.startswith("#"):
                # Es la URL del canal
                if nombre:
                    canales.append({"title": nombre, "url": linea})
                    nombre = None
    except Exception as e:
        xbmc.log(f"Error cargando M3U: {e}", xbmc.LOGERROR)
    return canales

def listar_canales():
    canales = cargar_m3u(M3U_URL)
    if not canales:
        list_item = xbmcgui.ListItem(label="No se pudo cargar la lista M3U")
        xbmcplugin.addDirectoryItem(handle=HANDLE, url="", listitem=list_item, isFolder=False)
    for canal in canales:
        list_item = xbmcgui.ListItem(label=canal["title"])
        list_item.setProperty("IsPlayable", "true")
        params = {"action": "play", "url": canal["url"]}
        url_plugin = sys.argv[0] + "?" + urllib.parse.urlencode(params)
        xbmcplugin.addDirectoryItem(handle=HANDLE, url=url_plugin, listitem=list_item, isFolder=False)
    xbmcplugin.endOfDirectory(HANDLE)

def reproducir(url):
    list_item = xbmcgui.ListItem(path=url)
    xbmcplugin.setResolvedUrl(HANDLE, True, list_item)

def parsear_params():
    query = sys.argv[2][1:] if len(sys.argv) > 2 else ""
    return dict(urllib.parse.parse_qsl(query))

def run():
    params = parsear_params()
    action = params.get("action")
    if action == "play":
        reproducir(params.get("url"))
    else:
        listar_canales()

if __name__ == "__main__":
    run()
