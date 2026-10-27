import click

# FDecorrator
@click.command()
@click.argument('nums',type=float, required=True, nargs=-1, help='numbers')
@click.option('--op',type=click.Choice(['sum', 'mul',"min","max"]), default='sum', help='Operation to perform')

def main(nums, op) -> None:

    """Apply operation to numbers."""

    match(op):
        case 'sum':
            result = sum(nums)
        case 'mul':
            result = 1
            for num in nums:
                result *= num
        case 'min':
            result = min(nums)
        case 'max':
            result = max(nums)

    if int(result) == result:
        result = int(result)
        
    click.echo(result)

