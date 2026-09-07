# build_pdf.py
from pathlib import Path
from playwright.sync_api import sync_playwright


def convert_sphinx_html_to_pdf(html_path: str, output_pdf: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the built Sphinx page
        file_url = Path(html_path).resolve().as_uri()
        page.goto(file_url, wait_until="networkidle")

        # Emulate standard screen CSS instead of print media query if desired
        page.emulate_media(media="screen")

        # Generate the PDF using Chrome's print engine
        page.pdf(
            path=output_pdf,
            format="A4",
            print_background=True,  # Keeps custom CSS backgrounds/colors
            margin={
                "top": "0.6in",
                "bottom": "0.6in",
                "left": "0.5in",
                "right": "0.5in",
            },
        )

        browser.close()


if __name__ == "__main__":
    # convert_sphinx_html_to_pdf("docs/_build/html/index.html",
    #                            "docs/_build/output.pdf")
    convert_sphinx_html_to_pdf("docs/_build/html/breadboard_quizzes/LEDs_quiz.html",
                                   "docs/_build/LEDs_quiz.pdf")

