
git add . && git commit -m "Your commit message here" && git push





# GitHub Basic Commands

## Initial Setup (First Time Only)

### Configure Git
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Initialize Repository (if not already initialized)
```bash
git init
```

## Connecting to GitHub

### Add Remote Repository
```bash
git remote add origin https://github.com/username/repository-name.git
```

### Verify Remote
```bash
git remote -v
```

### Change Remote URL (if needed)
```bash
git remote set-url origin https://github.com/username/repository-name.git
```

## Basic Workflow

### Check Status
```bash
git status
```

### Add Files to Staging
```bash
# Add specific file
git add filename.txt

# Add all files
git add .

# Add all files of a type
git add *.js
```

### Commit Changes
```bash
git commit -m "Your commit message"
```

### Push to GitHub
```bash
# First push (sets upstream)
git push -u origin main

# Subsequent pushes
git push
```

## Branch Management

### Create New Branch
```bash
git branch branch-name
```

### Switch to Branch
```bash
git checkout branch-name

# Or create and switch in one command
git checkout -b branch-name
```

### Push Branch to GitHub
```bash
git push -u origin branch-name
```

### List Branches
```bash
# Local branches
git branch

# All branches (including remote)
git branch -a
```

## Pulling Changes

### Pull Latest Changes
```bash
git pull origin main
```

### Fetch Changes (without merging)
```bash
git fetch origin
```

## Common Workflows

### Full Push Workflow
```bash
git status                    # Check what's changed
git add .                     # Stage all changes
git commit -m "Description"   # Commit with message
git push                      # Push to GitHub
```

### Update from GitHub
```bash
git pull origin main          # Get latest changes
```

### Clone Existing Repository
```bash
git clone https://github.com/username/repository-name.git
```

## Viewing Information

### View Commit History
```bash
git log

# Compact view
git log --oneline
```

### View Differences
```bash
# Changes not staged
git diff

# Changes staged for commit
git diff --staged
```

### View Remote Info
```bash
git remote show origin
```

## Troubleshooting

### Undo Last Commit (keep changes)
```bash
git reset --soft HEAD~1
```

### Discard Local Changes
```bash
# Specific file
git checkout -- filename.txt

# All files
git checkout -- .
```

### Remove File from Staging
```bash
git reset HEAD filename.txt
```

## Tips

- Always `git pull` before starting work on a shared repository
- Write clear, descriptive commit messages
- Commit related changes together
- Use `.gitignore` to exclude files you don't want to track
- Push regularly to keep remote repository up to date
