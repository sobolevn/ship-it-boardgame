import shutil
import logging
from typing import Final

import yaml
import requests
from jinja2 import Environment, FileSystemLoader, select_autoescape

logging.basicConfig(
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Add your language folder below when it's ready to be rendered
LANGUAGE_FOLDERS: Final = {'ru'}


def render_schemas(language: str) -> None:
    logger.info('[%s] rendering language', language)

    with open(f'{language}/schemas-info.yml') as f:
        info = yaml.safe_load(f)

    for template_name in env.list_templates():
        logger.info('[%s] rendering template "%s"', language, template_name)

        rendered = env.get_template(template_name).render(**info)

        logger.info('[%s] generating schema image from template', language)
        response = requests.post(
            'http://image-export:8000/',
            json={'format': 'jpg', 'xml': rendered},
            stream=True,
        )
        assert response.status_code == 200, response.text

        image_name, *_ = template_name.split('.')
        logger.info('[%s] saving image %s.jpg', language, image_name)
        with open(f'{language}/schemas/{image_name}.jpg', 'wb') as f:
            shutil.copyfileobj(response.raw, f)


if __name__ == '__main__':
    env = Environment(
        loader=FileSystemLoader('ru/schema-sources'),
        autoescape=select_autoescape(),
    )

    for language in LANGUAGE_FOLDERS:
        render_schemas(language)
