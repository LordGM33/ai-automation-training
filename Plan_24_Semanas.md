# Plan de Entrenamiento — De Arquitecto de Procesos a AI Automation Developer

**Duración:** 24 semanas (6 meses), lunes a viernes, tiempo completo
**Objetivo final:** poder responder con evidencia propia las 4 preguntas de screening del anuncio de referencia (sistema de IA construido personalmente · LLMs en producción con RAG/tool calling · workflows de engagement con captura de datos · backend + dashboard desplegados en cloud)
**Vehículo de portafolio:** extraer piezas de Eva como servicios reales. El aprendizaje y el MVP avanzan juntos — nunca proyectos de juguete.

**NOTA (10-ago-2026):** el programa arranca desde cero absoluto — sin asumir lógica de programación ni manejo de consola. La Semana 1 detallada está en `Semana_01_Guia_Desde_Cero.md`; las guías de cada semana siguiente se entregan al pasar la compuerta de la anterior, ajustadas al ritmo real. Este documento es el mapa maestro: los temas y compuertas son el compromiso; el ritmo puede estirarse si las compuertas lo piden.

---

## 0. Cómo está diseñado este plan

**Regla 1 — Escribís todo el código vos.** Nada de copiar/pegar de tutoriales ni de IA en las Fases 1–2. La IA (Claude) se usa como *profesor que explica*, nunca como *autor del código*. A partir de la Fase 3 la IA pasa a ser tu pair programmer, porque para entonces ya podés auditar lo que te propone.

**Regla 2 — Cada semana tiene una compuerta falsable.** Criterios objetivos de "pasa / no pasa" el viernes. Si no pasa, el lunes siguiente se dedica a cerrar la brecha antes de avanzar.

**Regla 3 — Los viernes no hay contenido nuevo.** Repaso activo, refactor, demo grabada de 3 minutos en inglés, retrospectiva escrita.

**Regla 4 — Diario de ingeniería, todos los días, 20 minutos.** Qué construí, qué no entendí, qué pregunto mañana.

**Regla 5 — Todo commit, todos los días, en inglés** (desde que existe la cuenta de GitHub, viernes de la semana 1).

**Regla 6 — Un solo proyecto eje, seis fases:** el "Eva Platform Extract".

### Ritmo diario (lunes a jueves)
08:00–08:30 repaso activo · 08:30–10:30 teoría guiada · 10:45–12:30 práctica dirigida · 12:30–13:30 almuerzo + caminata · 13:30–16:00 proyecto eje · 16:00–16:30 diario + commit + flashcards.

### Ritmo del viernes
08:00–09:30 repaso acumulado · 09:30–11:30 refactor · 11:30–12:30 demo grabada (3 min, inglés) · 13:30–15:00 compuerta semanal · 15:00–16:00 retrospectiva.

---

## FASE 1 — Python Profesional (Semanas 1–6)
**Recursos:** Semana 1 con guía propia desde cero; luego *Python for Everybody* (py4e.com) + docs oficiales + *Practical Python Programming* (dabeaz).
**Proyecto eje:** `veredicto-cli` — CLI que parsea logs de veredictos (ok/reason/action), calcula métricas de compuertas y genera reportes.

- **S1 — Terminal, Python, variables, condicionales, bucles, funciones** (guía aparte). Compuerta: 4/5 ejercicios sorpresa en 90 min.
- **S2 — Estructuras de datos y archivos:** dicts, sets, tuplas, sort con key, lectura/escritura, json, csv, try/except. Compuerta: reporte correcto de 500 veredictos simulados tolerando 20 líneas corruptas.
- **S3 — Código organizado:** módulos/paquetes, venv y pip, argparse con subcomandos, clases (init, dataclasses, repr), type hints + mypy. Compuerta: explicar la estructura del paquete en inglés; mypy limpio.
- **S4 — Testing:** pytest, parametrización, casos borde, fixtures, coverage, mini-TDD. Compuerta: 25+ tests en verde, coverage >80%, explicar qué caso de negocio cubre cada grupo.
- **S5 — Intermedio aplicado:** generadores (streaming de logs grandes), decoradores @timer/@retry con backoff, datetime/pathlib/logging, requests contra una API pública. Compuerta: script nuevo desde cero en 2 horas (API pública + errores + CSV + 5 tests) sin IA.
- **S6 — Integrador:** `gate-simulator` (pipeline de compuertas configurable en JSON, con tests) + READMEs en inglés + perfil GitHub. **Compuerta mayor:** explicar el código línea por línea en video + 3 katas medias en 90 min.

## FASE 2 — SQL, PostgreSQL y FastAPI (Semanas 7–11)
**Recursos:** SQLBolt → tutorial oficial de PostgreSQL → tutorial oficial de FastAPI completo.
**Proyecto eje:** `memoria-service` — la memoria estructurada de Eva como API REST con Postgres.

- **S7 — SQL:** SELECT/WHERE/ORDER, JOINs, GROUP BY/HAVING, DML, constraints y tipos; esquema `memoria` v1 (objectives, decisions, verdicts, assets). Compuerta: 8 queries de negocio sin ayuda.
- **S8 — FastAPI fundamentos:** HTTP en serio, endpoints, Pydantic, HTTPException con formato {ok, reason}, routers por dominio. Compuerta: CRUD en memoria documentado en /docs con tests de TestClient.
- **S9 — FastAPI + Postgres:** SQLModel, sesiones, Alembic básico, relaciones, paginación y filtros, índices, endpoints de métricas. Compuerta: API con una tabla y CRUD persistente desde cero en <3 horas.
- **S10 — Auth y robustez:** pydantic-settings y secretos, API keys → OAuth2+JWT, BackgroundTasks (escalación al insertar FAIL), logging estructurado, middleware request-id, retries. Compuerta: demo en inglés del servicio completo con tests de integración.
- **S11 — Integrador:** memoria-service v1.0 (4 dominios, seed, colección .http, README con diagrama) + `veredicto-cli` como cliente de la API. **Compuerta mayor:** sistema de dos piezas end-to-end + video de 5 min en inglés.

## FASE 3 — LLMs: structured outputs, tool calling y RAG (Semanas 12–15)
**Recursos:** docs oficiales de Anthropic y OpenAI; pgvector + Supabase.
**Proyecto eje:** `gates-service` + `eva-rag` (RAG sobre los 45+ docs del EvaRepo).
**Cambio de régimen:** la IA pasa a pair programmer; vos auditás.

- **S12 — APIs de LLM:** Messages API, tokens y costos, JSON mode/structured outputs con esquema {ok, reason, action}, rate limits/retries/streaming, y una eval de 50 casos etiquetados con comparación de prompts medida. Compuerta: salida estructurada garantizada + tabla prompt v1/v2/v3 con números.
- **S13 — Tool calling:** definición de herramientas, loop llamada→resultado, elección entre múltiples tools, presupuesto de iteraciones con ESCALATE real, registro auditable en DB, catálogo cerrado de acciones + dry-run. Compuerta: agente responde 5 preguntas de negocio contra la API con log auditable y escalación demostrada.
- **S14 — RAG 1:** embeddings con las manos, pgvector, ingesta de los .md del EvaRepo (chunking por headers), búsqueda semántica, RAG con citas y regla "si no hay chunk sobre umbral → 'no está en la base'". Compuerta: 15/20 preguntas citando el doc correcto; los 5 fallos documentados con hipótesis.
- **S15 — RAG 2 + integrador:** overlap, metadata filtering por status VIGENTE/HISTÓRICO, re-ranking simple, eval formal de retrieval vs fidelidad, endpoint /ask con auth y costos, y el agente gana la tool search_knowledge. **Compuerta mayor:** video 5–7 min en inglés (agente + RAG + audit trail + escalación) → responde la pregunta 2 del screening.

## FASE 4 — React y el Dashboard (Semanas 16–19)
**Recursos:** react.dev completo, Vite, Tailwind + shadcn/ui.
**Proyecto eje:** `eva-ops-dashboard` — aprobaciones pendientes, métricas de gates, log de veredictos.

- **S16 — JS mínimo viable + React básico:** sintaxis moderna en un día, map/filter/reduce, async/fetch contra memoria-service, componentes/JSX/props, useState y listas. Compuerta: mini-app que filtra una lista local, explicando qué re-renderiza.
- **S17 — Datos reales:** useEffect + trío loading/error/data, CORS (a propósito), formularios controlados, React Router (3 rutas), Tailwind + shadcn (badges PASS/FAIL/ESCALATED). Compuerta: dashboard navegable con datos vivos y estados manejados.
- **S18 — Flujo de aprobación humana:** endpoints approvals pending/approve/reject con razón, bandeja de aprobaciones, Recharts (2 gráficas), polish de operador. Compuerta: video del ciclo output FAIL → bandeja → rechazo con razón → audit log → métricas.
- **S19 — Integrador:** v1.0 completo, README con GIFs, diagrama retrospectivo del sistema vs. el diagrama original de papel. **Compuerta mayor:** demo end-to-end de 7 min en inglés.

## FASE 5 — Docker, Deploy y Observabilidad (Semanas 20–22)
**Recursos:** Docker Get Started, Railway/Fly.io, Supabase.

- **S20 — Docker:** imagen/contenedor, Dockerfile multi-stage básico, compose (API+Postgres), frontend dockerizado, volúmenes/healthchecks/logs. Compuerta: `git clone` + `docker compose up` levanta todo en una máquina limpia.
- **S21 — Deploy:** PaaS (Railway/Fly) + Supabase, secretos, HTTPS, deploy del frontend, CORS de producción, GitHub Actions (tests → deploy). Compuerta: URL pública + un push con test roto que bloquea el deploy.
- **S22 — Observabilidad:** JSON logs, Sentry, healthchecks + uptime, dashboard de latencia y costos LLM, runbook en inglés, simulacro de incidente con postmortem. **Compuerta mayor:** sistema en producción con CI/CD + postmortem escrito.

## FASE 6 — Voice AI y Relanzamiento (Semanas 23–24)
- **S23 — Voice AI (Vapi/Retell):** asistente de calificación de leads, webhooks a FastAPI, transcript → extracción estructurada → DB → tarea de seguimiento, vista de llamadas en el dashboard. Compuerta: video del ciclo completo (responde la pregunta 3 del screening).
- **S24 — Portafolio y relanzamiento:** GitHub consolidado con repo showcase, redactar las 4 respuestas del screening con evidencia, perfil de Upwork nuevo (título, portfolio, tarifa $30–40/hr inicial), 3 plantillas de propuesta. **Compuerta final:** simulacro de entrevista técnica de 60 min + plan de 90 días.

---

## Apéndices

**A. Protocolo de atasco:** 25 min solo → 15 min docs → preguntar el concepto a la IA (no la solución) → solo en Fase 3+ pedir código y auditarlo → a los 60 min: anotar, saltar de tarea, retomar mañana.

**B. Flashcards (Anki):** sintaxis poco usada pero necesaria, conceptos con definición precisa, errores propios memorables. No entra lo que autocompleta el editor.

**C. Alarmas del programa:** >30 min/día de video-tutoriales = tutorial hell; dos compuertas seguidas en "casi" = frenar y reforzar; diario abandonado 3 días = primer síntoma de deriva; cero commits un día laborable = anotar qué pasó.

**D. Costos:** todo gratuito o free tier; presupuestar $10–20/mes de API LLM desde la Fase 3 y $5–10/mes de PaaS en Fases 5–6.

**E. Relación con Eva:** Fases 2–4 construyen componentes que Eva necesita (memoria, gates, RAG, panel de aprobaciones). Pausado hasta la semana 25: pipelines multimedia e identidad visual. Pausa táctica, no abandono.
