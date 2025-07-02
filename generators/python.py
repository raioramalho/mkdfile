from jinja2 import Environment, FileSystemLoader
from pathlib import Path

def generate(multistage: bool = False, tag: str = "3.11", variant: str = "slim") -> str:
    """Gera o conteúdo do Dockerfile para projetos Python."""

    env = Environment(loader=FileSystemLoader(Path(__file__).parent.parent / "templates"))
    template = env.get_template("python.dockerfile.j2")
    builder_image = f"python:{tag}-{variant}"
    runtime_image = builder_image
    return template.render(multistage=multistage, builder_image=builder_image, runtime_image=runtime_image)
