# Xiaojiao Teacher Jarvis Workbench Concept Contract 1000A

## Stage Identity

```text
stage_code=1000A_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT
stage_name=Xiaojiao Teacher Jarvis Workbench Concept Contract
final_status_target=XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT_PASS
stage_type=concept_contract_only
runtime_change_allowed=false
ui_implementation_allowed=false
```

This stage is a concept contract only. It does not implement UI, connect runtime, call a provider/model, write database, write memory, write Feishu, create formal export, rename the repository, or modify old sealed stages.

## Background

1000A exists because the previous teaching-planning line exposed a product-shape risk. Continuing directly into the narrow `0998N` implementation would deepen the current teaching-planning page before the new workspace model is defined.

The current direction is not:

- a better chat page
- a better fixed module page
- a teaching-planning generator
- a fixed card UI
- one assistant per business module

The correct next move is to lock the system-level product shape first:

```text
Unified Xiaojiao Agent
-> leads Agent-led Progressive Workspace
-> organizes Dynamic Work Panel
-> displays Work Object
-> advances through Work Action
-> updates Work State
```

This makes 1000A the necessary boundary stage before any later UI, renderer, or runtime implementation.

## Product Identity

The product agent name from this line forward is:

```text
Chinese: 小教智能体
English: Xiaojiao Agent
```

`Jarvis` is an internal planning metaphor only. Teacher-facing product copy must not use `Jarvis` unless a later branding stage explicitly approves it.

Product definition:

```text
统一小教智能体根据工作状态，主导渐进式工作台，把教师的工作对象以动态工作面板呈现出来，并通过工作动作持续推进教师完成课前专业工作。
```

Xiaojiao is not a traditional page system, not a pure chat robot, and not a collection of fragmented page assistants. Xiaojiao is the unified teacher work agent that understands the current work, organizes work objects, composes dynamic panels, and exposes next actions only when useful.

## Naming and Legacy Boundary

New planning packages, new contracts, new schemas, new teacher-facing copy, new UI component display names, and new audit descriptions must use `小教 / Xiaojiao`.

Legacy names:

- `小备`
- `Xiaobei`
- `xiaobei`
- `xiaobei_agent`

These remain legacy internal namespace terms. Existing repository name, old stage file names, old validator markers, old audit packages, old sealed contracts, existing imports, and historical READMEs are not force-renamed in 1000A.

Rules:

- New teacher-facing copy uses `小教`.
- New system concepts use `Xiaojiao`.
- Internal legacy references may remain when marked as `legacy_internal_namespace=true`.
- Blind full-repository rename is forbidden.
- Rename must be allowlist-based only.
- 1000A defines the boundary; it does not perform broad rename migration.

## Core Concepts

### Unified Xiaojiao Agent / 统一小教智能体

The single Xiaojiao agent is the system's unified teacher work agent. It is not split by teaching planning, teaching design, classroom design, evaluation, resources, or research modules.

It is responsible for:

- understanding teacher intent
- identifying current work goals
- selecting active work objects
- maintaining Work State
- coordinating Dynamic Work Panel display
- deciding Work Action candidates
- triggering generate, modify, derive, sync, review, and confirm flows
- requiring confirmation before side-effectful actions

Forbidden patterns:

- one independent agent per page
- one assistant per business module
- multiple agents competing for the primary teacher response
- mock, router, or fallback content taking over the teacher-facing answer

### Agent-led Progressive Workspace / 小教主导的渐进式工作台

The workspace is not a fixed menu of modules. It is progressively organized by Xiaojiao according to the teacher's current task and Work State.

Principles:

- The task comes before the page.
- The workspace gradually expands as the teacher's work becomes clearer.
- The teacher should not need to know which module to open first.
- Irrelevant modules should not be exposed by default.
- Work objects and panels appear because they are useful to the active task.

### Dynamic Work Panel / 动态工作面板

Dynamic Work Panel is a task-aware view container. It is not a static card.

The same panel type can show different fields, actions, and summaries depending on teacher role, work scope, current task, known fields, missing information, generated candidates, linked artifacts, and review readiness.

It must not simply inject raw AI reply text into a card. It must be rendered through Work State and renderer mapping.

### Work Object / 工作对象

Work Object is the business object the teacher is actually working on.

Examples:

- teaching work plan
- unit lesson allocation
- semester weekly calendar
- weekly work graph
- today work items
- lesson design
- learning task sheet
- evaluation rubric
- classroom preparation package
- student work to evaluate
- resource package
- activity material
- research material

Work Object is not a page and not chat history. It can be generated, modified, derived, linked, synchronized, reviewed, and confirmed.

### Work Action / 工作动作

Work Action is the operation applied to a Work Object.

Suggested action types:

- `CLARIFY`
- `GENERATE`
- `MODIFY`
- `DERIVE`
- `SYNC`
- `REVIEW`
- `CONFIRM`
- `BLOCK`
- `PREPARE_EXPORT`
- `RECORD`

Any action that writes, exports, overwrites, submits, stores memory, or writes Feishu must require confirmation in later runtime stages. 1000A itself performs none of those actions.

### Work State / 工作状态

Work State is the structured state that prevents repeated questioning, random module jumps, chat black boxes, and token waste.

It tracks:

- current goal
- active domain
- active work scope
- active work objects
- known fields
- missing fields
- pending questions
- pending confirmations
- generated candidates
- work items
- linked artifacts
- next recommended actions
- last action
- assistant surface state
- renderer state
- boundary flags

Every later turn should be interpreted as an incremental update to Work State, not a restart from zero.

## Supporting Concepts

### Work View Composer / 工作视图组合器

Work View Composer converts Work State into visible workspace layout.

It decides:

- which Dynamic Work Panels appear
- panel order and priority
- which panel fields are visible or hidden
- which actions are exposed
- where the Assistant Surface sits
- what stays in work record instead of the primary workspace

Without Work View Composer, the system can fall back into a simple Agent + card + state model. 1000A requires it as a support concept.

### Assistant Surface / 小教交互表层

Assistant Surface is the lightweight interaction layer between Xiaojiao and the teacher.

Accepted Chinese aliases for validation:

- `小教表层`
- `助手表层`
- `小教交互表层`
- `助手交互表层`

Assistant Surface is not the full default workspace. It should provide suggestions, confirmations, mini dialogue, and work records when needed.

## Concept Relationship

```text
Unified Xiaojiao Agent
-> leads Agent-led Progressive Workspace
-> organizes Dynamic Work Panel
-> displays Work Object
-> advances through Work Action
-> updates Work State
```

Support layers:

```text
Work State
-> Work View Composer
-> Dynamic Work Panel layout
-> Assistant Surface
```

## Assistant Surface Policy

Assistant Surface states:

- `collapsed`: only the Xiaojiao entry is visible.
- `suggestion_bar`: Xiaojiao shows a compact current suggestion or next action.
- `mini_chat_overlay`: a temporary small dialogue surface appears for clarification or confirmation.
- `work_record_drawer`: historical dialogue and work trace can be opened without occupying the default main workspace.

Default teacher experience must not be full chat history. Conversation is input and confirmation, not the main content container.

## Dynamic Work Panel Contract

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

Rules:

- Dynamic Work Panel is not a fixed card.
- It must not show all fields by default.
- It must not treat raw AI text as the final panel body.
- It must be derived from Work State through Work View Composer and renderer mapping.

## Work Object Contract

Minimum fields:

- `object_id`
- `object_type`
- `display_name`
- `domain`
- `work_scope`
- `status`
- `field_schema_ref`
- `linked_objects`
- `source_objects`
- `available_actions`
- `missing_info`
- `last_updated`
- `owner_role`

## Work Action Contract

Minimum fields:

- `action_id`
- `action_type`
- `source_object`
- `target_object`
- `required_fields`
- `optional_fields`
- `side_effect_level`
- `requires_confirmation`
- `teacher_facing_label`
- `result_state_patch`

## Work State Contract

Minimum fields:

- `current_goal`
- `active_domain`
- `active_work_scope`
- `active_work_objects`
- `known_fields`
- `missing_fields`
- `pending_questions`
- `pending_confirmations`
- `generated_candidates`
- `work_items`
- `linked_artifacts`
- `next_recommended_actions`
- `last_action`
- `assistant_surface_state`
- `renderer_state`
- `boundary_flags`

## Teacher Workbench Positioning

Teaching planning should evolve into the teacher daily workbench / teacher home, not stay as a single document generator.

The workbench should answer:

- What should the teacher complete this semester?
- What should the teacher move forward this week?
- What should the teacher do today?
- Which lessons need preparation?
- Which student work needs evaluation?
- Which tasks need adjustment?
- Which materials need submission?
- Which issues need immediate handling?

Current focus is pre-class professional work. Classroom design, classroom execution, and evaluation are later submodules. 1000A does not connect student-side classroom runtime.

## Pre-Class Work Chain

```text
teacher role profile
-> semester teaching work plan
-> unit lesson allocation
-> semester weekly calendar
-> weekly work graph
-> today work items
-> lesson design
-> learning task sheet
-> evaluation rubric
-> classroom preparation package
```

The first sample role can be primary art teacher in 1000B, but art-teacher logic must not become a system-wide hardcoded rule.

## Weekly Work Graph Definition

`周工作图谱` does not replace `学期周历表`.

Definitions:

- `学期周历表 / semester_weekly_calendar`: semester progress supporting table; it answers which week teaches what.
- `周工作图谱 / weekly_work_graph`: higher-level weekly work panel; it organizes what to teach, prepare, evaluate, adjust, submit, handle, and carry over this week.

Weekly Work Graph should be derived from semester plan, semester weekly calendar, timetable, activity conflicts, evaluation tasks, resource preparation, and pending work items.

Suggested fields:

- `week_no`
- `date_range`
- `teaching_focus`
- `lesson_tasks`
- `prep_tasks`
- `evaluation_tasks`
- `student_followup_tasks`
- `resource_tasks`
- `activity_conflicts`
- `adjustment_notes`
- `urgent_issues`
- `pending_plans`
- `completed_items`
- `next_week_carryover`

## Today Work Item Definition

Work item types:

- `prepare_lesson`
- `design_learning_task`
- `prepare_resource`
- `evaluate_student_work`
- `adjust_plan`
- `submit_material`
- `review_progress`
- `handle_issue`
- `plan_activity`
- `generate_document`
- `reflect_and_summarize`

Minimum fields:

- `work_item_id`
- `type`
- `title`
- `source`
- `related_work_objects`
- `related_classes`
- `due_date`
- `priority`
- `status`
- `next_action`
- `completion_condition`

## QuickClass Boundary

QuickClass's main battlefield is classroom execution and learning analytics: classroom activity, student-side interaction, assignment flow, and learning feedback.

Xiaojiao's current battlefield is pre-class teacher professional work:

- semester teaching work plan
- unit lesson allocation
- semester weekly calendar
- weekly work graph
- today work items
- lesson design
- learning task sheet
- evaluation rubric
- classroom preparation package
- research and activity materials

1000A does not build a QuickClass-like classroom execution system and does not connect classroom student runtime.

## Prohibited Patterns

1000A prohibits:

1. left-side large chat box as the primary workspace
2. traditional module-menu stacking as the default product shape
3. multiple business-specific Xiaojiao agents
4. one assistant per page
5. fixed dead cards
6. raw AI reply text used as panel content without Work State mapping
7. chat history occupying the default main workspace
8. classroom student-side runtime connection
9. provider/model call
10. database write
11. memory write
12. Feishu write
13. formal export
14. blind full-repository rename
15. global replacement of `小备` with `小教`
16. teacher-facing use of `Jarvis`
17. using `周工作图谱` as a replacement name for `学期周历表`
18. treating supporting artifacts as the teaching work plan main document
19. implementing real UI in 1000A
20. modifying old sealed stages
21. hardcoding primary art teacher logic as system-wide logic
22. exposing engineering words such as dry-run, fixture, validator, stage, or boundary flags in teacher-facing primary copy
23. making 1000A a runtime behavior change
24. executing `0998N` inside this milestone

## Open Questions Deferred

1000A resolves product-shape boundary but does not finalize all teacher-facing naming decisions. Unresolved naming, UI terminology, and final presentation choices are deferred to 1000B/1000C.

Examples of deferred questions:

- final teacher-facing name for the broader workbench entry
- final UI label for Dynamic Work Panel
- whether `教学规划` is renamed in UI or reinterpreted internally first
- exact display language for weekly work graph in teacher-facing UI

## Future Milestones

- `1000B_EDUCATION_PRE_CLASS_WORK_SAMPLE_ROOM_BUSINESS_STRUCTURE`
- `1000C_DYNAMIC_WORK_PANEL_CONTRACT`
- `1000D_AGENT_ACTION_POLICY_AND_WORK_STATE_CONTRACT`
- `1000E_ART_TEACHER_PRE_CLASS_WORKBENCH_PILOT`

## Validation Requirements

1000A validation must confirm:

- required files exist
- stage identity is consistent
- final status target is correct
- stage type is `concept_contract_only`
- runtime/UI/provider/database/memory/Feishu/export/student-runtime/blind-rename boundaries are false
- six primary concepts exist in English and Chinese
- two support concepts exist in English and Chinese
- Assistant Surface states exist
- Dynamic Work Panel envelope and modes exist
- pre-class work chain exists
- weekly work graph does not replace semester weekly calendar
- today work item definition exists
- QuickClass boundary exists
- prohibited patterns count is at least 20
- future milestones include 1000B/1000C/1000D/1000E
- result boundary flags are safe
- manifest and ZIP are aligned
- no forbidden files or absolute paths are in the ZIP

