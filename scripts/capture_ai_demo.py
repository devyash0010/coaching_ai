"""Capture a demo screenshot of the AI Assistant page with a real RAG answer."""
from pathlib import Path

from playwright.sync_api import sync_playwright

OUT = Path(r"d:\projects\Coaching_ai\docs\screenshots\ai-assistant.png")
QUESTION = "Which students are weak in Physics?"

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=True)
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto("http://localhost:3000/ai-assistant", wait_until="networkidle")

    box = page.locator("textarea")
    box.fill(QUESTION)
    page.get_by_role("button", name="Ask").click()

    # Wait for the grounded answer to replace the "No answer yet" placeholder.
    page.get_by_text("No answer yet").wait_for(state="hidden", timeout=120_000)
    page.wait_for_timeout(1_000)  # let the text finish rendering

    OUT.parent.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=str(OUT), full_page=False)
    print(f"saved {OUT}")
    browser.close()
