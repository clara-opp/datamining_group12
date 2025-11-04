# datamining_group12
## Successful Repo Connection and SetUp
Johannes

## 🛠️ Local Environment Setup Guide

Follow these steps to create your own local Python environment, install all required dependencies, and connect it to VS Code.

---

### 1️⃣ Clone the repository
If you haven’t already, clone the project from GitHub using SSH (or HTTPS if preferred):

    git clone git@github.com:clara-opp/datamining_group12.git
    cd datamining_group12

---

### 2️⃣ Create a virtual environment
In your project folder, create a local Python environment named **`venv`**:

    python3 -m venv venv

This will create a folder `venv/` that contains an isolated Python installation for this project.

---

### 3️⃣ Activate the virtual environment
Activate your environment in the terminal:

    source venv/bin/activate

You’ll know it worked when your terminal prompt changes to something like:

    (venv) yourusername@ubuntu:~/datamining_group12$

If you ever want to deactivate it, just run:

    deactivate

---

### 4️⃣ Install all required dependencies
Once your virtual environment is active, install the project dependencies listed in `requirements.txt`:

    pip install -r requirements.txt

This ensures everyone on the team uses the exact same package versions.

---

### 5️⃣ Make the environment visible in Jupyter / VS Code
Register your new virtual environment as a Jupyter kernel so VS Code (or Jupyter Notebook) can detect it:

    python3 -m ipykernel install --user --name=spotify_env --display-name "Spotify Env"

---

### 6️⃣ Select the kernel in VS Code
In VS Code:

1. Open the **Command Palette** → `Ctrl + Shift + P`
2. Search for **Python: Select Interpreter**
3. Choose the interpreter named:
   
       Spotify Env

   (or `venv` if you didn’t run the kernel naming step)

After selection, you’ll see it in the bottom-right corner of VS Code, confirming that your notebook will run in the correct environment.

---

### 7️⃣ Verify everything works
Open a Jupyter notebook (e.g. `Spotify_Data_Analysis.ipynb`) and run a simple test cell:

    import pandas as pd
    import numpy as np

    print("Environment setup successful!")

If it runs without error — 🎉 you’re ready to go!

---

### 🧠 Notes
- Your local virtual environment (`venv/`) is excluded from Git via `.gitignore`, so you never push it to the repo.  
- If you install new packages, don’t forget to update the team’s dependency list:

      pip freeze > requirements.txt
      git add requirements.txt
      git commit -m "Update dependencies"
      git push


# 🧭 Git Workflow Guide

A concise, step-by-step guide for branching, committing, pushing, creating a pull request, and cleaning up after merge.

---

## 1. Checkout main and update it
```bash
git checkout main          # Switch to the main branch
git pull origin main       # Get the latest changes from remote
```

---

## 2. Create and switch to a new branch
```bash
git checkout -b feature/your-branch-name
```

---

## 3. Stage and commit your changes
```bash
git add .                  # Stage all modified files (or specify individual files)
git commit -m "Add login functionality"
```

---

## 4. Push your branch to remote
```bash
git push -u origin feature/your-branch-name
```

---

## 5. Create a Pull Request
1. Go to your repository on **GitHub**, **GitLab**, or **Bitbucket**.
2. Click **Compare & Pull Request** (or the equivalent).
3. Review the changes and open a PR targeting `main`.
4. Get it reviewed and **merge** it.

---

## 6. Delete the branch after merge
### Delete the remote branch
```bash
git push origin --delete feature/your-branch-name
```

### Delete the local branch
```bash
git branch -d feature/your-branch-name
```
> Use `-D` instead of `-d` only if necessary (e.g., local branch isn’t marked as merged but it’s already merged remotely).
