class PRGuardianAgent:
    def __init__(self, rag, scm, policy):
        self.rag = rag
        self.scm = scm
        self.policy = policy

    def analyze_pr(self, repo: str, pr_id: int, user_id: str):
        diff = self.scm.get_pr_diff(repo, pr_id)
        question = f"Analyze this PR diff for regression, security, IaC and architecture risk:\n{diff}"
        result = self.rag.answer(user_id=user_id, question=question, repo_scope=[repo])
        risk = self.policy.score_pr(diff=diff, rag_result=result)
        if risk["score"] >= 50:
            self.scm.comment_on_pr(repo, pr_id, self._format_comment(result, risk))
        return {"risk": risk, "commented": risk["score"] >= 50}

    def _format_comment(self, result, risk):
        citations = "\n".join(f"- {c}" for c in result["citations"])
        return f"## AI PR Guardian Review\n\nRisk score: **{risk['score']}**\nConfidence: **{result['confidence']}**\n\n{result['answer']}\n\nSources:\n{citations}"
