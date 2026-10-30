# Repository guidance

Use neutral scientific English for repository content: README,
documentation, notebooks, code comments, labels, generated outputs,
data field names and metadata. Follow [the editorial style](EDITORIAL_STYLE.md).
Use Irish/British spelling and `-ise`/`-isation` forms. Preserve external
API identifiers, format requirements, exact quotations, personal names
and original published titles.

Before editing, inspect the relevant files and briefly state the plan.
Make the smallest clear change, preserve others' work and keep code and
prose visually light. Use descriptive names, short lines and intermediate
steps where they help readers understand the calculation.

Preserve mathematical claims, domains, units, source locations and
limitations. Distinguish external references, original work, local
annotations, hypotheses and executed evidence. Test a claimed benefit
against a competent baseline; do not infer scientific novelty or general
numerical stability from a successful example.

Keep one application per standalone Colab notebook, with its own
references and results directory. After a relevant change, execute its
checks in a fresh process, inspect the outputs and update affected
records and links. Report the runtime and exact scope of checks; a saved
output or an earlier revision's record is not a new test.

Organise resources by subject or application under `topics/<topic>/`.
Keep the explanation, exact references, runnable scripts, relevant tests,
notebook and generated results together. Do not create separate global
folders for code, notebooks or references. Use root files for shared
guidance and `maintenance/` for repository-wide checks and generation.
Publish useful snippets as runnable topic scripts with explicit inputs
and limits. Keep generated script companions aligned with their notebooks.

Prepare reusable Wiki content for Julio's review. A local change or pull
request does not authorise Wiki publication or establish approved canon.
