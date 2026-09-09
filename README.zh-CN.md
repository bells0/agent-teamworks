# Agent Teamworks

[English](README.md) | 简体中文

> 团队构建一次，角色、上下文与未完成事项持续保留。

Agent Teamworks 是一个**用于构建项目团队的 Codex 插件**。当项目需要长期分工与协作时，提出组队请求；插件依据规范建立最小角色组合，明确职责、Agent 绑定、通信方式和项目内的接续记录。

团队建成后，日常工作交给现有协调者。普通功能请求不会重新触发组队。需要调整团队或交接、恢复角色时，再使用插件的相应能力。

## 安装一次

需要 Python 3.10 或更新版本来打包，以及支持 `codex plugin` 命令的 Codex。Python 第三方依赖只用于开发验证；打包和使用插件不需要安装这些依赖。

在本仓库目录运行：

```bash
python3 scripts/build_plugin.py
codex plugin marketplace add ./dist
codex plugin add agent-teamworks@agent-teamworks
```

第一条命令生成完整的本地插件市场目录，后两条将该市场注册到 Codex 并安装插件。安装后，在需要组队的目标项目里新开一个 Codex 任务，让新 Skill 被发现。日常使用不需要提供插件源码仓库路径。

打包脚本创建新的 `dist/`，不会覆盖已有目录。再次打包时，用 `--output dist/<构建名称>` 指定一个新目录。仓库根目录中的文件是唯一维护源；生成目录不作为第二份插件源码维护。

安装包包含插件清单、Skill、协议、Schema、适配器及其引用文档。单独复制 `skills/agent-teamworks/` 不构成完整插件。仅执行打包不会安装插件或修改 Codex 配置。

## 需要团队时使用

在目标项目选择 Agent Teamworks，直接说：

> 为这个项目构建一个 Agent 团队，建立最小角色组合，明确职责、协作方式和接续记录。

明确的自然语言组队请求也可以让 Codex 发现此 Skill；宿主支持时可用 `$agent-teamworks` 调用。无需每次指定插件仓库路径。

| 阶段 | 你提出的请求 | 插件或团队负责的事 |
| --- | --- | --- |
| 构建 | “为这个项目构建团队。” | 理解项目，读取已有团队，建立角色，绑定宿主支持的 Agent，配置通信。 |
| 日常工作 | “实现这个功能。” | 现有协调者把任务分派给已有角色，不重新组队。 |
| 调整 | “按新范围调整团队职责。” | 核对当前角色，只记录必要的职责和所有权变化。 |
| 交接与恢复 | “更换这个角色的 Agent，继续未完成的工作。” | 保留逻辑角色、决定、历史和未完成事项，完成正式交接。 |

构建结果会说明角色职责、真实的 Agent 就绪状态、协调入口、通信方式、待决事项和记录位置。如果 Agent 尚未创建成功，会明确报告团队草案。构建团队本身不代表自动开始所有实现任务。

## 团队保存在目标项目中

规范随插件安装；每个项目自己的团队状态保存在项目内：

```text
your-project/
├── AGENTS.md                 # 简短接续入口，保留原有项目规则
└── .agent-teamworks/
    ├── team.json
    ├── roles/
    ├── work-items/
    ├── decisions/
    └── handoffs/
```

记录按需要创建。接续入口指向项目内的团队记录，不写死某台电脑上的插件路径。新对话先核对已有角色绑定，再接手相应职责，不因新开任务就创建第二个协调者。

协调者负责收回、整合各角色的产物与证据。产品体验验收、独立技术评审、交付就绪和合并授权继续分别记录。插件安装不授予发布、付款或合并权限。

## 插件源码结构

```text
agent-teamworks/
├── .codex-plugin/plugin.json # Codex 插件身份与发现信息
├── skills/agent-teamworks/   # 构建、调整和交接入口
├── framework/                # 唯一维护的团队运行模型
├── protocols/                # 组建、路由、通信与验收协议
├── schemas/                  # 团队、角色、任务、交接和决策格式
├── adapters/codex/           # 运行时映射与项目接续模板
├── roles/                    # 角色契约指南
├── examples/                 # 虚构的项目记录
├── docs/                     # 决策、兼容说明和历史规格
├── evals/                    # 行为验收场景
├── scripts/                  # 打包与仓库验证
└── tests/                    # 安装包、记录和引用检查
```

[运行模型](framework/operating-model.md)、[组建协议](protocols/team-formation.md)、[通信协议](protocols/communication.md)和 [Codex 适配说明](adapters/codex/README.md)规定团队如何构建并持续工作。[虚构电商示例](examples/commerce-project/)展示记录格式，其中五个角色不代表固定团队规模。[通信示例](examples/communication-walkthrough.md)展示回传流程，不是真实执行日志。

Agent Teamworks 可以配合已有软件交付流程使用：插件负责团队构建、角色延续和任务路由，交付流程负责某项具体结果的实现与交付。构建团队不要求额外安装交付插件。

## 验证与贡献

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
```

检查覆盖 Schema、示例记录、跨记录引用、工作依赖、交接、Skill 元数据和源码链接，还会生成新的市场目录，检查复制后的插件内部引用。静态检查不能证明真实组队、消息回传或无人值守续跑成功；这些需要执行[行为验收场景](evals/scenarios.md)。

插件 `0.3.0` 实现了[团队构建插件的产品决策](docs/decisions/0001-codex-team-formation-plugin.md)。[Work Item Schema `0.2.0`](docs/migrations/work-item-0.2.0.md) 和其他 `0.1.0` 记录格式保持兼容。执行能力由 Codex 宿主提供；插件不包含托管运行时、仪表盘、Hook、MCP 服务或后台调度器。

开发使用“分支 → Pull Request → 独立审查 → 授权合并”的流程，详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

[MIT](LICENSE)
