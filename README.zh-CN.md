# Agent Harness Skills

这是一组可复用 skills，用来把一个项目建设成 agent 可稳定接手的工程：规则入口、设计文档、任务板、架构边界、验证命令、运行证据、协作记录、质量治理和原子化提交。

## 包含的 Skills

- `repo-harness-assessment`：评估仓库当前 agent/harness 成熟度，找出最小补强路径。
- `agent-entrypoint-design`：设计 `AGENTS.md`、镜像文件、指令优先级和事实源入口。
- `repo-contracts-and-boundaries`：把架构边界、目录边界、choke point、baseline/allowlist 变成机械检查。
- `validation-harness-design`：设计验证入口、test matrix、JSON/JUnit 输出和 CI 门禁。
- `runtime-evidence-and-tracing`：设计 run id、request id、artifact bundle、浏览器/真机/后端 trace 证据闭环。
- `agent-ledger-and-delivery`：设计 `agent_chats`/`agents_chat` 和 PR/交付证据汇总。
- `quality-gardening`：设计质量快照、结构指标、红线、债务收敛和质量报告。
- `design-doc-and-task-board`：抽象设计文档、`tasks.md`、exec plan、状态同步和验收规则。
- `atomic-commit-discipline`：抽象最小提交、提交前检查、提交信息、关联记录和禁止混入无关改动。

## 使用方式

把 agent runtime 指向本仓库的 `skills/` 目录即可。首版不是 Codex plugin，也不包含业务项目脚手架。

## 校验

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/validate_skill_quality.py
python3 scripts/check_skill_language.py
```

对 substantial skill wording changes，至少在 `docs/scenario-tests.md` 记录一个 realistic prompt 和 observed output。`SKILL.md` 正文统一使用英文。

## 适用问题

- “检查这个 repo 的 harness 缺什么”
- “给一个新项目设计 AGENTS.md 和验证入口”
- “把浏览器验证和后端 request id 串起来”
- “这个需求应该写 design doc 还是 tasks.md”
- “帮我把这批改动拆成原子提交”
