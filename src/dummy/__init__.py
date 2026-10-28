import click


# FDecorrator
@click.command()
@click.argument("nums", type=float, required=True, nargs=-1, help="numbers")
@click.option("--ml", is_flag=True, default=False, help="Multiply numbers")
@click.option("--mn", is_flag=True, default=False, help="Find minimum")
@click.option("--mx", is_flag=True, default=False, help="Find maximum")
def main(nums, ml, mn, mx) -> None:
    """
    Apply operation to numbers. Adds by Default.

    """

    # opcode validation
    if sum([ml, mn, mx]) > 1:
        raise click.UsageError("Please specify exactly one operation.")

    # perform operation

    if mx:
        result = max(nums)
    elif mn:
        result = min(nums)
    elif ml:
        result = 1
        for num in nums:
            result *= num
    else:  # add (default)
        result = sum(nums)

    if int(result) == result:
        result = int(result)

    click.echo(result)
