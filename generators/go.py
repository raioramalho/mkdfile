from jinja2 import Environment, FileSystemLoader
from pathlib import Path


def generate(
    multistage: bool = False,
    tag: str = "1.20",
    variant: str = "alpine",
) -> str:
    """Gera o conteúdo do Dockerfile para projetos Go."""

    env = Environment(
        loader=FileSystemLoader(Path(__file__).parent.parent / "templates")
    )
    template = env.get_template("go.dockerfile.j2")

    builder_image = f"golang:{tag}-{variant}"
    runtime_image = "alpine:latest" if multistage else builder_image
    return template.render(
        multistage=multistage,
        builder_image=builder_image,
        runtime_image=runtime_image,
    )
