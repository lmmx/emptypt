hyperfine --warmup 4 \
  -n 1.9 "uv run --with 'pydantic==1.9' test_pydantic_v1_speed.py" \
  -n 1.10 "uv run --with 'pydantic==1.10' test_pydantic_v1_speed.py" \
  -n 2.0 "uv run --with 'pydantic==2.0' test_pydantic_speed.py" \
  -n 2.1 "uv run --with 'pydantic==2.1' test_pydantic_speed.py" \
  -n 2.2 "uv run --with 'pydantic==2.2' test_pydantic_speed.py" \
  -n 2.3 "uv run --with 'pydantic==2.3' test_pydantic_speed.py" \
  -n 2.4 "uv run --with 'pydantic==2.4' test_pydantic_speed.py" \
  -n 2.5 "uv run --with 'pydantic==2.5' test_pydantic_speed.py" \
  -n 2.6 "uv run --with 'pydantic==2.6' test_pydantic_speed.py" \
  -n 2.7 "uv run --with 'pydantic==2.7' test_pydantic_speed.py" \
  -n 2.8 "uv run --with 'pydantic==2.8' test_pydantic_speed.py" \
  -n 2.9 "uv run --with 'pydantic==2.9' test_pydantic_speed.py" \
  -n 2.10 "uv run --with 'pydantic==2.10' test_pydantic_speed.py" \
  -n 2.11 "uv run --with 'pydantic==2.11' test_pydantic_speed.py"
