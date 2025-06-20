
# 📥 YouTube Playlist Downloader (Simple Python Script)

A simple Python script to download YouTube playlists in `.mp4` format using `yt-dlp`. No merging or post-processing required.

---

## 📦 Requirements

- Python 3.6 or higher  
- `yt-dlp` library

To install `yt-dlp`, run:

```bash
pip install yt-dlp
```

---

## ⚙️ How to Use

1. Open the script and modify the following variables:

🔗 **Playlist URL:**

```python
playlist_url = "your_playlist_url"
```

Example:

```python
playlist_url = "https://www.youtube.com/playlist?list=XXXXXXXXXXXX"
```

📁 **Save Path:**

```python
save_path = r"your_local_folder_path"
```

Example:

```python
save_path = r"D:\Downloads\MyPlaylist"
```

---

## ▶️ Run the Script

After editing the URL and save path, run the script using:

```bash
python download_playlist.py
```

All videos will be downloaded directly as `.mp4` files to the specified folder.

---

## 💡 Notes

- The script directly downloads videos in `.mp4` format.
- No extra processing steps are needed.
- Make sure the playlist URL is valid and the path exists.
- Using English folder names is recommended to avoid encoding issues.

---

## 🧑‍💻 Author

**Name:** Abdelrahman Atef Elsayed  
**GitHub:** [Abdelrahman-Atef-Elsayed](https://github.com/Abdelrahman-Atef-Elsayed)

---
