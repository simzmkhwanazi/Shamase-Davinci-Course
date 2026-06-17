#!/usr/bin/env python3
"""
MEMORANDUM (marking-key) generator for the Shamase Studios exams.

Answer data is pulled straight from each exam's own HTML (they all share one
engine: a `const QUESTIONS = [...]` array), so the keys are guaranteed to match
the live papers exactly. Output is self-contained printable HTML.

Targets:
  DaVinci Basics    (../../02-mock-exam-basics.html)    -> ../../memoranda/   PUBLISHED
  DaVinci Advanced  (../../02-mock-exam-advanced.html)  -> ../../memoranda/   PUBLISHED
  Fairlight Exam 1  (../exam1.html)                     -> ../_memoranda/     LOCAL ONLY
  Fairlight Exam 2  (../exam2.html)                     -> ../_memoranda/     LOCAL ONLY

`_memoranda/` is git-ignored; `memoranda/` is committed.

Run:  python3 memo_build.py
"""
import html
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FAIRLIGHT = os.path.dirname(HERE)
COURSE = os.path.dirname(FAIRLIGHT)
PUB_DIR = os.path.join(COURSE, "memoranda")          # published
LOCAL_DIR = os.path.join(FAIRLIGHT, "_memoranda")    # instructor-only, git-ignored

LETTERS = ["A", "B", "C", "D"]

CSS = """
:root{--bg:#0d0f17;--surface:#161a24;--surface-2:#1c2130;--border:#252a36;--border-2:#343b4a;
--text:#e8e6e0;--muted:#8b8e98;--dim:#5d626d;--gold:#d4a574;--gold-dim:#a07d52;--teal:#5dc8b7;--green:#7ec98e;--red:#ec5a5a;}
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg);color:var(--text);font-family:'Sora',sans-serif;line-height:1.5;font-size:15px}
.wrap{max-width:860px;margin:0 auto;padding:2.4rem 1.4rem 5rem}
.eyebrow{font-family:'JetBrains Mono',monospace;font-size:.7rem;text-transform:uppercase;letter-spacing:.22em;color:var(--red);margin-bottom:.8rem}
h1{font-family:'Fraunces',serif;font-weight:400;font-size:2.2rem;margin:0 0 .3rem}
.sub{font-family:'Fraunces',serif;font-style:italic;color:var(--muted);margin:0 0 1.2rem}
.banner{background:rgba(236,90,90,.1);border:1px solid var(--red);border-radius:8px;padding:.8rem 1.1rem;color:var(--red);font-size:.85rem;font-family:'JetBrains Mono',monospace;letter-spacing:.03em;margin:1rem 0 1.8rem}
.modhead{font-family:'JetBrains Mono',monospace;font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:var(--teal);margin:2rem 0 .4rem;border-top:1px solid var(--border-2);padding-top:1.2rem}
.q{border:1px solid var(--border);border-radius:9px;background:var(--surface);padding:.9rem 1.1rem;margin:.7rem 0}
.q .id{font-family:'JetBrains Mono',monospace;color:var(--gold-dim);font-size:.74rem;letter-spacing:.1em;margin-bottom:.35rem}
.q .scenario{font-family:'Fraunces',serif;font-style:italic;color:var(--muted);font-size:.92rem;margin:.2rem 0 .4rem;padding-left:.7rem;border-left:2px solid var(--border-2)}
.q .stem{font-weight:500;margin:.2rem 0 .55rem}
.opt{font-size:.9rem;padding:.28rem .5rem;border-radius:5px;margin:.18rem 0;color:var(--muted)}
.opt .l{font-family:'JetBrains Mono',monospace;font-weight:700;margin-right:.45rem;color:var(--dim)}
.opt.correct{background:rgba(126,201,142,.13);color:var(--text);border:1px solid rgba(126,201,142,.4)}
.opt.correct .l{color:var(--green)}
.opt.correct::after{content:" \\2713 CORRECT";font-family:'JetBrains Mono',monospace;font-size:.66rem;letter-spacing:.12em;color:var(--green);font-weight:700}
.key{margin-top:.55rem;padding-top:.5rem;border-top:1px dashed var(--border-2);font-size:.85rem}
.key .ans{font-family:'JetBrains Mono',monospace;color:var(--green);font-weight:700;font-size:.74rem;letter-spacing:.12em;margin-bottom:.25rem}
.key .rat{color:var(--text);margin:.25rem 0;font-size:.9rem}
.key .ex{color:var(--muted);margin:.35rem 0 .2rem;font-size:.87rem;padding:.45rem .6rem;background:rgba(126,201,142,.06);border-left:2px solid var(--green-dim,rgba(126,201,142,.4));border-radius:4px}
.key .ex b{color:var(--green);font-weight:600}
.key .wrong-head{font-family:'JetBrains Mono',monospace;color:var(--red);font-size:.68rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;margin:.7rem 0 .3rem}
.key .ww{color:var(--muted);font-size:.85rem;margin:.22rem 0;padding-left:1.6rem;position:relative;line-height:1.45}
.key .ww .wl{position:absolute;left:0;top:0;font-family:'JetBrains Mono',monospace;font-weight:700;color:var(--red);font-size:.78rem}
.key .prin{color:var(--gold);font-style:italic;font-size:.85rem;margin-top:.6rem;padding-top:.5rem;border-top:1px dashed var(--border-2)}
footer{margin-top:3rem;padding-top:1.2rem;border-top:1px solid var(--border);color:var(--dim);font-size:.7rem;font-family:'JetBrains Mono',monospace;text-align:center;letter-spacing:.08em}
@media print{
  body{background:#fff;color:#111}.q{break-inside:avoid;border-color:#ccc;background:#fafafa}
  .banner{color:#b00;border-color:#b00}.opt.correct{background:#eaf6ec}
  .key .prin{color:#9a6f30}.eyebrow{color:#b00}
}
"""

HEAD = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s — Memorandum (Instructor) — Shamase Studios</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..900&family=Sora:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>%s</style></head><body><div class="wrap">
"""


def esc(s):
    return html.escape(str(s))


def raw(s):
    # content fields may contain intended inline HTML (<code>, <kbd>, <em>); pass through
    return "" if s is None else str(s)


def extract_questions(html_path):
    """Pull the QUESTIONS array out of an exam HTML file."""
    with open(html_path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("const QUESTIONS = "):
                payload = line[len("const QUESTIONS = "):].rstrip().rstrip(";")
                return json.loads(payload)
    raise RuntimeError(f"No QUESTIONS array found in {html_path}")


def render_memo(bank, title, subtitle, out_dir, out_name, enrich=None):
    enrich = enrich or {}
    parts = [HEAD % (esc(title), CSS)]
    parts.append('<div class="eyebrow">Shamase Studios · Instructor Memorandum · Marking Key</div>')
    parts.append(f'<h1>{esc(title)}</h1>')
    parts.append(f'<p class="sub">{esc(subtitle)}</p>')
    parts.append('<div class="banner">⚠ INSTRUCTOR USE · Marking key. Question order matches the live exam exactly.</div>')
    current_mod = None
    for i, q in enumerate(bank):
        num = q.get("num", i + 1)
        mod = q.get("module_num")
        mod_title = q.get("module_title", "")
        e = enrich.get(num, {})
        key = (mod, mod_title)
        if key != current_mod:
            current_mod = key
            label = f"Module {mod:02d} · {esc(mod_title)}" if mod else esc(mod_title)
            parts.append(f'<div class="modhead">{label}</div>')
        correct = q["correct"]
        exps = q.get("explanations", {})

        # ── 1. QUESTION (leads, exam format) ──
        parts.append('<div class="q">')
        parts.append(f'<div class="id">Q{num:03d}{f" · Module {mod:02d}" if mod else ""}</div>')
        if q.get("scenario"):
            parts.append(f'<div class="scenario">{raw(q["scenario"])}</div>')
        parts.append(f'<div class="stem">{raw(q["stem"])}</div>')

        # ── 2. ANSWERS (A–D, exam format, correct marked) ──
        for j, opt in enumerate(q["options"]):
            L = LETTERS[j]
            cls = "opt correct" if L == correct else "opt"
            parts.append(f'<div class="{cls}"><span class="l">{L}</span>{raw(opt)}</div>')

        # ── 3. WHY CORRECT (+ worked example) ──
        parts.append('<div class="key">')
        parts.append(f'<div class="ans">✓ WHY {correct} IS CORRECT</div>')
        if exps.get(correct):
            parts.append(f'<div class="rat">{raw(exps[correct])}</div>')
        if e.get("example"):
            parts.append(f'<div class="ex"><b>Example.</b> {raw(e["example"])}</div>')

        # ── 4. WHY THE OTHERS ARE WRONG ──
        parts.append('<div class="wrong-head">Why the other options are incorrect</div>')
        ww = e.get("why_wrong", {})
        for L in LETTERS:
            if L == correct:
                continue
            reason = ww.get(L) or exps.get(L) or ""
            if reason:
                parts.append(f'<div class="ww"><span class="wl">{L}</span>{raw(reason)}</div>')

        # ── 5. PRINCIPLE ──
        if q.get("principle"):
            parts.append(f'<div class="prin">Principle: {raw(q["principle"])}</div>')
        parts.append('</div></div>')
    parts.append(f'<footer>{esc(title)} · Instructor Memorandum · Shamase Studios 2026</footer>')
    parts.append('</div></body></html>')
    _write(out_dir, out_name, "\n".join(parts))


def _write(out_dir, name, content):
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, name), "w", encoding="utf-8") as f:
        f.write(content)
    rel = os.path.relpath(os.path.join(out_dir, name), COURSE)
    print(f"  wrote {rel} ({len(content)//1024} KB)")


def render_index(out_dir, items, title, note):
    parts = [HEAD % (esc(title), CSS)]
    parts.append('<div class="eyebrow">Shamase Studios · Instructor Memoranda</div>')
    parts.append(f'<h1>{esc(title)}</h1>')
    parts.append(f'<p class="sub">{esc(note)}</p>')
    for fn, t, n in items:
        parts.append(f'<div class="q"><div class="stem"><a href="{fn}" style="color:var(--gold)">{esc(t)}</a></div>'
                     f'<div class="distract">{esc(n)} · {fn}</div></div>')
    parts.append('<footer>Instructor Memoranda · Shamase Studios 2026</footer>')
    parts.append('</div></body></html>')
    _write(out_dir, "index.html", "\n".join(parts))


def main():
    print("Building memoranda…")
    import enrich_basics
    import enrich_advanced
    basics_enrich = {n: {"example": ex} for n, ex in enrich_basics.EXAMPLES.items()}
    advanced_enrich = {n: {"example": ex} for n, ex in enrich_advanced.EXAMPLES.items()}

    # ---- PUBLISHED: the 2 DaVinci exams ----
    render_memo(
        extract_questions(os.path.join(COURSE, "02-mock-exam-basics.html")),
        "DaVinci Resolve — Mock Exam (Basics)",
        "Interface & Software Fundamentals · 100 questions · pass mark 90%",
        PUB_DIR, "davinci-basics-memo.html",
        enrich=basics_enrich,
    )
    render_memo(
        extract_questions(os.path.join(COURSE, "02-mock-exam-advanced.html")),
        "DaVinci Resolve — Mock Exam (Advanced / Mastery)",
        "Workflow & Decision Making · 100 questions · pass mark 90%",
        PUB_DIR, "davinci-advanced-memo.html",
        enrich=advanced_enrich,
    )
    render_index(
        PUB_DIR,
        [("davinci-basics-memo.html", "Mock Exam — Basics", "100 questions"),
         ("davinci-advanced-memo.html", "Mock Exam — Advanced (Mastery)", "100 questions")],
        "DaVinci Resolve — Memoranda",
        "Marking keys for the two DaVinci Resolve mock examinations.",
    )

    # ---- LOCAL ONLY: Fairlight (excluded from upload for now) ----
    render_memo(
        extract_questions(os.path.join(FAIRLIGHT, "exam1.html")),
        "Fairlight Exam 1 — Fundamentals",
        "Interface & Software Fundamentals · 100 questions · pass mark 90%",
        LOCAL_DIR, "fairlight-exam1-memo.html",
    )
    render_memo(
        extract_questions(os.path.join(FAIRLIGHT, "exam2.html")),
        "Fairlight Exam 2 — Workflow & Decisions",
        "Workflow & Decision Making (scenario-based) · 100 questions · pass mark 90%",
        LOCAL_DIR, "fairlight-exam2-memo.html",
    )
    render_index(
        LOCAL_DIR,
        [("fairlight-exam1-memo.html", "Fairlight Exam 1 — Fundamentals", "100 questions"),
         ("fairlight-exam2-memo.html", "Fairlight Exam 2 — Workflow & Decisions", "100 questions")],
        "Fairlight — Memoranda (held back)",
        "Marking keys for the Fairlight exams. NOT uploaded yet — instructor-only.",
    )

    print(f"\nPUBLISHED  -> {PUB_DIR}")
    print(f"LOCAL ONLY -> {LOCAL_DIR}")


if __name__ == "__main__":
    main()
