# platform-python-base

A shared foundational framework for Python-based microservices. Provides standard FastAPI setup, environment loading, structured logging, health checks, retries, and circuit breakers — used across trading services like order-manager, trade-manager, tick-ingestor, etc.

---

## 🚀 Features

- Unified FastAPI initialization across services
- Centralized logging with environment-based log levels
- `.env`-based configuration loader
- Health check endpoint (`/healthz`)
- Retry utility with exponential backoff
- Circuit breaker support with `aiobreaker`
- Shared schemas for consistent API responses

---

## Tech

### 📦 Tech stack

- Python 3.9+
- FastAPI (exposed via `create_base_app`)
- Pydantic 2.x
- aiobreaker (circuit breaker)
- python-dotenv for `.env` loading
- PyYAML (optional use in future configs)

---

### ⚙️ Usage (In Other Projects)

- Add to requirements.txt
```
platform-python-base @ git+ssh://git@github.com:Subrahmanya-Hegde/platform-python-base.git
```

- In your service main.py
```
from platform_base.config_loader import load_env_file
from platform_base.logging_factory import setup_logging
from platform_base.fastapi_app_base import create_base_app
from platform_base.health_checker import add_health_route

load_env_file()
setup_logging(log_dir="logs", log_name="system")

app = create_base_app(app_name="<service_name>")
add_health_route(app)
```

---

### 🧪 Local Development
```
cd platform-python-base
python3 -m venv venv
source venv/bin/activate
pip install -e .
```
This lets you develop the base locally and import it across other services.

---

### ✅ Components Provided
| File                          | Purpose                                 |
| ----------------------------- | --------------------------------------- |
| `fastapi_app_base.py`         | Creates FastAPI app with middleware     |
| `config_loader.py`            | Loads `.env` into `os.environ`          |
| `logging_factory.py`          | Structured logger factory               |
| `retry.py`                    | Retry decorator with backoff            |
| `circuit_breaker.py`          | Circuit breaker with `aiobreaker`       |
| `health_checker.py`           | Adds `/healthz` to your app             |
| `schemas/common_responses.py` | Standard success/error response schemas |

---