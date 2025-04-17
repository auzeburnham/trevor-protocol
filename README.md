# 🧠 Reform UK Bio Analyzer — *Trevor Protocol*

**Scrape, clean, and analyze candidate biographies from Reform UK using NLP to expose narrative structures, ideological fingerprints, and political archetypes.**  
This project is a real-world experiment at the intersection of political philosophy, technology, digital media, and narrative psychology — also known as the **Counterscript Framework**.

---

## ✨ What Is This?

This tool collects candidate biography data from Reform UK's official listings, cleans the raw web content, and applies light NLP to tag each bio by tone, ideology, archetype, and digital footprint. The results are used to illustrate how modern political narratives can be decoded, categorized, and analyzed using technology.

---

## 🎯 Problem Statement

Modern politics is shaped by more than policies — it's shaped by **narratives**.  
This project was created to test the hypothesis that a party's candidate bios can reveal:
- Underlying **ideological leanings**
- Personal **value systems**
- Shared **narrative strategies**
- And hidden **archetypes** (military, educator, entrepreneur, etc.)

We wanted to show that even small fragments of political writing — like bios — could be:
- Scraped with automation
- Cleaned with code
- Analyzed with language models
- And fed back as structured insights

The result is a living proof-of-concept for the Counterscript memo — a theory of how political psychology, psyops, and computational narrative analysis can intersect in one system.

---

## ⚙️ Features

- ✅ **Scrapes** Reform UK candidate bios from over 450 individual profile pages
- ✅ **Cleans** HTML, spacing, punctuation, and filters junk content
- ✅ **Tags** each bio using NLP-style logic:
  - Archetype (Educator, Business, Military, Technologist)
  - Tone (Aspirational, Adversarial, Anti-Establishment)
  - Ideology (Libertarian, Nationalist, Fiscal Conservative)
  - Digital footprint (Social presence, links, sites)
- ✅ **Exports** results to JSON and CSV
- ✅ Designed for further analysis, visualization, or use in political research

---

## 🧰 How to Run

1. Run the scraper:

```bash
python scripts/scraper.py
```

2. Run the tagger:

```bash
python scripts/biotagger.py
```

3. Find your data in:

```bash
/data/reform_uk_biographies_cleaned.json
/data/reform_uk_biographies_tagged.json
```

---

## 🧠 The Trevor Protocol

As we iterated through scraper versions and data filters, one profile — **Trevor Lloyd-Jones** — kept showing up as a rich, testable bio. He became our unit test, our baseline, and eventually, our in-joke.

Every major update was named a **Trevor Protocol**, culminating in v13 where full streaming, tagging, and memory-safe processing were stabilized.

This repo documents both the technical story and the narrative evolution of the project — from emails to bios to ideology mapping.

---

## 📁 Files and Structure

```bash
/scripts/
  scraper.py           # Collect bios from web
  biotagger.py         # Tag each bio with NLP rules

/data/
  reform_uk_biographies_cleaned.json
  reform_uk_biographies_tagged.json

README.md
requirements.txt
.gitignore
LICENSE
```

---

## 🧪 Next Steps

- Add Named Entity Recognition (NER) with spaCy
- Run topic modeling (LDA/NMF) to cluster issues across bios
- Build a public-facing explorer tool (web dashboard)
- Use this dataset as live input for the white paper outreach campaign

---

## 📜 License

This project is open-source under the MIT License. Use it, remix it, fork it — just give credit where credit’s due.

---

## 🙌 Credits

Built by shalimar the clown, with massive help from an AI assistant and the unstoppable spirit of **Trevor Lloyd-Jones**.  
Inspired by narrative warfare, counterscript theory, and the belief that data can reveal the stories politics is trying to tell.
