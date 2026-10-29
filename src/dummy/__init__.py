import pathlib

import click
import outputfile


# FDecorrator
@click.command()
@click.argument("nums", type=float, required=True, nargs=-1, help="numbers")
@click.option("--mul", "ml", is_flag=True, default=False, help="Multiply numbers")
@click.option("--min", "mn", is_flag=True, default=False, help="Find minimum")
@click.option("--max", "mx", is_flag=True, default=False, help="Find maximum")
@click.option(
    "--file",
    "dest",
    type=click.Path(exists=False, file_okay=True, dir_okay=False, writable=True, path_type=pathlib.Path),
    default=None,
    help="Result Destination",
)
def main(nums, ml, mn, mx, dest) -> None:
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

    # write to file if specified

    if dest:
        dest.parent.mkdir(parents=True, exist_ok=True)

        with outputfile.open_(dest, "w") as f:
            f.write(str(result))

    else:
        click.echo(result)
