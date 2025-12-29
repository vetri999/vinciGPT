# vinciGPT

vinciGPT is an educational + practical open-source repo to understand GPTs end-to-end and then build on top of them.

## Why vinciGPT?

### 1) Understand maths & science of GPT in own CPU → **Simple to understand (most critical)**
- Full training loop: see loss drop + improvement in sample tests
- Full inference loop: generate “coherent-enough” output (purely educational)

### 2) Deploy privately for custom usecases → **Simple to customise (most critical)**
- Rent GPUs, increase parameters for powerful training/inference
- Load open weights (from best open source models)
- Finetune with custom dataset

### 3) Agent Interface (interfaces + reference integrations) → **Reproducible + Testable agents**
- RAG interface: retrieve data (enterprise/open) → augment answers
- Agent interface: create actions → design workflows → get connector code to connect tools/connectors
- Test & govern agents: audit trace using step graph + policy

---

## Repo structure (high level)

- `Input/`  : datasets, tokenizers, configs (inputs to training/inference/agents)
- `Process/`: GPT core (model), training loop, inference loop, finetune, agent interfaces
- `Output/` : checkpoints, logs, samples, traces, reports

---

## Quickstart (placeholder)

> Coming soon:
- CPU toy training run (loss drops, samples improve)
- Load open weights + generate
- Finetune on custom dataset
- Minimal agent interfaces (RAG/tools/workflow) + traces + policy hooks

---

## Design rules

1. Every file starts with:
   - **WHAT** it does
   - **WHY** it exists
   - **WHERE** it fits (Input → Process → Output)
2. Prefer simple, readable code over abstractions.
3. Private-by-default: everything can run locally.

---

## License

See `LICENSE`.
