import click


@click.group(short_help="graspos CLI.")
def graspos():
    """graspos CLI.
    """
    pass


@graspos.command()
@click.argument("name", default="graspos")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [graspos]
