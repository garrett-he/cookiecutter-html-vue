import json

from pytest_cookies.plugin import Cookies

from .helper import generate_cookiecutter_context


def test_bake_package_json(cookies: Cookies):
    context = generate_cookiecutter_context()
    result = cookies.bake(extra_context=context)
    assert not result.exception

    with result.project_path.joinpath('package.json').open('r', encoding='utf-8') as fp:
        package_json = json.load(fp)

    assert package_json['name'] == context['project_slug']
    assert package_json['version'] == context['project_version']
    assert package_json['description'] == context['project_description']
    assert package_json['private'] == (context['project_private'] == 'true')
    assert package_json['repository']['url'] == f'git+https://github.com/{context["github_path"]}.git'
    assert package_json['keywords'] == context['project_keywords'].split(',')
    assert package_json['author'] == f'{context["author_name"]} <{context["author_email"]}>'
    assert package_json['license'] == context['license_id']
    assert package_json['bugs']['url'] == f'https://github.com/{context["github_path"]}/issues'
    assert package_json['homepage'] == f'https://github.com/{context["github_path"]}#readme'
