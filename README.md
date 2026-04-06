# Student Project Repository Guide

##  Overview

This repository is created to manage individual projects for **30 students**.
Each student must work on their assigned project and push their code to this repository using proper structure and guidelines.

---

## 📂 Repository Structure

Each student must create and work inside their own folder:

```
/project-repo
│
├── student_1_name/
├── student_2_name/
├── student_3_name/
│   └── project files
│
└── ...
```

### Folder name format:

```
yourname_project
Example: sarojbhandari_mlproject
```

---

## Instructions for Students

### 1. Clone the Repository

```bash
git clone <repository-link>
cd <repository-folder>
```

---

### 2. Create Your Own Branch

⚠️ Do NOT push directly to the main branch

```bash
git checkout -b yourname_branch
```

Example:

```bash
git checkout -b saroj_branch
```

---

### 3. Create Your Project Folder

Inside the repository, create your folder:

```bash
mkdir yourname_project
```

Add your project files inside this folder.

---

### 4. Add and Commit Your Code

```bash
git add .
git commit -m "Initial commit - Your Name Project"
```

---

### 5. Push to GitHub

```bash
git push origin yourname_branch
```

---

### 6. Create Pull Request

* Go to GitHub repository
* Click **Compare & Pull Request**
* Submit your PR for review

---

## 📋 Project Requirements

* Use **Django** for the project (if assigned)
* Choose **only one**:

  * Classification project
  * Prediction project
* Clean and readable code
* Include:

  * `README.md` inside your folder
  * Proper folder structure
  * Requirements file (`requirements.txt`)

---

## 📑 Your Project README Must Include

* Project Title
* Description
* Dataset used
* Installation steps
* How to run the project
* Output screenshots (if possible)

---

##  Rules

* Do NOT modify other students' folders
* Do NOT push to `main` branch directly
* Do NOT delete any existing files
* Follow proper naming conventions

---

## 🏁 Submission Criteria

* Project pushed to GitHub
* Pull Request created
* Code runs without errors
* Follows given instructions

---

##  Note

You will be provided with the **GitHub repository link**.
Make sure to follow all instructions carefully to avoid submission issues.

---

##  Support

If you face any issues, contact me saroj-15 before the deadline.

---

 *Follow the steps properly to ensure smooth evaluation.*
