import urllib.request
import zipfile
import io
import os
import shutil
import sys

if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

print(">> Downloading ffmpeg.exe...")
url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

with urllib.request.urlopen(req) as response:
    zip_bytes = response.read()

print(">> Extracting ffmpeg.exe...")
with zipfile.ZipFile(io.BytesIO(zip_bytes)) as z:
    ffmpeg_member = next(m for m in z.namelist() if m.endswith('ffmpeg.exe'))
    with z.open(ffmpeg_member) as src_file, open("ffmpeg.exe", "wb") as dst_file:
        shutil.copyfileobj(src_file, dst_file)

print("[+] Successfully downloaded ffmpeg.exe!")
