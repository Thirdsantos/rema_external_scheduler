## REMA External Scheduler – Municipality of Mandaluyong

This project is an **external companion application for REMA** used by the **Receiving Office of the City of Mandaluyong**.  
It is designed to:

- **Support the REMA system externally** for partners and external offices.
- **Promote the Receiving Machine workflow** in the city’s receiving office.
- Provide an **online scheduling and pre-submission receipt flow**, including automatic emailing of a **pre‑submission receipt** for tracking.

The stack is:

- **Backend**: FastAPI, SQLAlchemy, PostgreSQL
- **Frontend**: Single-page HTML (inline CSS + JS) served by FastAPI

---

### Features

- **Submission scheduling**
  - Collects submitter details (name, email, transaction ID).
  - Captures start/end date and time for the submission window.
  - Allows attaching one or more **documents**, each linked to a department and submission ID.

- **Database-backed scheduling**
  - Uses SQLAlchemy ORM models to persist users, departments, and schedules.
  - The main scheduling endpoint is `POST /schedule_submission`, accepting a `SubmissionDetails` payload.

- **External REMA integration goal**
  - Intended to run **outside** the main REMA system but aligned with its workflows.
  - Helps the receiving office manage **incoming transactions and documents** before they physically reach the Receiving Machine.
  - Future extensions are expected to:
    - Trigger **automatic emails** to external submitters with a **pre-submission receipt**.
    - Provide clear tracking for both the sender and the Receiving Office.

- **Modern, responsive UI**
  - `GET /schedule_submission` serves a fully styled, mobile-friendly page.
  - Users can schedule a submission and see an “About the developer” link:
    - `GET /developer` serves a separate author page (`author.html`).

---

### Project Structure (high level)

- `main.py` – FastAPI app entrypoint, routes for:
  - `GET /schedule_submission` – serves the frontend.
  - `POST /schedule_submission` – accepts scheduling data and stores it via the CRUD layer.
  - `GET /users` – used by the frontend to resolve department IDs.
  - `GET /developer` – serves the author information page.
- `app/`
  - `models/models.py` – SQLAlchemy models (`Users`, `Departments`, `SubmissionSchedule`, `TransactionSchedule`, etc.).
  - `schemas.py` – Pydantic models, including `SubmissionDetails`.
  - `repositories/crud.py` – CRUD and scheduling logic.
  - `routers/` & `services/` – additional route and service organization.
- `frontend/`
  - `index.html` – main REMA External Scheduler UI (all CSS + JS in one file).
  - `author.html` – “About the developer” page.

---

### Running the Application

1. **Clone / open the project** and ensure you are in the project root:
   ```bash
   cd external_rema
   ```

2. **(Optional but recommended) Activate the virtual environment**:
   ```bash
   # Windows (PowerShell)
   .\venv\Scripts\Activate.ps1
   ```

3. **Run the FastAPI server with Uvicorn**:
   ```bash
   uvicorn main:app --reload
   ```

4. **Access the application**:
   - Scheduler UI: `http://127.0.0.1:8000/schedule_submission`
   - Developer page: `http://127.0.0.1:8000/developer`
   - API docs: `http://127.0.0.1:8000/docs`

---

### Usage Flow (External Office / Partner)

1. The external user opens the **REMA External Scheduler** page.
2. They enter:
   - Full name, email, transaction ID.
   - Start and end date/time for when the submission will be made.
   - One or more **documents**, each tied to a department and submission ID.
3. On submission, the backend:
   - Validates the payload with Pydantic.
   - Uses the SQLAlchemy session to persist scheduling data.
   - (Planned) sends an **automatic email** with a **pre‑submission receipt**, which the sender can show when arriving at the Receiving Office.

This gives the **Receiving Machine / receiving office** a structured, pre-registered list of expected submissions, reducing friction and allowing better tracking for the **City of Mandaluyong**.


