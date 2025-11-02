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

