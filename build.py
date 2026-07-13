#!/usr/bin/env python3
"""
build.py
"""

from jinja2 import Environment, FileSystemLoader, select_autoescape
import os

from content import (
    SITE,
    about,
    experience,
    projects,
    #fellowship,
    family,
    skills,
    education,
    contact
)


def build_site():
    print("🚀 Building portfolio website...")

    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape(["html", "xml"])
    )

    template = env.get_template("base.html")

    html_content = template.render(
        site=SITE,
        about=about,
        experience=experience,
        projects=projects,
        #fellowship=fellowship,
        family=family,
        skills=skills,
        education=education,
        contact=contact,
    )

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("✅ Site built successfully!")
    print("📄 index.html is ready in the root")
    print("🌐 Preview: python -m http.server 8000")


if __name__ == "__main__":
    build_site()
    