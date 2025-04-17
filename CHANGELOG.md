# 📜 Changelog — Trevor Protocol (Reform UK Bio Analyzer)

All notable changes to this project will be documented in this file. This follows the structure and evolution of the Counterscript project and its companion tool: the Reform UK Bio Analyzer.

---

## [v13.0.0] — 2024-04-18
- ✅ Finalized memory-safe processing for large-scale tagging
- ✅ Tagged 450 full-length bios with archetypes, tones, and ideologies
- ✅ Cleaned and exported results to both JSON and CSV
- ✅ Project stabilized for GitHub publication
- ✅ Full README, LICENSE, and MIT-compliant release

**🔒 Trevor Protocol: Stabilized.**

---

## [v12.0.0] — 2024-04-17
- Added streaming-safe NLP routines
- Improved file parsing to prevent memory crashes
- Began analyzing tag distribution across the dataset
- Extracted top themes (business, educators, military, aspirational tone)

---

## [v11.0.0] — 2024-04-16
- ✅ Full-scale biography extraction successful for 450 profiles
- ✅ Identified real narratives (David Thomas, Trevor Lloyd-Jones)
- ✅ Eliminated placeholders and junk entries (Amazon ads, null profiles)

**🎉 Ground truth dataset complete.**

---

## [v10.0.0] to [v6.0.0] — Iterative bio scrapers
- Tested multiple ways to identify biography sections in HTML
- Fallback to `<body>` scraping for inconsistent `.text-box` loading
- Introduced debug markers and manual verification of entries
- Allowed optional wait time boosts to load JS-heavy pages

**🧪 The Trevor Protocol was born.**

---

## [v5.0.0] — First successful full page fetch (Aldershot test)
- Recognized Trevor Lloyd-Jones as stable bio anchor
- Verified structure of bios with multiple sections
- Identified need for structured tagging

---

## [v4.0.0] — Email scraping fully operational
- Collected candidate emails from primary and sub-links
- Established reliable link traversal pattern

---

## [v1.0.0] — Project created
- Established main problem: decode bios using automation and NLP
- Began with Reform UK listings
- Scraper initialized using `requests` + `BeautifulSoup`

---

**Legend:**
- ✅ Major feature or improvement
- 🧪 Experimental feature
- 🔒 Final, production-ready
- 🎉 Milestone event

---

Want to know what Trevor Protocol v14 will look like? Stick around.
