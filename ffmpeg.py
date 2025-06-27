import os
import subprocess
import sys
import shutil

YTDLP_PATH = r"C:\ffmpeg\yt-dlp.exe"
CLOUDFLARE_PREFIX = "https://customer-zlvlcdgbcvpukf1t.cloudflarestream.com/"
OUTDIR = os.path.join(os.path.expanduser("~"), "Documents", "cfdownloader")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_yt_dlp_available():
    return os.path.exists(YTDLP_PATH)

def get_input(prompt, allow_empty=False):
    while True:
        val = input(prompt).strip()
        if val or allow_empty:
            return val
        print("⚠ Input tidak boleh kosong.")

def download_video(source, url, outname=""):
    print("\n⏬ Mulai download...")
    if not os.path.exists(OUTDIR):
        os.makedirs(OUTDIR)

    output_template = os.path.join(OUTDIR, f"{outname}.%(ext)s") if outname else os.path.join(OUTDIR, "%(title)s.%(ext)s")

    if source == "YouTube":
        cmd = [
            YTDLP_PATH,
            "-f", "bv*+ba/b",
            "--merge-output-format", "mp4",
            "-o", output_template,
            url
        ]
    else:  # Cloudflare
        cmd = [
            YTDLP_PATH,
            "-o", output_template,
            url
        ]

    try:
        subprocess.run(cmd, check=True)
        print("\n✅ Download selesai.")
        print(f"📁 File tersimpan di: {OUTDIR}")
    except subprocess.CalledProcessError as e:
        print("❌ Gagal download.")
        print(f"Detail error: {e}")

def main():
    if not is_yt_dlp_available():
        print(f"❌ yt-dlp.exe tidak ditemukan di {YTDLP_PATH}")
        sys.exit(1)

    while True:
        clear()
        print("="*55)
        print("           VIDEO  DOWNLOADER  UTILITY")
        print("="*55)
        print("\nPilih sumber video:")
        print("  1) Cloudflare Stream")
        print("  2) YouTube")
        print("  3) Keluar")

        choice = input("Masukkan pilihan (1/2/3): ").strip()
        if choice == "3":
            print("👋 Keluar. Sampai jumpa!")
            break
        elif choice == "1":
            source = "Cloudflare"
            vid = get_input("Masukkan ID Cloudflare Stream: ")
            url = CLOUDFLARE_PREFIX + vid
        elif choice == "2":
            source = "YouTube"
            url = get_input("Masukkan URL YouTube: ")
        else:
            print("⚠ Pilihan tidak valid.")
            input("Tekan Enter untuk kembali...")
            continue

        outname = get_input("Nama file output (tanpa .mp4) [enter=default]: ", allow_empty=True)
        download_video(source, url, outname)

        again = input("\nTekan Enter untuk download lagi atau ketik 'exit' untuk keluar: ").strip().lower()
        if again == "exit":
            print("👋 Keluar. Terima kasih.")
            break

if __name__ == "__main__":
    main()
