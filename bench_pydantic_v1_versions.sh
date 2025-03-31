hyperfine -i --warmup 4 \
  -n 1.9 "uv run --with 'pydantic==1.9' test_pydantic_v1_speed.py" \
  -n 1.10 "uv run --with 'pydantic==1.10' test_pydantic_v1_speed.py"
  # -n 1.0 "uv run --with 'pydantic==1.0' test_pydantic_v1_speed.py" \
  # -n 1.1 "uv run --with 'pydantic==1.1' test_pydantic_v1_speed.py" \
  # -n 1.2 "uv run --with 'pydantic==1.2' test_pydantic_v1_speed.py" \
  # -n 1.3 "uv run --with 'pydantic==1.3' test_pydantic_v1_speed.py" \
  # -n 1.4 "uv run --with 'pydantic==1.4' test_pydantic_v1_speed.py" \
  # -n 1.5 "uv run --with 'pydantic==1.5' test_pydantic_v1_speed.py" \
  # -n 1.6 "uv run --with 'pydantic==1.6' test_pydantic_v1_speed.py" \
  # -n 1.7 "uv run --with 'pydantic==1.7' test_pydantic_v1_speed.py" \
  # -n 1.8 "uv run --with 'pydantic==1.8' test_pydantic_v1_speed.py" \
