import click
from generators import node as node_gen
from generators import python as py_gen
from generators import nginx as nginx_gen
from generators import go as go_gen
import inspect
import urllib.request
import json


@click.group(help="mkdfile - Gerador de Dockerfile")
def cli():
    """Ferramenta de linha de comando para gerar arquivos Dockerfile."""
    pass


@cli.command(help="Listar versões disponíveis do mkdfile")
def versions():
    """Exibe as tags do repositório no GitHub."""
    try:
        with urllib.request.urlopen(
            "https://api.github.com/repos/raioramalho/mkdfile/tags", timeout=5
        ) as resp:
            tags = json.load(resp)
        for tag in tags:
            click.echo(tag["name"])
    except Exception as exc:
        click.echo(f"Erro ao obter versões: {exc}", err=True)


@cli.command(help="Gerar Dockerfile para projetos Node.js")
@click.option("--tag", default="18", show_default=True, help="Vers\u00e3o do Node.js")
@click.option(
    "--variant",
    default=None,
    help="Variante da imagem como 'alpine' ou 'slim'",
)
@click.option("--multistage", is_flag=True, help="Usar build multistage")
@click.option("--output", default="Dockerfile", show_default=True, help="Caminho do arquivo gerado")
def node(tag, variant, multistage, output):
    """Gera Dockerfile para Node.js."""
    content = node_gen.generate(multistage=multistage, tag=tag, variant=variant)
    with open(output, "w") as f:
        f.write(content)
    click.echo(f"Dockerfile gerado em {output}")


def _simple_command(generator, help_msg, name, default_tag=None, default_variant=None):
    @cli.command(name=name, help=help_msg)
    @click.option("--tag", default=default_tag, show_default=default_tag is not None, help="Versão da imagem base")
    @click.option("--variant", default=default_variant, show_default=default_variant is not None, help="Variante da imagem")
    @click.option("--multistage", is_flag=True, help="Usar build multistage")
    @click.option(
        "--output",
        default="Dockerfile",
        show_default=True,
        help="Caminho do arquivo gerado",
    )
    def command(tag, variant, multistage, output):
        kwargs = {}
        sig = inspect.signature(generator)
        if "multistage" in sig.parameters:
            kwargs["multistage"] = multistage
        if "tag" in sig.parameters:
            kwargs["tag"] = tag
        if "variant" in sig.parameters:
            kwargs["variant"] = variant

        content = generator(**kwargs)
        with open(output, "w") as f:
            f.write(content)
        click.echo(f"Dockerfile gerado em {output}")

    return command


python = _simple_command(
    py_gen.generate,
    "Gerar Dockerfile para projetos Python",
    "python",
    default_tag="3.11",
    default_variant="slim",
)
nginx = _simple_command(
    nginx_gen.generate,
    "Gerar Dockerfile para projetos Nginx",
    "nginx",
    default_tag="1.25",
    default_variant="alpine",
)
go = _simple_command(
    go_gen.generate,
    "Gerar Dockerfile para projetos Go",
    "go",
    default_tag="1.20",
    default_variant="alpine",
)


if __name__ == "__main__":
    cli()
