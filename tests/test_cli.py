from dummy import main
from click.testing import CliRunner

def test_sum():
    runner = CliRunner()
    result = runner.invoke(main, ['1', '2', '3'])
    assert result.exit_code == 0
    assert result.output.strip() == '6'

def test_mul():
    runner = CliRunner()
    result = runner.invoke(main, ['1', '2', '3', '--mul'])
    assert result.exit_code == 0
    assert result.output.strip() == '6'

def test_no_args_sum():
    runner = CliRunner()
    result = runner.invoke(main, [])
    assert result.exit_code == 0
    assert result.output.strip() == '0'

def test_no_args_mul():
    runner = CliRunner()
    result = runner.invoke(main, ['--mul'])
    assert result.exit_code == 0
    assert result.output.strip() == '1'

def test_invalid_args_sum():
    runner = CliRunner()
    result = runner.invoke(main, ['a', 'b', 'c'])
    assert result.exit_code == 2
    assert 'Error' in result.output

def test_invalid_args_mul():
    runner = CliRunner()
    result = runner.invoke(main, ['a', 'b', 'c', '--mul'])
    assert result.exit_code == 2
    assert 'Error' in result.output

def test_invalid_ops():
    runner = CliRunner()
    result = runner.invoke(main, ['1', '2', '3', "--invalid"])
    assert result.exit_code == 2
    assert 'Error' in result.output

def test_invalid_str():
    runner = CliRunner()
    result = runner.invoke(main, ['1', '2', '3', "4 5"])
    assert result.exit_code == 2
    assert 'Error' in result.output