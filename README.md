# Cloudflare Stream Downloader – README

## Purpose

A quick guide to set up **yt-dlp** and **FFmpeg** on Windows, manually add them to your system `PATH`, and locate the **Cloudflare Stream video ID** required by the Python downloader script.

---

## 1. What to Download?

✔ **FFmpeg (essentials build)**
• Website: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
• File: `ffmpeg-YYYY-MM-DD-git-xxxxxxxxxx-essentials_build.zip`

✔ **yt-dlp (.exe version)**
• Website: [https://github.com/yt-dlp/yt-dlp/releases/latest](https://github.com/yt-dlp/yt-dlp/releases/latest)
• File: `yt-dlp.exe`

---

## 2. Where to Place the Files?

| Target Location             | Description                                   |
| --------------------------- | --------------------------------------------- |
| `C:\ffmpeg`                 | Create this folder on drive C:                |
| `C:\ffmpeg\yt-dlp.exe`      | Copy `yt-dlp.exe` into this folder            |
| `C:\ffmpeg\ffmpeg-2025\bin` | Extract FFmpeg ZIP so the executables go here |

**Final folder structure:**

```
C:\
└─ ffmpeg\
   ├─ yt-dlp.exe
   └─ ffmpeg-2025\
      └─ bin\
         ├─ ffmpeg.exe
         └─ ffprobe.exe
```

---

## 3. How to Add PATH Manually

1. Press `Win + S`, then search: `environment variables`

2. Click: **Edit the system environment variables**

3. Click the **\[Environment Variables...]** button

4. Under **System variables**, find and select `Path`, then click **\[Edit]**

5. Click **\[New]** twice and add these two lines:

   ```
   C:\ffmpeg\ffmpeg-2025\bin  
   C:\ffmpeg
   ```

6. Click **OK** on all open windows

7. Open a new Command Prompt and test:

   ```
   ffmpeg -version  
   yt-dlp --version
   ```

---

## 4. How to Find Cloudflare Stream Video ID

✔ From an embed iframe:
Example:

```html
<iframe src="https://customer-zlvlcdgbcvpukf1t.cloudflarestream.com/df4a8e35f02bb5fae2f9dfe96675cad5/iframe">
```

→ Video ID is: `df4a8e35f02bb5fae2f9dfe96675cad5`

✔ From a direct Cloudflare link:
`https://customer-zlvlcdgbcvpukf1t.cloudflarestream.com/<ID>`

✔ From Cloudflare Dashboard:

* Log into your Cloudflare account
* Navigate to **Stream**
* Each video has a **UID** → that's the video ID you need

---

## 5. How to Use the Python Downloader Script

1. Run the script `cloudflare_downloader.py` using Python

2. Choose video source:

   * `1` for Cloudflare Stream
   * `2` for YouTube

3. Provide the required video ID or URL

4. (Optional) Enter a custom output filename (no `.mp4` needed)

5. The downloaded video will be saved to:

   ```
   %USERPROFILE%\Documents\cfdownloader
   ```

6. Press any key to continue downloading or type `exit` to quit

---

🎉 Done! You can now download Cloudflare Stream or YouTube videos quickly and safely using your terminal.
