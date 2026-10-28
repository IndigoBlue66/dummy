from click.testing import CliRunner

from dummy import main


def test_sum():
    runner = CliRunner()
    result = runner.invoke(main, ["1", "2", "3"])
    assert result.exit_code == 0
    assert result.output.strip() == "6"


def test_mul():
    runner = CliRunner()
    result = runner.invoke(main, ["1", "2", "3", "--ml"])
    assert result.exit_code == 0
    assert result.output.strip() == "6"


def test_min():
    runner = CliRunner()
    result = runner.invoke(main, ["1", "2", "3", "--mn"])
    assert result.exit_code == 0
    assert result.output.strip() == "1"


def test_max():
    runner = CliRunner()
    result = runner.invoke(main, ["1", "2", "3", "--mx"])
    assert result.exit_code == 0
    assert result.output.strip() == "3"


def test_no_args_sum():
    runner = CliRunner()
    result = runner.invoke(main, ["--ml"])
    assert result.exit_code == 2
    assert "Error" in result.output


def test_invalid_op():
    runner = CliRunner()
    result = runner.invoke(main, ["1", "2", "3", "--invalid"])
    assert result.exit_code == 2
    assert "Error" in result.output


def test_multiple_ops():
    runner = CliRunner()
    result = runner.invoke(main, ["1", "2", "3", "--ml", "--mn"])
    assert result.exit_code == 2
    assert "Error" in result.output


def test_invalid_args():
    runner = CliRunner()
    result = runner.invoke(main, ["a", "b", "c"])
    assert result.exit_code == 2
    assert "Error" in result.output


def test_float_args():
    runner = CliRunner()
    result = runner.invoke(main, ["1.5", "2", "3.0"])
    assert result.exit_code == 0
    assert result.output.strip() == "6.5"
