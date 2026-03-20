# 🌿 Django Vanilla Web App Template (V2.1)
### *The Ultimate "Gold Master" for Agentic Development*

This is a production-hardened, high-performance template designed for rapid project initialization. It follows the **Skeptic Designer** philosophy: clean Vanilla CSS, atomic SCSS hierarchy, and a strict separation of infrastructure and logic.

---

## 🚀 AGENTIC ACTIVATION (Copy-Paste)
**Paste this to Antigravity/Agent to initialize a new project:**
> "I am starting a new project based on this template. 
> 1. Run `make rename NAME=your_new_project_slug` to synchronize identifiers.
> 2. Initialize a new Git repository (`rm -rf .git && git init`).
> 3. Perform a clean image build (`make build`).
> 4. Run migrations and collect static files (`make migrate`, `make collectstatic`).
> 5. Verify status via the `/health/` endpoint and perform a test run (`make test`).
> 6. Report once the ecosystem is 100% operational."

---

## 🏗 Key Features & Infrastructure

### 1. Production-Ready Backend
- **Core App**: Includes `BaseModel` (UUID + Timestamps) and system tags for SVG Icons.
- **Split Settings**: Clean separation for `local.py` and `production.py`.
- **Health Checks**: Built-in `/health/` endpoint for monitoring DB and Redis.
- **i18n (Internationalization)**: Pre-configured bilingual support (RU/EN).
- **Security**: Hardened Nginx proxy, HSTS, SSL-ready headers, and `django-axes` for brute-force protection.

### 2. SCSS Atomic Hierarchy (BEM-powered)
- **Tokens**: Global variables, fonts, and baseline resets.
- **Blocks**: Atomic UI components (Buttons, Forms, Cards).
- **Pages**: Layout-specific assemblies and page logic.
- **Utils**: Agnostic layout objects (`o-container`, `o-grid`).

### 3. High-Performance Stack
- **Web**: Python 3.13 + Django 5.2 (Poetry-managed).
- **Proxy**: Nginx Sidecar (handles static/media delivery).
- **Cache**: Redis 7.0 for session and cache speed.
- **DB**: PostgreSQL 16-alpine.
- **CI/CD**: GitHub Actions for automated quality control (`pytest`).

---

## 📂 Project Structure Guide
- `web/apps/`: Your business logic.
- `web/asset/scss/`: The design system.
- `web/templates/`: Atomic templates and page blocks.
- `scripts/`: System tools (e.g., `rename_project.py`).
- `docker/`: Industrial-grade container configurations.

---

## 🛠 Commands (Makefile)
- `make build` : Build/Rebuild all containers.
- `make up` : Launch the project (Port 80/8000).
- `make migrate` : Run database migrations.
- `make test` : Execute the full test suite (pytest).
- `make rename NAME=xxx` : Rebrand the entire project instantly.

---
*Created with ❤️ by Antigravity for VelValerian.*
