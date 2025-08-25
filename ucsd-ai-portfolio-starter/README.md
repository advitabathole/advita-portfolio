# UCSD AI Portfolio Starter

A clean starter to launch your AI portfolio **today** — includes:
- A static portfolio website (works with GitHub Pages)
- A projects folder with a reusable template
- Helpful `.gitignore` and MIT License

---

## Quickstart (10–15 min)

### 0) Prereqs
- Install **Git for Windows**: https://git-scm.com/download/win
- Create or sign in to **GitHub**: https://github.com/

### 1) Make a new repository
1. On GitHub, click **New** → name it `advita-portfolio` (or anything you like) → **Public**.
2. Click **Code** → copy the **HTTPS** URL.

### 2) Clone & open locally
```bash
# In your Documents folder (Windows)
cd %USERPROFILE%\Documents

# Clone your empty repo (paste your URL)
git clone https://github.com/YOUR-USERNAME/advita-portfolio.git

# Move the starter files into the repo
```
Now copy the contents of this starter folder into that new repo folder.

### 3) Commit + push
```bash
cd advita-portfolio
git add .
git commit -m "Initial portfolio"
git branch -M main
git remote -v  # (verify origin is set)
git push -u origin main
```

### 4) Turn on GitHub Pages
1. Go to your repo **Settings → Pages**.
2. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
3. Set **Branch** to `main` and **/root`** (or `/site` if you move files there).
4. Save. Your site will be live at the URL shown (give it ~1 minute).

> **Tip:** If you prefer the classic personal domain, create a repo named **`YOUR-USERNAME.github.io`** and put the `site/` contents at the root of that repo.

---

## What’s inside

```
ucsd-ai-portfolio-starter/
├─ site/
│  ├─ index.html
│  ├─ style.css
│  ├─ projects.json
│  └─ assets/ (you can add images here)
├─ projects/
│  └─ project-template/
│     └─ README.md
├─ .gitignore
├─ LICENSE
└─ README.md (this file)
```

- **site/** — your portfolio website (edit text in `index.html`, add projects in `projects.json`).
- **projects/** — keep each project in its own folder with a clear README.
- **.gitignore** — avoids committing junk files.
- **LICENSE** — MIT; you can keep or change it.

---

## How to add a project to the website

1. Duplicate the `projects/project-template` folder and rename it, e.g. `projects/ucsd-chatbot`.
2. Edit that project's `README.md` with details.
3. Open `site/projects.json` and add a new item like:
```json
{
  "title": "UCSD Enrollment Chatbot",
  "tech": ["Python", "OpenAI API", "FastAPI"],
  "summary": "Answers UCSD class & housing FAQs using RAG.",
  "github": "https://github.com/YOUR-USERNAME/advita-portfolio/tree/main/projects/ucsd-chatbot",
  "demo": "",
  "image": ""
}
```
4. Commit + push — the site updates automatically.

---

## Suggested first 3 projects

1. **UCSD Enrollment Chatbot** — FAQ assistant for classes/housing (RAG pipeline).
2. **UCSD Landmarks Vision** — classify Geisel vs. Price Center vs. Sun God.
3. **Triton Eats Predictor** — predict dining-hall menu ratings from text.

Each should have: problem → data → approach → results (metrics) → what’s next.

---

## Git basics cheat-sheet

```bash
# Configure once
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# See what changed
git status

# Stage + commit
git add .
git commit -m "Your message"

# Push to GitHub
git push

# Pull latest changes
git pull

# Create a new branch
git checkout -b feature/new-section

# Merge it back on GitHub via Pull Request, or locally:
git checkout main
git merge feature/new-section
git push
```

---

## Customize the site
- Edit **site/index.html** (text & links)
- Add/replace projects in **site/projects.json**
- Drop images into **site/assets/** and reference them as `"image": "assets/yourfile.png"`

---

Happy building! 🚀
