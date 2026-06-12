from __future__ import annotations

import argparse
import json
import sys
import zipfile
from pathlib import Path


STAGE_CODE = '1000D_AGENT_ACTION_POLICY_AND_WORK_STATE_CONTRACT'
FINAL_STATUS = 'XIAOJIAO_AGENT_ACTION_POLICY_AND_WORK_STATE_CONTRACT_PASS'
SLUG = 'xiaojiao_agent_action_policy_and_work_state_contract_1000D'
MARKER = 'ALL_1000D_AGENT_ACTION_POLICY_AND_WORK_STATE_CONTRACT_CHECKS_OK'
NEXT_STAGE = '1000E_ART_TEACHER_PRE_CLASS_WORKBENCH_PILOT_PENDING_REVIEW'
REQUIRED_FILES = ['docs/handoff/xiaojiao_teacher_jarvis_workbench_1000A_execution_handoff_20260612.md', 'docs/handoff/teacher_jarvis_workbench_planning_notes_1000_20260612.md', 'docs/foundation/xiaojiao_agent_action_policy_and_work_state_contract_1000D.md', 'docs/foundation/xiaojiao_agent_action_policy_and_work_state_contract_1000D.json', 'docs/audit/xiaojiao_agent_action_policy_and_work_state_contract_1000D_report.md', 'docs/audit/xiaojiao_agent_action_policy_and_work_state_contract_1000D_result.json', 'docs/audit/xiaojiao_agent_action_policy_and_work_state_contract_1000D_checklist.json', 'docs/audit_packages/xiaojiao_agent_action_policy_and_work_state_contract_1000D_manifest.json', 'scripts/validate_xiaojiao_agent_action_policy_and_work_state_contract_1000D.py']
BOUNDARY_FALSE_KEYS = ['database_written', 'memory_written', 'feishu_written', 'formal_export_created', 'classroom_student_runtime_connected', 'provider_called', 'frontend_runtime_modified', 'backend_runtime_modified', 'old_sealed_stage_modified', 'full_repo_blind_rename_performed', 'teacher_facing_jarvis_wording_introduced', 'teacher_facing_xiaobei_wording_introduced']
FORBIDDEN_PARTS = [".env", "token", "secret", "node_modules", "__pycache__", ".db", ".sqlite", "student_data", "provider_raw"]


def fail(message: str) -> None:
    raise SystemExit(f"VALIDATION_FAILED: {message}")


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"cannot read JSON {path}: {exc}")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=None)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parents[1]

    for rel in REQUIRED_FILES:
        if not (root / rel).exists():
            fail(f"missing required file: {rel}")

    contract = load_json(root / f"docs/foundation/{SLUG}.json")
    checklist = load_json(root / f"docs/audit/{SLUG}_checklist.json")
    result = load_json(root / f"docs/audit/{SLUG}_result.json")
    manifest = load_json(root / f"docs/audit_packages/{SLUG}_manifest.json")
    report_text = (root / f"docs/audit/{SLUG}_report.md").read_text(encoding="utf-8")
    contract_text = (root / f"docs/foundation/{SLUG}.md").read_text(encoding="utf-8")

    if contract.get("stage_code") != STAGE_CODE:
        fail("contract stage_code mismatch")
    if contract.get("final_status_target") != FINAL_STATUS:
        fail("contract final_status_target mismatch")
    if result.get("stage_code") != STAGE_CODE or result.get("final_status") != FINAL_STATUS or result.get("pass") is not True:
        fail("result identity/pass mismatch")
    if result.get("marker") != MARKER:
        fail("result marker mismatch")
    if checklist.get("stage_code") != STAGE_CODE:
        fail("checklist stage_code mismatch")
    if manifest.get("stage_code") != STAGE_CODE:
        fail("manifest stage_code mismatch")
    if contract.get("next_stage") != NEXT_STAGE or result.get("next_stage") != NEXT_STAGE:
        fail("next_stage mismatch")

    hard = contract.get("hard_boundaries", {})
    required_false = [
        "runtime_change_allowed",
        "ui_implementation_allowed",
        "provider_call_allowed",
        "database_write_allowed",
        "memory_write_allowed",
        "feishu_write_allowed",
        "formal_export_allowed",
        "classroom_student_runtime_allowed",
        "full_repo_blind_rename_allowed",
    ]
    for key in required_false:
        if hard.get(key) is not False:
            fail(f"hard boundary not false: {key}")

    flags = result.get("boundary_flags", {})
    for key in BOUNDARY_FALSE_KEYS:
        if flags.get(key) is not False:
            fail(f"unsafe boundary flag: {key}")

    required_terms = [
        "小教智能体",
        "Xiaojiao Agent",
        "Jarvis",
        "internal planning metaphor",
        "legacy internal namespace",
        "教学工作计划",
        "weekly_work_graph",
        "semester_weekly_calendar",
        "does not replace",
    ]
    combined = contract_text + "\n" + report_text + "\n" + json.dumps(contract, ensure_ascii=False)
    for term in required_terms:
        if term not in combined:
            fail(f"missing required term: {term}")

    if len(contract.get("prohibited_patterns", [])) < 20:
        fail("prohibited patterns fewer than 20")
    for prefix in ["1000B", "1000C", "1000D", "1000E"]:
        if not any(str(item).startswith(prefix) for item in contract.get("future_milestones", [])):
            fail(f"missing future milestone {prefix}")

    if STAGE_CODE.startswith("1000B"):
        sections = contract.get("stage_sections", {})
        profile = sections.get("teacher_role_profile", {})
        if profile.get("sample_role") != "primary_art_teacher":
            fail("1000B sample role mismatch")
        if profile.get("system_wide_hardcode_allowed") is not False:
            fail("1000B art role hardcode boundary missing")
        if "classroom_preparation_package_chain" not in sections:
            fail("1000B package chain missing")
    elif STAGE_CODE.startswith("1000C"):
        panel = contract.get("stage_sections", {}).get("panel_schema", {})
        for field in ["panel_id", "visible_fields", "hidden_fields", "available_actions", "linked_objects", "layout_region"]:
            if field not in panel.get("fields", []):
                fail(f"1000C panel field missing: {field}")
        if panel.get("fixed_card_component") is not False or panel.get("raw_ai_reply_container") is not False:
            fail("1000C fixed card/raw reply boundary missing")
    elif STAGE_CODE.startswith("1000D"):
        sections = contract.get("stage_sections", {})
        if sections.get("action_policy", {}).get("single_unified_agent") is not True:
            fail("1000D unified agent policy missing")
        if sections.get("action_policy", {}).get("business_specific_agent_split_allowed") is not False:
            fail("1000D agent split boundary missing")
        if "confirmation_gate" not in sections.get("gates", {}):
            fail("1000D confirmation gate missing")

    zip_path = root / f"docs/audit_packages/{SLUG}.zip"
    with zipfile.ZipFile(zip_path, "r") as zf:
        zip_entries = zf.namelist()
    for entry in zip_entries:
        normalized = entry.replace("\\", "/")
        if normalized.startswith("/") or ":" in normalized:
            fail(f"absolute or unsafe ZIP path: {entry}")
        lowered = normalized.lower()
        if any(part in lowered for part in FORBIDDEN_PARTS):
            fail(f"forbidden ZIP entry: {entry}")

    manifest_entries = manifest.get("zip_entries", [])
    if manifest.get("manifest_minus_zip") != [] or manifest.get("zip_minus_manifest") != []:
        fail("manifest alignment fields are not empty")
    if sorted(manifest_entries) != sorted(zip_entries):
        fail("manifest zip_entries do not match actual ZIP")
    if manifest.get("zip_entry_count") != len(zip_entries):
        fail("zip_entry_count mismatch")

    print(MARKER)
    return 0


if __name__ == "__main__":
    sys.exit(main())
