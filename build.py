#!/usr/bin/env python3
"""
build.py
Builds the static portfolio website from content.py + Jinja2 templates.
"""

from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import shutil

# Import all content
from content import (
    SITE,
    about,
    experience,
    projects,
    # fellowship,
    family,
    skills,
    education,
    contact
)


def build_site():
    print("🚀 Building portfolio website...")

    # Create output directory
    output_dir = "dist"
    os.makedirs(output_dir, exist_ok=True)

    # Setup Jinja2 environment
    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape(["html", "xml"])
    )

    # Render the main template (we'll create base.html next)
    template = env.get_template("base.html")

    html_content = template.render(
        site=SITE,
        about=about,
        experience=experience,
        projects=projects,
        # fellowship=fellowship,
        family=family,
        skills=skills,
        education=education,
        contact=contact,
    )

    # Write the final index.html
    output_file = os.path.join(output_dir, "index.html")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    # Copy static files (CSS, images, etc.)
    static_src = "static"
    static_dst = os.path.join(output_dir, "static")

    if os.path.exists(static_src):
        if os.path.exists(static_dst):
            shutil.rmtree(static_dst)
        shutil.copytree(static_src, static_dst)
        print("📁 Copied static assets")

    print(f"✅ Site built successfully!")
    print(f"📄 Open: {output_file}")
    print(f"🌐 Preview locally: python -m http.server 8000 --directory {output_dir}")


if __name__ == "__main__":
    build_site()
    
    