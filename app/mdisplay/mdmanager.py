import os
from flask import render_template
from app.mdisplay.mdisplay import md2html


def mdlist():
    md_dir = os.path.abspath('../../static/mdfile')
    md_list = []
    for root, dirs, files in os.walk(md_dir):
        for file in files:
            md_list.append(file)
    return md_list


def mdisplay(filename):
    if filename not in mdlist():
        return None
    else:
        content = md2html(filename)
        # maybe the file cannot be found, commit first
        return render_template('markdown.html', **locals())


if __name__ == '__main__':
    print(mdlist())
