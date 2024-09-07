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

| Rank   |               Configuration | Execution Time   |      entrypoint       | Autogenerate from config   |
|:-------|----------------------------:|:-----------------|:---------------------:|:---------------------------|
| 1      |  Stdlib [baseline], minimum | 0.015s           |    emptypt-minimum    | -                          |
| 2      |   Stdlib [baseline], simple | 0.015s           |    emptypt-simple     | -                          |
| 3      |  msgspec + argh (docstring) | 0.059s           | emptypt-m-argh-docstr | Yes                        |
| 4      |              msgspec + argh | 0.060s           |    emptypt-m-argh     | Yes                        |
| 5      |             msgspec + click | 0.072s           |    emptypt-m-click    | -                          |
| 6      |            msgspec + defopt | 0.152s           |   emptypt-m-defopt    | Yes                        |
| 7      |             pydantic + argh | 0.168s           |    emptypt-p-argh     | Yes                        |
| 8      | pydantic + argh (docstring) | 0.169s           | emptypt-p-argh-docstr | Yes                        |
| 9      |            pydantic + click | 0.188s           |    emptypt-p-click    | -                          |
| 10     |           pydantic + defopt | 0.249s           |   emptypt-p-defopt    | Yes                        |

Laptop: ThinkPad P14s (2.2 GHz, max. 5 GHz, 16 cores)

| Rank   |               Configuration | Execution Time   |      entrypoint       | Autogenerate from config   |
|:-------|----------------------------:|:-----------------|:---------------------:|:---------------------------|
| 1      |   Stdlib [baseline], simple | 0.025s           |    emptypt-simple     | -                          |
| 2      |  Stdlib [baseline], minimum | 0.026s           |    emptypt-minimum    | -                          |
| 3      |  msgspec + argh (docstring) | 0.063s           | emptypt-m-argh-docstr | Yes                        |
| 4      |              msgspec + argh | 0.082s           |    emptypt-m-argh     | Yes                        |
| 5      |             msgspec + click | 0.082s           |    emptypt-m-click    | -                          |
| 6      |            msgspec + defopt | 0.169s           |   emptypt-m-defopt    | Yes                        |
| 7      |             pydantic + argh | 0.171s           |    emptypt-p-argh     | Yes                        |
| 8      | pydantic + argh (docstring) | 0.171s           | emptypt-p-argh-docstr | Yes                        |
| 9      |            pydantic + click | 0.200s           |    emptypt-p-click    | -                          |
| 10     |           pydantic + defopt | 0.267s           |   emptypt-p-defopt    | Yes                        |

Laptop: GPD Win Max 2 2023 (3.3 GHz, max. 5.1 GHz)

| Rank   |               Configuration | Execution Time   |      entrypoint       | Autogenerate from config   |
|:-------|----------------------------:|:-----------------|:---------------------:|:---------------------------|
| 1      |   Stdlib [baseline], simple | 0.020s           |    emptypt-simple     | -                          |
| 2      |  Stdlib [baseline], minimum | 0.021s           |    emptypt-minimum    | -                          |
| 3      |  msgspec + argh (docstring) | 0.093s           | emptypt-m-argh-docstr | Yes                        |
| 4      |             msgspec + click | 0.120s           |    emptypt-m-click    | -                          |
| 5      |              msgspec + argh | 0.126s           |    emptypt-m-argh     | Yes                        |
| 6      | pydantic + argh (docstring) | 0.203s           | emptypt-p-argh-docstr | Yes                        |
| 7      |            pydantic + click | 0.203s           |    emptypt-p-click    | -                          |
| 8      |             pydantic + argh | 0.218s           |    emptypt-p-argh     | Yes                        |
| 9      |            msgspec + defopt | 0.236s           |   emptypt-m-defopt    | Yes                        |
| 10     |           pydantic + defopt | 0.263s           |   emptypt-p-defopt    | Yes                        |

Laptop: Lenovo IdeaPad Flex 3 (1.1 GHz, max. 3.1 GHz)

| Configuration              |   Execution Time | entrypoint        |  Autogenerate from config  |
|:---------------------------|-----------------:|:------------------|:--------------------------:|
| Stdlib [baseline]          |           0.036s | emptypt-m-minimum |             -              |
| msgspec                    |           0.038s | emptypt-m-simple  |             -              |
| msgspec + argh (docstring) |           0.147s | emptypt-m-argh    |            Yes             |
| msgspec + click            |           0.183s | emptypt-m-click   |             -              |
| msgspec + typer            |           0.242s | emptypt-m-typer   |             -              |
| msgspec + defopt           |           0.454s | emptypt-m-defopt  |            Yes             |

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
