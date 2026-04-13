# ❌ Comment out OpenAI imports (not needed for now)
# from openai import OpenAI
# import os
# from dotenv import load_dotenv

# load_dotenv()


class LLMEngine:
    def __init__(self):
        # No API needed for now
        pass
    
    def analyze_root_cause(self, bug_description: str, similar_bugs: list) -> dict:
        """Mock LLM using similarity-based reasoning"""

        # If no similar bugs found
        if not similar_bugs:
            return {
                "module": "Unknown",
                "severity": "Medium",
                "root_cause": "No similar bugs found",
                "explanation": "The system could not find related issues to analyze.",
                "suggested_fix": "Manual investigation required"
            }

        # Take most similar bug
        top_bug = similar_bugs[0]

        # Build smarter explanation
        explanation = (
            f"The reported issue is similar to bug '{top_bug.get('bug_id')}', "
            f"which involved '{top_bug.get('description')}'. "
            f"This suggests the issue is likely related to the {top_bug.get('module')} module."
        )

        return {
            "module": top_bug.get("module", "Unknown"),
            "severity": top_bug.get("severity", "Medium"),
            "root_cause": top_bug.get("root_cause", "Unknown issue"),
            "explanation": explanation,
            "suggested_fix": top_bug.get("suggested_fix", "Review related module logic")
        }