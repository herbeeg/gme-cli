import click

@click.command()
def default():
    click.echo('Welcome to the gme-cli interface. Please state your purpose.')

if '__main__' == __name__:
    """Run default command if no context has been given."""
    default()
