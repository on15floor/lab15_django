import os.path

import markdown
from django.templatetags.static import static
from django.conf import settings


def get_markdown(file_name):
    data_file = static(f'main/static/main/docs/{file_name}.md')
    data_file = os.path.join(settings.BASE_DIR, 'main/static/main/docs', f'{file_name}.md')
    print(data_file)
    with open(data_file) as f:
        return markdown.markdown(f.read())
