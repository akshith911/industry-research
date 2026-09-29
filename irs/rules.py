"""Deterministic evidence rules. These are the only place tiers and confidence are decided."""
import re
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

TIER_BY_TYPE = {
    # Tier 1: primary
    "government": 1, "regulator": 1, "legislation": 1, "official_statistics": 1, "court_record": 1,
    "company_filing": 1, "annual_report": 1, "investor_presentation": 1, "company_documentation": 1,
    "industry_body": 1, "standards_body": 1,
    # Tier 2: high-quality secondary
    "research_firm": 2, "academic": 2, "financial_press": 2, "industry_press": 2,
    # Tier 3: discovery
    "news": 3, "blog": 3, "startup_database": 3, "forum": 3, "social": 3, "aggregator": 3,
    "encyclopedia": 3, "other": 3,
}

# fact-check verdict -> claim status
VERDICT_TO_STATUS = {
    "verified": "verified",
    "partially_verified": "partially_verified",
    "unsupported": "unsupported",
    "out_of_context": "unsupported",
    "refuted": "refuted",
    "outdated": "outdated",
    "source_unavailable": "unverified",
}

EVIDENCED_TYPES = {"fact", "reported_claim", "estimate"}
REASONING_TYPES = {"inference", "interpretation", "assumption"}


def compute_confidence(claim: dict, sources: dict) -> tuple:
    """Return (confidence, reason) from status, claim type and source quality."""
    status, ctype = claim["status"], claim["claim_type"]
    srcs = [sources[s] for s in claim.get("source_ids", []) if s in sources]
    if status == "unknown" or ctype == "unknown":
        return "unknown", "Documented gap: public evidence insufficient."
    if status in ("refuted", "unsupported", "outdated"):
        return "low", f"Fact-check result: {status}. Do not rely on this claim."
    if status == "conflicting":
        return "low", "Credible sources disagree; see contradiction ledger."
    if ctype in REASONING_TYPES or status in ("inferred", "assumption"):
        return "low", f"{ctype.capitalize()} by the research team, not directly evidenced."
    if status == "unverified":
        return "low", "Recorded by a researcher; not yet independently fact-checked."
    if not srcs:
        return "low", "No source attached."
    best = min(s["tier"] for s in srcs)
    publishers = {s["publisher"].strip().lower() for s in srcs}
    if status == "verified":
        if best == 1:
            conf, why = "high", "Independently verified against a tier-1 primary source."
        elif best == 2 or len(publishers) >= 2:
            conf, why = "medium", ("Verified against a tier-2 source." if best == 2
                                   else f"Verified; corroborated by {len(publishers)} independent tier-3 publishers.")
        else:
            conf, why = "low", "Verified, but only against a single tier-3 source."
    else:  # partially_verified
        conf, why = ("medium", "Partially verified against a tier-1 source.") if best == 1 else \
                    ("low", "Only partially verified, and not against a primary source.")
    if ctype == "reported_claim" and conf == "high":
        conf, why = "medium", why + " Capped at medium: the entity's own claim about itself."
    return conf, why


_TRACKING = re.compile(r"^(utm_|fbclid|gclid|mc_|ref$|ref_src$)")


def normalize_url(url: str) -> str:
    p = urlsplit(url.strip())
    query = urlencode([(k, v) for k, v in parse_qsl(p.query) if not _TRACKING.match(k)])
    path = p.path.rstrip("/") or "/"
    host = p.netloc.lower().removeprefix("www.")
    return urlunsplit(("https", host, path, query, ""))


def normalize_text(s: str) -> str:
    return re.sub(r"[^a-z0-9%.]+", " ", s.lower()).strip()
