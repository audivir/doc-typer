import click
import doctyper


@click.group()
def cli():
    pass


@cli.command()
def initdb():
    click.echo("Initialized the database")


@cli.command()
def dropdb():
    click.echo("Dropped the database")


app = doctyper.Typer()


@app.command()
def sub():
    """
    A single-command Typer sub app
    """
    print("Typer is now below Click, the Click app is the top level")


typer_click_object = doctyper.main.get_command(app)

cli.add_command(typer_click_object, "sub")

if __name__ == "__main__":
    cli()
