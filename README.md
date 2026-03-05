# ZENCSE010 — CertShield

Digital certificate verification microservice. Institutions issue cryptographically signed certificates with QR codes. Anyone can scan the QR to instantly verify authenticity.

**Stack**: Python 3.12 · FastAPI · MongoDB · ECDSA P-256 · React 18 · Docker

---

## Project Structure

```
cert-shield/
├── backend/              # FastAPI microservice
├── frontend-admin/       # React admin dashboard (port 3000)
├── frontend-portal/      # React verification portal (port 3001)
├── docker-compose.yml
└── SPRINTS.md            # 4 sprints · 35 user stories
```

---

## Getting Started

### Prerequisites
- Python 3.12+
- Node.js 18+
- MongoDB 7.0 (or use Docker)

### 1. Clone
```bash
git clone https://github.com/ZenVInnovations/ZENCSE010.git
cd ZENCSE010
```

### 2. Backend Setup
```bash
cd backend
cp .env.example .env          # fill in your values
pip install -r requirements.txt
python generate_keys.py       # creates keys/private_key.pem + public_key.pem
uvicorn app.main:app --reload --port 8000
```

### 3. Frontend Setup
```bash
# Admin Dashboard
cd frontend-admin
cp .env.example .env
npm install
npm run dev                   # runs on http://localhost:3000

# Verification Portal
cd frontend-portal
cp .env.example .env
npm install
npm run dev                   # runs on http://localhost:3001
```

### 4. Run with Docker
```bash
docker-compose up             # starts MongoDB + backend
```

---

## API Docs

Once backend is running: **http://localhost:8000/docs**

---

## Sprint Plan

See [SPRINTS.md](./SPRINTS.md) for all 35 user stories across 4 sprints.
