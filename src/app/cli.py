import typer
from .main import app

client = app.test_client()

cli = typer.Typer()

@cli.command()
def health():
    response = client.get("/health")
    typer.echo(response.json())

if __name__ == "__main__":
    cli()
