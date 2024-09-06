# emptypt

Template for an entrypoint CLI using msgspec

## Workspace setup

This repo has been refactored as a [uv workspace][uvws] in August 2024.

Each CLI is a standalone package, and there's also a package called `emptypt` (all in the
`msgspec_packages` subdirectory).

To install all CLI packages (each of which exposes entrypoints in its `pyproject.toml`
project scripts section) and therefore to obtain all CLI commands, run:

```sh
uv pip install .
```

[uvws]: https://docs.astral.sh/uv/concepts/workspaces/

## Timing Benchmarks

Desktop (3.7 GHz, max. 5.3 GHz, 20 cores)

| Configuration              |   Execution Time | entrypoint      |  Autogenerate from config  |
|:---------------------------|-----------------:|:----------------|:--------------------------:|
| Stdlib [baseline]          |           0.014s | emptypt-minimum |             -              |
| msgspec                    |           0.014s | emptypt-simple  |             -              |
| msgspec + argh (docstring) |           0.054s | emptypt-argh    |            Yes             |
| msgspec + click            |           0.067s | emptypt-click   |             -              |
| msgspec + typer            |           0.088s | emptypt-typer   |             -              |
| msgspec + defopt           |           0.162s | emptypt-defopt  |            Yes             |

Laptop: ThinkPad P14s (2.2 GHz, max. 5 GHz, 16 cores)

| Configuration              |   Execution Time | entrypoint      |  Autogenerate from config  |
|:---------------------------|-----------------:|:----------------|:--------------------------:|
| Stdlib [baseline]          |           0.018s | emptypt-minimum |             -              |
| msgspec                    |           0.018s | emptypt-simple  |             -              |
| msgspec + argh (docstring) |           0.066s | emptypt-argh    |            Yes             |
| msgspec + click            |           0.077s | emptypt-click   |             -              |
| msgspec + typer            |           0.236s | emptypt-typer   |             -              |
| msgspec + defopt           |           0.176s | emptypt-defopt  |            Yes             |

Laptop: GPD Win Max 2 2023 (3.3 GHz, max. 5.1 GHz)

| Configuration              |   Execution Time | entrypoint      |  Autogenerate from config  |
|:---------------------------|-----------------:|:----------------|:--------------------------:|
| Stdlib [baseline]          |           0.020s | emptypt-minimum |             -              |
| msgspec                    |           0.021s | emptypt-simple  |             -              |
| msgspec + argh (docstring) |           0.109s | emptypt-argh    |            Yes             |
| msgspec + click            |           0.124s | emptypt-click   |             -              |
| msgspec + typer            |           0.411s | emptypt-typer   |             -              |
| msgspec + defopt           |           0.234s | emptypt-defopt  |            Yes             |

Laptop: Lenovo IdeaPad Flex 3 (1.1 GHz, max. 3.1 GHz)

| Configuration              |   Execution Time | entrypoint      |  Autogenerate from config  |
|:---------------------------|-----------------:|:----------------|:--------------------------:|
| Stdlib [baseline]          |           0.036s | emptypt-minimum |             -              |
| msgspec                    |           0.038s | emptypt-simple  |             -              |
| msgspec + argh (docstring) |           0.147s | emptypt-argh    |            Yes             |
| msgspec + click            |           0.183s | emptypt-click   |             -              |
| msgspec + typer            |           0.242s | emptypt-typer   |             -              |
| msgspec + defopt           |           0.454s | emptypt-defopt  |            Yes             |

## Details

- `argh.dispatch_command` autogenerates nice simple CLIs from `msgspec.Struct`s, very fast
- `click` can't annotate classes and requires doubling the documentation of config fields as CLI flags
- `typer.run` exits early and the decorator didn't get invoked in the entrypoint (fail)
- `defopt.run` autogenerates nice CLIs from Pydantic models but the ones for msgspec Structs
  interpret all fields as positional CLI args by default

## Example usage

The `argh` CLI reads flag type hints and descriptions from `msgspec.Struct` field metadata.

```
usage: emptypt-argh [-h] [-i] [-f] [-q] [-d] [-u]

Configure input filtering and output display.

options:
  -h, --help          show this help message and exit
  -i, --io-arg1       Example IO flag (type: bool, default: False)
  -f, --filter-arg1   Example filter flag (type: bool, default: False)
  -q, --quiet         Run silently (type: bool, default: False)
  -d, --debug         Run debug diagnostics (type: bool, default: False)
  -u, --undocumented  (type: bool, default: False)
```

The 2nd `argh` CLI (docstring variant) handles field descriptions from the class docstring, like defopt.
This is a more scalable way to write field descriptions.

```
usage: emptypt-argh-docstr [-h] [-i] [-f] [-q] [-d] [-u]

Configure input filtering and output display.

options:
  -h, --help          show this help message and exit
  -i, --io-arg1       Example IO flag with a description that can go on and
                      become split over multiple lines in the docstring.
                      (type: bool, default: False)
  -f, --filter-arg1   Example filter flag (type: bool, default: False)
  -q, --quiet         Run silently (type: bool, default: False)
  -d, --debug         Run debug diagnostics (type: bool, default: False)
  -u, --undocumented  (type: bool, default: False)
```
