# Deepu Fabricator Production API Core

Secure enterprise backend built on Python FastAPI with automated 3-month media storage purging, safe native bcrypt credentials processing, and a streaming PDF rate matrix document engine.

## Local Development Configuration

### 1. Manual Setup (Virtual Environment)
```bash
# Move into backend workspace
cd backend

# Create and activate environment
python -m venv .venv
source .venv/Scripts/activate # On Windows PowerShell: .venv\Scripts\activate

# Install application dependencies
pip install -r requirements.txt

# Launch development reload server process
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

### 2. Testing Framework Automation
```bash
# Run isolated unit testing sweep checks
pip install pytest httpx
pytest -v
```

## Production Docker Orchestration

To run the entire application ecosystem inside an isolated, containerized environment, execute the following command from your parent project directory:

```bash
docker-compose up --build
```

- **API Documentation Portal**: `http://localhost:8000/docs`
- **Active Backend Core Node URL**: `http://localhost:8000`
