from string import Template

"""
Example:
![sem-1](https://img.shields.io/static/v1?label=University%20Work&message=SEMESTER%2001&style=for-the-badge&logo=Microsoft%20OneNote&link=http://left&link=http://right&logoColor=violet&logoWidth=20&color=fb4934&labelColor=1d2021)
"""

UNIVERSITY_WORK_TEMPLATE = Template(
    "![sem-$sem_no](https://img.shields.io/static/v1?label=University%20Work&message=SEMESTER%20$sem_no&style=for-the-badge&logo=Microsoft%20OneNote&link=$link&link=$link&logoColor=violet&logoWidth=20&color=$color&labelColor=$label_color)"
)

GRUVBOX_COLORS = ['fb4934', 'b8bb26', 'fabd2f',
                  '83a598', 'd3869b', '8ec07c', 'fe8019', 'ebdbb2']

UNIVERSITY_WORK_URL_TEMPLATE = Template(
    "http://github.com/satyajitghana/University-Work-SEM-$sem_no"
)

HEADER = "# University Work\n\n"


def gen_university_work():
    sem_nos = [1, 2, 3, 4, 5, 6]

    md_file = open('university-work.md', 'w+')

    semesters_texts = [UNIVERSITY_WORK_TEMPLATE.substitute(sem_no=f'{no:02}', link=UNIVERSITY_WORK_URL_TEMPLATE.substitute(
        sem_no=f'{no:02}'), color=color, label_color='1d2021') + '\n\n' for no, color in zip(sem_nos, GRUVBOX_COLORS)]

    md_file.writelines([HEADER] + semesters_texts)

    md_file.close()


gen_university_work()
