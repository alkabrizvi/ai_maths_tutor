# =========================
# EXPLANATION STYLES
# =========================

STYLE_INSTRUCTIONS = {
    "simple": "Explain in simple and clear English using short sentences.",

    "real_life": "Explain using practical real-life examples and analogies.",

    "story": "Explain the concept through a short and simple story.",

    "sports": "Explain using sports-related examples or analogies when useful.",

    "daily_life": "Explain using examples from common daily life situations.",

    "exam": "Explain in an exam-focused way with important points and steps.",

    "step_by_step": "Explain the solution clearly one step at a time.",

    "beginner": "Assume the student is a complete beginner. Avoid difficult terminology.",

    "visual_words": "Use text-based visual representations, arrows, boxes, and simple layouts.",

    "math_only": "Focus only on the mathematical reasoning and calculations. Avoid unnecessary examples."
}


# =========================
# STYLE DETECTION
# =========================

def detect_style(style: str) -> str:
    """
    Return a valid explanation style.
    If the requested style is invalid, use 'simple'.
    """

    if style in STYLE_INSTRUCTIONS:
        return style

    return "simple"