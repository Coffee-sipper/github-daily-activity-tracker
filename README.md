# GitHub Daily Activity Tracker

A small Python project that uses GitHub Actions to automatically record a daily activity update.

## What it does

Every day, the workflow:

* runs `update.py`
* adds the current UTC date and time to `activity.log`
* updates the counter in `stats.json`
* commits the changes to the repository

You can also run the workflow manually from the **Actions** tab.

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

Create a repository called `github-daily-activity-tracker` and add the project files to it.

Then go to:

**Repository → Actions → Daily Activity Update**

You can use **Run workflow** to test it manually.

The workflow is scheduled to run once a day at **19:30 UTC**.

## Run locally

This is optional. If you want to run the script yourself, you'll need Python 3.9+.

```bash
python update.py
```

It will update:

```text
activity.log
stats.json
```

## Example

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

## What I used

* Python
* Git
* GitHub Actions
* JSON
* basic file handling

## Note about contributions

For the commits to count toward your GitHub contribution graph, the commit email needs to be associated with your GitHub account and the commits generally need to be on the repository's default branch.

## License

MIT
