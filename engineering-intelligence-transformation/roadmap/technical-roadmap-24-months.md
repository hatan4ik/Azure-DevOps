# 18-24 Month Technical Roadmap

## Phase 0: Foundation, Months 0-2
Build secure LLM access, AI Gateway/RAG orchestrator, vector/hybrid search, metadata store, private networking, identity, token logging and retrieval telemetry.

Exit: 2-3 repos indexed, citation-backed answers, RBAC enforced, cost per query visible.

## Phase 1: Knowledge Layer, Months 3-5
Scale ingestion for repos, Azure Boards/Jira, ADRs, runbooks and CI/CD history. Add commit-aware incremental indexing, metadata ownership and developer UI/IDE integration.

Exit: engineers find internal answers without Slack archaeology.

## Phase 2: PR Intelligence, Months 6-8
Deploy PR Guardian. Check diffs against secure coding, IaC patterns, architecture rules, similar regressions and ownership context.

Exit: useful PR comments with measured false positive rate.

## Phase 3: Incident Intelligence, Months 9-12
Integrate Azure Monitor, Log Analytics, App Insights, Kubernetes events and deployment history. Build failure investigator and incident summarizer.

Exit: probable cause and runbook suggestion within minutes.

## Phase 4: Deployment Risk Scoring, Months 12-16
Score changes based on diff size, infra touched, service criticality, historical failure similarity, blast radius and test coverage. Gate releases by risk.

## Phase 5: Guardrailed Self-Healing, Months 16-24
Add drift detection, allow-listed runbooks, policy evaluation, non-prod execution, production approval gates, verification loop and corrective PR creation.