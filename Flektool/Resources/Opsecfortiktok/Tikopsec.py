import sys,traceback,ctypes
from playwright.sync_api import sync_playwright

ctypes.windll.kernel32.SetConsoleTitleW("Fleks opsec tiktok thingy")

try:
    u=input("Input text here for ultimate tiktok opsec o algo : ").strip()
    if "tiktok.com" not in u.lower():
        print("sorry saar ur too dumb to do dis o algo");input("to JSID click enter");sys.exit()
    if not u.startswith("http"):u="https://"+u.lstrip("/")
    with sync_playwright() as p:
        b=p.chromium.launch(headless=True)
        c=b.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        g=c.new_page()
        g.goto(u)
        g.wait_for_timeout(2000)
        print(g.url.split("?")[0])
        b.close()
    input("to JSID click enter")
except Exception:
    traceback.print_exc()
    input("to JSID click enter")