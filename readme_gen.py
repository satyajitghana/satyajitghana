import random
import re
from string import Template

"""
Example Shield:
[![sem-1](https://img.shields.io/static/v1?label=University%20Work&message=SEMESTER%2001&style=for-the-badge&logo=Microsoft%20OneNote&link=http://left&link=http://right&logoColor=violet&logoWidth=20&color=fb4934&labelColor=1d2021)](http://link)
"""

"""
Shield Template

Args:
    logo (str): name of the logo refer to https://simpleicons.org/, ex: Github, Microsoft%20OneNote
    label (str): the label text
    label_color (str): the color for the label text, in hex string without the #
    message (str): the message text
    message_color (str): the color for the message text in hex string without the #
    link (str): the link that will be applied on the image, basically the href
"""
SHIELD_TEMPLATE = Template(
    "[![$project_name](https://img.shields.io/static/v1?logo=$logo&logoColor=violet&logoWidth=20&label=$label&labelColor=$label_color&message=$message&color=$message_color&style=for-the-badge)]($link)"
)

"""
Github Respository URL Template

Args:
    repo_name (str): repository name, ex: University-Work-SEM-01
"""
URL_TEMPLATE = Template(
    "https://github.com/satyajitghana/$repo_name"
)

GRUVBOX_COLORS = ['fb4934', 'b8bb26', 'fabd2f',
                  '83a598', 'd3869b', '8ec07c',
                  'fe8019', 'ebdbb2']

GRUVBOX_ADDITIONAL = ['9d0006', '79740e', 'b57614',
                      '076678', '8f3f71', '427b58',
                      'af3a03']


def urlify(s):
    s = re.sub(r'[^\w\s]', '', s)
    s = re.sub(r'\s+', '_', s)

    return s


def gen_university_work():
    md_file = open('university-work.md', 'w+')

    sem_nos = [1, 2, 3, 4, 5, 6]

    university_work_texts = [
        SHIELD_TEMPLATE.substitute(
            project_name=f'sem-{sem_no:02}',
            logo='Microsoft%20OneNote',
            label='University%20Work',
            label_color='1d2021',
            message=f'SEMESTER%20{sem_no:02}',
            message_color=color,
            link=URL_TEMPLATE.substitute(
                repo_name=f'University-Work-SEM{sem_no:02}')
        ) + '\n\n'

        for sem_no, color in zip(sem_nos, GRUVBOX_COLORS)
    ]

    university_projects = ['ruas-lms', 'ProjektZirconium',
                           'ProjektBarium', 'ProjektPlutus']

    projects_text = [
        SHIELD_TEMPLATE.substitute(
            project_name=project_name.lower(),
            logo='Github',
            label='Project',
            label_color='1d2021',
            message=project_name,
            message_color=random.choice(GRUVBOX_COLORS + GRUVBOX_ADDITIONAL),
            link=URL_TEMPLATE.substitute(repo_name=project_name)
        ) + '\n\n'

        for project_name in university_projects
    ]

    md_file.writelines(
        ["# University Work - B.Tech - RUAS\n\n"] +
        ["These are all the Assignments(do check them out) and Lab Records made during my time in RUAS\n\n"] +
        university_work_texts +
        ["## Projects\n\n"] +
        ["I had done a few projects as well, which are showcased here\n\n"] +
        projects_text
    )

    md_file.close()


def gen_cv_deeplearning():
    md_file = open('cv_deeplearning.md', 'w+')

    project_names = [('Course', 'TSAI-DeepVision-EVA4.0'),
                     ('Course', 'TSAI-DeepVision-EVA4.0-Phase-2'),
                     ('Course', 'PadhAI-Course'),
                     ('Project', 'PySodium'),
                     ('Project/ML', 'IndiaGDPPrediction'),
                     ('Hackathon', 'ProjektIodine'),
                     ('Project/CV', 'ProjektCerium')
                     ]

    project_texts = [
        '## ' +
        SHIELD_TEMPLATE.substitute(
            project_name=proj_name.lower(),
            logo='Github',
            label=proj_type,
            label_color='1d2021',
            message=proj_name,
            message_color=random.choice(GRUVBOX_COLORS + GRUVBOX_ADDITIONAL),
            link=URL_TEMPLATE.substitute(repo_name=proj_name)
        ) + '\n\n'

        for proj_type, proj_name in project_names
    ]

    md_file.writelines(
        ["# Deep Learning - Computer Vision - Machine Learning\n\n"] +
        project_texts
    )

    md_file.close()


# generate the files
gen_university_work()
gen_cv_deeplearning()
