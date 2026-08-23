"""Fail-closed governance for F140 Agentic Animation Studio."""

PROTECTED_ACTIONS = {
    "approve_final_master",
    "authorize_public_release",
    "approve_rights_clearance",
    "approve_final_credits",
    "authorize_likeness_use",
    "external_distribution",
}

REQUIRED_REVIEWS = (
    "storyboard_reviewed",
    "visual_development_reviewed",
    "motion_reviewed",
    "continuity_reviewed",
    "rights_provenance_reviewed",
    "accessibility_reviewed",
    "production_quality_reviewed",
    "qualified_producer_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "binding release, rights, likeness, credit, master, or distribution action is outside reference-system scope"}
    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required animation review", "missing": missing}
    checks = {
        "rights_clearance_gap": "asset, music, script, character, footage, voice, font, or other rights evidence unresolved",
        "likeness_consent_gap": "identity, voice, performer, or likeness consent unresolved",
        "continuity_failure": "material story, character, prop, environment, timing, or production continuity issue unresolved",
        "accessibility_failure": "material caption, subtitle, audio-description, flashing, readability, or accessibility issue unresolved",
        "production_quality_gap": "material animation, compositing, render, sound, editorial, or delivery-quality issue unresolved",
        "credit_attribution_gap": "required creator, performer, source, license, or production attribution incomplete",
        "synthetic_media_disclosure_gap": "required synthetic-media provenance or disclosure incomplete",
        "provenance_documentation_gap": "source, asset, model, reference, approval, or production provenance incomplete",
    }
    blockers = [message for key, message in checks.items() if context.get(key)]
    if blockers:
        return {"allowed": False, "reason": "animation governance blocker", "blockers": blockers}
    return {"allowed": True, "reason": "animation support package approved after qualified human review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS
