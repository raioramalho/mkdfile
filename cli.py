import click
from generators import node, python, nginx, go

IMAGES = {
    "node": node.generate,
    "python": python.generate,
    "nginx": nginx.generate,
    "go": go.generate,
}

@click.command()
@click.option("--image", type=click.Choice(IMAGES.keys()), required=True, help="Base image")
@click.option("--multistage", is_flag=True, help="Use multistage build")
@click.option("--output", default="Dockerfile", help="Output path")
def main(image, multistage, output):
    content = IMAGES[image](multistage=multistage)
    with open(output, "w") as f:
        f.write(content)
    click.echo(f"Dockerfile generated at {output}")

if __name__ == "__main__":
    main()
