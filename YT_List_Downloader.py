import subprocess, sys, os, re, unicodedata, pathlib
from concurrent.futures import ThreadPoolExecutor
try:
    from yt_dlp import YoutubeDL
except:
    subprocess.check_call([sys.executable,"-m","pip","install","yt-dlp"])
    from yt_dlp import YoutubeDL

def clean(n,l=80):
    n=unicodedata.normalize("NFKD",n).encode("ascii","ignore").decode()
    return re.sub(r'[\\/:*?"<>|]+','',re.sub(r'\s+',' ',n)).strip()[:l]

url=input("⌨️ Playlist Link : ")
d=pathlib.Path.home()/"Downloads"

with YoutubeDL({'extract_flat':1,'quiet':1}) as y:
    info=y.extract_info(url,download=0)
    p=d/clean(info.get("title","Playlist"))
    p.mkdir(exist_ok=1)
    vids=[v for v in info.get("entries",[]) if v]

def dl(v):
    t=clean(v.get("title","video"))
    print("⬇️",t)
    with YoutubeDL({
        'format':'bestaudio/best',
        'outtmpl':f'{p}/{t}.%(ext)s',
        'postprocessors':[{'key':'FFmpegExtractAudio','preferredcodec':'mp3','preferredquality':'192'}],
        'quiet':1
    }) as y:
        y.download([v['url']])

with ThreadPoolExecutor(5) as ex:
    list(ex.map(dl,vids))

print("🎉 Done :",p)