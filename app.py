import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="My Resume"
)

# Biodata
with st.container(border=True, height=400):
 col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
 with col1:
    st.image("img\profile_image.jpeg", width=230)
    with col2:
       st.title("NAQIYA MUTMAINNAH")
       st.write("Data Scientist")
       st.write("Working at Machine Learning, Data, Web Development, and many more.")




# Education
st.write("\n")
st.subheader("EDUCATION")
with st.container(border=True, height=100):
    st.write(
        """
        - Universitas Sebelas Maret | Informatics
        GPA 3.6/4.0
        Worked on the final project with the title "Automatic Essay Grading Answers Using ROUGE Summary Evaluation in Indonesian Language"
        """
    )

# Pengalaman Kerja dan Organisasi
st.write("\n")
st.subheader("EXPERIENCE AND ORGANIZATION")
with st.container(border=True, height=550):
    st.write(
        """
        Software Engineer Intern | Sebelas Maret University (Sep 2022 - Dec 2022)
        - 16 weeks internship on ERP project for school cloud based. Develop new software features, modules, and integrations with existing stack using golang, docker, databases (PostgreSQL), collaborate with trello and git.
        - Wrote efficient code to improve the scenario-based performance of the application.
        - Conducted code reviews to ensure that the code meets company standards.
        - Assisted in the development, implementation, and maintenance of new software solutions.
        \n
        Assistant Lecturer of Computer Network | Sebelas Maret University (Mar 2022 - Aug 2022)
        - Prepared learning materials and made learning videos according to the syllabus.
        - Corrected and graded student project assignments as an assessment of student practicum.
        \n
        Head of Media Department | SKI FMIPA UNS (Jul 2021 - Jan 2022)
        - Collected Organize social media SKI FMIPA UNS as a media publication to disseminate information related to the organization.
        - Activated social media SKI FMIPA on Instagram @skifmipauns to gain more attention and increased the number of followers.
        - Directed and produced a team in making creative graphic design posts on social media.
        - Led and coordinated division members to carry out work programs.
        """
    )

# Pengalaman Pelatihan
st.write("\n")
st.subheader("CAREER TRAINING")
with st.container(border=True, height=300):
    st.write(
        """
        Data Scientist | Sanbercampus (April 2024 - Present)
        \n
        Machine Learning Path | Bangkit Academy 2022 by Google, GoTo, Traveloka (Feb 2022 - Aug 2022)
        - Bangkit is a Google-led academy designed to produce high-caliber technical talent for world-class Indonesia technology companies and startups.
        - Master the key concepts and applications of Al to solve a wide range of ML problems.
        - Received 5 certificates related to Machine Learning through Coursera.
        - Worked on a Product-Based Capstone Project, “BantuAku” the mentoring Application, which is used to help develop small businesses with targeted solutions.
        """
    )

# SKILLS
st.write("\n")
st.subheader("SKILLS")
with st.container(border=True, height=200):
    st.write(
        """
        - Python (Tensorflow, Scikit-learn, Pandas)
        - SQL
        - Power BI
        - Machine Learning and AI Modelling
        - Project Management (Scrum, Agile)
        """
    )