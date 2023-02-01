import yaml
from pytest_cookies.plugin import Cookies

from .helper import generate_cookiecutter_context


def test_create_project(cookies: Cookies):
    result = cookies.bake()
    assert not result.exception

    assert result.project_path.joinpath('.editorconfig').exists()


def test_bake_vuex(cookies: Cookies):
    context = generate_cookiecutter_context()

    context['with_vuex'] = 'yes'
    result = cookies.bake(extra_context=context)
    assert not result.exception

    assert result.project_path.joinpath('src/store/index.ts').exists()

    context['with_vuex'] = 'no'
    result = cookies.bake(extra_context=context)
    assert not result.exception

    assert not result.project_path.joinpath('src/store').exists()


def test_bake_nvmrc(cookies: Cookies):
    context = generate_cookiecutter_context()

    result = cookies.bake(extra_context=context)
    assert not result.exception

    assert result.project_path.joinpath('.nvmrc').read_text(encoding='utf-8').strip() == context['node_version']


def test_bake_docker_compose(cookies: Cookies):
    context = generate_cookiecutter_context()
    result = cookies.bake(extra_context=context)
    assert not result.exception

    with result.project_path.joinpath('docker-compose.yml').open('r', encoding='utf-8') as fp:
        docker_compose = yaml.load(fp, Loader=yaml.Loader)

    assert docker_compose['services']['web']['image'] == context['project_slug']
    assert docker_compose['services']['web']['build']['args']['NODE_VERSION'] == context['node_version']
    assert docker_compose['services']['web']['ports'][0] == f"{context['docker_port']}:80"
