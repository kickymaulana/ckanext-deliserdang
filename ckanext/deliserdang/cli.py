import click


@click.group(short_help="deliserdang CLI.")
def deliserdang():
    """deliserdang CLI.
    """
    pass


@deliserdang.command()
@click.argument("name", default="deliserdang")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [deliserdang]
