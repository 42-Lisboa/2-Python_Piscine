clean:
	find . \( -name "__pycache__" -o -name ".mypy_cache" \) -type d -exec rm -rf {} +