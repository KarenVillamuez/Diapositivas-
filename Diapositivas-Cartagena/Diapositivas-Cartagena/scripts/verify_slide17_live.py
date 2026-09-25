# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
png_path = os.path.join(output_dir, "slide_17_live_verified.png")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    page.goto("http://localhost:8085/#slide-17")
    page.wait_for_timeout(600)
    page.screenshot(path=png_path)
    print(f"Captured live slide 17: {png_path}")
    browser.close()
