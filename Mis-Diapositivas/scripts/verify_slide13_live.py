# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40"
os.makedirs(output_dir, exist_ok=True)
png_path = os.path.join(output_dir, "slide_13_live_verified.png")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    page.goto("http://localhost:8085/?t=123#slide-13")
    page.wait_for_timeout(600)
    
    page.evaluate("""
        const slides = document.querySelectorAll('.slide');
        slides.forEach((s) => {
            if (s.id === 'slide-13') {
                s.classList.add('active');
            } else {
                s.classList.remove('active');
            }
        });
    """)
    page.wait_for_timeout(500)
    page.screenshot(path=png_path)
    print("Captured slide_13_live_verified.png")
    browser.close()
