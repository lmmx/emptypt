# emptypt

Template for an entrypoint CLI using msgspec

## Timing Benchmarks

Desktop

| Configuration        | Execution Time | entrypoint       | Autogenerate from config  |
|----------------------|----------------|------------------|---------------------------|
| Stdlib (baseline)    | 0.019s         | emptypt-minimum  | -                         |
| msgspec              | 0.046s         | emptypt-simple   | -                         |
| msgspec + argh       | 0.060s         | emptypt-argh     | Yes                       |
| msgspec + click      | 0.075s         | emptypt-click    | No                        |
| msgspec + typer      | 0.094s         | emptypt-typer    | No                        |
| msgspec + defopt     | 0.175s         | emptypt-defopt   | Yes                       |

Laptop (1.1 GHz)

| Configuration        | Execution Time | entrypoint       | Autogenerate from config  |
|----------------------|----------------|------------------|---------------------------|
| Stdlib (baseline)    | 0.038s         | emptypt-minimum  | -                         |
| msgspec              | 0.110s         | emptypt-simple   | -                         |
| msgspec + argh       | 0.145s         | emptypt-argh     | Yes                       |
| msgspec + click      | 0.180s         | emptypt-click    | No                        |
| msgspec + typer      | 0.235s         | emptypt-typer    | No                        |
| msgspec + defopt     | 0.440s         | emptypt-defopt   | Yes                       |

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
