# 🚀 Fullstack QA Automation Framework

## 🏗️ Tech Stack
*   **Backend:** FastAPI (Python 3.9)
*   **Database:** PostgreSQL 15 (Dockerized)
*   **Infrastructure:** Docker & Docker Compose
*   **Testing:** Pytest, Requests (API), Psycopg2 (DB)
*   **CI/CD:** GitHub Actions (Automated Test Execution)

## 🌟 Key Features
- **Isolated Testing:** Every test run uses a fresh, containerized PostgreSQL instance.
- **API + DB Validation:** Tests don't just check HTTP codes; they verify data persistence directly in the database.
- **Automated CI/CD:** Fully integrated GitHub Actions pipeline that builds the environment and runs tests on every push.
- **Modular Design:** Uses a dedicated `db_client.py` and `api_client.py` for clean, reusable code.

## 📁 Project Structure
```text
├── .github/workflows/    # CI/CD Pipeline (GitHub Actions)
├── api/                  # FastAPI Application Source Code
├── tests_api/            # Pytest Suite (test_db_basic.py, etc.)
├── db_client.py          # PostgreSQL Interaction Wrapper
├── api_client.py         # Requests-based API Client
├── docker-compose.yaml   # Service Orchestration (API + DB)
└── Dockerfile            # API Container Definition
