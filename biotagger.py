import json
import re

# === CONFIG ===
INPUT_FILE = "reform_uk_biographies_cleaned.json"
OUTPUT_FILE = "reform_uk_biographies_tagged.json"

# === ANALYSIS LOGIC ===
def analyze_bio(text):
    text_lower = text.lower()
    tags = []

    # Archetype detection
    if re.search(r"\bteacher|educator|school|headteacher|lecturer\b", text_lower):
        tags.append("Archetype: Educator")
    if re.search(r"\bmilitary|army|navy|veteran|defense|served\b", text_lower):
        tags.append("Archetype: Military")
    if re.search(r"\bbusiness|entrepreneur|founder|ceo|director\b", text_lower):
        tags.append("Archetype: Business")
    if re.search(r"\bengineer|developer|technology|tech\b", text_lower):
        tags.append("Archetype: Technologist")

    # Tone / Psychological framing
    if re.search(r"\bfight|protect|stand against|threat\b", text_lower):
        tags.append("Tone: Adversarial")
    if re.search(r"\bhope|opportunity|build|better future\b", text_lower):
        tags.append("Tone: Aspirational")
    if re.search(r"\bcorrupt|elite|ignored|betrayed\b", text_lower):
        tags.append("Tone: Anti-Establishment")

    # Ideology indicators
    if re.search(r"\bfreedom of speech|liberty|individual rights\b", text_lower):
        tags.append("Ideology: Libertarian")
    if re.search(r"\bnational interest|british values|patriot\b", text_lower):
        tags.append("Ideology: Nationalist")
    if re.search(r"\btax reform|small government|cut bureaucracy\b", text_lower):
        tags.append("Ideology: Fiscal Conservative")

    # Digital footprint
    if re.search(r"http|www|social media|youtube|linkedin|facebook|twitter|instagram", text_lower):
        tags.append("Digital: Online Presence")

    return tags

# === MAIN EXECUTION ===
if __name__ == "__main__":
    with open(INPUT_FILE, "r", encoding="utf-8") as infile:
        data = json.load(infile)

    tagged_data = []
    for entry in data:
        tags = analyze_bio(entry["biography"])
        tagged_data.append({
            "url": entry["url"],
            "biography": entry["biography"],
            "tags": tags
        })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:
        json.dump(tagged_data, outfile, indent=2)

    print(f"✅ Done! Tagged {len(tagged_data)} bios and saved to {OUTPUT_FILE}")
