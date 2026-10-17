# SnailSight

Identify and locate GALS from visual data to enable targeted eradication.

# Galaxy Events MVP

A minimal FastAPI service detecting galaxy events.

## Usage

Run server:
uvicorn main:app --reload

Test:
pytest -q

## Architecture

![Architecture](docs/architecture.png)

<details>
<summary>Mermaid source</summary>

```mermaid
flowchart LR
    A[Client] --> B[FastAPI Server]
    B --> C{detect_gals}
    C -->|Default Region| D[Return Event]
    C -->|Other Region| E[Return Empty]
    D --> F[HTTP 200]
    E --> G[HTTP 404]
```

</details>
