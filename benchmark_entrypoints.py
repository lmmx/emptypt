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


def sort_and_rank_results(results):
    """Sort the results based on execution time and add rank column to each row."""
    sorted_results = sorted(results, key=lambda x: float(x[1].rstrip("s")))
    ranked_results = [[i + 1] + result for i, result in enumerate(sorted_results)]
    return ranked_results


def benchmark_entrypoints():
    configurations = [
        ("Stdlib [baseline], minimum", "emptypt-minimum", False),
        ("Stdlib [baseline], simple", "emptypt-simple", False),
        ("msgspec + argh", "emptypt-m-argh", True),
        ("msgspec + argh (docstring)", "emptypt-m-argh-docstr", True),
        ("msgspec + click", "emptypt-m-click", False),
        ("msgspec + typer", "emptypt-m-typer", False),
        ("msgspec + defopt", "emptypt-m-defopt", True),
        ("pydantic + argh", "emptypt-p-argh", True),
        ("pydantic + argh (docstring)", "emptypt-p-argh-docstr", True),
        ("pydantic + click", "emptypt-p-click", False),
        ("pydantic + typer", "emptypt-p-typer", False),
        ("pydantic + defopt", "emptypt-p-defopt", True),
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
            ],
        )

    headers = [
        "Rank",
        "Configuration",
        "Execution Time",
        "entrypoint",
        "Autogenerate from config",
    ]
    table = tabulate(
        sort_and_rank_results(results),
        headers=headers,
        tablefmt="pipe",
        colalign=("left", "right", "left", "center"),
    )

    print(table)


if __name__ == "__main__":
    benchmark_entrypoints()
