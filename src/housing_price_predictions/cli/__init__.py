import click

@click.group()
@click.version_option()
def root():
    """CLI for running the housing price predictions example."""
    pass

def run():
    root()
