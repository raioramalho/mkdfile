from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from typing import Optional


def generate(
    multistage: bool = False,
    tag: str = "18",
    variant: Optional[str] = None,
) -> str:
    """Gera o conteúdo do Dockerfile para projetos Node.js."""

    env = Environment(
        loader=FileSystemLoader(Path(__file__).parent.parent / "templates")
    )
    template = env.get_template("node.dockerfile.j2")

    builder_image = f"node:{tag}"
    if variant:
        runtime_image = f"node:{tag}-{variant}"
    else:
        runtime_image = f"node:{tag}-slim" if multistage else builder_image

    return template.render(
        multistage=multistage,
        builder_image=builder_image,
        runtime_image=runtime_image,
    )
