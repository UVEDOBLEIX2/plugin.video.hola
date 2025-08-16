# -*- coding: utf-8 -*-
import sys
import urllib.parse

import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon

ADDON = xbmcaddon.Addon()
HANDLE = int(sys.argv[1])

def listar_elementos():
    items = [
        {
            "title": "Big Buck Bunny (demo)",
            "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
            "thumb": ""
        },
        {
            "title": "Sintel (demo)",
            "url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4",
            "thumb": ""
        }
    ]

    for it in items:
        list_item = xbmcgui.ListItem(label=it["title"])
        list_item.setInfo("video", {"title": it["title"]})
        if it["thumb"]:
            list_item.setArt({"thumb": it["thumb"], "icon": it["thumb"]})
        list_item.setProperty("IsPlayable", "true")
        params = {"action": "play", "url": it["url"]}
        url_plugin = sys.argv[0] + "?" + urllib.parse.urlencode(params)
        xbmcplugin.addDirectoryItem(handle=HANDLE, url=url_plugin, listitem=list_item, isFolder=False)

    xbmcplugin.endOfDirectory(HANDLE)

def reproducir(url):
    list_item = xbmcgui.ListItem(path=url)
    list_item.setInfo("video", {"title": "Reproduciendo"})
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
        listar_elementos()

if __name__ == "__main__":
    run()
