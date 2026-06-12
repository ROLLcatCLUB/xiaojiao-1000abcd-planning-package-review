# 1000C_DYNAMIC_WORK_PANEL_CONTRACT

Date: 2026-06-12

## Stage Identity

```text
package_code=1000_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_PLANNING_PACKAGE
stage_code=1000C_DYNAMIC_WORK_PANEL_CONTRACT
stage_name=Dynamic Work Panel Contract
stage_type=dynamic_panel_contract_only
final_status_target=XIAOJIAO_DYNAMIC_WORK_PANEL_CONTRACT_PASS
runtime_change_allowed=false
ui_implementation_allowed=false
```

## Purpose

Define Dynamic Work Panel as a renderer contract and state-derived view envelope, not a fixed card component.

This stage is a review package and contract artifact only. It does not implement UI, modify real frontend pages, connect runtime, call provider/model, write database, write memory, write Feishu, create formal export, connect classroom student-side runtime, modify old sealed stages, or perform blind repository rename.

## Source Handoffs

- `docs/handoff/xiaojiao_teacher_jarvis_workbench_1000A_execution_handoff_20260612.md`
- `docs/handoff/teacher_jarvis_workbench_planning_notes_1000_20260612.md`

## Product Identity And Naming Boundary

The product agent remains `小教智能体 / Xiaojiao Agent`.

`Jarvis` is an internal planning metaphor only. Teacher-facing product copy must use Xiaojiao / 小教 language and must not expose Jarvis unless a later branding stage explicitly approves it.

Old `小备 / Xiaobei / xiaobei` wording remains a legacy internal namespace. Blind full-repository rename is forbidden; any future rename must be allowlist-based.

## Main Document Boundary

`教学工作计划 / teaching_work_plan` remains the role-scoped main document. Supporting tables such as `单元课时分配`, `学期周历表`, `课务日程表`, and `课表` remain supporting artifacts and do not replace the main document.

## Weekly Work Graph Boundary

`周工作图谱 / weekly_work_graph` does not replace `学期周历表 / semester_weekly_calendar`.

- `学期周历表 / semester_weekly_calendar`: semester progress supporting table; answers which week teaches what.
- `周工作图谱 / weekly_work_graph`: higher-level weekly work panel; organizes what to teach, prepare, evaluate, adjust, submit, handle, and carry over this week.

## Stage Contract

```json
{
  "panel_schema": {
    "fields": [
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
      "render_intent",
      "teacher_safe_summary",
      "audit_trace_ref"
    ],
    "fixed_card_component": false,
    "raw_ai_reply_container": false
  },
  "panel_modes": [
    "empty",
    "intake",
    "draft",
    "working",
    "review",
    "blocked",
    "ready_to_confirm"
  ],
  "visible_hidden_field_rules": [
    "visible fields must be teacher-actionable or reviewable",
    "hidden fields may carry audit trace references and internal derivation state",
    "missing information must stay explicit until resolved",
    "provider prompts and raw responses must not be visible teacher content"
  ],
  "layout_rules": {
    "primary": "current work object and next safe action",
    "supporting": "linked artifacts and progress context",
    "assistant_surface": "suggestion or confirmation only when useful",
    "chat_history_default": "not primary workspace"
  },
  "display_rules": [
    "derive panel display from Work State through Work View Composer",
    "show status, gaps, linked artifacts, and available actions",
    "avoid engineering terms in teacher-facing primary experience",
    "preserve semester weekly calendar as supporting artifact when weekly work graph is visible"
  ]
}
```

## Hard Boundaries

```json
{
  "runtime_change_allowed": false,
  "ui_implementation_allowed": false,
  "provider_call_allowed": false,
  "database_write_allowed": false,
  "memory_write_allowed": false,
  "feishu_write_allowed": false,
  "formal_export_allowed": false,
  "classroom_student_runtime_allowed": false,
  "full_repo_blind_rename_allowed": false
}
```

## Validation Focus

- panel schema has stable envelope
- visible fields and actions are dynamic
- not a fixed card
- not raw AI reply display
- chat history does not dominate default workspace

## Prohibited Patterns

1. implement real UI
2. modify real frontend pages
3. connect runtime
4. call provider or model
5. write database
6. write memory
7. write Feishu
8. create formal export
9. connect classroom student runtime
10. modify old sealed stages
11. blind full-repository rename
12. globally replace Xiaobei with Xiaojiao
13. put Jarvis into teacher-facing product copy
14. make Dynamic Work Panel a fixed dead card
15. split Xiaojiao into multiple business agents
16. let chat history dominate the workspace
17. replace semester weekly calendar with weekly work graph
18. let supporting tables replace the teaching work plan main document
19. hardcode art-teacher logic as a system-wide rule
20. turn sample room into classroom execution runtime
21. expose audit flags in teacher-facing primary copy
22. skip validator before next stage

## Future Milestones

- `1000B_EDUCATION_PRE_CLASS_WORK_SAMPLE_ROOM_BUSINESS_STRUCTURE`
- `1000C_DYNAMIC_WORK_PANEL_CONTRACT`
- `1000D_AGENT_ACTION_POLICY_AND_WORK_STATE_CONTRACT`
- `1000E_ART_TEACHER_PRE_CLASS_WORKBENCH_PILOT`

Do not enter 1000E without explicit user authorization.

## Validation Requirements

- required files exist
- validator supports no-arg and `--root .`
- JSON contract, checklist, result, report, manifest, and ZIP exist
- stage identity and final status match
- all hard boundaries remain false
- no `.env`, token, secret, database, real student data, provider raw prompt/response, `node_modules`, or `__pycache__` enters the ZIP
- ZIP entries use relative `/` paths only
- `manifest_minus_zip=[]`
- `zip_minus_manifest=[]`

## Next Stage

```text
next_stage=1000D_AGENT_ACTION_POLICY_AND_WORK_STATE_CONTRACT
```
