#!/usr/bin/env python3
"""
Automated arXiv cs.HC (Human-Computer Interaction) paper fetcher.
Uses standard Python library (no pip packages required).
Generates an Obsidian-friendly weekly / daily reading digest.
"""

import os
import sys
import datetime
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

ARXIV_API_URL = "https://export.arxiv.org/api/query"
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}

def clean_text(text: str) -> str:
    if not text:
        return ""
    return " ".join(text.strip().split())

def fetch_recent_hci_papers(max_results: int = 8):
    params = {
        "search_query": "cat:cs.HC",
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": str(max_results)
    }
    url = f"{ARXIV_API_URL}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "HCI-Newsletter-Collector/1.0 (Academic Research Digest)"}
    )
    
    with urllib.request.urlopen(req, timeout=30) as response:
        content = response.read()
    
    root = ET.fromstring(content)
    papers = []
    
    for entry in root.findall("atom:entry", ATOM_NS):
        title = clean_text(entry.findtext("atom:title", namespaces=ATOM_NS))
        summary = clean_text(entry.findtext("atom:summary", namespaces=ATOM_NS))
        published = clean_text(entry.findtext("atom:published", namespaces=ATOM_NS))
        
        # arXiv ID & Links
        arxiv_id_full = entry.findtext("atom:id", namespaces=ATOM_NS)
        arxiv_id = arxiv_id_full.split("/abs/")[-1] if "/abs/" in arxiv_id_full else arxiv_id_full
        
        pdf_url = ""
        abs_url = f"https://arxiv.org/abs/{arxiv_id}"
        for link in entry.findall("atom:link", ATOM_NS):
            if link.attrib.get("title") == "pdf":
                pdf_url = link.attrib.get("href", "")
        
        # Authors
        authors = []
        for author in entry.findall("atom:author", ATOM_NS):
            name = author.findtext("atom:name", namespaces=ATOM_NS)
            if name:
                authors.append(clean_text(name))
        
        author_str = ", ".join(authors[:3])
        if len(authors) > 3:
            author_str += f" et al. ({len(authors)} authors)"
            
        papers.append({
            "title": title,
            "authors": author_str,
            "published": published[:10] if published else "N/A",
            "summary": summary,
            "abs_url": abs_url,
            "pdf_url": pdf_url,
            "id": arxiv_id
        })
        
    return papers

def generate_markdown(papers, output_dir: str):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"arxiv-digest-{today}.md"
    filepath = os.path.join(output_dir, filename)
    
    lines = [
        "---",
        f"date: {today}",
        "type: arxiv-digest",
        "category: cs.HC",
        "tags: [hci, arxiv, reading-queue]",
        "---",
        "",
        f"# 📡 arXiv cs.HC Digest — {today}",
        "",
        "> Automated intake of the latest Human-Computer Interaction preprints.",
        "> Pick 1–2 papers that look promising to dissect using [[90-templates/paper-note|Paper Note Template]].",
        "",
        "---",
        ""
    ]
    
    for i, paper in enumerate(papers, 1):
        lines.append(f"### {i}. {paper['title']}")
        lines.append(f"- **Authors**: {paper['authors']}")
        lines.append(f"- **Date**: {paper['published']} | **Links**: [Abstract]({paper['abs_url']}) | [PDF]({paper['pdf_url']})")
        lines.append(f"- **Status**: [ ] Unread  |  [ ] Dissected for Social Post")
        lines.append("")
        lines.append("<details>")
        lines.append("<summary><b>📖 Abstract / Summary (click to expand)</b></summary>")
        lines.append("")
        lines.append(paper["summary"])
        lines.append("")
        lines.append("</details>")
        lines.append("")
        lines.append("---")
        lines.append("")
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
        
    print(f"✅ Generated digest with {len(papers)} papers at: {filepath}")
    return filepath

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, ".."))
    digests_dir = os.path.join(project_root, "10-data", "sources", "arxiv-digests")
    os.makedirs(digests_dir, exist_ok=True)
    
    print("Fetching recent cs.HC papers from arXiv...")
    recent_papers = fetch_recent_hci_papers(max_results=8)
    generate_markdown(recent_papers, digests_dir)
