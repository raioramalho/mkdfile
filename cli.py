import click
from generators import node as node_gen
from generators import python as py_gen
from generators import nginx as nginx_gen
from generators import go as go_gen


@click.group(help="mkdfile - Gerador de Dockerfile")
def cli():
    """Ferramenta de linha de comando para gerar arquivos Dockerfile."""
    pass


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


def _simple_command(generator, help_msg, name):
    @cli.command(name=name, help=help_msg)
    @click.option("--multistage", is_flag=True, help="Usar build multistage")
    @click.option(
        "--output",
        default="Dockerfile",
        show_default=True,
        help="Caminho do arquivo gerado",
    )
    def command(multistage, output):
        content = generator(multistage=multistage)
        with open(output, "w") as f:
            f.write(content)
        click.echo(f"Dockerfile gerado em {output}")

    return command


python = _simple_command(py_gen.generate, "Gerar Dockerfile para projetos Python", "python")
nginx = _simple_command(nginx_gen.generate, "Gerar Dockerfile para projetos Nginx", "nginx")
go = _simple_command(go_gen.generate, "Gerar Dockerfile para projetos Go", "go")


if __name__ == "__main__":
    cli()
