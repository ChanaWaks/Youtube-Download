import tkinter as tk
from tkinter import ttk, scrolledtext
import subprocess
import threading
import os

# ── Fixed paths ──────────────────────────────────────────────────────────────
YTDLP_PATH  = r'C:\Users\RCG REP 22\OneDrive\Desktop\yt-dlp.exe'
FFMPEG_PATH = r'C:\Users\RCG REP 22\OneDrive\Desktop\ffmpeg-8.1.1-essentials_build\ffmpeg-8.1.1-essentials_build\bin'
OUTPUT_DIR  = r'C:\Users\RCG REP 22\OneDrive\Desktop\Rivka Mp4\Accapella Mix'
# ─────────────────────────────────────────────────────────────────────────────

THEMES = {
    "zalman": {
        "name":     "Zalman",
        "age":      "12",
        "emoji":    "🎧",
        "bg":       "#0d0d0d",
        "card":     "#1a1a1a",
        "accent":   "#00e5ff",
        "accent2":  "#00b8d4",
        "btn_fg":   "#000000",
        "tag":      "#1a2a2a",
        "tag_fg":   "#00e5ff",
        "dark":     "#050505",
        "log_fg":   "#00e5ff",
        "title":    "Zalman's Download Station",
        "subtitle": "Fast. Clean. No cap. 🎧",
        "step1":    "Drop the YouTube link 🔗",
        "step2":    "Pick your format 🎯",
        "mp3_lbl":  "🎵  Audio\n     MP3",
        "mp4_lbl":  "🎬  Video\n     MP4",
        "dl_text":  "⬇  LET'S GO",
        "done":     "✅ Done! That was fast 🔥",
        "stars":    ["🎧","🔥","⚡","🎵","💿","🎤","🎶"],
        "border":   "#00e5ff",
        "progress": "#00e5ff",
        "trough":   "#1a2a2a",
        "title_fg": "#00e5ff",
        "sub_fg":   "#666666",
        "step_fg":  "#00e5ff",
        "font_title": ("Consolas", 20, "bold"),
        "font_sub":   ("Consolas", 11),
        "font_step":  ("Consolas", 10, "bold"),
        "font_btn":   ("Consolas", 13, "bold"),
        "font_dl":    ("Consolas", 15, "bold"),
        "switcher_active_fg": "#000000",
        "switcher_inactive_fg": "#555555",
        "switcher_inactive_bg": "#1a1a1a",
    },
    "shmuli": {
        "name":     "Shmuli",
        "age":      "6",
        "emoji":    "🚀",
        "bg":       "#f0f7ff",
        "card":     "#dbeafe",
        "accent":   "#2563eb",
        "accent2":  "#1d4ed8",
        "btn_fg":   "#ffffff",
        "tag":      "#eff6ff",
        "tag_fg":   "#1d4ed8",
        "dark":     "#0a1a2d",
        "log_fg":   "#93c5fd",
        "title":    "🚀 Shmuli's Super Downloader! 🚀",
        "subtitle": "WOOHOO! Let's get some songs!! ⚡🎮",
        "step1":    "Step 1 — Paste the link here! 🎮",
        "step2":    "Step 2 — What do you want? 🎯",
        "mp3_lbl":  "🎵\nJust Music!\nMP3",
        "mp4_lbl":  "🎬\nMusic+Video!\nMP4",
        "dl_text":  "⬇  DOWNLOAD NOW!! 🚀",
        "done":     "🎉 YESSS!! ALL DONE!! SO COOL!! 🚀⚡🏆",
        "stars":    ["🚀","⚡","🎮","🌟","🏆","💥","🎯"],
        "border":   "#93c5fd",
        "progress": "#2563eb",
        "trough":   "#dbeafe",
        "title_fg": "#1d4ed8",
        "sub_fg":   "#3b82f6",
        "step_fg":  "#1d4ed8",
        "font_title": ("Segoe UI", 19, "bold"),
        "font_sub":   ("Segoe UI", 12, "bold"),
        "font_step":  ("Segoe UI", 10, "bold"),
        "font_btn":   ("Segoe UI", 13, "bold"),
        "font_dl":    ("Segoe UI Rounded", 16, "bold"),
        "switcher_active_fg": "#ffffff",
        "switcher_inactive_fg": "#888888",
        "switcher_inactive_bg": "#dbeafe",
    },
    "rivka": {
        "name":     "Rivka",
        "age":      "9",
        "emoji":    "🌸",
        "bg":       "#fff5fb",
        "card":     "#fce7f3",
        "accent":   "#ec4899",
        "accent2":  "#db2777",
        "btn_fg":   "#ffffff",
        "tag":      "#fdf2f8",
        "tag_fg":   "#be185d",
        "dark":     "#2d0a1a",
        "log_fg":   "#f9a8d4",
        "title":    "✨ Rivka's Music Corner ✨",
        "subtitle": "Download your favourite songs & videos! 🎀🦋",
        "step1":    "Step 1 — Paste your YouTube link 🎵",
        "step2":    "Step 2 — Music or Video? 💖",
        "mp3_lbl":  "🎵\nJust Music!\nMP3",
        "mp4_lbl":  "🎬\nMusic+Video!\nMP4",
        "dl_text":  "⬇  Download Now! 🌸",
        "done":     "🎉 YAY!! All done! Your songs are ready! 🌸💖🦋",
        "stars":    ["🌸","💖","🌺","🦋","🌷","⭐","🎀"],
        "border":   "#f9a8d4",
        "progress": "#ec4899",
        "trough":   "#fce7f3",
        "title_fg": "#ec4899",
        "sub_fg":   "#f472b6",
        "step_fg":  "#db2777",
        "font_title": ("Segoe UI", 18, "bold"),
        "font_sub":   ("Segoe UI", 12, "bold"),
        "font_step":  ("Segoe UI", 10, "bold"),
        "font_btn":   ("Segoe UI", 13, "bold"),
        "font_dl":    ("Segoe UI Rounded", 15, "bold"),
        "switcher_active_fg": "#ffffff",
        "switcher_inactive_fg": "#888888",
        "switcher_inactive_bg": "#fce7f3",
    },
}

GREEN = "#22c55e"
RED   = "#ef4444"
GRAY  = "#888888"
WHITE = "#ffffff"


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x740")
        self.resizable(False, False)
        self.fmt = tk.StringVar(value="mp3")
        self.theme_key = "rivka"
        self.theme = THEMES["rivka"]
        self._build()
        self._apply_theme()

    def _build(self):
        # ── Switcher bar ──
        self.switcher = tk.Frame(self, bd=0)
        self.switcher.pack(fill="x")

        self.sw_btns = {}
        for key in ["zalman", "shmuli", "rivka"]:
            t = THEMES[key]
            b = tk.Button(
                self.switcher,
                text=f"{t['emoji']} {t['name']}",
                font=("Segoe UI", 11, "bold"),
                bd=0, relief="flat", cursor="hand2", pady=10,
                command=lambda k=key: self._switch_theme(k)
            )
            b.pack(side="left", expand=True, fill="x")
            self.sw_btns[key] = b

        # ── Stars strip ──
        self.stars_canvas = tk.Canvas(self, height=38, highlightthickness=0)
        self.stars_canvas.pack(fill="x")

        # ── Header ──
        self.hdr = tk.Frame(self)
        self.hdr.pack(pady=(10, 2))
        self.lbl_emoji = tk.Label(self.hdr, font=("Segoe UI", 50))
        self.lbl_emoji.pack()
        self.lbl_title = tk.Label(self.hdr)
        self.lbl_title.pack()
        self.lbl_sub = tk.Label(self.hdr)
        self.lbl_sub.pack()

        # ── Step 1 ──
        self.lbl_step1 = tk.Label(self, anchor="w")
        self.lbl_step1.pack(fill="x", padx=32, pady=(16, 4))

        self.url_outer = tk.Frame(self, bd=3, relief="flat")
        self.url_outer.pack(fill="x", padx=28, pady=(0, 12))
        self.url_var = tk.StringVar()
        self.url_var.trace_add("write", lambda *_: self._on_url_change())
        self.url_entry = tk.Entry(
            self.url_outer, textvariable=self.url_var,
            font=("Segoe UI", 12, "bold"),
            bd=0, relief="flat", fg="#333"
        )
        self.url_entry.pack(fill="x", padx=14, pady=11)

        # ── Step 2 ──
        self.lbl_step2 = tk.Label(self, anchor="w")
        self.lbl_step2.pack(fill="x", padx=32, pady=(0, 6))

        self.fmt_frame = tk.Frame(self)
        self.fmt_frame.pack(fill="x", padx=28, pady=(0, 12))

        self.btn_mp3 = tk.Button(
            self.fmt_frame, bd=0, relief="flat", cursor="hand2", pady=18,
            command=lambda: self._select_fmt("mp3")
        )
        self.btn_mp3.pack(side="left", expand=True, fill="both", padx=(0, 6))

        self.btn_mp4 = tk.Button(
            self.fmt_frame, bd=0, relief="flat", cursor="hand2", pady=18,
            command=lambda: self._select_fmt("mp4")
        )
        self.btn_mp4.pack(side="left", expand=True, fill="both", padx=(6, 0))

        # ── Download button ──
        self.dl_btn = tk.Button(
            self, bd=0, relief="flat", cursor="hand2",
            padx=20, pady=18,
            command=self._start_download
        )
        self.dl_btn.pack(fill="x", padx=28, pady=(4, 12))

        # ── Status ──
        self.status_var = tk.StringVar(value="Pick your name above to get started! 😊")
        self.status_lbl = tk.Label(
            self, textvariable=self.status_var,
            font=("Segoe UI", 11, "bold"), wraplength=550
        )
        self.status_lbl.pack(pady=(0, 6))

        # ── Progress ──
        self.pb_style = ttk.Style()
        self.pb_style.theme_use("clam")
        self.progress = ttk.Progressbar(self, mode="indeterminate", length=544)
        self.progress.pack(padx=28, pady=(0, 8))

        # ── Log ──
        self.log_lbl = tk.Label(self, font=("Segoe UI", 9, "bold"), fg=GRAY, anchor="w")
        self.log_lbl.pack(fill="x", padx=28)
        self.log = scrolledtext.ScrolledText(
            self, font=("Consolas", 9),
            insertbackground="white", relief="flat",
            height=7, state="disabled", wrap="word"
        )
        self.log.pack(fill="both", padx=28, pady=(4, 16))

    # ── Theme ─────────────────────────────────────────────────────────────────
    def _switch_theme(self, key):
        self.theme_key = key
        self.theme = THEMES[key]
        self._apply_theme()

    def _apply_theme(self):
        t = self.theme
        key = self.theme_key
        self.title(f"{t['emoji']} {t['name']}'s Downloader")
        self.configure(bg=t["bg"])

        # switcher buttons
        self.switcher.configure(bg=t["card"])
        for k, b in self.sw_btns.items():
            tk = THEMES[k]
            if k == key:
                b.configure(bg=t["accent"], fg=t["switcher_active_fg"])
            else:
                b.configure(bg=t["switcher_inactive_bg"], fg=t["switcher_inactive_fg"])

        # stars
        self.stars_canvas.configure(bg=t["card"])
        self.stars_canvas.delete("all")
        for i, s in enumerate(t["stars"]):
            x = 44 + i * 76
            self.stars_canvas.create_text(x, 19, text=s, font=("Segoe UI", 17))

        # header
        self.hdr.configure(bg=t["bg"])
        self.lbl_emoji.configure(bg=t["bg"], text=t["emoji"])
        self.lbl_title.configure(
            bg=t["bg"], fg=t["title_fg"], text=t["title"],
            font=t["font_title"]
        )
        self.lbl_sub.configure(
            bg=t["bg"], fg=t["sub_fg"], text=t["subtitle"],
            font=t["font_sub"]
        )

        # steps
        self.lbl_step1.configure(bg=t["bg"], fg=t["step_fg"], text=t["step1"], font=t["font_step"])
        self.lbl_step2.configure(bg=t["bg"], fg=t["step_fg"], text=t["step2"], font=t["font_step"])

        # url
        self.url_outer.configure(bg=t["accent"])
        self.url_entry.configure(bg=t["tag"], insertbackground=t["accent"])

        # fmt frame
        self.fmt_frame.configure(bg=t["bg"])
        self._refresh_fmt_buttons()

        # dl button
        self.dl_btn.configure(
            bg=t["accent"], fg=t["btn_fg"],
            text=t["dl_text"], font=t["font_dl"],
            activebackground=t["accent2"], activeforeground=t["btn_fg"]
        )

        # status
        self.status_lbl.configure(bg=t["bg"], fg=GRAY)

        # progress
        self.pb_style.configure(
            "kid.Horizontal.TProgressbar",
            troughcolor=t["trough"], background=t["progress"],
            thickness=16, borderwidth=0
        )
        self.progress.configure(style="kid.Horizontal.TProgressbar")

        # log
        self.log_lbl.configure(bg=t["bg"],
            text="📋 What's happening:" if key != "zalman" else "// live log")
        self.log.configure(bg=t["dark"], fg=t["log_fg"])

    def _refresh_fmt_buttons(self):
        t = self.theme
        fmt = self.fmt.get()
        fnt = t["font_btn"]
        if fmt == "mp3":
            self.btn_mp3.configure(bg=t["accent"], fg=t["btn_fg"],
                                   text=t["mp3_lbl"], font=fnt,
                                   activebackground=t["accent2"], activeforeground=t["btn_fg"])
            self.btn_mp4.configure(bg=t["tag"], fg=t["accent"],
                                   text=t["mp4_lbl"], font=fnt,
                                   activebackground=t["tag"], activeforeground=t["accent"])
        else:
            self.btn_mp4.configure(bg=t["accent"], fg=t["btn_fg"],
                                   text=t["mp4_lbl"], font=fnt,
                                   activebackground=t["accent2"], activeforeground=t["btn_fg"])
            self.btn_mp3.configure(bg=t["tag"], fg=t["accent"],
                                   text=t["mp3_lbl"], font=fnt,
                                   activebackground=t["tag"], activeforeground=t["accent"])

    def _select_fmt(self, value):
        self.fmt.set(value)
        self._refresh_fmt_buttons()

    # ── URL ───────────────────────────────────────────────────────────────────
    def _on_url_change(self):
        url = self.url_var.get().strip()
        t = self.theme
        if not url:
            self._set_status("Paste a link to get started! 😊", GRAY)
        elif "list=" not in url:
            self._set_status("🤔 That doesn't look right — make sure it has list= in it!", "#f97316")
        else:
            if self.theme_key == "zalman":
                self._set_status("✅ Link looks good. Hit the button.", GREEN)
            elif self.theme_key == "shmuli":
                self._set_status("✅ GREAT LINK!! Now press the big button!! 🚀", GREEN)
            else:
                self._set_status("✅ Perfect! Now press the button! 🌸", GREEN)

    def _set_status(self, msg, color=GRAY):
        self.status_var.set(msg)
        self.status_lbl.configure(fg=color)

    # ── Log ───────────────────────────────────────────────────────────────────
    def _log(self, text):
        self.log.configure(state="normal")
        self.log.insert("end", text + "\n")
        self.log.see("end")
        self.log.configure(state="disabled")

    # ── Download ──────────────────────────────────────────────────────────────
    def _start_download(self):
        url = self.url_var.get().strip()
        if not url or "list=" not in url:
            self._set_status("⚠ Paste a real playlist link first!", RED)
            return
        if not os.path.exists(YTDLP_PATH):
            self._set_status("❌ Can't find yt-dlp! Ask a grown-up for help 😊", RED)
            return

        os.makedirs(OUTPUT_DIR, exist_ok=True)
        t = self.theme
        self.dl_btn.configure(state="disabled", text="⏳ Downloading...", bg="#888")
        self.progress.start(10)
        if self.theme_key == "zalman":
            self._set_status("Downloading... this won't take long.", t["accent"])
        elif self.theme_key == "shmuli":
            self._set_status("🚀🚀 DOWNLOADING!! SO EXCITING!! WAIT A BIT!! 🚀🚀", t["accent"])
        else:
            self._set_status("🌸 Downloading your songs... almost there! 🎵", t["accent"])

        threading.Thread(target=self._run_download, args=(url,), daemon=True).start()

    def _run_download(self, url):
        fmt = self.fmt.get()
        out_template = os.path.join(OUTPUT_DIR, "%(playlist_index)s - %(title)s.%(ext)s")
        cmd = [YTDLP_PATH]
        if fmt == "mp3":
            cmd += ["-x", "--audio-format", "mp3"]
        else:
            cmd += ["-f", "bestvideo+bestaudio"]
        cmd += ["--ffmpeg-location", FFMPEG_PATH, "-i", "-o", out_template, url]
        self._log("▶ Starting...\n")
        try:
            proc = subprocess.Popen(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                text=True, encoding="utf-8", errors="replace"
            )
            for line in proc.stdout:
                line = line.rstrip()
                if line:
                    self.after(0, self._log, line)
            proc.wait()
            self.after(0, self._done, proc.returncode == 0)
        except Exception as e:
            self.after(0, self._log, f"ERROR: {e}")
            self.after(0, self._done, False)

    def _done(self, success):
        t = self.theme
        self.progress.stop()
        self.dl_btn.configure(state="normal", text=t["dl_text"], bg=t["accent"])
        if success:
            self._set_status(t["done"], GREEN)
            self._log("\n✅ Complete!")
        else:
            self._set_status("⚠ Some files had errors. Check the log!", RED)
            self._log("\n⚠ Finished with some errors.")


if __name__ == "__main__":
    app = App()
    app.mainloop()
