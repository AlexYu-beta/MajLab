from flask import Markup
import markdown


def md2html(filename):
    """
    https://blog.csdn.net/wangchao8110/article/details/85221568
    :param filename:
    :return:
    """
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.tables',
            'markdown.extensions.toc']
    mdcontent = ""
    with open(filename, 'r', encoding='utf-8') as f:
        mdcontent = f.read()
        pass
    html = markdown.markdown(mdcontent, extensions=exts)
    content = Markup(html)
    return content