# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 20:29:13 2023

@author: Steve
"""
import streamlit as st
from pathlib import Path
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"



css_file = current_dir / "styles" / "main.css"
if st.session_state.show_resume:
   

    # Load CSS, PDF, and Profile Picture
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)

    # Display the Digital Resume
    st.image(profile_pic, width=230)

    st.title(st.session_state["name"])
    st.write(st.session_state["description"])
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", st.session_state["email"])

    # Display Social Media Links
    st.write('\n')
    st.subheader("Social Media Links")
    smedia = st.session_state["social_media"]
    for platform, link in smedia.items():
        st.write(f"[{platform}]({link})")

    # Display Experience & Qualifications
    st.write('\n')
    st.subheader("Experience & Qualifications")
    exp_qua = st.session_state["experience_qualifications_list"]
    for entry in exp_qua:
        st.write(f"- {entry}")

    # Display Hard Skills
    st.write('\n')
    st.subheader("Hard Skills")
    ha_sk = st.session_state["hard_skills_list"]
    for skill in ha_sk:
        st.write(f"- {skill}")

    # Display Work History
    st.write('\n')
    st.subheader("Work History")
    work_hi = st.session_state["work_history_list"]
    for workh in work_hi:
        st.write(f"- {workh}")

    # Display projects and accomplishments
    st.write('\n')
    st.subheader("Projects & Accomplishments")
    st.write("---")
    proj = st.session_state["projects"]
    for project, link in proj.items():
        st.write(f"[{project}]({link})")

    st.write('\n')

    
    