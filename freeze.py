"""
freeze.py — generate a static version of this Flask portfolio for GitHub Pages.

This does NOT change app.py, the templates, or static/ in any way. It just
runs the existing Flask app internally (the same way a browser request would
hit it), captures what it renders, and writes that out as plain files.

Usage:
    python freeze.py

Output:
    docs/
    ├── index.html      <- fully-rendered HTML, no Jinja/Flask needed to view it
    └── static/...      <- copy of the static/ folder

Deploying:
    Commit the docs/ folder and, in your GitHub repo, go to
    Settings -> Pages -> Deploy from a branch -> select your branch and
    the /docs folder. GitHub will serve docs/index.html as the site.

Re-run this script any time you change app.py, index.html, base.html,
components/, or static/ and want the static copy to catch up.
"""

import shutil
from pathlib import Path

from app import app  # the existing, unmodified Flask app

OUTPUT_DIR = Path(__file__).parent / "docs"


def render_pages():
    """
    Render every simple GET route on the app to HTML, using Flask's own
    test client (no real server, no extra dependency needed).

    Routes that take URL arguments (e.g. "/projects/<slug>") are skipped,
    since a freeze script has no way to know which values to render ahead
    of time. This app currently only has "/", so that's what gets rendered.
    """
    pages = {}
    with app.test_client() as client:
        for rule in app.url_map.iter_rules():
            if rule.endpoint == "static" or rule.arguments:
                continue
            if "GET" not in rule.methods:
                continue

            response = client.get(rule.rule)
            if response.status_code != 200:
                print(f"  ! Skipping {rule.rule} (status {response.status_code})")
                continue

            html = response.get_data(as_text=True)
            # url_for('static', ...) produces root-relative paths like
            # "/static/css/style.css". That only works if the site is
            # hosted at the domain root. GitHub Pages project sites are
            # usually served from a subfolder (e.g. username.github.io/repo/),
            # so we rewrite these to plain relative paths ("static/...")
            # which work in both cases.
            html = html.replace('="/static/', '="static/')

            filename = "index.html" if rule.rule == "/" else rule.rule.strip("/") + ".html"
            pages[filename] = html

    return pages


def copy_static_assets():
    src = Path(app.static_folder)
    dst = OUTPUT_DIR / "static"
    if not src.exists():
        return
    # The PLACE_YOUR_PHOTO_HERE.txt reminders are for local development only.
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns("PLACE_YOUR_PHOTO_HERE.txt"))


def main():
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)

    print("Rendering pages...")
    for filename, html in render_pages().items():
        out_path = OUTPUT_DIR / filename
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(html, encoding="utf-8")
        print(f"  wrote {out_path.relative_to(OUTPUT_DIR.parent)}")

    print("Copying static/ ...")
    copy_static_assets()

    # Tells GitHub Pages not to run this through Jekyll, which otherwise
    # ignores/mishandles some filenames and folder structures by default.
    (OUTPUT_DIR / ".nojekyll").touch()

    print(f"\nDone. Static site written to: {OUTPUT_DIR}")
    print("GitHub Pages -> Settings -> Pages -> Deploy from a branch -> /docs")


if __name__ == "__main__":
    main()
