# Portfolio site

A one-page portfolio built with Flask + Jinja templates.

## Deploying this

`index.html` and `base.html` are **Jinja templates**, not plain HTML — they
contain `{% %}` / `{{ }}` syntax that only a running Flask process understands.
That means:

- **Flask hosting** (Render, Railway, PythonAnywhere, Fly.io, a VPS, etc.):
  works as-is. Deploy `app.py` and everything alongside it (including
  `index.html`, `base.html`, `components/`, and `static/`) and run it the same
  way as `python app.py`, just with a production WSGI server instead of the
  dev server.
- **Static hosting** (GitHub Pages, Netlify, S3, plain file upload with no
  server process): will **not** work by uploading these files directly — a
  browser has no idea what to do with `{% for %}` or `{{ site.name }}` and
  will display that text literally. To get a static version, the templates
  would need to be pre-rendered to plain HTML first (e.g. save the output of
  `render_template()` to a `.html` file, or use a tool like Flask-Frozen).
  That's a separate conversion this project doesn't currently do.

## Running it locally

```bash
pip install flask
python app.py
```

Then open http://127.0.0.1:5000/

## Project structure

```
portfolio-flask/
├── app.py                       # Routes + ALL editable content (see below)
├── base.html                    # <head>, header/footer includes, script tag
├── index.html                   # Page content, extends base.html
├── components/
│   ├── navbar.html              # Site header / nav
│   ├── footer.html              # Contact footer
│   ├── icons.html                # Every SVG icon, as Jinja macros
│   └── project_card.html         # Reusable project-card macro
├── static/
│   ├── css/style.css             # All styling
│   ├── js/main.js                # Mobile nav, scroll-spy, header shadow
│   ├── files/
│   │   └── Your-Name-Resume.pdf  # Served directly for the "Download résumé" buttons
│   └── images/
│       ├── profile/               # Drop profile.jpg here — see below
│       └── projects/              # Drop internship.jpg here — see below
└── README.md
```

Note: `base.html`, `index.html`, and `components/` are still Jinja templates
rendered by Flask — they live at the project root now instead of inside a
`templates/` folder, but they're not plain static HTML. See "Deploying this"
below before uploading them to a static host.

## Where to edit things

**Almost everything content-related lives in `app.py`**, not in the templates:

- `SITE` — name, tagline, location, email, LinkedIn, GitHub, résumé filename
- `ABOUT_FACTS` — the fact list next to the About text
- `PROJECTS` — the 4 project cards (currently **placeholder examples** — see below)
- `EXPERIENCE` — the two timeline entries
- `SKILL_GROUPS` — the four skill categories
- `ACHIEVEMENTS` — the achievements list

Editing those Python data structures updates the rendered page — you shouldn't
need to touch HTML for routine content changes.

The one-off sections that only appear once (Hero copy, the Featured Project
case study, and its diagram) are written directly into `templates/index.html`,
since turning a single occurrence into a data-driven loop would add
indirection without benefit.

## Adding your photos

The site has two photo slots, both optional — until you add a file, a dashed
placeholder box shows the expected path instead:

| Photo | Exact path | Shown in |
|---|---|---|
| Profile / portrait | `static/images/profile/profile.jpg` | About section |
| Internship / project | `static/images/projects/internship.jpg` | Featured Project section |

Drop a file at the exact path above (same filename) and it appears
automatically — no code or template changes needed. Each folder has a
`PLACE_YOUR_PHOTO_HERE.txt` reminder you can delete once your photo is in.

## Before publishing

The `PROJECTS` list in `app.py` currently holds four example projects shaped
around common IT-graduate interests (frontend, networking, automation, AI/ML)
— they are **not real projects**. Replace their `description`, `github`, and
`demo` values with your actual work before this goes live. Same for the
placeholder name/email/LinkedIn/GitHub in `SITE`.

## Notes on a couple of implementation choices

- **Résumé is a real static file**, not embedded in the page. This replaced an
  ~80KB base64 blob that was previously inlined directly in the HTML.
- **The hero network diagram and the featured-project pipeline diagram stay as
  inline SVG** in `index.html` rather than external image files, because their
  draw-in animation is driven by CSS classes (`.node` / `.edge`) that need the
  SVG to be part of the page's DOM — an external `<img>` couldn't be animated
  or coloured this way.
- Mobile nav relies on the header **not** using `backdrop-filter`: that
  property creates a CSS containing block that breaks `position: fixed` on
  the mobile menu panel. If you reintroduce a blurred header, test the mobile
  menu again afterwards.
