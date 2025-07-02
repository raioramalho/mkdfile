from jinja2 import Environment, FileSystemLoader
from pathlib import Path

def generate(multistage=False):
    env = Environment(loader=FileSystemLoader(Path(__file__).parent.parent / "templates"))
    template = env.get_template("python.dockerfile.j2")
    return template.render(multistage=multistage)
