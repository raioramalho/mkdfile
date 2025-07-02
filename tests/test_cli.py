from click.testing import CliRunner
from cli import cli, NODE_TAGS


def test_node_list_tags():
    runner = CliRunner()
    result = runner.invoke(cli, ['node', '--list'])
    assert result.exit_code == 0
    for tag in NODE_TAGS:
        assert tag in result.output


def test_img_list():
    runner = CliRunner()
    result = runner.invoke(cli, ['img', '--list'])
    assert result.exit_code == 0
    for name in ['node', 'python', 'nginx', 'go']:
        assert name in result.output
