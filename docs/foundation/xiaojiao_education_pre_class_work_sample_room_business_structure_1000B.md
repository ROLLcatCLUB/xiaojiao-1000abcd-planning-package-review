# 1000B_EDUCATION_PRE_CLASS_WORK_SAMPLE_ROOM_BUSINESS_STRUCTURE

Date: 2026-06-12

## Stage Identity

```text
package_code=1000_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_PLANNING_PACKAGE
stage_code=1000B_EDUCATION_PRE_CLASS_WORK_SAMPLE_ROOM_BUSINESS_STRUCTURE
stage_name=Education Pre-Class Work Sample Room Business Structure
stage_type=business_structure_contract_only
final_status_target=XIAOJIAO_EDUCATION_PRE_CLASS_WORK_SAMPLE_ROOM_BUSINESS_STRUCTURE_PASS
runtime_change_allowed=false
ui_implementation_allowed=false
```

## Purpose

Define the education pre-class sample room business structure before any UI or runtime pilot.

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
  "teacher_role_profile": {
    "sample_role": "primary_art_teacher",
    "role_scope": "first sample role only",
    "system_wide_hardcode_allowed": false,
    "profile_slots": [
      "school_stage",
      "grade_band",
      "subject",
      "textbook_catalog",
      "semester_calendar",
      "class_count",
      "weekly_periods",
      "classroom_resource_conditions",
      "assessment_preference",
      "school_activity_windows"
    ]
  },
  "work_scopes": [
    "semester_preparation",
    "unit_preparation",
    "weekly_preparation",
    "daily_preparation",
    "classroom_material_preparation",
    "evaluation_preparation",
    "issue_follow_up"
  ],
  "pre_class_artifact_map": {
    "main_document": "teaching_work_plan",
    "supporting_artifacts": [
      "unit_lesson_allocation",
      "semester_weekly_calendar",
      "weekly_work_graph",
      "today_work_items",
      "lesson_design",
      "learning_task_sheet",
      "evaluation_rubric",
      "resource_pack",
      "classroom_preparation_package"
    ]
  },
  "classroom_preparation_package_chain": [
    "teacher_role_profile",
    "semester_teaching_work_plan",
    "unit_lesson_allocation",
    "semester_weekly_calendar",
    "weekly_work_graph",
    "today_work_items",
    "lesson_design",
    "learning_task_sheet",
    "evaluation_rubric",
    "resource_pack",
    "classroom_preparation_package"
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

- sample role is primary art teacher without system-wide hardcoding
- teaching work plan remains the main document
- supporting artifact graph is explicit
- weekly work graph does not replace semester weekly calendar
- classroom preparation package chain exists

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
next_stage=1000C_DYNAMIC_WORK_PANEL_CONTRACT
```
