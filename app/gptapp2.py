# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 00:41:30 2023

@author: Steve
"""

import streamlit as st
from pathlib import Path
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"

# --- GENERAL SETTINGS ---
st.set_page_config(page_title="Digital CV", page_icon=":wave:")

# Page 1: User Input
st.header("Page 1: User Input")

# User Input: Personal Information
name = st.text_input("Full Name")
description = st.text_area("Description", height=3)
email = st.text_input("Email")
linkedin = st.text_input("LinkedIn Profile (Optional)")

# User Input: Social Media Links
st.subheader("Social Media Links")
social_media = {}
for platform in ["YouTube", "LinkedIn", "GitHub", "Twitter"]:
    link = st.text_input(platform)
    if link:
        social_media[platform] = link

# User Input: Projects & Accomplishments
st.subheader("Projects & Accomplishments")
projects = {}
project_count = st.number_input("Number of Projects", min_value=1, max_value=10, step=1)
for i in range(project_count):
    project_name = st.text_input(f"Project {i + 1} Name")
    project_link = st.text_input(f"Project {i + 1} Link")
    if project_name and project_link:
        projects[project_name] = project_link
        

# User Input: Experience & Qualifications
st.header("Experience & Qualifications")
experience_qualifications = st.text_area("Enter your experience and qualifications, one per line")
experience_qualifications_list = [entry.strip() for entry in experience_qualifications.split('\n') if entry]

# User Input: Hard Skills
st.header("Hard Skills")
hard_skills = st.text_area("Enter your hard skills, one per line")
hard_skills_list = [skill.strip() for skill in hard_skills.split('\n') if skill]

#User Input: Work History
st.header("Work History")
work_history = st.text_area("Enter your work history, in brief")
work_history_list = [workh.strip() for workh in work_history.split('\n') if workh]


# "Build My Resume" Button
if st.button("Build My Resume"):
    show_resume = True

# Page 2: Display Resume
if show_resume:
    st.header("Page 2: Your Resume")

    # Load CSS, PDF, and Profile Picture
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)

    # Display the Digital Resume
    st.image(profile_pic, width=230)

    st.title(name)
    st.write(description)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", email)

    # Display Social Media Links
    st.write('\n')
    st.subheader("Social Media Links")
    for platform, link in social_media.items():
        st.write(f"[{platform}]({link})")

    

    # Display Experience & Qualifications
    st.write('\n')
    st.subheader("Experience & Qualifications")
    for entry in experience_qualifications_list:
        st.write(f"- {entry}")

    # Display Hard Skills
    st.write('\n')
    st.subheader("Hard Skills")
    for skill in hard_skills_list:
        st.write(f"- {skill}")

    # Display Work History
    st.write('\n')
    st.subheader("Work History")
    for workh in work_history_list:
        st.write(f"- {workh}")

    # Display projects and accomplishments
    st.write('\n')
    st.subheader("Projects & Accomplishments")
    st.write("---")
    for project, link in projects.items():
        st.write(f"[{project}]({link})")

    st.write('\n')


