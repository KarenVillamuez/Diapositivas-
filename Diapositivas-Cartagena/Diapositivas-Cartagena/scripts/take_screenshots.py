# -*- coding: utf-8 -*-
"""
Captura screenshots de alta definición (1920x1080) para cada diapositiva
usando Playwright.
"""
import os
from playwright.sync_api import sync_playwright

output_dir = r"C:\Users\ASUS\.gemini\antigravity-ide\brain\a6624504-511c-4b9d-bc9a-468e348bde40\verified_slides"
os.makedirs(output_dir, exist_ok=True)

slides_to_check = list(range(1, 20))

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    
    page.goto("http://localhost:8085/?v=12#slide-1")
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(600)

    for s_idx in slides_to_check:
        page.evaluate(f"window.location.hash = 'slide-{s_idx}'")
        page.evaluate(f"""
            const slides = document.querySelectorAll('.slide');
            slides.forEach((s, idx) => {{
                if (idx === {s_idx - 1}) {{
                    s.classList.add('active');
                }} else {{
                    s.classList.remove('active');
                }}
            }});
        """)
        page.wait_for_timeout(350)
        shot_path = os.path.join(output_dir, f"slide_{s_idx:02d}.png")
        page.screenshot(path=shot_path)
        print(f"Captured Slide {s_idx:02d} -> {shot_path}")

    browser.close()

print("All screenshots captured successfully!")
