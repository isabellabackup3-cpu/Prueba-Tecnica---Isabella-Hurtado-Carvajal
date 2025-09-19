# Informe de Pruebas — Your Store (API)

**Fecha:** [Completar]  
**Tester:** [Tu nombre]  
**Entorno:** `https://fakestoreapi.com`

## 1. Resumen Ejecutivo
- Funcionalidad crítica validada (categoría, consulta por ID, creación, actualización de imagen).  
- Pruebas de carga (150 VUs / 2m) y estrés (100→1000 VUs).

## 2. Resultados Funcionales
| Caso | Resultado | Evidencia breve |
|------|-----------|-----------------|
| F1 Listar electronics | ✅/❌ | [status, tamaño lista, ejemplos] |
| F2 Get por ID | ✅/❌ | [status, campos] |
| F3 Crear producto | ✅/❌ | [status, id creado] |
| F4 Actualizar imagen | ✅/❌ | [status, imagen final] |
| F5 Borrado (opcional) | ✅/❌ | [status] |

## 3. Resultados de Performance

### 3.1 Carga — 150 VUs / 2m
- **Promedio (http_req_duration):** [ms]
- **p(95):** [ms]
- **RPS (req/s):** [valor]
- **Errores (http_req_failed):** [%]
- **Observaciones:** [picos, timeouts, throttling]

### 3.2 Estrés — 100→1000 VUs (30s por etapa)
- **Promedio (http_req_duration):** [ms]
- **p(95):** [ms]
- **Max observado:** [ms]
- **% Errores total:** [%]
- **Comportamiento por etapa:**  
  - 100 → 250: [comportamiento]  
  - 250 → 400: [comportamiento]  
  - 400 → 550: [comportamiento]  
  - 550 → 700: [comportamiento]  
  - 700 → 850: [comportamiento]  
  - 850 → 1000: [comportamiento]

## 4. Conclusiones y Recomendaciones
- [ ] Endpoints estables bajo carga base.
- [ ] Revisar límites de POST si se observa aumento de latencia o errores.
- [ ] Ajustar umbrales/alertas: p95 < 800 ms, error rate < 2%.
- [ ] Pruebas adicionales sugeridas: autenticación, carts, usuarios, seguridad.

## 5. Anexos
- Comando de ejecución y versión de k6/pytest.
- Extractos de logs o capturas.
