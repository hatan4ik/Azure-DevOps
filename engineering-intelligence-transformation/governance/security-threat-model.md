# Security Threat Model

## Main Threats
- Prompt injection through retrieved code/comments/docs.
- Cross-repo or cross-team data leakage.
- Secrets or PII embedded into vector store.
- Hallucinated answers or unsafe remediation.
- Cost abuse through excessive token usage.
- Uncontrolled production mutation.
- Missing audit trail.
- Poisoned stale documentation.

## Required Controls
- Instruction isolation and prompt firewall.
- RBAC before retrieval.
- Secret scanning and redaction before embedding.
- Citation-required answers.
- Confidence threshold and refusal behavior when sources are insufficient.
- Allow-listed runbooks only.
- OPA/Azure Policy approval before action.
- Human gate for high-risk production operations.
- Immutable audit logs.
- Quotas, caching and model tiering.