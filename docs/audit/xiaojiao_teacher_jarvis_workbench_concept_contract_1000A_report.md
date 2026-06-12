# 1000A Xiaojiao Teacher Jarvis Workbench Concept Contract Report

Stage: `1000A_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT`

Final status: `XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT_PASS`

Marker: `ALL_1000A_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT_CHECKS_OK`

## What 1000A Completed

1000A converts the planning handoff into a formal concept-contract review package for the Xiaojiao teacher dynamic workbench line.

It creates:

- concept contract markdown
- concept contract JSON
- audit checklist
- audit result
- audit report
- audit package manifest
- validator
- ZIP package

1000A locks the product-shape boundary:

```text
Unified Xiaojiao Agent
-> leads Agent-led Progressive Workspace
-> organizes Dynamic Work Panel
-> displays Work Object
-> advances through Work Action
-> updates Work State
```

It also requires two support concepts:

- `Work View Composer / 工作视图组合器`
- `Assistant Surface / 小教交互表层`

These support concepts prevent the later system from collapsing into only Agent + card + state.

## What 1000A Did Not Do

1000A did not:

- implement UI
- modify real frontend pages
- connect runtime
- call provider/model
- write database
- write memory
- write Feishu
- create formal export
- connect classroom student runtime
- modify old sealed stages
- perform blind repository rename
- execute `0998N`
- enter `1000B`

This is a concept-contract package, not runtime apply, not a seal, and not a teacher-facing implementation.

## Why 1000A Comes Before 0998N

The previous narrow next step was:

```text
0998N_SUBJECT_TEACHER_SEMESTER_WORK_PLAN_PILOT_READONLY
```

That narrow path remains technically valid, but continuing it first would deepen the current teaching-planning page shape before the product model is clear.

1000A comes first because the system needs to avoid returning to:

- left-side large chat + right-side business page
- traditional fixed module page
- teaching-planning-only generator
- fixed card UI
- multiple business-specific agents

1000A instead defines Xiaojiao as a unified teacher work agent that organizes work objects through a progressive dynamic workspace.

## Xiaojiao Naming Boundary

New product identity:

```text
Chinese: 小教智能体
English: Xiaojiao Agent
```

New planning packages, contracts, schemas, teacher-facing copy, UI component display names, and new audit descriptions should use `小教 / Xiaojiao`.

Legacy names:

- `小备`
- `Xiaobei`
- `xiaobei`

These remain allowed as legacy internal namespace only. The `xiaobei-core` repository name, old stage files, old validator markers, old audit packages, old sealed contracts, and existing import paths are not renamed in 1000A.

Rules:

- blind full-repository rename is forbidden
- rename must be allowlist-based
- internal legacy references should be marked `legacy_internal_namespace=true` in new contracts when relevant

## Internal Metaphor Policy

`Jarvis` is an internal planning metaphor only.

Jarvis is an internal planning metaphor only.

Teacher-facing product copy must not use `Jarvis` unless a later branding stage explicitly approves it.

1000A resolves the product-shape boundary but does not finalize every future teacher-facing naming decision. Unresolved UI terms and final display language are deferred to `1000B` and `1000C`.

## Core Concepts

Six primary concepts are defined:

- `Unified Xiaojiao Agent / 统一小教智能体`
- `Agent-led Progressive Workspace / 小教主导的渐进式工作台`
- `Dynamic Work Panel / 动态工作面板`
- `Work Object / 工作对象`
- `Work Action / 工作动作`
- `Work State / 工作状态`

Two support concepts are defined:

- `Work View Composer / 工作视图组合器`
- `Assistant Surface / 小教交互表层`

Assistant Surface accepts these Chinese aliases for later validation:

- `小教表层`
- `助手表层`
- `小教交互表层`
- `助手交互表层`

## Assistant Surface Policy

Assistant Surface states:

- `collapsed`
- `suggestion_bar`
- `mini_chat_overlay`
- `work_record_drawer`

Default teacher experience should not be full chat history.

Conversation is input and confirmation, not the main content container.

## Dynamic Work Panel

Dynamic Work Panel is a task-aware view container, not a fixed card.

Stable envelope fields:

- `panel_id`
- `panel_type`
- `artifact_type`
- `title`
- `status`
- `mode`
- `priority`
- `context`
- `visible_fields`
- `hidden_fields`
- `missing_info`
- `available_actions`
- `linked_objects`
- `layout_region`

Panel modes:

- `empty`
- `intake`
- `draft`
- `working`
- `review`

Dynamic Work Panel must be derived from Work State through Work View Composer and renderer mapping. It must not simply place raw AI reply text into a card.

## Weekly Work Graph And Semester Weekly Calendar

`周工作图谱` does not replace `学期周历表`.

Definitions:

- `学期周历表 / semester_weekly_calendar`: semester progress supporting table; answers which week teaches what.
- `周工作图谱 / weekly_work_graph`: higher-level weekly work panel; organizes what to teach, prepare, evaluate, adjust, submit, handle, and carry over this week.

This keeps supporting tables from being confused with the role-scoped teaching work plan main document.

## QuickClass Boundary

QuickClass focuses on classroom execution and learning analytics.

Xiaojiao currently focuses on pre-class teacher professional work:

- semester teaching work plan
- unit lesson allocation
- semester weekly calendar
- weekly work graph
- today work items
- lesson design
- learning task sheet
- evaluation rubric
- classroom preparation package

1000A does not build a QuickClass-like classroom execution system and does not connect student-side classroom runtime.

## Validation Evidence

Commands:

```text
python scripts/validate_xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.py
python scripts/validate_xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.py --root .
```

Expected marker:

```text
ALL_1000A_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT_CHECKS_OK
```

The validator checks:

- required file existence
- stage identity consistency
- final status target
- concept-contract-only boundary
- no UI/runtime/provider/database/memory/Feishu/export/student-runtime/blind-rename permissions
- six primary concepts in English and Chinese
- two support concepts in English and Chinese
- Assistant Surface states
- Dynamic Work Panel envelope and modes
- pre-class work chain
- weekly work graph does not replace `semester_weekly_calendar`
- today work item definition
- QuickClass boundary
- at least 20 prohibited patterns
- future milestones include 1000B/1000C/1000D/1000E
- safe boundary flags
- forbidden-file scan
- ZIP entry path safety
- manifest / ZIP alignment

## Manifest And ZIP

Package path:

```text
docs/audit_packages/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.zip
```

Manifest path:

```text
docs/audit_packages/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A_manifest.json
```

The validator requires:

```text
manifest_minus_zip=[]
zip_minus_manifest=[]
```

## Boundary Flags

All must remain false:

- `database_written`
- `memory_written`
- `feishu_written`
- `formal_export_created`
- `classroom_student_runtime_connected`
- `provider_called`
- `frontend_runtime_modified`
- `backend_runtime_modified`
- `old_sealed_stage_modified`
- `full_repo_blind_rename_performed`
- `teacher_facing_jarvis_wording_introduced`
- `teacher_facing_xiaobei_wording_introduced`

## Next Recommended Stage

```text
1000B_EDUCATION_PRE_CLASS_WORK_SAMPLE_ROOM_BUSINESS_STRUCTURE
```

Do not enter 1000B until 1000A is reviewed or explicitly accepted.

## Future Milestones

- `1000B_EDUCATION_PRE_CLASS_WORK_SAMPLE_ROOM_BUSINESS_STRUCTURE`
- `1000C_DYNAMIC_WORK_PANEL_CONTRACT`
- `1000D_AGENT_ACTION_POLICY_AND_WORK_STATE_CONTRACT`
- `1000E_ART_TEACHER_PRE_CLASS_WORKBENCH_PILOT`
