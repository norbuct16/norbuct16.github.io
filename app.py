"""
Portfolio site — Flask app.

Almost everything you'd want to personalise (name, contact links, projects,
skills, achievements, experience) lives in the data below. Edit here first;
you shouldn't need to touch the templates just to update content.
"""

import os
from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__, template_folder=".")


# ---------------------------------------------------------------------------
# Images
# Paths are relative to static/. Drop your files at these exact locations —
# the template checks whether they exist and swaps a placeholder box for the
# real photo automatically, no code changes needed.
# ---------------------------------------------------------------------------
PROFILE_IMAGE_PATH = "images/profile/profile.jpg"
PROJECT_IMAGE_PATH = "images/projects/internship.jpg"


def _static_file_exists(relative_path):
    return os.path.isfile(os.path.join(app.static_folder, relative_path))


# ---------------------------------------------------------------------------
# Site-wide info
# ---------------------------------------------------------------------------
SITE = {
    "name": "Norbu Chogyel Tobgyel",
    "role": "Software & Network Engineering Graduate",
    "location": "Canberra, ACT, Australia",
    "location_short": "Canberra, ACT",
    "degree_short": "B.Eng (Honours), 2025",
    "email": "norbuct16@gmail.com",
    "linkedin": "https://linkedin.com/in/norbuct16",
    "linkedin_display": "linkedin.com/in/norbuct16",
    "github": "https://github.com/norbuct16",
    "github_display": "github.com/norbuct16",
    # Path is relative to the static/ folder.
    "resume_file": "files/Norbu_C_Tobgyel_Resume.pdf",
    "resume_filename": "Norbu_C_Tobgyel_Resume.pdf",
}
# Initials for the nav brand mark, derived from the name so it never
# goes stale if you update SITE["name"].
SITE["initials"] = "".join(part[0] for part in SITE["name"].split()[:2]).upper()


# ---------------------------------------------------------------------------
# About section — right-hand fact list
# ---------------------------------------------------------------------------
ABOUT_FACTS = [
    {"label": "Based in", "value": "Canberra, ACT, Australia"},
    {"label": "Degree", "value": "B.Eng (Honours), Network & Software Engineering"},
    {"label": "Graduated", "value": "December 2025"},
    {"label": "Focus areas", "value": "Software, Cybersecurity, Networking, AI/ML"},
    {"label": "Looking for", "value": "Graduate / entry-level IT roles"},
]

FEATURED_PROJECT_TAGS = ["Python", "Cisco", "AlgoSec", "Automation", "Report generation"]


# ---------------------------------------------------------------------------
# Selected projects
# Example projects shaped around common IT-graduate interests — replace with
# real projects and their actual GitHub/demo links as you build them.
# dot_class must match a .cat-dot-* rule in static/css/style.css.
# ---------------------------------------------------------------------------
PROJECTS = [
    {
    "category": "Full-Stack · Cybersecurity",
    "dot_class": "cat-dot-cybersecurity",
    "title": "Integrated Web Vulnerability Scanner",
    "description": (
        "A web-based vulnerability assessment platform that integrates SQLMap "
        "and XSStrike with NVD and Vulners vulnerability intelligence, presenting "
        "scan findings, CVSS severity, and ML-assisted prioritisation in a "
        "readable dashboard."
    ),
    "tags": ["Python", "Flask", "SQLMap", "XSStrike", "NVD", "Vulners", "ML"],
    "github": "https://github.com/norbuct16/Integrated-Web-Vulnerability-Scanner",
    
    },
]


# ---------------------------------------------------------------------------
# Experience (most recent first)
# ---------------------------------------------------------------------------
EXPERIENCE = [
    {
        "role": "Software Engineer Intern",
        "org": "Innovation Central Canberra",
        "date": "Jun 2025 – Aug 2025",
        "description": (
            "Developed an automation solution for device vulnerability and "
            "lifecycle reporting in collaboration with Cisco and AlgoSec — "
            "covering project planning, delivery, and stakeholder engagement. "
            "Won Best Project across all teams and reached the AIIA ACT Finals, "
            "Student category."
        ),
    },
    {
        "role": "Mentor",
        "org": "SK Education Consultancy and Firm, Thimphu",
        "date": "Oct 2021",
        "description": (
            "Mentored students preparing for the TOEFL exam, delivering "
            "strategies, lesson content, and presentation practice — early "
            "experience in communication and structured teaching."
        ),
    },
]


# ---------------------------------------------------------------------------
# Skills
# ---------------------------------------------------------------------------
SKILL_GROUPS = [
    {
        "title": "Software development",
        "subtitle": "Core",
        "tags": ["Python", "Java", "HTML", "CSS", "SQL"],
    },
    {
        "title": "Networking & security",
        "subtitle": "Core, from coursework and internship",
        "tags": ["Computer Networks", "Cybersecurity", "Cisco", "AlgoSec"],
    },
    {
        "title": "Data & cloud",
        "subtitle": "Core",
        "tags": ["Data Analysis", "Database Systems", "Cloud Computing"],
    },
    {
        "title": "Currently building",
        "subtitle": "Growing through personal projects",
        "tags": ["JavaScript", "React", "Machine Learning"],
    },
]


# ---------------------------------------------------------------------------
# Achievements
# ---------------------------------------------------------------------------
ACHIEVEMENTS = [
    {"org": "Innovation Central Canberra", "title": "Best Project Award, all teams", "year": "2025"},
    {"org": "AIIA", "title": "ACT Finalist, Student Category", "year": "2025"},
    {"org": "University of Canberra", "title": "Dean's Excellence, four semesters", "year": "2022–2025"},
    {"org": "University of Canberra", "title": "Second Class Honours, Division II", "year": "2026"},
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        site=SITE,
        about_facts=ABOUT_FACTS,
        featured_project_tags=FEATURED_PROJECT_TAGS,
        projects=PROJECTS,
        experience=EXPERIENCE,
        skill_groups=SKILL_GROUPS,
        achievements=ACHIEVEMENTS,
        current_year=datetime.now().year,
        profile_image_path=PROFILE_IMAGE_PATH,
        profile_image_exists=_static_file_exists(PROFILE_IMAGE_PATH),
        project_image_path=PROJECT_IMAGE_PATH,
        project_image_exists=_static_file_exists(PROJECT_IMAGE_PATH),
    )


if __name__ == "__main__":
    app.run(debug=True)
