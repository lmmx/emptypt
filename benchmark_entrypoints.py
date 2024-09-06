import subprocess
import time

from tabulate import tabulate


def run_command(command):
    start_time = time.time()
    subprocess.run(
        command,
        shell=True,
        # check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    end_time = time.time()
    return end_time - start_time


def benchmark_entrypoints():
    configurations = [
        ("Stdlib [baseline]", "emptypt-m-minimum", False),
        ("msgspec", "emptypt-m-simple", False),
        ("msgspec + argh (docstring)", "emptypt-m-argh", True),
        ("msgspec + click", "emptypt-m-click", False),
        ("msgspec + typer", "emptypt-m-typer", False),
        ("msgspec + defopt", "emptypt-m-defopt", True),
    ]

    results = []

    for config, entrypoint, autogenerate in configurations:
        execution_time = run_command(entrypoint)
        results.append(
            [
                config,
                f"{execution_time:.3f}s",
                entrypoint,
                "Yes" if autogenerate else "-",
            ]
        )

    headers = [
        "Configuration",
        "Execution Time",
        "entrypoint",
        "Autogenerate from config",
    ]
    table = tabulate(
        results,
        headers=headers,
        tablefmt="pipe",
        colalign=("left", "right", "left", "center"),
    )

    print(table)


if __name__ == "__main__":
    benchmark_entrypoints()