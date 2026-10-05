---
week: 3
title: "Human Abilities: Perception, Memory & Motor Control"
start: 2026-10-19
due: 2026-10-25
homework: "Build & Run a Fitts's Law Experiment"
status: not-started   # not-started | in-progress | submitted | graded
tags: [course, week/03]
---

# Week 3 — Human Abilities: Perception, Memory & Motor Control

> 📅 **Mon Oct 19 → Sun Oct 25, 2026** · Homework due **Sun Oct 25, 23:59**  
> [[week-02|← Week 2]] · [[syllabus]] · [[schedule]] · [[week-04|Week 4 →]]

## 🎯 Learning goals

- [ ] Explain perception, working memory limits and cognitive load in interface terms
- [ ] State Fitts's law and compute an index of difficulty
- [ ] Run your first tiny quantitative experiment

## 📚 Materials

- **Lecture:** Stanford CS147: *Human Abilities & Visual Design* (Perception, Motor Skills, Fitts’s Law)
- **Textbook:** Norman, *DOET* — Ch. 3 *Knowledge in the Head and in the World*
- **Textbook:** Amy Ko, *User Interface Software and Technology* (free): https://faculty.washington.edu/ajko/books/user-interface-software-and-technology/ — ch. *Pointing*
- **Paper of the week:** MacKenzie (1992). *Fitts' Law as a Research and Design Tool in Human-Computer Interaction*. Human-Computer Interaction 7(1).

## 🗓️ Daily jobs (~18 h)

| Day | Time | Job | Output (where it goes) |
|---|---|---|---|
| Mon | 2 h | Watch lecture, take notes | `20-notes/lectures/week-03.md` |
| Tue | 2 h | Textbook reading → write concept notes | `20-notes/concepts/*.md` |
| Wed | 2 h | Read paper of the week | `20-notes/papers/<author-year-title>.md` |
| Thu | 2 h | **Homework kickoff:** Design conditions; scaffold the web app | `20-notes/homework/hw03-fitts-law-experiment/submission.md` |
| Fri | 2 h | **Homework:** Finish app + pilot it on yourself; fix bugs | `20-notes/homework/hw03-fitts-law-experiment/` |
| Sat | 4 h | **Field work:** Run 2 other participants; analyze in Python (pandas + numpy/scipy) | `20-notes/homework/hw03-fitts-law-experiment/` |
| Sun | 4 h | Finish write-up → self-grade → weekly review → post draft → skim next week | `grade.md`, journal, `30-posts/` |

## 🧠 Concept notes to create this week

- [ ] [[fitts-law]]
- [ ] [[index-of-difficulty]]
- [ ] [[working-memory]]
- [ ] [[cognitive-load]]
- [ ] [[recognition-over-recall]]

## 📝 Homework 03 — Build & Run a Fitts's Law Experiment

**Engineering week.** Build a small web page that shows circular targets at varying **distance (D)** and **width (W)**, logs click time and errors, and exports CSV.
Run it with **3 participants** (you + 2 others), ≥ 3 D × 3 W conditions, ≥ 10 trials each.
Fit `MT = a + b · log2(D/W + 1)` and report R².

**Deliverables**

- [ ] Link to code (repo or gist) + screenshot
- [ ] Method: participants, device, conditions, trials
- [ ] Plot: MT vs. ID with regression line; table of a, b, R²
- [ ] Discussion: does Fitts's law hold? What would this mean for button placement in a real UI?

**Rubric (/15)**

| Criterion | Points |
|---|---|
| Working experiment app with correct logging | /4 |
| Sound method (conditions, trials, randomized order) | /3 |
| Correct regression and plot | /3 |
| Thoughtful discussion linked to UI design | /3 |
| Reproducible (code + data shared) | /2 |

**Grading:** ≥ 13 = A · ≥ 10 = B · below that → redo the weakest criterion before moving on.

## ✅ Definition of done

- [ ] Lecture notes written
- [ ] All concept notes created (in your own words)
- [ ] Paper note written
- [ ] `20-notes/homework/hw03-fitts-law-experiment/submission.md` complete
- [ ] `20-notes/homework/hw03-fitts-law-experiment/grade.md` self-graded (optional: sent to TA for review)
- [ ] Weekly review in journal
- [ ] Post drafted in `30-posts/`

## 📣 Post idea

- "I built a Fitts's law experiment in an evening. Here's why your 'Delete' button is in the wrong place."
