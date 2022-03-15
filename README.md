# Flask + Tailwind template

This serves as a template to `flask` projects using `poetry`, `npm` and `tailwindcss` with `postcss` preprocessor.

# Usage

- `poetry install` to install python dependencies; to use venv - `poetry env list` & `poetry env use 3.9`
- `npm install` to install js and Tailwind packages
- `npm run dev` runs Tailwind watchdog to compile styles for html templates in real time
- `npm run build:prod` (kill flask dev server beforehand) will prepare production-ready css

Remember to alter any names and paths after changing something.
