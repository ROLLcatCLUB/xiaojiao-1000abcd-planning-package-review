from __future__ import annotations

import argparse
import hashlib
import json
import py_compile
import re
import sys
import zipfile
from pathlib import Path
from typing import Any


STAGE_CODE = "1000A_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT"
FINAL_STATUS = "XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT_PASS"
SLUG = "xiaojiao_teacher_jarvis_workbench_concept_contract_1000A"
MARKER = "ALL_1000A_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT_CHECKS_OK"


REQUIRED_FILES = [
    "docs/handoff/xiaojiao_teacher_jarvis_workbench_1000A_execution_handoff_20260612.md",
    "docs/handoff/teacher_jarvis_workbench_planning_notes_1000_20260612.md",
    f"docs/foundation/{SLUG}.md",
    f"docs/foundation/{SLUG}.json",
    f"docs/audit/{SLUG}_report.md",
    f"docs/audit/{SLUG}_result.json",
    f"docs/audit/{SLUG}_checklist.json",
    f"docs/audit_packages/{SLUG}_manifest.json",
    f"docs/audit_packages/{SLUG}.zip",
    f"scripts/validate_{SLUG}.py",
]

PRIMARY_EN = [
    "Unified Xiaojiao Agent",
    "Agent-led Progressive Workspace",
    "Dynamic Work Panel",
    "Work Object",
    "Work Action",
    "Work State",
]

PRIMARY_ZH = [
    "统一小教智能体",
    "小教主导的渐进式工作台",
    "动态工作面板",
    "工作对象",
    "工作动作",
    "工作状态",
]

SUPPORT_EN = [
    "Work View Composer",
    "Assistant Surface",
]

SUPPORT_ZH_ACCEPTED = {
    "Work View Composer": ["工作视图组合器"],
    "Assistant Surface": ["小教表层", "助手表层", "小教交互表层", "助手交互表层"],
}

ASSISTANT_STATES = ["collapsed", "suggestion_bar", "mini_chat_overlay", "work_record_drawer"]
PANEL_FIELDS = [
    "panel_id",
    "panel_type",
    "artifact_type",
    "title",
    "status",
    "mode",
    "priority",
    "context",
    "visible_fields",
    "hidden_fields",
    "missing_info",
    "available_actions",
    "linked_objects",
    "layout_region",
]
PANEL_MODES = ["empty", "intake", "draft", "working", "review"]
FUTURE_MILESTONE_PREFIXES = ["1000B", "1000C", "1000D", "1000E"]

SAFE_FALSE_FLAGS = [
    "database_written",
    "memory_written",
    "feishu_written",
    "formal_export_created",
    "classroom_student_runtime_connected",
    "provider_called",
    "frontend_runtime_modified",
    "backend_runtime_modified",
    "old_sealed_stage_modified",
    "full_repo_blind_rename_performed",
    "teacher_facing_jarvis_wording_introduced",
    "teacher_facing_xiaobei_wording_introduced",
]

FORBIDDEN_NAME_PATTERNS = [
    ".env",
    "token",
    "secret",
    ".db",
    ".sqlite",
    ".sqlite3",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(read_text(path))
    require(isinstance(data, dict), f"JSON root must be object: {path}")
    return data


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def flat_text(*payloads: Any) -> str:
    return "\n".join(json.dumps(payload, ensure_ascii=False, sort_keys=True) for payload in payloads)


def require_all_text(text: str, values: list[str], label: str) -> None:
    missing = [value for value in values if value not in text]
    require(not missing, f"{label} missing: {missing}")


def require_false_flags(flags: dict[str, Any], label: str) -> None:
    for key in SAFE_FALSE_FLAGS:
        require(flags.get(key) is False, f"{label} flag must be false: {key}")


def check_allowed_false(contract: dict[str, Any]) -> None:
    for key in [
        "runtime_change_allowed",
        "ui_implementation_allowed",
        "provider_call_allowed",
        "database_write_allowed",
        "memory_write_allowed",
        "feishu_write_allowed",
        "formal_export_allowed",
        "classroom_student_runtime_allowed",
        "full_repo_blind_rename_allowed",
    ]:
        require(contract.get(key) is False, f"contract must set {key}=false")
    required = contract.get("boundary_flags_required") or {}
    for key in [
        "runtime_change_allowed",
        "ui_implementation_allowed",
        "provider_call_allowed",
        "database_write_allowed",
        "memory_write_allowed",
        "feishu_write_allowed",
        "formal_export_allowed",
        "classroom_student_runtime_allowed",
        "full_repo_blind_rename_allowed",
    ]:
        require(required.get(key) is False, f"boundary_flags_required must set {key}=false")


def validate_contract(root: Path, md_text: str, contract: dict[str, Any]) -> None:
    require(contract.get("stage_code") == STAGE_CODE, "contract stage_code mismatch")
    require(contract.get("final_status_target") == FINAL_STATUS, "contract final_status_target mismatch")
    require(contract.get("stage_type") == "concept_contract_only", "contract stage_type mismatch")
    check_allowed_false(contract)

    source_handoffs = contract.get("source_handoffs") or contract.get("source_handoff")
    require(isinstance(source_handoffs, list) and len(source_handoffs) >= 2, "source handoffs must be a list with at least two entries")
    for rel in source_handoffs:
        require((root / rel).exists(), f"source handoff missing: {rel}")

    combined = flat_text(contract, md_text)
    require_all_text(combined, PRIMARY_EN, "primary English concepts")
    require_all_text(combined, PRIMARY_ZH, "primary Chinese concepts")
    require_all_text(combined, SUPPORT_EN, "support English concepts")
    for concept, zh_options in SUPPORT_ZH_ACCEPTED.items():
        require(any(option in combined for option in zh_options), f"support Chinese concept missing for {concept}: {zh_options}")
    require_all_text(combined, ASSISTANT_STATES, "assistant surface states")
    require_all_text(combined, PANEL_FIELDS, "dynamic work panel fields")
    require_all_text(combined, PANEL_MODES, "panel modes")
    require("Unified Xiaojiao Agent\n-> leads Agent-led Progressive Workspace\n-> organizes Dynamic Work Panel\n-> displays Work Object\n-> advances through Work Action\n-> updates Work State" in md_text, "concept relationship chain missing in markdown")

    product = contract.get("product_identity") or {}
    require(product.get("teacher_facing_jarvis_allowed") is False, "teacher-facing Jarvis must not be allowed")
    naming = contract.get("naming_policy") or {}
    require(naming.get("blind_full_repository_rename_allowed") is False, "blind rename must be forbidden")
    require(naming.get("allowlist_based_rename_only") is True, "allowlist rename rule missing")
    legacy = contract.get("legacy_namespace_policy") or {}
    require(legacy.get("legacy_internal_namespace") is True, "legacy_internal_namespace must be true")
    metaphor = contract.get("internal_metaphor_policy") or {}
    require(metaphor.get("internal_planning_metaphor_only") is True, "Jarvis internal metaphor policy missing")
    require(metaphor.get("teacher_facing_copy_allowed") is False, "teacher-facing Jarvis copy must be false")

    dw_panel = contract.get("dynamic_work_panel_contract") or {}
    require(dw_panel.get("not_fixed_card") is True, "Dynamic Work Panel must not be fixed card")
    require(dw_panel.get("raw_ai_text_as_panel_body_allowed") is False, "raw AI text panel body must be disallowed")
    require(set(PANEL_FIELDS) <= set(dw_panel.get("stable_envelope_fields") or []), "dynamic panel envelope incomplete")
    require(set(PANEL_MODES) <= set(contract.get("panel_modes") or []), "panel modes incomplete")

    require(contract.get("work_object_contract", {}).get("minimum_fields"), "work object contract missing")
    require(contract.get("work_action_contract", {}).get("minimum_fields"), "work action contract missing")
    require(contract.get("work_state_contract", {}).get("minimum_fields"), "work state contract missing")
    require(contract.get("pre_class_work_chain"), "pre_class_work_chain missing")
    weekly = contract.get("weekly_work_graph_definition") or {}
    require(weekly.get("replaces_semester_weekly_calendar") is False, "weekly work graph must not replace semester_weekly_calendar")
    require("semester_weekly_calendar" in flat_text(weekly), "weekly work graph definition must mention semester_weekly_calendar")
    require(contract.get("today_work_item_definition", {}).get("types"), "today work item types missing")
    require(contract.get("quickclass_boundary"), "quickclass boundary missing")
    require((contract.get("quickclass_boundary") or {}).get("student_side_runtime_allowed_in_1000A") is False, "student runtime boundary mismatch")
    require(len(contract.get("prohibited_patterns") or []) >= 20, "prohibited_patterns must include at least 20 entries")
    milestones = contract.get("future_milestones") or []
    for prefix in FUTURE_MILESTONE_PREFIXES:
        require(any(str(item).startswith(prefix) for item in milestones), f"future milestone missing: {prefix}")
    require("1000A resolves product-shape boundary but does not finalize all teacher-facing naming decisions" in md_text, "open questions deferral missing")


def validate_audit(root: Path, contract: dict[str, Any]) -> None:
    result = load_json(root / f"docs/audit/{SLUG}_result.json")
    require(result.get("stage_code") == STAGE_CODE, "result stage_code mismatch")
    require(result.get("final_status") == FINAL_STATUS, "result final_status mismatch")
    require(result.get("pass") is True, "result pass must be true")
    for key in [
        "concept_contract_created",
        "json_contract_created",
        "checklist_created",
        "report_created",
        "manifest_created",
        "zip_created",
        "validator_created",
        "naming_policy_pass",
        "legacy_namespace_policy_pass",
        "internal_metaphor_policy_pass",
        "core_concepts_pass",
        "supporting_concepts_pass",
        "assistant_surface_pass",
        "dynamic_work_panel_pass",
        "workbench_positioning_pass",
        "pre_class_work_chain_pass",
        "weekly_work_graph_pass",
        "today_work_items_pass",
        "quickclass_boundary_pass",
        "prohibited_patterns_pass",
        "future_milestones_pass",
        "validator_no_arg_pass",
        "validator_root_pass",
        "manifest_zip_alignment_pass",
        "forbidden_files_pass",
    ]:
        require(result.get(key) is True, f"result must set {key}=true")
    require_false_flags(result.get("boundary_flags") or {}, "result boundary_flags")
    require(result.get("next_recommended_stage") == "1000B_EDUCATION_PRE_CLASS_WORK_SAMPLE_ROOM_BUSINESS_STRUCTURE", "next stage mismatch")

    checklist = load_json(root / f"docs/audit/{SLUG}_checklist.json")
    items = checklist.get("items") or []
    require(len(items) >= 30, "checklist must include at least 30 items")
    require(all(item.get("status") == "PASS" for item in items), "checklist contains non-PASS item")

    report = read_text(root / f"docs/audit/{SLUG}_report.md")
    require_all_text(
        report,
        [
            STAGE_CODE,
            FINAL_STATUS,
            "Jarvis is an internal planning metaphor only",
            "周工作图谱",
            "学期周历表",
            "QuickClass",
            "1000B_EDUCATION_PRE_CLASS_WORK_SAMPLE_ROOM_BUSINESS_STRUCTURE",
            MARKER,
        ],
        "report",
    )
    require("1000A resolves the product-shape boundary but does not finalize every future teacher-facing naming decision" in report, "report must defer open questions")
    require(set(contract.get("future_milestones") or []) <= set(re.findall(r"1000[A-Z]_[A-Z0-9_]+", report)), "report missing future milestone text")


def validate_manifest_zip(root: Path) -> None:
    manifest_path = root / f"docs/audit_packages/{SLUG}_manifest.json"
    manifest = load_json(manifest_path)
    require(manifest.get("stage_code") == STAGE_CODE, "manifest stage_code mismatch")
    require(manifest.get("final_status") == FINAL_STATUS, "manifest final_status mismatch")
    require(manifest.get("zip_path") == f"docs/audit_packages/{SLUG}.zip", "manifest zip_path mismatch")
    require(manifest.get("manifest_minus_zip") == [], "manifest_minus_zip must be []")
    require(manifest.get("zip_minus_manifest") == [], "zip_minus_manifest must be []")

    entries = manifest.get("entries") or []
    zip_entries = manifest.get("zip_entries") or []
    require(zip_entries, "zip_entries missing")
    require(all(isinstance(item, str) for item in zip_entries), "zip_entries must be strings")
    metadata_by_path = {item.get("path"): item for item in entries if isinstance(item, dict)}
    for rel in zip_entries:
        path = Path(rel)
        require(not path.is_absolute(), f"absolute zip entry forbidden: {rel}")
        require("\\" not in rel, f"zip entry must use slash separators: {rel}")
        require(".." not in path.parts, f"zip entry traversal forbidden: {rel}")
        lowered = rel.lower()
        require(not any(pattern in lowered for pattern in FORBIDDEN_NAME_PATTERNS), f"forbidden file name pattern: {rel}")
        require((root / rel).exists(), f"zip source missing: {rel}")
        if rel != f"docs/audit_packages/{SLUG}_manifest.json":
            meta = metadata_by_path.get(rel)
            require(meta is not None, f"metadata missing for entry: {rel}")
            require(meta.get("size") == (root / rel).stat().st_size, f"size mismatch: {rel}")
            require(str(meta.get("sha256", "")).upper() == sha256_file(root / rel), f"sha256 mismatch: {rel}")
    manifest_meta = metadata_by_path.get(f"docs/audit_packages/{SLUG}_manifest.json")
    require(manifest_meta is not None, "manifest metadata entry missing")
    require(manifest_meta.get("sha256") == "SELF_REFERENTIAL", "manifest self sha256 must be SELF_REFERENTIAL")

    zip_path = root / f"docs/audit_packages/{SLUG}.zip"
    require(zip_path.exists(), "zip file missing")
    with zipfile.ZipFile(zip_path, "r") as zf:
        actual_entries = sorted(zf.namelist())
    require(actual_entries == sorted(zip_entries), f"zip entries mismatch: {actual_entries} != {sorted(zip_entries)}")
    require(manifest.get("zip_entry_count") == len(zip_entries), "zip_entry_count mismatch")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=None)
    args = parser.parse_args()
    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parents[1]

    missing = [rel for rel in REQUIRED_FILES if not (root / rel).exists()]
    require(not missing, f"missing required files: {missing}")

    py_compile.compile(str(root / f"scripts/validate_{SLUG}.py"), doraise=True)

    contract_md = read_text(root / f"docs/foundation/{SLUG}.md")
    contract = load_json(root / f"docs/foundation/{SLUG}.json")
    validate_contract(root, contract_md, contract)
    validate_audit(root, contract)
    validate_manifest_zip(root)

    print(MARKER)


if __name__ == "__main__":
    main()
