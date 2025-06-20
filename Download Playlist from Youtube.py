import os
import yt_dlp

# === 1. رابط البلاي ليست ===
playlist_url = " رابط البلاي ليست "

# === 2. مكان الحفظ ===
save_path = r" مكان الحفظ"
os.makedirs(save_path, exist_ok=True)

# === 3. إعدادات التحميل (بدون ffmpeg) ===
ydl_opts = {
    'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
    'format': 'mp4[ext=mp4]',  # صيغة mp4 فقط، بدون دمج
    'merge_output_format': 'mp4',
    'postprocessors': [],  # ما تستخدمش ffmpeg
    'noplaylist': False,
}

# === 4. تحميل البلاي ليست ===
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])
