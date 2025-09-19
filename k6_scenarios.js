import http from 'k6/http';
import { sleep } from 'k6';
import { check } from 'k6';

export const options = {
  scenarios: {
    load_test: {
      executor: 'constant-vus',
      vus: 150,
      duration: '2m',
      exec: 'loadScenario',
    },
    stress_test: {
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '30s', target: 100 },
        { duration: '30s', target: 250 },
        { duration: '30s', target: 400 },
        { duration: '30s', target: 550 },
        { duration: '30s', target: 700 },
        { duration: '30s', target: 850 },
        { duration: '30s', target: 1000 },
        { duration: '30s', target: 0 },
      ],
      exec: 'stressScenario',
      startTime: '2m5s'
    },
  },
  thresholds: {
    http_req_duration: ['p(95)<800'],
    http_req_failed: ['rate<0.02'],
  },
};

const BASE = __ENV.FAKESTORE_BASE_URL || 'https://fakestoreapi.com';

function makeProductPayload() {
  const id = Math.floor(Math.random() * 1000000);
  return JSON.stringify({
    title: `k6 product ${id}`,
    price: 9.99,
    description: 'load test product',
    image: 'https://i.pravatar.cc/300?img=3',
    category: 'electronics'
  });
}

export function loadScenario() {
  const roll = Math.random();
  if (roll < 0.7) {
    const res = http.get(`${BASE}/products`);
    check(res, { 'GET /products 200': (r) => r.status === 200 });
  } else {
    const res = http.post(`${BASE}/products`, makeProductPayload(), { headers: { 'Content-Type': 'application/json' } });
    check(res, { 'POST /products 200/201': (r) => r.status === 200 || r.status === 201 });
  }
  sleep(0.5);
}

export function stressScenario() {
  const roll = Math.random();
  if (roll < 0.8) {
    const res = http.get(`${BASE}/products`);
    check(res, { 'GET /products 200': (r) => r.status === 200 });
  } else {
    const res = http.post(`${BASE}/products`, makeProductPayload(), { headers: { 'Content-Type': 'application/json' } });
    check(res, { 'POST /products 200/201': (r) => r.status === 200 || r.status === 201 });
  }
  sleep(0.3);
}
