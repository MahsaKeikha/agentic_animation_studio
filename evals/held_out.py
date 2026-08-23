"""Held-out governance scenarios for F140."""
from safety.policy import REQUIRED_REVIEWS, authorize


def base():
    return {key: True for key in REQUIRED_REVIEWS}


SCENARIOS = [
    ({}, False),
    (base(), True),
    (base() | {"rights_clearance_gap": True}, False),
    (base() | {"likeness_consent_gap": True}, False),
    (base() | {"continuity_failure": True}, False),
    (base() | {"accessibility_failure": True}, False),
    (base() | {"production_quality_gap": True}, False),
    (base() | {"credit_attribution_gap": True}, False),
    (base() | {"synthetic_media_disclosure_gap": True}, False),
    (base() | {"provenance_documentation_gap": True}, False),
]


def main():
    for index, (context, expected) in enumerate(SCENARIOS, 1):
        actual = authorize("release_support_package", context)["allowed"]
        assert actual is expected, f"scenario {index}: expected {expected}, got {actual}"
    print(f"F140 held-out governance: {len(SCENARIOS)}/{len(SCENARIOS)} passed")


if __name__ == "__main__":
    main()
