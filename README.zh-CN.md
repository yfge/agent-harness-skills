# Agent Harness Skills

一组可复用 skills，用来把真实软件仓库建设成 agent-ready repository。

Agent Harness Skills 是一组面向 agent 的仓库 harness 工程规范，用来把真实项目整理成 agent 能读懂规则、尊重边界、运行验证、留下证据并稳定交付的工程环境。

## 它是什么

Agent Harness Skills 是一个用来设计仓库 harness 的 skill library。

仓库 harness 不是业务脚手架，也不是只跑测试的框架。它是包在代码仓库外层的一组工程控制面：告诉 agent 从哪里开始读、哪些规则是事实源、哪些边界不能越过、什么验证可以证明改动安全、交付时应该留下哪些可审查的证据。

当一个项目已经不适合只靠“读 README、跑测试”来接手时，就需要仓库 harness。它把规则入口、事实源导航、架构边界、验证入口、运行证据、质量门禁和交付记录整理成 agent 可以稳定使用的工程表面。

## 为什么需要它

Coding agent 可以很快改文件，但真实项目需要的不只是快。它需要一个稳定的操作环境。

没有 harness 时，agent 会被迫猜很多事情：哪个文档才是事实源，哪个目录属于哪个子系统，哪些检查真正有效，浏览器里的错误能不能对应到后端日志，PR 里应该附什么证据。这会带来重复摸索、边界漂移、验证薄弱，以及无法复盘的交付记录。

Agent Harness Skills 的目标不是增加仪式感，而是把这些关键约定变成可发现、可执行、可审查的仓库实践。

## 它帮助 agent 做什么

- 在动手前找到正确的入口文件和事实源。
- 理解架构边界、目录归属和依赖方向。
- 选择真正能证明改动的验证入口。
- 把页面、设备、后端、日志、trace、request id、截图和 artifact 串成运行证据。
- 区分代码回归、环境不可用、供应商阻塞、数据缺失和额度问题。
- 通过 commit、PR 说明、ledger 和 handoff 留下简洁的交付记录。
- 在不扩大范围的前提下，逐步收敛质量问题和历史债务。

## 包含的 Skills

这些 skills 组成了一张 agent-ready repository 的能力图：

- `repo-harness-assessment`：评估仓库当前 agent/harness 成熟度，找出最小补强路径。
- `agent-entrypoint-design`：设计 `AGENTS.md`、镜像文件、指令优先级和事实源入口。
- `repo-contracts-and-boundaries`：把架构边界、目录边界、choke point、baseline/allowlist 变成机械检查。
- `validation-harness-design`：设计验证入口、test matrix、JSON/JUnit 输出和 CI 门禁。
- `runtime-evidence-and-tracing`：设计 run id、request id、artifact bundle、浏览器/真机/后端 trace 证据闭环。
- `agent-ledger-and-delivery`：设计 `agent_chats`/`agents_chat` 和 PR/交付证据汇总。
- `quality-gardening`：设计质量快照、结构指标、红线、债务收敛和质量报告。
- `design-doc-and-task-board`：抽象设计文档、`tasks.md`、exec plan、状态同步和验收规则。
- `atomic-commit-discipline`：抽象最小提交、提交前检查、提交信息、关联记录和禁止混入无关改动。

## 适用场景

当你希望完成这些工作时，可以使用这个仓库：

- 让一个现有仓库具备 agent-driven engineering 的接手条件。
- 把零散文档、脚本和团队约定整理成清晰的仓库 harness。
- 设计 `AGENTS.md` 和相关入口，让 agent 知道先读什么、信什么。
- 增加本地可运行、CI 可复用的验证门禁。
- 把浏览器、设备、后端、供应商调用和日志证据串成 artifact bundle。
- 为 PR、commit、handoff 和后续任务建立可追溯的交付记录。

它尤其适合那些已经有产品代码、测试和脚本，但 agent 仍然需要反复摸索规则、猜测边界、或者交付证据不足的仓库。

## 它不是什么

- 它不是业务项目模板，也不包含业务脚手架。
- 它不是把某个团队的私有流程复制出来的 workflow bundle。
- 它不能替代具体项目自己的架构决策。
- 它不只是 test harness；测试只是验证入口的一部分。
- 它不要求先建设平台；很多时候，一个清楚的脚本或文档就是第一层 harness。

## 使用方式

把 agent runtime 指向本仓库的 `skills/` 目录即可。首版不是 Codex plugin，也不包含业务项目脚手架。

适合用来回答这类问题：

- “检查这个 repo 的 harness 缺什么”
- “给一个新项目设计 `AGENTS.md` 和验证入口”
- “把浏览器验证和后端 request id 串起来”
- “这个需求应该写 design doc 还是 `tasks.md`”
- “帮我把这批改动拆成原子提交”

## Repository Layout

```text
skills/
  <skill-name>/SKILL.md
docs/
  scenario-tests.md
references/
  harness-patterns.md
scripts/
  check_skill_closure.py
  check_skill_language.py
  validate_skill_quality.py
```

## 校验

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/validate_skill_quality.py
python3 scripts/check_skill_language.py
python3 scripts/check_skill_closure.py
```

对 substantial skill wording changes，至少在 `docs/scenario-tests.md` 记录一个 realistic prompt 和 observed output。`SKILL.md` 正文统一使用英文。
