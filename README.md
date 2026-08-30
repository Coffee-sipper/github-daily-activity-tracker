# GitHub Daily Activity Tracker

A small Python + GitHub Actions project that records one daily activity entry and commits the updated log automatically.

## What it does

Every day, GitHub Actions:

1. Runs `update.py`
2. Adds today's UTC date/time to `activity.log`
3. Increments the activity counter
4. Updates `stats.json`
5. Commits the real file changes back to the repository

You can also run it manually from the **Actions** tab.

> This project is intentionally designed to record actual automated project activity, not to create meaningless empty commits.

## Project structure

```text
github-daily-activity-tracker/
├── .github/
│   └── workflows/
│       └── daily-update.yml
├── activity.log
├── stats.json
├── update.py
├── .gitignore
└── README.md
```

## Setup

### 1. Create the repository

Create a new GitHub repository named:

```text
github-daily-activity-tracker
```

Make it **public** if you want the repository itself to be visible on your profile.

### 2. Put these files in the repository

Copy the project files into your repository and push them to the default branch (`main`).

### 3. Enable Actions

Open:

**Repository → Actions**

The workflow should appear as:

**Daily Activity Update**

The workflow has a manual **Run workflow** button, so you can test it immediately.

### 4. Let it run automatically

The workflow runs once per day at **19:30 UTC**.

You can change the schedule in:

```text
.github/workflows/daily-update.yml
```

GitHub scheduled workflows use cron syntax and run on the repository's default branch.

## Run locally

You need Python 3.9+.

```bash
python update.py
```

Then check:

```text
activity.log
stats.json
```

## Example output

`activity.log`

```text
2026-08-30T19:30:00Z | Daily activity update #1
2026-08-31T19:30:00Z | Daily activity update #2
```

`stats.json`

```json
{
  "total_updates": 2,
  "last_update": "2026-08-31T19:30:00Z"
}
```

## Why this is a useful project

This tiny project demonstrates:

- Python file I/O
- JSON handling
- Git
- GitHub
- GitHub Actions
- scheduled automation
- CI/CD concepts
- automated commits

It is a better portfolio project than a repository containing thousands of empty commits.

## Important GitHub contribution note

For a commit to appear on your GitHub contribution graph, GitHub requires the commit email to be associated with your account, and the commit generally needs to be on the repository's default branch. Contributions can also take some time to appear.

The workflow uses GitHub's built-in Actions identity, so the commit author should be configured to an email associated with your GitHub account if you want the commits attributed to you.

## License

MIT
