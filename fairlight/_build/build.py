#!/usr/bin/env python3
"""
Fairlight Certification build script.

Clones the PROVEN exam engine from the existing basics mock exam
(../../02-mock-exam-basics.html) and injects Fairlight question banks +
config, producing exam1.html and exam2.html. Also renders the study
guide, the Fairlight landing page and the certificate page.

Run from anywhere:  python3 build.py
Outputs land in the parent fairlight/ folder.
"""
import json
import re
import os
import html

HERE = os.path.dirname(os.path.abspath(__file__))
FAIRLIGHT = os.path.dirname(HERE)              # .../Davinci Course/fairlight
COURSE = os.path.dirname(FAIRLIGHT)            # .../Davinci Course
ENGINE_TEMPLATE = os.path.join(COURSE, "02-mock-exam-basics.html")

import data_exam1
import data_exam2
import data_studyguide

MODULE_TITLES = {
    1: "Introduction to Audio & the Fairlight Page",
    2: "Editing Dialogue",
    3: "Sound Design & Effects Editing",
    4: "Recording Voiceover & ADR",
    5: "Mixing",
    6: "Repairing & Restoring Audio",
    7: "Delivering & Mastering",
}


def number(bank):
    """Assign sequential num + ensure module_title/section_label present."""
    out = []
    for i, q in enumerate(bank):
        q = dict(q)
        q["num"] = i + 1
        mn = q["module_num"]
        q["module_title"] = MODULE_TITLES[mn]
        roman = ["", "I", "II", "III", "IV", "V", "VI", "VII"][mn]
        q["section_label"] = f"SECTION {roman} · MODULE {mn:02d}"
        if "scenario" not in q:
            q["scenario"] = None
        out.append(q)
    return out


def validate(bank, name):
    assert len(bank) == 100, f"{name}: expected 100 questions, got {len(bank)}"
    for q in bank:
        assert len(q["options"]) == 4, f"{name} q{q['num']}: needs 4 options"
        assert q["correct"] in "ABCD", f"{name} q{q['num']}: bad correct"
        for L in "ABCD":
            assert L in q["explanations"], f"{name} q{q['num']}: missing exp {L}"
        assert q.get("principle"), f"{name} q{q['num']}: missing principle"
        assert q["module_num"] in MODULE_TITLES, f"{name} q{q['num']}: bad module"
    print(f"  {name}: {len(bank)} questions OK")


def build_exam(out_name, bank, *, exam_title, eyebrow, h1, lede,
               storage_key, secs_per_q_note):
    with open(ENGINE_TEMPLATE, encoding="utf-8") as f:
        tpl = f.read()

    bank = number(bank)
    validate(bank, out_name)

    # 1. Swap the QUESTIONS data line (single line starting `const QUESTIONS = `)
    lines = tpl.split("\n")
    for i, ln in enumerate(lines):
        if ln.startswith("const QUESTIONS = "):
            lines[i] = "const QUESTIONS = " + json.dumps(bank, ensure_ascii=False) + ";"
            break
    else:
        raise RuntimeError("QUESTIONS line not found in engine template")
    tpl = "\n".join(lines)

    # 2. Swap MODULE_TITLES block
    mt_js = "const MODULE_TITLES = {\n" + ",\n".join(
        f'  {k}:{json.dumps(v, ensure_ascii=False)}' for k, v in MODULE_TITLES.items()
    ) + "\n};"
    tpl = re.sub(r"const MODULE_TITLES = \{.*?\};", mt_js, tpl, flags=re.DOTALL)

    # 3. Storage key (unique per exam so attempts don't collide)
    tpl = tpl.replace('const STORAGE_KEY = "drm_basics_v1";',
                      f'const STORAGE_KEY = "{storage_key}";')

    # 4. Visible text
    tpl = tpl.replace("<title>DaVinci Resolve Basics — Mock Exam</title>",
                      f"<title>{exam_title}</title>")
    tpl = tpl.replace('<div class="eyebrow">Shamase Studios · Basics Examination</div>',
                      f'<div class="eyebrow">{eyebrow}</div>')
    tpl = tpl.replace("<h1>DaVinci Resolve Basics</h1>", f"<h1>{h1}</h1>")
    tpl = re.sub(r'<p class="lede">A 100-question interface-fluency examination.*?</p>',
                 f'<p class="lede">{lede}</p>', tpl, count=1, flags=re.DOTALL)
    tpl = re.sub(r"that's <strong>72 seconds per question</strong>[^<]*",
                 f"that's <strong>{secs_per_q_note}</strong>. ", tpl, count=1)
    tpl = tpl.replace("DaVinci Resolve Basics · Mock Examination", f"{h1}")

    out_path = os.path.join(FAIRLIGHT, out_name)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print(f"  wrote {out_name} ({len(tpl)//1024} KB)")


def main():
    print("Building Fairlight certification…")
    build_exam(
        "exam1.html", data_exam1.QUESTIONS,
        exam_title="Fairlight Certification · Exam 1 — Fundamentals — Shamase Studios",
        eyebrow="Shamase Studios · Fairlight · Exam 1",
        h1="Fairlight Exam 1 — Fundamentals",
        lede="A 100-question examination on the Fairlight page: interface, tools, "
             "terminology and where every control lives. Two hours. Pass mark 90%. "
             "Three attempts maximum.",
        storage_key="flt_exam1_v1",
        secs_per_q_note="72 seconds per question",
    )
    build_exam(
        "exam2.html", data_exam2.QUESTIONS,
        exam_title="Fairlight Certification · Exam 2 — Workflow & Decisions — Shamase Studios",
        eyebrow="Shamase Studios · Fairlight · Exam 2",
        h1="Fairlight Exam 2 — Workflow & Decisions",
        lede="A 100-question scenario examination. Real talking-head, location-sound and "
             "delivery situations. Tests reasoning, not recall. Two hours. Pass mark 90%. "
             "Three attempts maximum.",
        storage_key="flt_exam2_v1",
        secs_per_q_note="72 seconds per question",
    )
    data_studyguide.render(FAIRLIGHT)
    print("Done.")


if __name__ == "__main__":
    main()
