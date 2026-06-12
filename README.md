# Xiaojiao 1000A-1000D Planning Package Review

This repository is a dedicated GitHub review area for:

1000_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_PLANNING_PACKAGE

It is not the full xiaobei-core source repository.

## Stages

| Stage | final_status | Validator marker |
| --- | --- | --- |
| 1000A_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT | XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT_PASS | ALL_1000A_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_CONCEPT_CONTRACT_CHECKS_OK |
| 1000B_EDUCATION_PRE_CLASS_WORK_SAMPLE_ROOM_BUSINESS_STRUCTURE | XIAOJIAO_EDUCATION_PRE_CLASS_WORK_SAMPLE_ROOM_BUSINESS_STRUCTURE_PASS | ALL_1000B_EDUCATION_PRE_CLASS_WORK_SAMPLE_ROOM_BUSINESS_STRUCTURE_CHECKS_OK |
| 1000C_DYNAMIC_WORK_PANEL_CONTRACT | XIAOJIAO_DYNAMIC_WORK_PANEL_CONTRACT_PASS | ALL_1000C_DYNAMIC_WORK_PANEL_CONTRACT_CHECKS_OK |
| 1000D_AGENT_ACTION_POLICY_AND_WORK_STATE_CONTRACT | XIAOJIAO_AGENT_ACTION_POLICY_AND_WORK_STATE_CONTRACT_PASS | ALL_1000D_AGENT_ACTION_POLICY_AND_WORK_STATE_CONTRACT_CHECKS_OK |

## Validator commands

`powershell
python scripts/validate_xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.py
python scripts/validate_xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.py --root .
python scripts/validate_xiaojiao_education_pre_class_work_sample_room_business_structure_1000B.py
python scripts/validate_xiaojiao_education_pre_class_work_sample_room_business_structure_1000B.py --root .
python scripts/validate_xiaojiao_dynamic_work_panel_contract_1000C.py
python scripts/validate_xiaojiao_dynamic_work_panel_contract_1000C.py --root .
python scripts/validate_xiaojiao_agent_action_policy_and_work_state_contract_1000D.py
python scripts/validate_xiaojiao_agent_action_policy_and_work_state_contract_1000D.py --root .
`

## ZIP artifacts

- docs/audit_packages/xiaojiao_teacher_jarvis_workbench_concept_contract_1000A.zip
- docs/audit_packages/xiaojiao_education_pre_class_work_sample_room_business_structure_1000B.zip
- docs/audit_packages/xiaojiao_dynamic_work_panel_contract_1000C.zip
- docs/audit_packages/xiaojiao_agent_action_policy_and_work_state_contract_1000D.zip

## Review prompt

请审核这个 GitHub review area，判断 1000A-1000D 是否可以作为连续规划包收下：

- 每个阶段 final_status 是否可收
- validator no-arg / --root 通过证据是否成立
- 每个 manifest 的 manifest_minus_zip / zip_minus_manifest 是否为空
- ZIP 内部路径是否 clean，是否没有绝对路径
- 是否夹带 forbidden files
- 是否违反硬边界：不实现 UI、不接 runtime/provider/model/database/memory/Feishu/formal export/课堂学生端、不 blind rename
- 是否正确处理 小教 / Xiaojiao 命名边界
- 是否正确把 Jarvis 限定为内部隐喻
- 是否没有把 Dynamic Work Panel 做成固定死卡片
- 是否没有把小教拆成多个业务 Agent
- 是否没有让周工作图谱替代学期周历表
- 是否可以把最终 next_stage 标记为 1000E_ART_TEACHER_PRE_CLASS_WORKBENCH_PILOT_PENDING_REVIEW

注意：这里是 review area，不是完整源码仓库。1000A-1000D 都是规划/contract 包，不是 UI/runtime apply。