# DSA for ML Interviews

An interactive, step-through course on data structures and algorithms, built for ML engineer, data scientist and ML research engineer interviews.

Each lesson has five parts:

1. **Walkthrough**: an animated diagram you step through, with live meters counting the work.
2. **Code template**: tested Python for every pattern in the lesson.
3. **Spot the pattern**: the problem wording that tells you which technique to use.
4. **Practice problems**: real LeetCode problems with two hints each.
5. **Quiz**: four questions with explanations.

## Lessons

| # | Lesson | Status |
|---|--------|--------|
| 1 | Hashing and search | Ready |
| 2 | Two pointers and sliding windows | Ready |
| 3 | Prefix sums and intervals | Next |
| 4–17 | Core DSA, the ML coding round, SQL and pandas | Planned (see the Roadmap tab) |

## Run it

Open `index.html` in a browser. It's a single self-contained file: no install and no server. It loads the Figtree font from Google Fonts, and falls back to the system font when offline.

## Project layout

```
index.html              built course (generated; this is what you open or deploy)
src/course.html         page source, with %%CODEn%% placeholders for the code
src/templates.py        the Python templates, the single source of truth for code
build.py                copies each lesson's templates into the page -> index.html
tests/test_templates.py randomized checks of every template against brute force
```

## Making changes

```bash
python3 tests/test_templates.py   # or: pytest
python3 build.py
```

Always run the tests before building. The page shows exactly the code in `src/templates.py`, so a passing test run means the code on the page is correct.

To add a lesson:

1. Add a `# ---- Lesson N ----` block to `src/templates.py`, with tests in `tests/test_templates.py`.
2. Add a lesson object to the `LESSONS` array in `src/course.html`, using `CODE.lN` for its code.
3. Add `lN:%%CODEN%%` to the `CODE` object in `src/course.html`.
4. Test, then build.

## Deploy

The site is static. Import the repo into [Vercel](https://vercel.com) or turn on GitHub Pages for the root folder. Either one serves `index.html` with no build step, since the built file is committed.
