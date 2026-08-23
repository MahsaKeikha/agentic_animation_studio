# F140 | Agentic Animation Studio | L3 Gold Standard | v1.0

A governed five-agent reference architecture for animation production decision support across storyboarding, visual development, motion planning, continuity, editorial coordination, asset and rights provenance, accessibility, production quality, delivery review, and qualified human approval.

F140 can organize sequences, storyboard state, visual-development rules, motion plans, continuity evidence, production dependencies, review findings, and delivery packages. It cannot autonomously approve a final master, authorize public release, clear intellectual-property rights, approve final credits, authorize use of a person's likeness or voice, or distribute finished media externally.

## Animation lifecycle

```text
Creative Brief and Script
        -> Storyboard and Sequence Planning
        -> Visual Development and Asset Planning
        -> Motion, Performance, Layout, and Production Planning
        -> Continuity, Rights, Accessibility, and Quality Review
        -> Qualified Human Production Approval
        -> Human-Controlled Mastering, Release, and Distribution
```

The workflow fails closed when required reviews are missing or when material rights, consent, continuity, accessibility, production-quality, attribution, synthetic-media disclosure, or provenance issues remain unresolved.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Storyboard Agent | Structures beats, shots, staging, camera intent, transitions, timing assumptions, and sequence coverage | Does the storyboard communicate the intended story and production requirements? |
| Visual Agent | Organizes character, environment, prop, color, lighting, style, asset, and visual-development rules | Is the visual language coherent, original, traceable, and production-ready? |
| Motion Agent | Plans movement, acting, camera motion, timing, spacing, effects, simulation dependencies, and motion constraints | Can motion communicate performance and story clearly and safely? |
| Continuity Agent | Tracks character, prop, environment, costume, spatial, temporal, story, technical, and editorial continuity | Does the production remain internally consistent across shots and versions? |
| Review Agent | Integrates rights, consent, accessibility, production quality, credits, provenance, delivery readiness, and qualified approval | Is the package appropriate for human production review? |

Agents support directors, producers, storyboard artists, animators, designers, editors, technical directors, compositors, sound teams, accessibility specialists, rights teams, and production managers. They do not replace authorized creative, legal, labor, performer, safety, platform, or distribution decision makers.

## Repository structure

```text
AGENTS/
├── storyboard_agent.py
├── visual_agent.py
├── motion_agent.py
├── continuity_agent.py
└── review_agent.py

SKILLS/
├── storyboard_reasoning.py
├── visual_reasoning.py
├── motion_reasoning.py
├── continuity_reasoning.py
└── review_reasoning.py

TOOLS/
├── storyboard_index.py
├── visual_bible.py
├── motion_plan.py
├── continuity_log.py
└── review_gate.py

orchestration/
memory/
observability/
evals/
benchmarks/
examples/
docs/
prompts/
config/
safety/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

## Creative brief

Animation work should begin with a traceable brief covering audience, format, duration, platform, narrative purpose, visual direction, production constraints, accessibility requirements, rights constraints, budget assumptions, schedule, approval owners, and delivery expectations.

The system should distinguish verified requirements from preferences, assumptions, experiments, references, and unresolved questions.

## Script and story source

Scripts, treatments, books, games, music, performances, or other source material can carry ownership and adaptation rights. F140 should record source status and should not assume adaptation rights exist merely because material is available to the production team.

## Storyboard architecture

The policy requires `storyboard_reviewed`. `TOOLS/storyboard_index.py` provides a deterministic surface for sequence, scene, shot, beat, staging, camera, dialogue, action, duration, dependency, and version information.

Storyboards communicate intent and are not automatically final timing, animation, editorial, or rights approvals.

## Story beats

Beats can capture character objective, action, reaction, conflict, reveal, emotional turn, comedy, exposition, transition, or other story function. Each beat should support the intended sequence rather than exist only as visual decoration.

## Shot design

Shot planning can include framing, lens intent, camera height, angle, movement, screen direction, eyelines, staging, depth, focus, duration, transitions, and editorial purpose.

## Staging

Staging should make action, relationships, emotional intent, and visual priority understandable. Complex action may require additional coverage, reference, previs, or safety review.

## Screen direction

Continuity of movement, eyelines, geography, and camera relationships can affect audience comprehension. Intentional discontinuity should be distinguished from accidental continuity errors.

## Animatics

Animatics can test sequence rhythm, timing, dialogue, shot duration, transitions, music, sound, and editorial structure before expensive production work. Animatic timing should remain versioned and traceable.

## Previsualization

Previs can help plan cameras, staging, complex action, virtual production, effects, and technical dependencies. It should not be represented as final-quality animation or verified physical simulation unless actually validated.

## Visual development

The policy requires `visual_development_reviewed`. Visual development can establish character language, environments, props, palette, lighting, shape, texture, composition, graphic treatment, rendering strategy, and style rules.

`TOOLS/visual_bible.py` provides a deterministic surface for preserving approved visual-development state.

## Originality

Visual references should inform rather than become instructions to reproduce another creator's protected expression. F140 should favor descriptions of attributes, principles, periods, media, mood, composition, or production technique over imitation of a living creator's distinctive style.

## Character design

Character design can include silhouette, proportion, shape language, anatomy, costume, color, facial range, pose language, mobility, props, turnaround requirements, rig needs, and performance constraints.

## Character consistency

Character models should preserve approved proportions, identifying features, costume state, scale, color, rig limitations, and expression rules across shots unless a documented story change requires otherwise.

## Environment design

Environment development can include geography, architecture, scale, materials, atmosphere, lighting, set dressing, navigation, camera needs, effects requirements, and story function.

## Prop design

Props should track ownership, scale, handedness, state, damage, transformations, interactions, rig requirements, and continuity across shots.

## Color

Color scripts can organize emotional progression, location identity, time, atmosphere, contrast, focal hierarchy, and sequence transitions. Accessibility and display conditions should be considered where color communicates essential information.

## Lighting

Lighting development can define time, mood, depth, readability, continuity, material response, render complexity, and story focus. Lighting continuity should be evaluated across editorial cuts.

## Layout

Layout can establish camera, character blocking, environment relationships, lens, scale, composition, and technical framing before final animation.

## Motion architecture

The policy requires `motion_reviewed`. `TOOLS/motion_plan.py` can preserve action, performer or character, start and end state, timing, reference, camera relationship, physical constraints, effects dependencies, review status, and version.

## Principles of motion

Timing, spacing, anticipation, follow-through, overlap, arcs, weight, acceleration, deceleration, staging, exaggeration, and secondary action can support readable movement. Their use depends on the production's visual language rather than a single universal formula.

## Performance

Character performance can combine pose, silhouette, gaze, facial expression, gesture, rhythm, dialogue, reaction, and interaction. Generated performance suggestions remain creative proposals until approved by responsible artists and directors.

## Acting reference

Live-action reference can support timing, weight, gesture, lip sync, or complex movement. Performer consent, privacy, labor terms, and likeness rights should be documented when applicable.

## Motion capture

Motion-capture data can include performer identity, body motion, face, voice, biometric-like features, and production metadata. Access, retention, reuse, and rights should follow applicable agreements and privacy requirements.

## Physics and simulation

Cloth, hair, fluids, particles, destruction, crowds, rigid bodies, and other simulations can support animation but may produce visually plausible results that are physically inaccurate. Simulation output should be reviewed for story, safety, continuity, and technical quality.

## Camera motion

Camera animation can affect clarity, emotion, motion sickness, accessibility, and visual comfort. Excessive shake, rapid acceleration, extreme field-of-view changes, or uncontrolled movement may require accessibility review.

## Motion safety

Animated content can include rapid flashing, high-contrast patterns, strobing, intense camera motion, or other effects that may create accessibility or safety concerns. These should be reviewed against applicable platform and accessibility requirements.

## 2D animation

2D workflows can include rough animation, cleanup, inbetweening, paint, compositing, multiplane effects, camera, and final editorial. Line, proportion, color, exposure, and registration continuity should be tracked.

## 3D animation

3D workflows can include modeling, topology, UVs, texturing, shading, rigging, layout, animation, simulation, lighting, rendering, and compositing. Asset dependencies and software or renderer assumptions should be explicit.

## Stop motion

Stop-motion production can involve physical puppets, armatures, sets, replacement parts, motion-control systems, lighting, frame capture, rig removal, and physical safety. F140 can support planning but does not replace qualified stage or production safety processes.

## Motion graphics

Motion graphics can combine typography, illustration, icons, data, logos, transitions, effects, and sound. Brand, font, music, image, and trademark rights should remain traceable.

## Experimental animation

Experimental workflows can combine generative systems, procedural methods, hand processes, found media, live action, simulation, or unconventional display. Rights and provenance remain necessary even when the creative process is intentionally nontraditional.

## Continuity architecture

The policy requires `continuity_reviewed`. `TOOLS/continuity_log.py` can preserve continuity item, sequence, shot, prior state, expected state, actual state, source, owner, severity, disposition, and version.

`continuity_failure` blocks release when material story, character, prop, environment, timing, or production continuity issues remain unresolved.

## Story continuity

Character knowledge, motivations, relationships, injuries, transformations, locations, time, weather, damage, and causal events should remain consistent with the approved narrative unless intentionally changed.

## Spatial continuity

Entrances, exits, screen direction, geography, object positions, character positions, and camera relationships should remain understandable across edits.

## Costume continuity

Costume state, accessories, damage, dirt, wetness, transformations, and story-specific changes should be tracked across shots and sequences.

## Prop continuity

Props can change hands, break, disappear, transform, or move between locations. The continuity system should expose contradictions before final delivery.

## Lighting continuity

Adjacent shots should be reviewed for intended continuity of time, direction, exposure, color, atmosphere, and practical sources.

## Technical continuity

Resolution, frame rate, color pipeline, camera settings, asset versions, rigs, shaders, render settings, and effects dependencies can create technical continuity failures even when the story appears consistent.

## Editorial

Animation editorial can evolve throughout production. Shot IDs, handles, duration, frame ranges, version, dialogue, sound, music, and replacement state should remain synchronized with production tracking.

## Frame rate

Frame rate and animation exposure affect timing, motion character, delivery, and technical compatibility. Mixed-frame-rate workflows should be intentional and documented.

## Timecode and frame identity

Frame-accurate review requires stable identifiers. Production should preserve sequence, shot, version, frame range, timecode where applicable, and source references.

## Sound

Animation depends on dialogue, effects, ambience, Foley, music, silence, and mix. Audio rights, performer agreements, accessibility, localization, and delivery requirements should be tracked alongside picture.

## Dialogue

Dialogue workflows can involve production recording, ADR, synthetic speech, localization, editing, cleanup, and lip sync. Voice identity and performer rights require explicit handling.

## Voice and synthetic speech

A person's voice should not be cloned, synthesized, transformed, or reused beyond authorized scope without appropriate consent and rights. `likeness_consent_gap` blocks release when identity, voice, performer, or likeness consent remains unresolved.

## Music

Music can involve composition, master rights, publishing rights, synchronization rights, performance rights, library licenses, cue sheets, territories, duration, and platform restrictions. Availability of an audio file does not establish permission to use it.

## Sound effects

Sound libraries, recordings, generated audio, and field recordings can carry licenses or attribution requirements. Source and permitted use should be preserved.

## Rights architecture

The policy requires `rights_provenance_reviewed`. `rights_clearance_gap` blocks release when asset, music, script, character, footage, voice, font, or other rights evidence remains unresolved.

`approve_rights_clearance` is permanently protected.

## Asset provenance

Every production asset should have enough provenance to determine where it came from, what rights apply, what transformations occurred, which version is current, and who approved its use.

## Copyright

F140 should not treat public availability as public-domain status. Copyright status, license scope, territory, duration, attribution, modification rights, commercial use, and downstream distribution requirements can matter.

## Trademarks

Logos, branded products, trade dress, fictional brands, signage, and marketing materials can create trademark or clearance questions. Legal review may be appropriate for final use.

## Fonts

Font files and typefaces can carry desktop, web, app, broadcast, embedding, or other license terms. Production should preserve the applicable license evidence.

## Stock assets

Stock images, video, 3D models, textures, music, sound effects, and templates can have restrictions on redistribution, merchandise, editorial use, AI training, modification, or audience size.

## Generated assets

AI-generated images, animation, voices, music, textures, models, or effects should preserve generation provenance, input rights where relevant, review state, and downstream usage constraints.

## Synthetic-media disclosure

`synthetic_media_disclosure_gap` blocks release when a required synthetic-media provenance or disclosure obligation is incomplete.

Disclosure requirements can depend on platform, jurisdiction, contract, context, or production policy.

## Likeness and identity

`authorize_likeness_use` is protected. A production should not assume permission to depict, clone, transform, animate, or synthesize a real person's face, body, voice, or identity merely because reference material exists.

## Performer rights

Actors, voice performers, motion-capture performers, stunt performers, musicians, and other contributors can have contractual, union, residual, credit, reuse, consent, and synthetic-replica protections.

## Credits

`credit_attribution_gap` blocks release when required creator, performer, source, license, or production attribution is incomplete.

`approve_final_credits` is protected. F140 can assemble proposed credits but cannot make binding contractual determinations.

## Cultural representation

Characters, settings, clothing, rituals, languages, symbols, histories, and communities can require cultural expertise and consultation. Reference gathering should not collapse distinct cultures into stereotypes.

## Historical representation

Historical animation should distinguish documented evidence, interpretation, composite characters, dramatization, and creative invention where accuracy materially matters.

## Accessibility architecture

The policy requires `accessibility_reviewed`. `accessibility_failure` blocks release when material caption, subtitle, audio-description, flashing, readability, or accessibility issues remain unresolved.

## Captions

Captions can include dialogue, speaker identification, meaningful sound, music information, timing, reading speed, placement, and synchronization. Platform requirements can differ.

## Subtitles

Subtitles should preserve meaning, timing, readability, line breaks, character limits, cultural context, and safe areas while distinguishing translation from accessibility captioning where appropriate.

## Audio description

Audio description can communicate visual information needed to understand action, expression, setting, text, or transitions while fitting around dialogue and important sound.

## Readability

On-screen text should consider size, duration, contrast, background complexity, safe areas, motion, language expansion, viewing distance, and platform.

## Flashing and photosensitivity

Sequences containing flashing or rapidly changing high-contrast imagery may require specialized testing and mitigation. F140 should flag risk rather than claim safety without validation.

## Motion sensitivity

Rapid camera movement, simulated acceleration, spinning, zooming, shake, or immersive motion can affect some viewers. Alternative presentation or reduced-motion considerations may be appropriate.

## Children and family audiences

Content intended for children can require additional review for age suitability, advertising, privacy, platform rules, frightening imagery, imitation risk, and commercial practices.

## Content review

Violence, self-harm themes, sexual content, substance use, fear, discrimination, harassment, and other sensitive material may affect ratings, audience suitability, platform acceptance, and production review.

## Production quality

The policy requires `production_quality_reviewed`. `production_quality_gap` blocks release when material animation, compositing, render, sound, editorial, or delivery-quality issues remain unresolved.

## Animation quality

Quality review can consider pose clarity, timing, spacing, arcs, weight, intersections, foot sliding, facial performance, lip sync, deformation, popping, jitter, and unintended artifacts.

## Rig quality

Rigs should be reviewed for deformation, control behavior, range, naming, version compatibility, performance, constraints, and known limitations.

## Model quality

Models can be reviewed for topology, scale, normals, intersections, UVs, naming, hierarchy, deformation needs, material assignments, and downstream compatibility.

## Texture and shading quality

Textures and shaders can be reviewed for resolution, seams, color pipeline, consistency, memory, material behavior, naming, licensing, and render compatibility.

## Effects quality

Effects can be reviewed for timing, scale, integration, simulation artifacts, intersections, noise, render cost, continuity, and story clarity.

## Render quality

Render review can include missing frames, noise, flicker, sampling, motion blur, depth of field, color, alpha, mattes, artifacts, asset versions, and render settings.

## Compositing

Compositing can integrate renders, effects, mattes, live action, color, depth, grain, atmosphere, and final polish. Edge artifacts, mismatched color, continuity, and rights should be reviewed.

## Color management

Color pipelines should identify working space, display transforms, render output, compositing assumptions, review display, mastering target, and delivery requirements.

## Resolution and aspect ratio

Resolution, aspect ratio, framing, safe areas, crop variants, and platform-specific versions should be documented to prevent accidental loss of important content.

## Delivery

Delivery packages can include picture masters, audio stems, captions, subtitles, audio description, artwork, metadata, credits, cue sheets, localization assets, platform variants, and archival materials.

## Final master

`approve_final_master` is protected. F140 can run checks and prepare a master-review package, but final master approval remains a human production authority.

## Public release

`authorize_public_release` is protected. Passing internal governance does not authorize publication, broadcast, streaming, theatrical exhibition, festival submission, marketing release, or platform upload.

## External distribution

`external_distribution` is protected. External transfer of masters, unreleased footage, scripts, sensitive production files, or licensed assets should remain under authorized human control.

## Localization

Localization can involve translation, dubbing, subtitles, graphics replacement, cultural adaptation, lip sync, timing, credits, censorship requirements, and platform specifications.

## Dubbing

Dubbing requires voice casting, performance direction, translation, adaptation, recording, editing, mixing, lip-sync strategy, rights, and credits. Synthetic dubbing requires additional consent and provenance controls.

## On-screen text localization

Text embedded in animation may require replacement, expansion, re-layout, right-to-left support, font coverage, and cultural review.

## Production planning

Animation schedules can track development, boards, design, assets, layout, animation, effects, lighting, rendering, compositing, editorial, sound, localization, review, and delivery dependencies.

## Dependencies

A shot can depend on approved boards, dialogue, layout, character rigs, environments, props, effects, simulations, camera, lighting, sound, and editorial timing. Dependency state should be visible rather than inferred.

## Asset management

Asset systems should preserve stable identifiers, type, owner, source, rights, version, dependencies, approval state, publication restrictions, and archive status.

## Naming and identifiers

Consistent sequence, shot, asset, version, and task identifiers reduce production ambiguity and improve traceability across departments.

## Version control

Animation production creates many iterations. Versions should preserve creator or process, timestamp, source dependencies, review state, notes, supersession, and delivery status.

## Change management

Changes to story, timing, design, assets, rigs, cameras, effects, sound, or delivery should expose downstream impact rather than silently invalidate dependent work.

## Production review

Dailies, rounds, reviews, and approvals should record reviewer, version, notes, disposition, required changes, approval scope, and date.

## Human approval

The policy requires `qualified_producer_approval`. Depending on the production, qualified approval may include director, producer, animation supervisor, VFX supervisor, editorial, legal or rights, accessibility, technical, and platform stakeholders.

## Privacy

Reference footage, performer scans, voice recordings, production communications, unreleased scripts, biometric-like capture data, and personal information should be access controlled and retained only as appropriate.

## Security

Unreleased films, episodes, characters, trailers, scripts, models, source files, and distribution masters can have high commercial sensitivity. Access should follow least privilege and project authorization.

## Provenance

`provenance_documentation_gap` blocks release when source, asset, model, reference, approval, or production provenance is incomplete.

F140 must never fabricate asset ownership, license terms, performer consent, production approval, credit status, release status, or source history.

## Memory and state

The `memory/` layer can preserve briefs, storyboard state, visual bibles, motion plans, continuity, rights evidence, asset versions, accessibility findings, production reviews, approvals, and unresolved issues.

It should distinguish approved state from work in progress, reference, rejected work, superseded versions, and generated proposals.

## Observability

The `observability/` layer supports traceability across storyboard, visual development, motion, continuity, rights, accessibility, quality, approvals, and governance.

Useful telemetry includes sequence and shot version, unresolved continuity items, rights gaps, consent gaps, accessibility findings, quality blockers, credit gaps, synthetic-media disclosure state, provenance gaps, approval state, and protected-action attempts.

## Required reviews

The executable policy requires all eight conditions:

```text
storyboard_reviewed
visual_development_reviewed
motion_reviewed
continuity_reviewed
rights_provenance_reviewed
accessibility_reviewed
production_quality_reviewed
qualified_producer_approval
```

Missing any condition fails closed.

## Fail-closed governance

The implemented policy blocks release when:

- asset, music, script, character, footage, voice, font, or other rights evidence is unresolved
- identity, voice, performer, or likeness consent is unresolved
- material story, character, prop, environment, timing, or technical continuity problems remain
- caption, subtitle, audio-description, flashing, readability, or other accessibility issues remain
- material animation, compositing, render, sound, editorial, or delivery-quality issues remain
- required creator, performer, source, license, or production attribution is incomplete
- required synthetic-media provenance or disclosure is incomplete
- source, asset, model, reference, approval, or production provenance is incomplete
- any required review is missing
- qualified human production approval is missing

The system exposes blockers rather than manufacturing rights clearance, consent, accessibility compliance, production approval, credits, or release status.

## Protected actions

The safety policy permanently protects:

```text
approve_final_master
authorize_public_release
approve_rights_clearance
approve_final_credits
authorize_likeness_use
external_distribution
```

These remain outside autonomous authority even after all required reviews are satisfied.

## Human authority boundaries

F140 must not autonomously clear intellectual-property rights, authorize likeness or voice use, make binding performer-rights decisions, approve contractual credits, certify accessibility, approve a final master, authorize release, or distribute finished or sensitive production media externally.

Qualified human stakeholders retain control over creative approval, rights, legal review, performer consent, accessibility, production safety, mastering, release, and distribution.

## Explicit failure states

```text
STORYBOARD REVIEW REQUIRED
VISUAL DEVELOPMENT REVIEW REQUIRED
MOTION REVIEW REQUIRED
CONTINUITY REVIEW REQUIRED
RIGHTS AND PROVENANCE REVIEW REQUIRED
ACCESSIBILITY REVIEW REQUIRED
PRODUCTION QUALITY REVIEW REQUIRED
QUALIFIED PRODUCER APPROVAL REQUIRED
RIGHTS CLEARANCE GAP
LIKENESS OR VOICE CONSENT GAP
CONTINUITY FAILURE
ACCESSIBILITY FAILURE
PRODUCTION QUALITY GAP
CREDIT OR ATTRIBUTION GAP
SYNTHETIC MEDIA DISCLOSURE GAP
PROVENANCE DOCUMENTATION GAP
FINAL MASTER APPROVAL PROHIBITED
PUBLIC RELEASE AUTHORIZATION PROHIBITED
AUTONOMOUS RIGHTS CLEARANCE PROHIBITED
AUTONOMOUS CREDIT APPROVAL PROHIBITED
AUTONOMOUS LIKENESS AUTHORIZATION PROHIBITED
EXTERNAL DISTRIBUTION PROHIBITED
```

## End-to-end reference workflow

1. Capture the creative brief, audience, script source, format, delivery requirements, rights constraints, schedule, and approval owners.
2. Build sequence and storyboard coverage with beats, staging, camera intent, timing assumptions, dialogue, and dependencies.
3. Establish visual-development rules for characters, environments, props, color, lighting, style, and asset state.
4. Plan layout, performance, motion, camera, effects, simulation, sound, and technical dependencies.
5. Track story, character, costume, prop, spatial, lighting, editorial, and technical continuity across versions.
6. Verify asset, script, music, voice, performer, font, stock, generated-media, trademark, and other rights provenance.
7. Review consent, likeness, synthetic-media disclosure, credits, cultural context, privacy, and security requirements.
8. Review captions, subtitles, audio description, flashing, motion sensitivity, readability, and other accessibility needs.
9. Perform animation, rig, model, texture, effects, render, compositing, sound, editorial, color, and delivery quality checks.
10. Preserve versions, dependencies, review notes, approvals, superseded state, and unresolved blockers.
11. Apply fail-closed governance and require qualified human production approval.
12. Keep final-master approval, rights clearance, credit approval, likeness authorization, public release, and external distribution outside autonomous authority.

## Evaluation and held-out governance suite

The repository contains evaluation logic under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test storyboard completeness, visual consistency, motion reasoning, continuity detection, rights discipline, consent handling, accessibility awareness, production-quality review, provenance, and governance behavior.

The behavioral verification layer includes direct governance tests and a 10-scenario held-out suite covering missing review, approved support release, rights gaps, likeness or voice consent gaps, continuity failures, accessibility failures, production-quality gaps, credit gaps, synthetic-media disclosure gaps, and provenance gaps.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

These gates verify syntax-critical linting, fail-closed behavior, held-out governance scenarios, and execution of the governed reference workflow.

## Reproducibility

Reproducible animation review requires preserving brief version, script state, storyboard and animatic versions, visual-development state, asset identifiers, motion plans, continuity logs, editorial timing, rights evidence, consent, accessibility findings, quality review, credits, synthetic-media provenance, approvals, and unresolved issues.

## Extension points

Organization-specific implementations can add governed integrations for storyboard systems, digital asset management, production tracking, animation and compositing tools, render farms, review platforms, editorial systems, sound systems, localization platforms, rights databases, accessibility workflows, and delivery systems.

Any integration capable of publishing content, transferring unreleased media, changing binding rights records, approving credits, authorizing likeness use, or releasing masters should remain behind explicit authorization, least privilege, audit logging, and human-controlled execution.

## Example applications

Potential governed uses include animated films, episodic animation, shorts, game cinematics, motion graphics, educational animation, advertising animation, previs, virtual production planning, character animation, effects animation, localization, accessibility review, continuity tracking, rights review, and delivery QA.

F140 is not an autonomous director, producer, animator of record, rights attorney, clearance authority, performer representative, accessibility certifier, final-master authority, distributor, broadcaster, or platform publisher.

## Design principles

1. Begin with a traceable brief, story source, audience, production constraints, and approval authority.
2. Keep storyboard, visual, motion, editorial, and continuity state versioned and synchronized.
3. Distinguish reference, generated proposals, work in progress, approved assets, and final delivery state.
4. Never fabricate ownership, licenses, performer consent, credits, approvals, or release status.
5. Preserve provenance for source material, assets, voices, music, generated media, and production decisions.
6. Treat likeness, voice, and synthetic replicas as consent-sensitive production assets.
7. Treat accessibility and viewer safety as production requirements rather than optional polish.
8. Fail closed when rights, consent, continuity, accessibility, quality, attribution, disclosure, provenance, or approval is incomplete.
9. Keep final creative, legal, mastering, release, and distribution authority under qualified human control.

## Scope statement

F140 demonstrates a governed multi-agent architecture for animation-production decision support. It combines specialized storyboard, visual, motion, continuity, and review agents with deterministic storyboard, visual-bible, motion-plan, continuity, and review tools, observability, held-out evaluation, and fail-closed governance while preserving strict human authority over rights, consent, credits, final mastering, release, and external distribution.

Author: Mahsa Keikha
