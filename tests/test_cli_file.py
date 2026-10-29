from click.testing import CliRunner

from dummy import main


def test_no_file(tmp_path):
    runner = CliRunner()
    output_file = tmp_path / "out"
    result = runner.invoke(main, ["--file", str(output_file), "1", "2", "3"])
    assert result.exit_code == 0
    assert output_file.read_text().strip() == "6"
    assert result.output.strip() == ""


def test_already_file(tmp_path):
    runner = CliRunner()
    output_file = tmp_path / "out"
    output_file.write_text("existing content")
    result = runner.invoke(main, ["--file", str(output_file), "1", "2", "3"])
    assert result.exit_code == 0
    assert output_file.read_text().strip() == "6"
    assert result.output.strip() == ""


def test_no_dir(tmp_path):
    runner = CliRunner()
    output_file = tmp_path / "subdir" / "out"
    result = runner.invoke(main, ["--file", str(output_file), "1", "2", "3"])
    assert result.exit_code == 0
    assert output_file.read_text().strip() == "6"
    assert result.output.strip() == ""


def test_no_dir_recursive(tmp_path):
    runner = CliRunner()
    output_file = tmp_path / "subdir" / "subdir" / "out"
    result = runner.invoke(main, ["--file", str(output_file), "1", "2", "3"])
    assert result.exit_code == 0
    assert output_file.read_text().strip() == "6"
    assert result.output.strip() == ""


def test_timestamp_no_update(tmp_path):
    runner = CliRunner()
    output_file = tmp_path / "out"
    output_file.write_text("existing content")
    runner.invoke(main, ["--file", str(output_file), "1", "2", "3"])
    mtime = output_file.stat().st_mtime
    result = runner.invoke(main, ["--file", str(output_file), "1", "2", "3"])
    assert output_file.stat().st_mtime == mtime
    assert result.exit_code == 0
