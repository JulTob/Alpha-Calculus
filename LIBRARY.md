# Shared-library review and development

The user and relevant specialists share this library. The Wiki is a
reading and navigation surface; runnable scripts, notebooks, tests and
editable diagram sources remain with their topic. Agent catalogues link
to these canonical resources rather than duplicate the whole repository.

## Current bounded review

Reviewed on 30 October 2026 at
[`3c7c8235e12bff89a14f57b6f480d70c7557e94f`](https://github.com/JulTob/Alpha-Calculus/tree/3c7c8235e12bff89a14f57b6f480d70c7557e94f).
Two temporary workers applied distinct review criteria: Professor's source
and teaching method, and Alphy's subject/material method. They used the
same model; this was not installed-plugin execution or independent-model
corroboration. The [review record](maintenance/library_review.json) gives
the inspected paths, scope, source hashes, findings and remaining gaps.

| Topic | Suitable use now | Boundary |
| --- | --- | --- |
| Transported arithmetic | Supported scalar operations and coordinate traces | Three generators; selected formula checks, not symbolic calculus |
| Gain chains | Positive composition, known-stage replacement and numerical limits | Restricted workload; conventional caching has the same complexity |
| Power laws | Log-log representation, elasticity and fitting assumptions | Chosen data; no empirical mechanism or noise model validated |
| Parallel resistance | Positive fixed-size resistance bank and update traces | Restricted reciprocal construction; conventional conductance caching matches cost |

Both reviews found the material suitable for those uses. This is a
bounded teaching/application library, not a complete Alpha Calculus
reference. The reviews checked existing execution records and source
hashes; they did not rerun code, reread the original books or certify a
live Colab session. Original numerical checks retain their own records.

## Necessary next materials

1. **Function transport and derivative conditions.** We need one public
   explanation of the forward and inverse maps, types, domains and
   derivative assumptions, with the existing boundary example and a
   labelled coordinate model.
2. **Log-odds and information.** We need a shared lesson with the probability
   domain, logarithm base, units and intermediate surprisals. The Alpha
   formulation, information interpretation and any inferential claims
   require their respective subject checks.
3. **Transfer questions and visual models.** We add a relevant model and a
   misconception or transfer check when it helps us understand an
   application. We keep one application per Colab.

<!--
Agent guidance

## Necessary next materials

1. **Function transport and derivative conditions.** Alphy should develop
   one public explanation of the forward and inverse maps, types and
   domains, followed by the derivative assumptions and existing boundary
   example. Professor reviews prerequisites and exposition. Use a labelled
   coordinate diagram beside the equations.
2. **Log-odds and information.** Prepare one shared lesson with probability
   domain, logarithm base, units and intermediate surprisals. Alphy owns
   the Alpha formulation; Shanny should review the information-theory
   interpretation. A material inferential claim needs statistical review.
3. **Transfer questions and visual models.** Add one relevant model and a
   misconception or transfer check to each application when it helps the
   reader understand the method. Keep one application per Colab.
-->

The source-route gap found by both reviews has been addressed in
[sources.json](sources.json): sources already cited in topic reference
pages now have global IDs and concept-level consultation routes.
This reindexing is not a new consultation of the external texts.

## Source and presentation review

For adopting a new topic or a material addition, use two complementary
reviews:

We review source fit, prerequisites, teaching sequence, intermediate
steps, retrieval and maintainability. We also review definitions,
domains, units, methods, references, examples, tools and checks.
These are complementary questions, rather than interchangeable approvals.

<!--
Agent guidance

- Professor assesses source fit, prerequisites, teaching sequence,
  intermediate steps, retrieval and maintainability.
- The subject specialist assesses definitions, domain, units, methods,
  required references, examples, tools and their checks.
-->

Record the intended use, actual revision, inspected and uninspected
material, gaps and smallest useful repair. Re-review affected content
when it changes. A typo does not require a full-library audit.

The user's [Wiki-Documentation](https://github.com/JulTob/Wiki-Documentation/wiki)
is the shared authoring library for concept/system diagrams, mathematics
and readable notebooks. Consult its relevant technique and verify the
intended renderer. Retain editable Mermaid/draw.io sources, short labels,
units, a text equivalent and a checked SVG/PNG fallback where needed.
GitHub, Colab and Quarto are separate rendering targets.

## Keep local work lightweight

Retrieve the relevant pages and scripts; clone a working copy only when
needed for editing. Do not mirror every library or copy books into every
agent. Main and Wiki have separate histories, so record both revisions
when a task uses both. Keep a single maintained explanation or program
and link to it from other agents and reading routes.

Scientific claims, learning preferences, adoption and publication
retain separate status. A review covers its stated revision and scope.

<!--
Agent guidance

Wiki additions remain reviewable proposals for the user. This review
does not publish a Wiki or validate every future commit. Scientific
claims, user preferences, adoption and publication retain separate status.
-->
