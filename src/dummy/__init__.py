import click

@click.command()
@click.argument('num-a',type=int, help='First number')
@click.argument('num-b', type=int,help='Second number')
@click.option('--mul', is_flag=True, help='Enable multiplication')
def main(num_a, num_b, mul) -> None:

    if mul:
        click.echo(num_a * num_b)
    else:
        click.echo(num_a + num_b)
