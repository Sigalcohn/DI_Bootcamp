# Course repository structure

This repository follows the course's GitHub submission layout:

`Week1` through `Week17` contain `Day1` through `Day5`, and each day has `DailyChallenge` and `ExerciseXP` folders.

Place each assignment's Python (`.py`) file inside the corresponding folder.

The `.gitkeep` files are empty placeholders because Git does not track empty folders. You may leave them in place after adding your assignments.

## Example

`Week1/Day1/ExerciseXP/exercise1.py`

## Saving work with Git

From the repository folder in the VS Code terminal:

```bash
git status
git add .
git commit -m "Add Week1 Day1 exercises"
git push
```

Only commit files you intend to submit. If others also edit the repository, run `git pull` before starting your work.
