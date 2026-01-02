
# Backend — Quick start

1. Create venv and install
```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

2. (recommended) Enable direnv for automatic `.env` loading
```bash
brew install direnv
echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc
source ~/.zshrc
direnv allow
```

3. Verify env is loaded
```bash
printenv LANGSMITH_API_KEY
PYTHONPATH=. uv run python -c "from app.config import settings; print('OK' if settings.LANGSMITH_API_KEY else 'MISSING')"
```

4. Run Langgraph Studio
```bash
uv run langgraph dev
```

If you don't use `direnv`, prefix the run with `.env` exported:
```bash
set -a
. .env
set +a
uv run langgraph dev
```

