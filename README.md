# Your Store — API Testing Pack (FakeStoreAPI)

This pack includes **functional tests (pytest)** and **load/stress tests (k6)** for the public API at `https://fakestoreapi.com`.

## Quick Start

### 1) Functional tests (pytest)
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -U pytest requests
pytest -q
```

### 2) Load & Stress tests (k6)
Install k6: https://k6.io/docs/get-started/installation/

Run **load test (150 VUs for 2 minutes)** and **stress test (100 -> 1000 VUs)**:
```bash
k6 run k6_scenarios.js
```

To save a JSON summary:
```bash
K6_SUMMARY=summary.json k6 run k6_scenarios.js
```

Then paste metrics into `report_template.md`.

> ⚠️ Using a public demo API. Avoid excessively high rates or running tests for too long.
