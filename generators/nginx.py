from jinja2 import Environment, FileSystemLoader
from pathlib import Path


def generate(tag: str = "1.25", variant: str = "alpine") -> str:
    """Gera o conteúdo do Dockerfile para Nginx."""

    env = Environment(loader=FileSystemLoader(Path(__file__).parent.parent / "templates"))
    template = env.get_template("nginx.dockerfile.j2")
    runtime_image = f"nginx:{tag}-{variant}" if variant else f"nginx:{tag}"
    return template.render(runtime_image=runtime_image)
