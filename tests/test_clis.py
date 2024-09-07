import subprocess
from inline_snapshot import snapshot


def run_cli(command, args=""):
    result = subprocess.run(
        f"{command} {args}", shell=True, text=True, capture_output=True
    )
    return result.stdout.strip()


def test_cli_help(command):
    assert run_cli(command, "--help") == snapshot(
        """\
usage: emptypt-m-defopt [-h]
                        [io_arg1] [filter_arg1] [quiet] [debug] [undocumented]

Configure input filtering and output display.

positional arguments:
  io_arg1       (type: bool, default: False)
  filter_arg1   (type: bool, default: False)
  quiet         (type: bool, default: False)
  debug         (type: bool, default: False)
  undocumented  (type: bool, default: False)

options:
  -h, --help    show this help message and exit\
"""
    )


# Tests for emptypt-m-* CLIs
def test_emptypt_m_argh():
    run_cli("emptypt-m-argh") == snapshot()
    run_cli("emptypt-m-argh", "--help") == snapshot()


def test_emptypt_m_argh_docstr():
    run_cli("emptypt-m-argh-docstr") == snapshot()
    run_cli("emptypt-m-argh-docstr", "--help") == snapshot()


def test_emptypt_m_click():
    run_cli("emptypt-m-click") == snapshot()
    run_cli("emptypt-m-click", "--help") == snapshot()


def test_emptypt_m_defopt():
    run_cli("emptypt-m-defopt") == snapshot()
    run_cli("emptypt-m-defopt", "--help") == snapshot()


def test_emptypt_m_minimum():
    run_cli("emptypt-m-minimum") == snapshot()
    run_cli("emptypt-m-minimum", "--help") == snapshot()


def test_emptypt_m_simple():
    run_cli("emptypt-m-simple") == snapshot()
    run_cli("emptypt-m-simple", "--help") == snapshot()


# Tests for emptypt-p-* CLIs
def test_emptypt_p_argh():
    run_cli("emptypt-p-argh") == snapshot()
    run_cli("emptypt-p-argh", "--help") == snapshot()


def test_emptypt_p_argh_docstr():
    run_cli("emptypt-p-argh-docstr") == snapshot()
    run_cli("emptypt-p-argh-docstr", "--help") == snapshot()


def test_emptypt_p_click():
    run_cli("emptypt-p-click") == snapshot()
    run_cli("emptypt-p-click", "--help") == snapshot()


def test_emptypt_p_defopt():
    run_cli("emptypt-p-defopt") == snapshot()
    run_cli("emptypt-p-defopt", "--help") == snapshot()


def test_emptypt_p_minimum():
    run_cli("emptypt-p-minimum") == snapshot()
    run_cli("emptypt-p-minimum", "--help") == snapshot()


def test_emptypt_p_simple():
    run_cli("emptypt-p-simple") == snapshot()
    run_cli("emptypt-p-simple", "--help") == snapshot()
