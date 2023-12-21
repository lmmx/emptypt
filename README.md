# emptypt

Template for an entrypoint CLI using msgspec

## Timing Benchmarks

| Configuration        | Execution Time | entrypoint       | Autogenerate from config  |
|----------------------|----------------|------------------|---------------------------|
| Stdlib (baseline)    | 0.015s         | emptypt-minimum  | -                         |
| msgspec              | 0.034s         | emptypt-simple   | -                         |
| msgspec + argh       | 0.048s         | emptypt-argh     | Yes                       |
| msgspec + click      | 0.074s         | emptypt-click    | No                        |
| msgspec + typer      | 0.094s         | emptypt-typer    | No                        |
| msgspec + defopt     | 0.160s         | emptypt-defopt   | Yes                       |

## Details

- `argh.dispatch_command` autogenerates nice simple CLIs from `msgspec.Struct`s, very fast
- `click` can't annotate classes and requires doubling the documentation of config fields as CLI flags
- `typer.run` exits early and the decorator didn't get invoked in the entrypoint (fail)
- `defopt.run` autogenerates nice CLIs from Pydantic models but the ones for msgspec Structs
  interpret all fields as positional CLI args by default
