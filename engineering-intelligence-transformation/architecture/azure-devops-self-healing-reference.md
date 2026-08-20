# Azure DevOps + AKS Self-Healing Reference Architecture

## Control Plane
- AI Gateway / RAG Orchestrator: auth, RBAC, hybrid retrieval, reranking, prompt construction, model routing, audit and cost telemetry.
- Ingestion Pipeline: parses code, Terraform, YAML, ADRs, runbooks, work items and incident records.
- Retrieval Store: Azure AI Search or Postgres/pgvector plus metadata store.
- SDLC Agents: PR Guardian, Deployment Failure Investigator, Drift Detection Agent and Remediation Agent.
- Policy Engine: Azure Policy / OPA to approve or deny actions.
- Runbook Engine: deterministic, allow-listed remediation only.

## Core Data Flow
Developer/CI/Incident event -> AI Gateway -> RBAC-aware retrieval -> enterprise LLM -> recommendation -> policy decision -> runbook execution if approved -> verification -> audit record and PR/ticket.

## Key Design Decisions
1. Retrieval authorization happens before LLM invocation.
2. AI may recommend and classify; policy authorizes mutation.
3. Production action is limited to explicit allow-listed runbooks.
4. Every answer/action has evidence, source context and audit trail.
5. Self-healing starts with low-blast-radius reversible fixes only.