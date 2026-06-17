# -*- coding: utf-8 -*-
"""
Fairlight Certification — STUDY GUIDE generator.

Holds the written curriculum for all 7 modules (overview, lesson notes,
takeaways, shortcuts, common mistakes, practical exercise, exam-prep notes)
plus interactive Knowledge Checks, and renders study-guide.html in the
Shamase Studios design system.
"""
import html
import json
import os

# ───────────────────────────── CONTENT ─────────────────────────────
# Each module: title, overview, notes (list of (heading, [html-safe paragraphs/bullets])),
# takeaways[], shortcuts[(keys, action)], mistakes[], exercise, exam_notes[], checks[]

MODULES = [
{
 "num": 1,
 "title": "Introduction to Audio & the Fairlight Page",
 "overview": "Fairlight is DaVinci Resolve's built-in digital audio workstation (DAW). "
   "This module orients you in the page, the meters and the core vocabulary so every "
   "later skill has a home. Because Fairlight and the Edit page share one timeline, you "
   "move into serious audio work without exporting or re-importing anything.",
 "notes": [
   ("The page layout", [
     "The <strong>timeline</strong> sits in the centre with one lane (track) per audio element.",
     "The <strong>Index</strong> (left) lists tracks and markers and controls track visibility.",
     "The <strong>Mixer</strong> (right) is the channel-strip view: a fader, pan, EQ, dynamics and bus routing for every track, plus the buses and the Main.",
     "<strong>Transport controls and the toolbar</strong> run along the bottom.",
   ]),
   ("Reading levels", [
     "Digital meters read <strong>dBFS</strong> (decibels relative to full scale). <strong>0 dBFS is the ceiling</strong> — go above it and you clip (distort).",
     "Meters turning <em>red</em> at the top warn you of clipping. Pull the level down to restore headroom.",
     "Perceived loudness for delivery is measured separately in <strong>LUFS</strong> (covered in Module 7).",
   ]),
   ("Core vocabulary", [
     "<strong>Clip</strong>: one segment of audio sitting on a track. <strong>Track</strong>: the lane that holds clips. <strong>Bus</strong>: a destination that sums multiple tracks.",
     "<strong>Playhead</strong>: your current position in the timeline.",
     "<strong>Clip gain</strong> changes one clip's level; the <strong>track fader</strong> changes the whole track's level. Set clip gain first, then mix with faders.",
     "Track formats describe channel count: <strong>mono</strong> (1), <strong>stereo</strong> (2), <strong>5.1</strong> (6), <strong>adaptive</strong> (variable).",
   ]),
   ("Transport & navigation", [
     "<strong>Spacebar</strong> plays/stops. <strong>J-K-L</strong> shuttles: J back, K stop, L forward — tap L or J repeatedly to speed up.",
     "Zoom in horizontally to see waveform detail down to sample level; this precision underpins editing and repair.",
   ]),
 ],
 "takeaways": [
   "Fairlight is a full DAW inside Resolve, sharing the Edit page's timeline.",
   "0 dBFS is the hard digital ceiling — never clip; keep headroom.",
   "Clip gain = one clip; fader = whole track. Balance clip gain before mixing.",
   "Solo (S) and Mute (M) on track headers are non-destructive monitoring tools.",
 ],
 "shortcuts": [
   ("Spacebar", "Play / stop"),
   ("J / K / L", "Shuttle back / stop / forward (repeat to speed up)"),
   ("S / M", "Solo / Mute a track"),
   ("Cmd/Ctrl + S", "Save project"),
 ],
 "mistakes": [
   "Treating red meters as 'good and loud' — red means clipping.",
   "Riding the track fader to fix one loud clip instead of using clip gain.",
   "Exporting/re-importing audio instead of just switching to the Fairlight page.",
   "Ignoring headroom and mixing everything near 0 dBFS.",
 ],
 "exercise": "Open a finished interview edit, switch to Fairlight, and identify the Index, "
   "Mixer, timeline and transport. Solo each track in turn, watch the meters, and bring any "
   "clipping clip down with clip gain until peaks sit comfortably below 0 dBFS.",
 "exam_notes": [
   "Know the role of each panel: Index, Mixer, timeline, transport.",
   "dBFS vs LUFS; 0 dBFS = clipping ceiling.",
   "Clip gain vs track fader; mono/stereo/5.1/adaptive formats.",
   "J-K-L and spacebar transport behaviour.",
 ],
 "checks": [
   ("Which page is Resolve's dedicated audio workstation?",
    ["Edit", "Fairlight", "Color", "Cut"], 1,
    "Fairlight is the full DAW page; Edit has tracks but is picture-led."),
   ("0 dBFS represents…", ["Silence", "The digital clipping ceiling", "The loudness target", "A pan position"], 1,
    "0 dBFS is the maximum digital level; above it the signal clips."),
   ("Clip gain adjusts…", ["The whole track", "One clip's level", "The Main bus", "The monitor only"], 1,
    "Clip gain is per-clip; the fader is per-track."),
   ("J-K-L keys control…", ["EQ", "Transport/shuttle", "Pan", "Buses"], 1,
    "J back, K stop, L forward; repeat taps speed up."),
   ("The Mixer panel contains…", ["Markers", "Faders, pan, EQ, dynamics, routing", "Imported media", "Grades"], 1,
    "The Mixer is the channel-strip workspace."),
   ("A mono track carries…", ["One channel", "Two channels", "Six channels", "Variable channels"], 0,
    "Mono = 1 channel; stereo = 2; 5.1 = 6; adaptive = variable."),
   ("Red at the top of a meter means…", ["Muted", "Soloed", "Clipping", "Flagged"], 2,
    "Red = the signal hit/exceeded 0 dBFS."),
   ("Fairlight and the Edit page…", ["Are separate projects", "Share one timeline", "Need a render to sync", "Can't both edit audio"], 1,
    "They're two views of the same timeline."),
   ("The S button on a track header…", ["Saves", "Solos", "Splits", "Shows spectrogram"], 1,
    "S solos; M mutes."),
   ("Spacebar in Fairlight…", ["Splits the clip", "Plays/stops", "Adds a marker", "Opens the Mixer"], 1,
    "Spacebar is play/stop."),
 ],
},
{
 "num": 2,
 "title": "Editing Dialogue",
 "overview": "Dialogue is the spine of talking-head, interview and corporate work. This module "
   "covers organising production sound, cutting cleanly, smoothing edits, and keeping picture "
   "and audio in sync — the day-to-day craft that makes speech sound effortless.",
 "notes": [
   ("Organise first", [
     "Put each character / microphone on its <strong>own track</strong> so you can choose the best mic, balance levels and process each voice independently.",
     "Keep and reuse <strong>room tone</strong> (ambient 'silence' recorded on location) — it fills gaps so cuts don't drop to dead digital silence.",
   ]),
   ("Cutting & smoothing", [
     "Split clips with the <strong>razor / Cmd-Ctrl+B</strong> at the playhead.",
     "Add small <strong>fades</strong> to clip edges and <strong>crossfades</strong> between overlapping takes — they remove the clicks caused by cutting on a non-zero waveform point.",
     "<strong>Edit Selection (A)</strong> moves whole clips; <strong>Range Selection (R)</strong> selects a span of time across tracks regardless of clip boundaries.",
   ]),
   ("Levelling & sync", [
     "Use <strong>clip gain / volume keyframes</strong> to lift quiet words and tame loud ones <em>before</em> compression.",
     "Use <strong>snapping</strong> plus <strong>nudge keys</strong> for frame-accurate placement and lip-sync.",
     "<strong>Link/group</strong> related clips so trims keep them in sync; <strong>disable</strong> (don't delete) a clip to silence it non-destructively.",
   ]),
   ("Comping the best performance", [
     "A/B takes by soloing each in place.",
     "Splice the clearest word or phrase from another take and match its level/EQ so the join is invisible.",
     "Keep natural breaths (or gently reduce them) — stripping every breath makes speech robotic.",
   ]),
 ],
 "takeaways": [
   "Separate characters/mics onto their own tracks.",
   "Fades and crossfades kill edit-point clicks.",
   "Room tone fills gaps so cuts are inaudible.",
   "Level with clip gain before EQ and compression.",
 ],
 "shortcuts": [
   ("A", "Edit Selection mode (move whole clips)"),
   ("R", "Range Selection mode (select a time span)"),
   ("Cmd/Ctrl + B", "Split clip at playhead"),
   ("M", "Add marker"),
   ("N", "Toggle snapping (commonly)"),
 ],
 "mistakes": [
   "Cutting without fades, leaving clicks at every edit.",
   "Deleting room tone, then fighting dead-silent gaps.",
   "Stripping every breath until speech sounds unnatural.",
   "Compressing before levelling, so the compressor chases a moving target.",
 ],
 "exercise": "Take a two-minute interview. Separate the speaker onto a clean track, remove an 'umm' "
   "and a chair creak, patch the gaps with room tone, add edge fades, and even out two quiet words "
   "with clip gain. The cut should sound continuous and natural.",
 "exam_notes": [
   "A vs R selection modes; razor/split.",
   "Why fades/crossfades remove clicks.",
   "Role of room tone in gap-filling.",
   "Order: edit → clean → level → process.",
 ],
 "checks": [
   ("First step organising production dialogue?", ["Bounce to one clip", "Each character/mic on its own track", "Delete room tone", "Add reverb"], 1,
    "Separate sources for independent control."),
   ("Small fades on clip edges…", ["Change pitch", "Remove edit-point clicks", "Raise sample rate", "Create surround"], 1,
    "They smooth the waveform discontinuity that clicks."),
   ("Room tone is used to…", ["Replace dialogue", "Fill gaps so silence isn't dead", "Set loudness", "Act as a click track"], 1,
    "It keeps ambience continuous across cuts."),
   ("Range Selection (R) selects…", ["Whole clips only", "A time span across tracks", "The Main bus", "Markers"], 1,
    "R selects by time; A selects whole clips."),
   ("Blend two overlapping takes with a…", ["Crossfade", "Bus", "Marker", "Submix"], 0,
    "A crossfade fades one out as the other fades in."),
   ("To even out level swings within one lav clip, use…", ["A gate", "Clip gain / volume keyframes", "Reverb", "Pitch shift"], 1,
    "Ride clip gain before compression."),
   ("Disabling a clip…", ["Deletes it", "Silences it non-destructively", "Exports it", "Makes it a marker"], 1,
    "Disabled clips stay in place, silent, reversible."),
   ("Frame-accurate sync uses…", ["Reverb + chorus", "Snapping + nudge keys", "Solo + mute", "Pan + EQ"], 1,
    "Snapping locks to references; nudge fine-tunes."),
   ("Best practice on breaths?", ["Remove all", "Keep/reduce, not eliminate", "Replace with silence", "Add reverb"], 1,
    "Natural breaths keep speech human."),
   ("Correct order of operations?", ["Compress then level", "Edit/level/clean, then EQ/compress", "Master first", "Music before dialogue"], 1,
    "Clean and even the source before shaping it."),
 ],
},
{
 "num": 3,
 "title": "Sound Design & Effects Editing",
 "overview": "Sound design adds impact, realism and emotion. In Fairlight that means a disciplined "
   "spotting pass, smart use of the Sound Library, layering elements into custom effects, and "
   "building believable ambience — all routed so you can control whole layers at once.",
 "notes": [
   ("Spot before you build", [
     "Do a <strong>spotting pass</strong>: place <strong>named markers (M)</strong> at every point that needs a sound. This is your build map.",
   ]),
   ("The Sound Library", [
     "Search, <strong>preview/audition</strong> and drag in effects from the built-in library; you can <strong>mount your own folders</strong> so your whole collection is searchable in-app.",
   ]),
   ("Layering & organisation", [
     "Keep <strong>hard FX</strong> (footsteps, slams), <strong>designed elements</strong> (whooshes, impacts, drones) and <strong>ambience</strong> on separate tracks.",
     "<strong>Layer</strong> multiple elements into one richer effect (e.g. whoosh + low boom + transient).",
     "<strong>Colour-code</strong> tracks by type (dialogue / Foley / ambience / SFX) so a dense session stays readable.",
   ]),
   ("Control the layer with a bus", [
     "Route all SFX tracks to a single <strong>SFX sub-bus</strong> so one fader rides the entire effects layer.",
     "Use <strong>clip gain</strong> for per-effect level tweaks without touching the rest.",
     "<strong>Foley</strong> is performed everyday sound (footsteps, cloth, props) recorded to picture for realism.",
   ]),
 ],
 "takeaways": [
   "Spot with named markers first; design second.",
   "Audition in the Sound Library, commit only the keeper.",
   "Layer elements for custom, impactful sounds.",
   "Bus a layer to one fader for instant control.",
 ],
 "shortcuts": [
   ("M", "Add marker (build your spotting list)"),
   ("Double-click marker", "Name/note the cue"),
   ("Drag from Sound Library", "Place an effect on a track"),
 ],
 "mistakes": [
   "Dropping effects randomly instead of spotting first.",
   "Mixing SFX onto the dialogue track, losing independent control.",
   "Relying on one thin library file instead of layering for weight.",
   "Audible loop seams in short ambience beds (fix with crossfades).",
 ],
 "exercise": "Spot a 30-second advert with named markers. Build one 'whoosh-to-impact' transition by "
   "layering three elements, add an ambience bed under the scene, route all SFX to one sub-bus, and "
   "balance the whole layer with a single fader.",
 "exam_notes": [
   "Spotting list via markers; Sound Library audition/mount.",
   "Track separation: hard FX / design / ambience.",
   "Layering concept; SFX sub-bus for group control.",
   "Foley vs ADR distinction.",
 ],
 "checks": [
   ("A spotting list is built with…", ["Buses", "Named markers", "Grades", "Codecs"], 1,
    "Markers map every needed sound."),
   ("Audition an effect before committing in the…", ["Deliver queue", "Sound Library", "Index", "ADR panel"], 1,
    "Preview in the Sound Library, then drag in."),
   ("Hard FX belong on…", ["The dialogue track", "Dedicated SFX tracks", "The Main bus", "A muted track"], 1,
    "Separate so you can group and balance them."),
   ("Layering means…", ["Normalising", "Combining elements into one richer sound", "Bouncing", "Patching"], 1,
    "Stack complementary elements into one effect."),
   ("Route all SFX to one bus to…", ["Delete dialogue", "Ride the whole layer with one fader", "Change sample rate", "Export faster"], 1,
    "Group control via a sub-bus."),
   ("Foley is…", ["Dialogue replacement", "Performed everyday sounds to picture", "A loudness standard", "A bus type"], 1,
    "Footsteps, cloth, props performed in sync."),
   ("Ambience beds provide…", ["A click track", "A continuous sense of place", "The loudness meter", "Pan automation"], 1,
    "They ground a scene's environment."),
   ("Per-effect level changes use…", ["The Main fader", "Clip gain", "Monitor level", "The loudness target"], 1,
    "Clip gain rides one effect independently."),
   ("Colour-coding tracks mainly helps with…", ["Loudness", "Reading a busy session", "Sample rate", "Pitch"], 1,
    "Visual organisation of complex sessions."),
   ("Audible loop in a short ambience is fixed by…", ["Muting", "Crossfading overlapping copies", "A marker", "Higher bit depth"], 1,
    "Crossfades hide the loop seam."),
 ],
},
{
 "num": 4,
 "title": "Recording Voiceover & ADR",
 "overview": "Sometimes you must capture new audio: a narration to picture, or replacement dialogue "
   "when production sound is unusable. This module covers routing inputs, arming tracks, setting "
   "safe levels, the ADR panel, and blending new recordings into the scene.",
 "notes": [
   ("Setting up to record", [
     "Use <strong>Patch Input/Output</strong> to route your mic/source input to a track and route tracks to outputs.",
     "<strong>Record-enable (arm)</strong> only the target track — stray arms risk recording onto the wrong track.",
     "Set a <strong>healthy level with headroom</strong>: peaks well below 0 dBFS. Clipped recordings can't be fixed.",
     "<strong>Monitor on headphones</strong> when recording live to picture so speaker output doesn't bleed into the mic.",
   ]),
   ("ADR (Automated Dialogue Replacement)", [
     "ADR re-records a line in sync to replace ruined production audio.",
     "The <strong>ADR panel</strong> manages a cue list, take recording, and <strong>count-in beeps/streamers</strong> plus a <strong>guide track</strong> so the performer lands exactly on time.",
     "<strong>Loop/punch recording</strong> lets you re-take a section without rebuilding the session.",
   ]),
   ("Blending the new audio", [
     "Record <strong>multiple takes</strong>, then audition and comp the best performance.",
     "Match <strong>level, EQ and the scene's space</strong> (room tone/reverb) so the new line sits believably — a pristine line stands out against a noisy scene.",
   ]),
 ],
 "takeaways": [
   "Patch input → arm the target track → set safe level → record.",
   "Headphones prevent mic bleed when recording to picture.",
   "ADR uses guide track + count-in cues for tight timing.",
   "Blend new recordings by matching level, EQ and ambience.",
 ],
 "shortcuts": [
   ("Arm/Record-enable button", "Marks the track that will capture audio"),
   ("Patch Input/Output", "Route inputs to tracks, tracks to outputs"),
   ("ADR panel", "Cue list, guide track, count-in, take recording"),
 ],
 "mistakes": [
   "Recording with several tracks armed and overwriting the wrong one.",
   "Monitoring on speakers and capturing bleed/feedback.",
   "Peaking at 0 dBFS with no headroom.",
   "Leaving ADR too 'clean' so it doesn't match the scene.",
 ],
 "exercise": "Add a narration track, patch your mic, arm only that track, set levels for safe headroom on "
   "headphones, and record three takes of a line. Comp the best, then drop matching room tone under it so "
   "it blends with the scene.",
 "exam_notes": [
   "Patch Input/Output and arming workflow.",
   "Why headphones for live-to-picture recording.",
   "ADR = Automated Dialogue Replacement; guide track + cues.",
   "Blending: level/EQ/ambience matching.",
 ],
 "checks": [
   ("Before recording onto a track you must…", ["Render", "Arm it and set its input", "Delete the Main", "Open Color"], 1,
    "Arm the target track and patch an input."),
   ("Patch Input/Output is for…", ["Grading", "Routing inputs to tracks/outputs", "Loudness", "Markers"], 1,
    "It's the routing matrix."),
   ("ADR stands for…", ["Audio Data Recording", "Automated Dialogue Replacement", "Ambient Dynamic Range", "Adaptive Direct Routing"], 1,
    "Re-recording dialogue to picture."),
   ("Monitor on headphones when recording to picture to…", ["Raise sample rate", "Prevent speaker bleed into the mic", "Change codec", "Add reverb"], 1,
    "Stops feedback/bleed into the live mic."),
   ("The ADR guide track…", ["Is the Main bus", "Plays the original line for timing reference", "Is a meter", "Is a colour preset"], 1,
    "The performer matches its timing."),
   ("Set record levels so peaks…", ["Hit 0 dBFS", "Sit safely below 0 dBFS (headroom)", "Stay in the red", "Are muted"], 1,
    "Headroom protects against clipping."),
   ("Recording multiple takes lets you…", ["Reduce bit depth", "Choose the best performance", "Skip editing", "Export faster"], 1,
    "Comp the strongest take."),
   ("Count-in beeps/streamers exist to…", ["Trigger render", "Cue the performer to start on time", "Set codec", "Add a fade"], 1,
    "They give a precise start point."),
   ("Loop recording is used to…", ["Render in a loop", "Capture repeated takes without stopping", "Change bus format", "Solo the Main"], 1,
    "Cycle a cue for multiple takes."),
   ("To make clean ADR sit in a noisy scene…", ["Leave it pristine", "Add the scene's room tone/ambience under it", "Add heavy reverb everywhere", "Lower the whole mix"], 1,
    "Match the scene's noise floor and space."),
 ],
},
{
 "num": 5,
 "title": "Mixing",
 "overview": "Mixing balances every element into a clear, controlled whole. This module covers panning, "
   "EQ, dynamics (compressor, limiter, gate), buses and sends, and automation — with dialogue "
   "intelligibility as the constant priority.",
 "notes": [
   ("Balance & space", [
     "The <strong>fader</strong> sets a track's overall level — your primary balancing tool.",
     "<strong>Pan</strong> places sound across the stereo field. Keep <strong>lead dialogue centred</strong>; widen music/ambience to make space for the voice.",
   ]),
   ("Tone & dynamics", [
     "<strong>EQ</strong> boosts/cuts frequency bands. A <strong>high-pass (low-cut)</strong> on dialogue clears rumble below the voice.",
     "A <strong>compressor</strong> reduces dynamic range (evens loud/soft); <strong>threshold</strong> sets where it acts, <strong>ratio</strong> how hard.",
     "A <strong>limiter</strong> is a brick-wall ceiling that stops peaks exceeding a set level. A <strong>noise gate</strong> silences signal below a threshold (cleaning gaps).",
     "Track EQ shapes a whole track; Clip EQ fixes one clip; bus EQ shapes a group.",
   ]),
   ("Routing & automation", [
     "A <strong>bus</strong> sums tracks. <strong>Main 1</strong> is the master output. An <strong>Aux send</strong> feeds several tracks to one shared effect (e.g. reverb).",
     "<strong>Automation</strong> records fader/pan/plugin moves that replay over time. <strong>Touch</strong> writes only while you hold the control; <strong>Latch</strong> keeps the last value; <strong>Write</strong> overwrites continuously.",
     "<strong>Duck</strong> music under speech with level automation or side-chain ducking so dialogue always leads.",
     "<strong>Monitor/Control-Room level</strong> changes only what you hear — never the actual mix.",
   ]),
 ],
 "takeaways": [
   "Dialogue leads: keep it centred and clear; duck the bed under it.",
   "High-pass dialogue to clear rumble; compress to even dynamics.",
   "Use sub-buses for cohesive group processing; aux sends for shared reverb.",
   "Monitor level ≠ mix level.",
 ],
 "shortcuts": [
   ("Fader", "Track output level"),
   ("S / M", "Solo / Mute while balancing"),
   ("Automation mode (Touch/Latch/Write)", "How moves are recorded"),
 ],
 "mistakes": [
   "Letting dialogue get buried so it vanishes at low volume.",
   "Compressing noisy audio hard, making it 'pump'.",
   "Putting reverb on every clip instead of one aux send.",
   "Mixing to a too-quiet monitor and over-pushing levels.",
 ],
 "exercise": "Mix a talking-head with music: high-pass and gently compress the dialogue on a dialogue "
   "sub-bus, centre the voice, widen the music, and automate the music to duck under the presenter. "
   "Confirm the voice stays clear at low volume on a phone.",
 "exam_notes": [
   "Compressor threshold/ratio; limiter vs compressor; gate.",
   "High-pass purpose on dialogue.",
   "Bus vs Aux send; Main 1 as master.",
   "Automation modes; monitor level vs mix level.",
 ],
 "checks": [
   ("Lead dialogue is usually panned…", ["Hard left", "Centre", "Hard right", "Randomly"], 1,
    "Centred voice anchors the mix."),
   ("A high-pass filter on dialogue…", ["Adds bass", "Removes low rumble", "Boosts loudness", "Creates reverb"], 1,
    "Low-cut clears rumble below the voice."),
   ("A compressor…", ["Adds echo", "Reduces dynamic range", "Changes pitch", "Makes markers"], 1,
    "It evens out loud and soft."),
   ("A limiter…", ["Boosts bass", "Acts as a hard ceiling on peaks", "Changes frame rate", "Only works on buses"], 1,
    "Brick-wall ceiling that protects against clipping."),
   ("A noise gate…", ["Adds reverb", "Silences signal below a threshold", "Raises loudness", "Pans the track"], 1,
    "It closes on quiet passages."),
   ("The default master bus is…", ["Aux 1", "Main 1", "Solo bus", "Sound Library"], 1,
    "Main 1 carries the final mix."),
   ("An Aux send is used to…", ["Replace dialogue", "Share one effect (e.g. reverb) across tracks", "Set frame rate", "Disable a track"], 1,
    "Send tracks to a shared effect."),
   ("Touch automation writes…", ["Always", "Only while you hold the control", "Never", "Only on buses"], 1,
    "It reverts when released; Write overwrites continuously."),
   ("To keep a voiceover clear over music, you…", ["Pan VO hard left", "Duck the music under the VO", "Raise both to 0 dBFS", "Mute the VO"], 1,
    "Automate/side-chain the music down under speech."),
   ("Monitor/Control-Room level affects…", ["The exported mix", "Only what you hear", "The codec", "Marker colour"], 1,
    "It's your listening volume, not the mix."),
 ],
},
{
 "num": 6,
 "title": "Repairing & Restoring Audio",
 "overview": "Location work means rooms you can't treat: hum, hiss, clicks and reverberant spaces. "
   "Fairlight FX is the bundled plugin set for fixing them. The golden rule: diagnose first, repair "
   "before you mix, and use the least processing that works.",
 "notes": [
   ("Know your tools (Fairlight FX)", [
     "<strong>De-Hummer</strong>: removes mains hum (50/60 Hz) and harmonics from location power/lighting.",
     "<strong>De-Esser</strong>: tames harsh sibilance ('s', 'sh') without dulling the whole voice.",
     "<strong>Noise Reduction</strong>: learn a <em>profile</em> from a voice-free moment, then subtract that signature. Use conservatively — too much makes voices watery/metallic.",
     "<strong>De-Click / De-Crackle</strong>: remove short transient pops and crackle.",
     "<strong>Voice Isolation</strong> (recent versions): AI separation that pulls clean dialogue out of noisy/reverberant rooms.",
   ]),
   ("Method", [
     "<strong>Diagnose first</strong>: listen and identify each specific defect (hum, hiss, click, reverb) before choosing a tool. A frequency analyser/spectrogram helps you see tones you might miss.",
     "Match repair <strong>scope</strong> to the problem: a one-off click gets a clip/sample-level fix; a consistent shoot-day defect gets a track-level chain or saved preset.",
     "<strong>Repair before you mix</strong>: clean source makes EQ/compression/levels behave predictably; heavy compression on noisy audio pumps the noise.",
   ]),
   ("Finishing", [
     "After heavy de-noising, lay a low bed of <strong>matching room tone</strong> so cleaned gaps feel natural, and restore lost presence with a gentle EQ lift.",
     "<strong>A/B bypass</strong> every repair and check on multiple systems — confirm a real improvement, not just a change.",
     "<strong>Clipping at the source is largely unrecoverable</strong> — mitigate, consider ADR, and capture clean levels next time.",
   ]),
 ],
 "takeaways": [
   "Diagnose, then pick the matching tool.",
   "Noise Reduction needs a clean noise profile; less is more.",
   "Repair before mixing.",
   "Clipping is destructive — prevention beats repair.",
 ],
 "shortcuts": [
   ("Zoom to sample level", "Find and remove individual clicks"),
   ("Insert on clip vs track", "Fix one clip vs process the whole track"),
   ("Bypass (A/B)", "Verify the repair genuinely helps"),
 ],
 "mistakes": [
   "Over-applying noise reduction, leaving watery/metallic artefacts.",
   "Compressing before repairing, so the noise pumps.",
   "Blanket Main-bus repair that harms clean elements.",
   "Trusting the waveform instead of listening on multiple systems.",
 ],
 "exercise": "Take an untreated-room interview with AC hiss and a single cable click. Capture a noise "
   "profile from a clean moment and reduce the hiss conservatively, de-click the single pop at sample "
   "level, lay subtle room tone under the cleaned gaps, then A/B bypass to confirm improvement.",
 "exam_notes": [
   "De-Hummer / De-Esser / Noise Reduction / De-Click roles.",
   "Noise profile learning; artefacts from over-processing.",
   "Repair-before-mix order; scope matching.",
   "Clipping is unrecoverable; Voice Isolation for rooms.",
 ],
 "checks": [
   ("The bundled audio plugins are called…", ["ResolveFX", "Fairlight FX", "OpenFX", "Color FX"], 1,
    "Fairlight FX = the audio plugin set."),
   ("Steady 50/60 Hz mains hum is removed with…", ["De-Esser", "De-Hummer", "Reverb", "Chorus"], 1,
    "De-Hummer targets hum and harmonics."),
   ("Harsh 'sss' sounds are tamed with…", ["De-Hummer", "De-Esser", "Gate", "Flanger"], 1,
    "A de-esser targets sibilance."),
   ("Noise Reduction works best when you…", ["Guess settings", "Capture a noise profile from clean noise", "Mute the track", "Raise loudness"], 1,
    "Teach it the noise, then subtract it."),
   ("Over-applying noise reduction causes…", ["Perfect audio", "Watery/metallic artefacts", "Higher sample rate", "More markers"], 1,
    "Use the least amount that works."),
   ("A single click on one clip is best fixed…", ["On the whole track", "At clip/sample level on that clip", "On the Main bus", "Across the timeline"], 1,
    "Match scope to the problem."),
   ("Best processing order for noisy, uneven, dull dialogue?", ["Compress, EQ, de-noise", "De-noise, EQ, compress", "EQ, de-noise, nothing", "Master first"], 1,
    "Clean first, then tone, then dynamics."),
   ("Clipped source audio is…", ["Always fully recoverable", "Largely unrecoverable", "Fixed by noise reduction", "Fixed by loudness"], 1,
    "Clipping destroys data permanently."),
   ("A reverberant, echoey room is best helped by…", ["More reverb", "AI Voice Isolation", "A gate alone", "Pitch shift"], 1,
    "Voice Isolation separates dialogue from the room."),
   ("To verify a repair really helped…", ["Trust it blindly", "A/B bypass and check on multiple systems", "Look at the waveform only", "Master louder"], 1,
    "Confirm improvement by listening, not just looking."),
 ],
},
{
 "num": 7,
 "title": "Delivering & Mastering",
 "overview": "Delivery makes your mix meet the spec of wherever it plays. This module covers loudness "
   "(LUFS), true peak, normalisation, the loudness meter, stems, and the Deliver page audio settings — "
   "so the same content lands correctly on broadcast, web and social.",
 "notes": [
   ("Loudness & true peak", [
     "Perceived loudness is measured in <strong>LUFS</strong>. Targets: <strong>broadcast ≈ -23 LUFS</strong> (EBU R128) / <strong>-24 LKFS</strong> (US ATSC A/85); <strong>online/social ≈ -14 LUFS</strong>; <strong>spoken-word/podcast ≈ -16 LUFS</strong>.",
     "Cap <strong>True Peak around -1 dBTP</strong> so lossy encoding doesn't push peaks into clipping.",
     "The Fairlight <strong>loudness meter</strong> shows Momentary, Short-term and <strong>Integrated</strong> (whole-programme average) — Integrated is what specs reference.",
   ]),
   ("Hitting the target", [
     "<strong>Audio Normalization</strong> can target a peak level or a loudness standard (e.g. R128) to reach a target automatically.",
     "Watch the <strong>Main bus meter</strong> before export: no clipping, correct loudness, safe true peak.",
     "A clean master near <strong>-14 LUFS / -1 dBTP</strong> travels well across most social platforms; don't mix far hotter just to be turned down.",
   ]),
   ("Stems & export", [
     "Set codec, sample rate and bit depth on the <strong>Deliver page → render settings → Audio tab</strong>. Professional masters are <strong>48 kHz / 24-bit</strong>.",
     "Deliver <strong>D/M/E stems</strong> (separate dialogue, music, effects buses) so clients can re-balance, re-version or dub. Keep <strong>dialogue separate + M&amp;E</strong> for translation.",
     "Confirm every sub-bus is routed to the <strong>Main</strong> and do a full-listen QC before sending.",
   ]),
 ],
 "takeaways": [
   "LUFS targets differ by platform; integrated loudness is the spec number.",
   "True peak ≈ -1 dBTP protects against encoding clipping.",
   "Stems (D/M/E) enable re-balancing and translation.",
   "Deliver 48 kHz / 24-bit; QC by listening before sending.",
 ],
 "shortcuts": [
   ("Deliver page → Audio tab", "Codec, sample rate, bit depth"),
   ("Loudness meter", "Integrated / Short-term / Momentary LUFS"),
   ("Audio Normalization", "Hit a peak or loudness target automatically"),
 ],
 "mistakes": [
   "Mastering to 0 dBFS / ignoring loudness specs.",
   "Forgetting to route a sub-bus to the Main (missing layer on export).",
   "Delivering a flat mix when the client needs stems for translation.",
   "Exporting without a full-listen QC.",
 ],
 "exercise": "Master a finished talking-head to ≈ -14 LUFS with true peak ≤ -1 dBTP, verify on the loudness "
   "meter, route D/M/E to separate buses, and export both the full mix and the stems at 48 kHz / 24-bit. "
   "QC the file end-to-end before 'delivery'.",
 "exam_notes": [
   "LUFS targets: -23/-24 broadcast, -14 online, -16 podcast.",
   "True peak ≈ -1 dBTP; Integrated loudness meaning.",
   "Audio Normalization modes; 48 kHz/24-bit masters.",
   "Stems & M&E for re-versioning/translation; route to Main.",
 ],
 "checks": [
   ("Loudness is measured in…", ["dBFS peaks only", "LUFS", "Hertz", "Pixels"], 1,
    "LUFS measures perceived loudness over time."),
   ("EBU R128 broadcast target is about…", ["-9 LUFS", "-14 LUFS", "-23 LUFS", "0 LUFS"], 2,
    "Broadcast ≈ -23 LUFS (US ATSC -24 LKFS)."),
   ("Online/social platforms target roughly…", ["-23 LUFS", "-14 LUFS", "-3 LUFS", "+6 LUFS"], 1,
    "Around -14 LUFS."),
   ("True Peak is usually capped at…", ["0 dBTP", "-1 dBTP", "+3 dBTP", "-23 dBTP"], 1,
    "≈ -1 dBTP to survive encoding."),
   ("Integrated loudness is…", ["The loudest sample", "The whole-programme average", "The pan position", "The codec"], 1,
    "It's the number specs reference."),
   ("Audio export settings live on the…", ["Color page", "Deliver page Audio tab", "Sound Library", "Index"], 1,
    "Deliver → render settings → Audio."),
   ("Delivering D/M/E stems lets clients…", ["Lower sample rate", "Re-balance/re-version/dub", "Change the grade", "Add markers"], 1,
    "Separate stems enable re-versioning."),
   ("For translation, keep separate…", ["The dialogue (with M&E)", "The grade", "The markers", "The thumbnail"], 0,
    "Dialogue separate + M&E allows dubbing."),
   ("Professional master audio is…", ["48 kHz / 24-bit", "8 kHz / 8-bit", "22 kHz / 16-bit mono", "96 kHz / 4-bit"], 0,
    "48 kHz, 24-bit is the standard."),
   ("If a sub-bus isn't routed to Main on export…", ["Nothing happens", "That layer goes missing", "Loudness changes", "Frame rate changes"], 1,
    "Verify routing before delivery."),
 ],
},
]


# ───────────────────────────── RENDERER ─────────────────────────────
CSS = """
:root{--bg:#0d0f17;--surface:#161a24;--surface-2:#1c2130;--surface-3:#232936;
--border:#252a36;--border-2:#343b4a;--text:#e8e6e0;--muted:#8b8e98;--dim:#5d626d;
--gold:#d4a574;--gold-dim:#a07d52;--teal:#5dc8b7;--red:#ec5a5a;--green:#7ec98e;}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{margin:0;padding:0;background:var(--bg);color:var(--text);font-family:'Sora',sans-serif;line-height:1.6;font-size:16px}
body{background-image:radial-gradient(ellipse at top,rgba(212,165,116,.05),transparent 60%);min-height:100vh}
a{color:var(--teal);text-decoration:none}a:hover{text-decoration:underline}
.wrap{max-width:820px;margin:0 auto;padding:2.5rem 1.25rem 6rem}
h1,h2,h3{font-family:'Fraunces',serif;letter-spacing:-.015em;font-weight:400}
h1{font-size:clamp(2.1rem,7vw,3rem);margin:0 0 .4rem;font-variation-settings:"opsz" 144}
h2{font-size:1.7rem;color:var(--gold);font-style:italic;margin:2.4rem 0 .8rem}
h3{font-size:1.12rem;color:var(--teal);margin:1.6rem 0 .6rem;font-style:normal}
h4{font-family:'JetBrains Mono',monospace;font-size:.74rem;text-transform:uppercase;letter-spacing:.18em;color:var(--gold);margin:1.4rem 0 .6rem;font-weight:600}
.eyebrow{font-family:'JetBrains Mono',monospace;font-size:.7rem;text-transform:uppercase;letter-spacing:.22em;color:var(--teal);margin-bottom:1rem}
.lede{font-family:'Fraunces',serif;font-style:italic;font-size:1.12rem;color:var(--muted);margin:.6rem 0 1.6rem}
strong{color:var(--gold);font-weight:600}em{color:var(--teal);font-style:italic}
p{margin:.7rem 0}ul{margin:.6rem 0;padding-left:1.3rem}li{margin:.4rem 0}
code{font-family:'JetBrains Mono',monospace;font-size:.85em;background:var(--surface-2);padding:.12em .42em;border-radius:3px;color:var(--gold);border:1px solid var(--border)}
.toc{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:1.2rem 1.4rem;margin:1.6rem 0 2.4rem}
.toc h4{margin-top:0}
.toc ol{margin:.4rem 0;padding-left:1.3rem}.toc li{margin:.45rem 0}
.module{border-top:2px solid var(--border-2);padding-top:1rem;margin-top:3rem}
.module .mnum{font-family:'JetBrains Mono',monospace;font-size:.72rem;letter-spacing:.18em;color:var(--gold-dim);text-transform:uppercase}
.card{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:1.1rem 1.3rem;margin:1rem 0}
.card.teal{border-left:3px solid var(--teal)}
.card.gold{border-left:3px solid var(--gold)}
.card.red{border-left:3px solid var(--red)}
.kbd-table{width:100%;border-collapse:collapse;margin:.6rem 0;font-size:.92rem}
.kbd-table td{padding:.5rem .7rem;border-bottom:1px solid var(--border);vertical-align:top}
.kbd-table td.k{font-family:'JetBrains Mono',monospace;color:var(--gold);white-space:nowrap;width:38%}
.checks{margin:1rem 0}
.check{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:1rem 1.2rem;margin:.8rem 0}
.check .qq{font-weight:500;margin-bottom:.7rem}
.check .qnum{font-family:'JetBrains Mono',monospace;color:var(--gold-dim);font-size:.75rem;margin-right:.4rem}
.opt{display:block;width:100%;text-align:left;background:var(--surface-2);border:1.5px solid var(--border-2);border-radius:8px;color:var(--text);padding:.7rem .9rem;margin:.4rem 0;font-family:'Sora',sans-serif;font-size:.92rem;cursor:pointer;transition:all .12s}
.opt:hover{border-color:var(--gold-dim)}
.opt .l{font-family:'JetBrains Mono',monospace;font-weight:700;color:var(--teal);margin-right:.5rem}
.opt.correct{background:rgba(126,201,142,.14);border-color:var(--green)}
.opt.correct .l{color:var(--green)}
.opt.wrong{background:rgba(236,90,90,.12);border-color:var(--red)}
.opt.wrong .l{color:var(--red)}
.exp{display:none;margin-top:.7rem;padding-top:.7rem;border-top:1px dashed var(--border-2);color:var(--muted);font-size:.9rem}
.exp.show{display:block}
.exp strong.lbl{display:block;font-family:'JetBrains Mono',monospace;font-size:.64rem;letter-spacing:.18em;color:var(--teal);text-transform:uppercase;margin-bottom:.3rem}
footer{text-align:center;padding:2.5rem 1rem 0;color:var(--dim);font-size:.7rem;font-family:'JetBrains Mono',monospace;letter-spacing:.1em}
.backlink{display:inline-block;margin-bottom:1.5rem;font-family:'JetBrains Mono',monospace;font-size:.78rem;letter-spacing:.05em}
"""

JS = """
document.querySelectorAll('.opt').forEach(function(btn){
  btn.addEventListener('click', function(){
    var check = btn.closest('.check');
    if(check.dataset.answered) return;
    check.dataset.answered = '1';
    var correct = btn.dataset.correct === '1';
    btn.classList.add(correct ? 'correct' : 'wrong');
    if(!correct){
      var right = check.querySelector('.opt[data-correct="1"]');
      if(right) right.classList.add('correct');
    }
    var exp = check.querySelector('.exp');
    if(exp) exp.classList.add('show');
  });
});
"""

LETTERS = ["A", "B", "C", "D"]


def render(out_dir):
    parts = []
    parts.append("""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0d0f17">
<title>Fairlight Certification — Study Guide — Shamase Studios</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..900;1,9..144,300..900&family=Sora:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>%s</style></head><body><main class="wrap">
<a class="backlink" href="index.html">← Fairlight Certification</a>
<div class="eyebrow">Shamase Studios · Fairlight · Study Guide</div>
<h1>The Fairlight Audio Course</h1>
<p class="lede">A complete written curriculum for audio post in DaVinci Resolve — built for talking-head,
commercial, corporate and location work. Work through each module, then test yourself with the
Knowledge Checks before sitting the certification exams.</p>
""" % CSS)

    # TOC
    parts.append('<div class="toc"><h4>Modules</h4><ol>')
    for m in MODULES:
        parts.append(f'<li><a href="#m{m["num"]}">{html.escape(m["title"])}</a></li>')
    parts.append('</ol></div>')

    for m in MODULES:
        parts.append(f'<section class="module" id="m{m["num"]}">')
        parts.append(f'<div class="mnum">Module {m["num"]:02d}</div>')
        parts.append(f'<h2>{html.escape(m["title"])}</h2>')

        parts.append('<h3>Chapter overview</h3>')
        parts.append(f'<p>{m["overview"]}</p>')

        parts.append('<h3>Detailed lesson notes</h3>')
        for heading, items in m["notes"]:
            parts.append(f'<h4>{html.escape(heading)}</h4><ul>')
            for it in items:
                parts.append(f'<li>{it}</li>')
            parts.append('</ul>')

        parts.append('<div class="card gold"><h4>Key takeaways</h4><ul>')
        for t in m["takeaways"]:
            parts.append(f'<li>{t}</li>')
        parts.append('</ul></div>')

        parts.append('<h3>Important shortcuts &amp; controls</h3>')
        parts.append('<table class="kbd-table">')
        for k, act in m["shortcuts"]:
            parts.append(f'<tr><td class="k">{html.escape(k)}</td><td>{html.escape(act)}</td></tr>')
        parts.append('</table>')

        parts.append('<div class="card red"><h4>Common mistakes</h4><ul>')
        for mis in m["mistakes"]:
            parts.append(f'<li>{html.escape(mis)}</li>')
        parts.append('</ul></div>')

        parts.append('<div class="card teal"><h4>Practical exercise</h4>')
        parts.append(f'<p>{html.escape(m["exercise"])}</p></div>')

        parts.append('<div class="card"><h4>Exam preparation notes</h4><ul>')
        for en in m["exam_notes"]:
            parts.append(f'<li>{html.escape(en)}</li>')
        parts.append('</ul></div>')

        # Knowledge checks
        parts.append('<h3>Knowledge check</h3>')
        parts.append('<div class="checks">')
        for i, (qq, opts, correct, exp) in enumerate(m["checks"]):
            parts.append('<div class="check">')
            parts.append(f'<div class="qq"><span class="qnum">{m["num"]}.{i+1}</span>{html.escape(qq)}</div>')
            for j, opt in enumerate(opts):
                cd = '1' if j == correct else '0'
                parts.append(
                    f'<button class="opt" data-correct="{cd}">'
                    f'<span class="l">{LETTERS[j]}</span>{html.escape(opt)}</button>')
            parts.append(f'<div class="exp"><strong class="lbl">Explanation</strong>{html.escape(exp)}</div>')
            parts.append('</div>')
        parts.append('</div>')
        parts.append('</section>')

    parts.append('<footer>Fairlight Certification · Study Guide · Shamase Studios 2026</footer>')
    parts.append(f'</main><script>{JS}</script></body></html>')

    out_path = os.path.join(out_dir, "study-guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    total_checks = sum(len(m["checks"]) for m in MODULES)
    print(f"  wrote study-guide.html ({len(MODULES)} modules, {total_checks} knowledge-check questions)")
