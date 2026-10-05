# HCI Foundations — Self-Directed Course Vault

An Obsidian vault for a software engineer learning HCI from scratch over a 12-week, classroom-style course (lectures + readings + weekly field-work homework), preparing for HCI PhD applications and learning in public.

Start at **[00-home.md](00-home.md)** · Syllabus: [10-data/course/syllabus.md](10-data/course/syllabus.md)

## Structure

```
.
├── 00-home.md                      # dashboard: current week, quick links
├── 00-thoughts/                    # PRIVATE capture
│   ├── inbox.md                    #   quick capture, triage weekly
│   ├── questions.md                #   open questions (→ TA / future research)
│   ├── post-ideas.md               #   sparks for posts
│   └── journal/YYYY-MM-DD.md       #   daily log + Sunday weekly review
├── 10-data/                        # COURSE PACK (inputs)
│   ├── course/
│   │   ├── syllabus.md
│   │   ├── schedule.md
│   │   ├── phd-roadmap.md
│   │   └── weeks/week-01..12.md    #   brief: goals, materials, daily jobs, homework, rubric
│   └── sources/
│       ├── arxiv-digests/          #   auto-filled weekly by GitHub Actions
│       ├── feeds-and-labs.md
│       └── reading-library.md
├── 20-notes/                       # YOUR WORK
│   ├── lectures/week-NN.md         #   Mon
│   ├── concepts/<concept>.md       #   Tue: atomic, own words, linked
│   ├── papers/<author-year-short-title>.md   # Wed
│   └── homework/hwNN-<slug>/       #   Thu–Sun
│       ├── submission.md
│       ├── grade.md
│       └── assets/
├── 30-posts/                       # PUBLIC output
│   └── YYYY-MM-<slug>/
│       ├── blog.md                 #   canonical long-form (→ WordPress, category HCI)
│       ├── x-thread.md / linkedin.md
│       └── assets/
├── 90-templates/                   # note templates
├── 99-archive/
├── scripts/  .github/workflows/    # automation (arXiv fetcher)
```

## Conventions

| Thing | Convention | Example |
|---|---|---|
| File names | lowercase kebab-case | `gulf-of-execution.md` |
| Weeks / homework | zero-padded | `week-03.md`, `hw03-fitts-law-experiment/` |
| Journal | ISO date | `2026-10-05.md` |
| Papers | author-year-short-title | `hutchins-1985-direct-manipulation.md` |
| Posts | year-month-slug folder | `2026-10-heuristic-audit-docker/` |
| Images | `assets/` next to the note that uses them | `hw02-.../assets/screen-1.png` |
| Participants | P1, P2, … numbered across the whole course | never real names |
| Status field | `not-started → in-progress → submitted → graded` (homework), `idea → drafting → ready → published` (posts) | |

## Rules
1. **Notes are the source of truth.** Posts are built from notes, never from scratch.
2. **Concept notes are atomic.** One idea per note, in your own words, linked to at least one other.
3. **Keep it shallow.** Max 3 folder levels; use links and tags for everything else.
4. **Privacy.** No recordings or identifiable participant data in Git. Only `30-posts/` is meant to be public.
