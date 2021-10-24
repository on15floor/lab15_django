import markdown


def get_markdown(file_name):
    data_file = f'main/static/main/docs/{file_name}.md'
    with open(data_file) as f:
        return markdown.markdown(f.read())
