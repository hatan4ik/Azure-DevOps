class RemediationAgent:
    def __init__(self, rag, policy, runbooks, observability, audit):
        self.rag = rag
        self.policy = policy
        self.runbooks = runbooks
        self.observability = observability
        self.audit = audit

    def handle_alert(self, alert):
        diagnosis = self.rag.answer(
            user_id="agent:remediation",
            question=f"Find likely cause and approved runbook for alert: {alert}",
            repo_scope=[alert.get("service_repo")],
        )
        candidate = self.runbooks.match(diagnosis)
        decision = self.policy.evaluate_remediation(alert=alert, runbook=candidate)
        if not decision["approved"]:
            self.audit.record(alert, diagnosis, decision, action="recommend_only")
            return {"mode": "recommend_only", "diagnosis": diagnosis, "decision": decision}
        result = self.runbooks.execute(candidate, alert)
        healthy = self.observability.verify(alert["service"])
        self.audit.record(alert, diagnosis, decision, action="executed", result=result, healthy=healthy)
        return {"mode": "executed", "healthy": healthy}
