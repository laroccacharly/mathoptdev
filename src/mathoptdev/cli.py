import click

@click.group()
def cli():
    pass


@cli.command()
def hello():
    print("Hello, world!")
