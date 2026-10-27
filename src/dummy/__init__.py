import click

@click.command()
@click.argument('nums',type=int, nargs=-1, help='First number')
@click.option('--mul', is_flag=True, help='Enable multiplication')
def main(nums, mul) -> None:

    """Add list of nums or multiply them if --mul is specified."""
    if mul:
        product = 1
        
        for n in nums:
            product *= n 

        click.echo(product)
    else:
        sum = 0

        for n in nums:
            sum += n 

        click.echo(sum)
