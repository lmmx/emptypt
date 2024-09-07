import subprocess
from inline_snapshot import snapshot


def run_cli(*command):
    result = subprocess.run(command, text=True, capture_output=True)
    return result.stdout.strip(), result.stderr.strip()


# Tests for emptypt-m-* CLIs
def test_emptypt_m_argh():
    run_cli("emptypt-m-argh") == snapshot(("", "[]"))
    run_cli("emptypt-m-argh", "--help") == snapshot(
        (
            """\
usage: emptypt-m-argh [-h] [-i] [-f] [-q] [-d] [-u]

Configure input filtering and output display.

options:
  -h, --help          show this help message and exit
  -i, --io-arg1       Example IO flag (type: bool, default: False)
  -f, --filter-arg1   Example filter flag (type: bool, default: False)
  -q, --quiet         Run silently (type: bool, default: False)
  -d, --debug         Run debug diagnostics (type: bool, default: False)
  -u, --undocumented  (type: bool, default: False)\
""",
            "",
        )
    )


def test_emptypt_m_argh_docstr():
    run_cli("emptypt-m-argh-docstr") == snapshot(("", "[]"))
    run_cli("emptypt-m-argh-docstr", "--help") == snapshot(
        (
            """\
usage: emptypt-m-argh-docstr [-h] [-i] [-f] [-q] [-d] [-u]

Configure input filtering and output display.

options:
  -h, --help          show this help message and exit
  -i, --io-arg1       Example IO flag with a description that can go on and
                      become split over multiple lines in the docstring.
                      (type: bool, default: False)
  -f, --filter-arg1   Example filter flag (type: bool, default: False)
  -q, --quiet         Run silently (type: bool, default: False)
  -d, --debug         Run debug diagnostics (type: bool, default: False)
  -u, --undocumented  (type: bool, default: False)\
""",
            "",
        )
    )


def test_emptypt_m_click():
    run_cli("emptypt-m-click") == snapshot(("", ""))
    run_cli("emptypt-m-click", "--help") == snapshot(
        (
            """\
Usage: emptypt-m-click [OPTIONS]

Options:
  --io_arg1      The first IO configuration entry.
  --filter_arg1  The first filtering configuration entry.
  --quiet        Whether to suppress console output.
  --debug        Whether to run debug diagnostics.
  -h, --help     Show this message and exit.\
""",
            "",
        )
    )


def test_emptypt_m_defopt():
    run_cli("emptypt-m-defopt") == snapshot(("", "[]"))
    run_cli("emptypt-m-defopt", "--help") == snapshot(
        (
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
""",
            "",
        )
    )


def test_emptypt_minimum():
    run_cli("emptypt-minimum") == snapshot(("", "[]"))
    run_cli("emptypt-minimum", "--help") == snapshot(("", "[]"))


def test_emptypt_simple():
    run_cli("emptypt-simple") == snapshot(("", "[]"))
    run_cli("emptypt-simple", "--help") == snapshot(("", "[]"))


# Tests for emptypt-p-* CLIs
def test_emptypt_p_argh():
    run_cli("emptypt-p-argh") == snapshot(("", "[]"))
    run_cli("emptypt-p-argh", "--help") == snapshot(
        (
            """\
usage: emptypt-p-argh [-h] [-i] [-f] [-q] [-d] [-u]

Configure input filtering and output display.

options:
  -h, --help          show this help message and exit
  -i, --io-arg1       Example IO flag (type: bool, default: False)
  -f, --filter-arg1   Example filter flag (type: bool, default: False)
  -q, --quiet         Run silently (type: bool, default: False)
  -d, --debug         Run debug diagnostics (type: bool, default: False)
  -u, --undocumented  (type: bool, default: False)\
""",
            "",
        )
    )


def test_emptypt_p_argh_docstr():
    run_cli("emptypt-p-argh-docstr") == snapshot(("", "[]"))
    run_cli("emptypt-p-argh-docstr", "--help") == snapshot(
        (
            """\
usage: emptypt-p-argh-docstr [-h] [-i] [-f] [-q] [-d] [-u]

Configure input filtering and output display.

options:
  -h, --help          show this help message and exit
  -i, --io-arg1       Example IO flag with a description that can go on and
                      become split over multiple lines in the docstring.
                      (type: bool, default: False)
  -f, --filter-arg1   Example filter flag (type: bool, default: False)
  -q, --quiet         Run silently (type: bool, default: False)
  -d, --debug         Run debug diagnostics (type: bool, default: False)
  -u, --undocumented  (type: bool, default: False)\
""",
            "",
        )
    )


def test_emptypt_p_click():
    run_cli("emptypt-p-click") == snapshot(("", ""))
    run_cli("emptypt-p-click", "--help") == snapshot(
        (
            """\
Usage: emptypt-p-click [OPTIONS]

Options:
  --io_arg1      The first IO configuration entry.
  --filter_arg1  The first filtering configuration entry.
  --quiet        Whether to suppress console output.
  --debug        Whether to run debug diagnostics.
  -h, --help     Show this message and exit.\
""",
            "",
        )
    )


def test_emptypt_p_defopt():
    run_cli("emptypt-p-defopt") == snapshot(("", "[]"))
    run_cli("emptypt-p-defopt", "--help") == snapshot(
        (
            """\
usage: emptypt-p-defopt [-h] [-i] [-f] [-q] [-d] [-u]

Configure input filtering and output display.

options:
  -h, --help          show this help message and exit
  -i, --io-arg1       (default: False)
  -f, --filter-arg1   (default: False)
  -q, --quiet         (default: False)
  -d, --debug         (default: False)
  -u, --undocumented  (default: False)\
""",
            "",
        )
    )
