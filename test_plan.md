# Test Plan — Your Store (API Functional & Performance)

## Scope
Validate key product endpoints in FakeStoreAPI to allow back-end validation before front-end is complete.

## Endpoints under test (base: https://fakestoreapi.com)
- GET /products
- GET /products/{id}
- GET /products/category/electronics
- POST /products
- PUT /products/{id}
- (Optional) DELETE /products/{id}  — cleanup

## Functional Test Cases

| ID | Title | Method | Endpoint | Data | Expected |
|----|-------|--------|----------|------|----------|
| F1 | List electronics | GET | /products/category/electronics | — | 200 OK, array > 0, each item.category == 'electronics' |
| F2 | Get product by id | GET | /products/{id} (e.g., 1) | — | 200 OK, object with `id`, `title`, `price`, `category`, `image` |
| F3 | Create product | POST | /products | title, price, description, image, category | 200/201 OK, response has `id` and echoes fields |
| F4 | Update product image | PUT | /products/{id} (id from F3) | image | 200 OK, image changed |
| F5 | (Optional) Delete created product | DELETE | /products/{id} | — | 200 OK |

## Non-Functional (Performance)

### Load Test
- 150 virtual users (VUs) for 2 minutes.
- Mix: 70% GET /products, 30% POST /products.

### Stress Test
- Ramp-up: 100 → 250 → 400 → 550 → 700 → 850 → 1000 VUs, 30s per stage.
- Endpoints: GET /products (80%), POST /products (20%).

### Metrics
- `http_req_duration` avg, p(95)
- Requests per second
- Success rate (2xx/3xx) vs errors (4xx/5xx)
- Notes on saturation or timeouts
