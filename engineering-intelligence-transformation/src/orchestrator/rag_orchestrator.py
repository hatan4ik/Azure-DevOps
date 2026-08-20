from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class RetrievedChunk:
    source: str
    title: str
    text: str
    score: float
    metadata: Dict[str, Any]

class RagOrchestrator:
    def __init__(self, search_client, llm_client, policy_client):
        self.search = search_client
        self.llm = llm_client
        self.policy = policy_client

    def answer(self, user_id: str, question: str, repo_scope: List[str]) -> Dict[str, Any]:
        allowed_scope = self.policy.allowed_repos(user_id, repo_scope)
        chunks = self.search.hybrid_search(question, filters={"repo": allowed_scope}, top_k=8)
        if not chunks:
            return {"answer": "No authorized source found.", "confidence": "low", "citations": []}
        prompt = self._build_grounded_prompt(question, chunks)
        response = self.llm.complete(prompt, max_tokens=900)
        return {"answer": response.text, "confidence": self._confidence(chunks), "citations": [c.source for c in chunks]}

    def _build_grounded_prompt(self, question, chunks):
        context = "\n\n".join(f"SOURCE: {c.source}\n{c.text}" for c in chunks)
        return f"Answer only from authorized sources. If insufficient, say so.\nQUESTION:\n{question}\nSOURCES:\n{context}"

    def _confidence(self, chunks):
        best = max(c.score for c in chunks)
        return "high" if best >= 0.85 else "medium" if best >= 0.65 else "low"
