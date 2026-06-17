# -*- coding: utf-8 -*-
"""
Fairlight Certification — EXAM 1: Interface & Software Fundamentals.
100 recall/identification questions. Every item: 4 options, one best answer,
per-option explanations, and a one-line principle.

Authored against the official Blackmagic "DaVinci Resolve Fairlight Training"
series (Mary Plummer) and current Fairlight behaviour (Resolve 17–20, which are
consistent for these fundamentals).
"""

Q = []  # convenience accumulator


def q(module_num, stem, options, correct, explanations, principle, scenario=None):
    Q.append({
        "module_num": module_num,
        "scenario": scenario,
        "stem": stem,
        "options": options,
        "correct": correct,
        "explanations": explanations,
        "principle": principle,
    })


# ───────────────────────── MODULE 1 · Intro & Interface (18) ─────────────────────────
q(1, "Which DaVinci Resolve page is dedicated to professional audio post-production?",
  ["Edit", "Fairlight", "Color", "Fusion"], "B",
  {"A": "The Edit page has audio tracks but is built around picture editing.",
   "B": "Correct: Fairlight is Resolve's full digital audio workstation (DAW) page.",
   "C": "Color is for grading, not audio.",
   "D": "Fusion is for compositing and VFX."},
  "Fairlight is Resolve's built-in DAW for editing, mixing, recording and mastering audio.")

q(1, "On the Fairlight page, what runs along the very bottom of the timeline by default?",
  ["The Mixer", "The transport / playback controls and toolbar", "The Inspector", "The Color wheels"],
  "B",
  {"A": "The Mixer opens on the right-hand side, not the bottom.",
   "B": "Correct: transport controls and the toolbar sit at the bottom of the page.",
   "C": "Fairlight has no Inspector like the Edit page; clip controls live elsewhere.",
   "D": "Color wheels belong to the Color page."},
  "Transport and tools live at the bottom; the Mixer docks on the right.")

q(1, "Which panel, toggled on the right of the Fairlight page, contains every track's fader, pan, EQ, dynamics and bus routing?",
  ["Index", "Mixer", "Metadata", "Effects Library"], "B",
  {"A": "The Index lists tracks/markers but has no faders.",
   "B": "Correct: the Mixer is the channel-strip view with faders, pan, EQ, dynamics and routing.",
   "C": "Metadata shows clip information, not mixing controls.",
   "D": "The Effects Library holds plugins you drag onto clips/tracks."},
  "The Mixer is the channel-strip workspace: one strip per track plus the buses and Main.")

q(1, "In Fairlight, audio levels are measured in which unit on the meters?",
  ["dB SPL", "dBFS (decibels relative to full scale)", "LUFS only", "Hertz"], "B",
  {"A": "dB SPL measures acoustic loudness in air, not a digital meter scale.",
   "B": "Correct: digital peak meters read dBFS, where 0 dBFS is the clipping ceiling.",
   "C": "LUFS is a loudness scale shown separately, not the standard peak meter unit.",
   "D": "Hertz measures frequency, not level."},
  "Digital peak meters are in dBFS; 0 dBFS is the absolute digital ceiling (clipping).")

q(1, "What is the standard professional sample rate for video audio that Fairlight projects use by default?",
  ["44.1 kHz", "48 kHz", "96 kHz", "32 kHz"], "B",
  {"A": "44.1 kHz is the CD standard, not the video standard.",
   "B": "Correct: 48 kHz is the standard sample rate for film and video audio.",
   "C": "96 kHz is high-resolution capture, not the default delivery standard.",
   "D": "32 kHz is below professional video standards."},
  "48 kHz is the universal sample rate for film/video audio post.")

q(1, "Which keys give you JKL-style transport control in Fairlight?",
  ["A, S, D", "J, K, L", "Q, W, E", "Z, X, C"], "B",
  {"A": "A and S are selection/tool shortcuts, not shuttle keys.",
   "B": "Correct: J reverses, K stops, L plays forward; tap L/J repeatedly to shuttle faster.",
   "C": "Q/W/E are not the transport shortcuts.",
   "D": "Z/X/C are not the transport shortcuts."},
  "J-K-L is the universal shuttle: J back, K stop, L forward, repeat to speed up.")

q(1, "Tapping the L key a second and third time during playback does what?",
  ["Mutes the track", "Increases forward playback speed (2x, 4x…)", "Adds a marker", "Solos the clip"],
  "B",
  {"A": "Muting is the M key on a track header, not L.",
   "B": "Correct: each extra tap of L shuttles forward faster.",
   "C": "Markers are added with M.",
   "D": "Solo is the S key on a track header."},
  "Repeated L (or J) taps step playback speed up for fast scrubbing.")

q(1, "What does the 'S' button on a track header do?",
  ["Saves the project", "Solos the track (mutes all others)", "Splits the clip", "Shows the spectrogram"],
  "B",
  {"A": "Saving is Cmd/Ctrl+S, not the track S button.",
   "B": "Correct: S solos that track so you hear it in isolation.",
   "C": "Splitting/cutting uses the razor or Cmd/Ctrl+B.",
   "D": "The spectrogram is a view option, not the S button."},
  "On a track header: S = Solo, M = Mute.")

q(1, "Where do you import media for use on the Fairlight page?",
  ["The Media Pool", "The Deliver page", "The Fusion node graph", "The Color gallery"], "A",
  {"A": "Correct: media is imported into the Media Pool, shared across all pages including Fairlight.",
   "B": "Deliver is for export, not import.",
   "C": "The Fusion node graph is for compositing.",
   "D": "The gallery stores colour grades."},
  "The Media Pool is shared project-wide; Fairlight pulls clips from it.")

q(1, "A track that carries a single audio channel is described as which format?",
  ["Stereo", "Mono", "5.1", "Adaptive"], "B",
  {"A": "Stereo carries two channels (left/right).",
   "B": "Correct: a mono track carries one channel — typical for a single mic/lav.",
   "C": "5.1 carries six channels for surround.",
   "D": "Adaptive carries a variable number of channels in one track."},
  "Track formats describe channel count: mono (1), stereo (2), 5.1 (6), adaptive (variable).")

q(1, "The vertical line that shows your current position in the timeline is the:",
  ["Playhead", "Marker", "Fade handle", "Bus line"], "A",
  {"A": "Correct: the playhead marks the current playback/edit position.",
   "B": "A marker is a coloured flag you place for reference.",
   "C": "Fade handles are the corner triangles on a clip.",
   "D": "There is no 'bus line' on the timeline."},
  "The playhead is your current position; transport and editing happen relative to it.")

q(1, "Which left-side panel lists all your tracks, markers and an overview of the timeline?",
  ["Index", "Mixer", "Sound Library", "ADR"], "A",
  {"A": "Correct: the Index lists tracks and markers and lets you show/hide tracks.",
   "B": "The Mixer is the right-side faders panel.",
   "C": "The Sound Library browses sound effects.",
   "D": "ADR is the dialogue-replacement panel."},
  "The Index (left) is your track/marker overview and visibility manager.")

q(1, "Pressing the spacebar in Fairlight does what?",
  ["Splits the clip at the playhead", "Starts/stops playback", "Adds a fade", "Opens the Mixer"], "B",
  {"A": "Splitting is Cmd/Ctrl+B or the razor.",
   "B": "Correct: spacebar toggles play/stop, the universal transport shortcut.",
   "C": "Fades are dragged with the clip's fade handles.",
   "D": "The Mixer has its own toggle button."},
  "Spacebar = play/stop, the most-used transport control.")

q(1, "What does the term 'clip' refer to on the Fairlight timeline?",
  ["A single segment of audio placed on a track", "An entire track", "A bus", "A keyframe"],
  "A",
  {"A": "Correct: a clip is one piece of audio sitting on a track in the timeline.",
   "B": "A track is the lane that holds clips.",
   "C": "A bus is a routing/summing destination.",
   "D": "A keyframe is an automation point."},
  "Clip = one audio segment on a track; tracks are the lanes that hold clips.")

q(1, "To zoom the timeline horizontally so you can see waveforms in fine detail, you typically:",
  ["Press M", "Use the horizontal zoom control / scroll, or press the zoom shortcut",
   "Open the Deliver page", "Solo the track"], "B",
  {"A": "M adds a marker.",
   "B": "Correct: horizontal zoom (slider, scroll-zoom, or shortcut) reveals waveform detail down to sample level.",
   "C": "Deliver is for export.",
   "D": "Solo isolates audio but doesn't zoom."},
  "Horizontal zoom lets you work from whole-timeline down to sample-accurate detail.")

q(1, "Which statement about the Fairlight and Edit pages sharing a timeline is TRUE?",
  ["They are completely separate projects",
   "They show the same timeline — audio edited in Fairlight updates everywhere",
   "Fairlight can only open exported audio files",
   "You must render before audio appears in Fairlight"], "B",
  {"A": "They are the same timeline within one project, not separate.",
   "B": "Correct: Fairlight and Edit are two views of the same timeline; changes are shared live.",
   "C": "Fairlight works on the live timeline clips, not exports.",
   "D": "No render is needed; the timeline is shared instantly."},
  "Fairlight and Edit are different views of one shared timeline — no round-tripping needed.")

q(1, "Clip gain (the volume overlay across the top of a clip) differs from the track fader because it:",
  ["Affects the whole track", "Adjusts the level of that one clip only",
   "Only works on buses", "Is the same as solo"], "B",
  {"A": "The track fader affects the whole track; clip gain does not.",
   "B": "Correct: clip gain changes the level of that single clip independently of the fader.",
   "C": "Clip gain is per clip, not per bus.",
   "D": "Solo isolates monitoring; it is unrelated to clip gain."},
  "Clip gain = per-clip level; track fader = whole-track level. Set clip gain first, then mix.")

q(1, "The colour-coded meters in the Mixer turn red to warn you of what?",
  ["A muted track", "Clipping (signal exceeding 0 dBFS)", "A flagged marker", "A soloed track"],
  "B",
  {"A": "Mute is shown on the track header, not by a red meter peak.",
   "B": "Correct: red at the top of a meter means the signal has hit/exceeded 0 dBFS and is clipping.",
   "C": "Markers don't drive the meters.",
   "D": "Solo doesn't turn a meter red."},
  "Red on a peak meter = clipping at 0 dBFS; pull the level down to avoid distortion.")

# ───────────────────────── MODULE 2 · Editing Dialogue (14) ─────────────────────────
q(2, "A common first step when organising production dialogue is to:",
  ["Delete all room tone", "Place each character / mic on its own track", "Bounce everything to one mono clip",
   "Add reverb to every clip"], "B",
  {"A": "Room tone is valuable for filling gaps — you keep it, not delete it.",
   "B": "Correct: separating characters onto their own tracks lets you process each voice independently.",
   "C": "Flattening to one clip removes your ability to balance voices.",
   "D": "Reverb is a creative/mix choice, not an organising step."},
  "Split dialogue so each character/mic has its own track — independent levels, EQ and processing.")

q(2, "Which tool cuts a clip into two at the playhead?",
  ["The razor / split (Cmd or Ctrl+B)", "The pan control", "The bus assign", "The solo button"], "A",
  {"A": "Correct: the razor (or Cmd/Ctrl+B) splits a clip at the playhead.",
   "B": "Pan positions the sound in the stereo field.",
   "C": "Bus assign is routing, not cutting.",
   "D": "Solo isolates monitoring."},
  "Split/razor (Cmd/Ctrl+B) cuts at the playhead — the basic edit for trimming dialogue.")

q(2, "Why add short fades to the start and end of dialogue clips?",
  ["To change the pitch", "To prevent clicks/pops at edit points and smooth transitions",
   "To raise the sample rate", "To create surround sound"], "B",
  {"A": "Fades affect level over time, not pitch.",
   "B": "Correct: small fades stop the clicks caused by cutting on a non-zero waveform point.",
   "C": "Fades don't change sample rate.",
   "D": "Fades don't create surround."},
  "Tiny fades on clip edges remove edit-point clicks and make cuts inaudible.")

q(2, "Room tone (ambient silence recorded on location) is mainly used to:",
  ["Replace the dialogue", "Fill gaps between dialogue so silence isn't 'dead'",
   "Boost the loudness target", "Act as a click track"], "B",
  {"A": "Room tone supports dialogue; it doesn't replace it.",
   "B": "Correct: room tone fills holes left by cuts so the background doesn't drop to digital silence.",
   "C": "It isn't a loudness tool.",
   "D": "It isn't a metronome/click."},
  "Room tone glues edits together — fill gaps so the ambience never abruptly cuts out.")

q(2, "The Range Selection tool (shortcut R) is useful for:",
  ["Selecting a time range across one or more tracks regardless of clip boundaries",
   "Soloing the Main bus", "Adding a bus", "Exporting the timeline"], "A",
  {"A": "Correct: Range selection grabs a span of time/tracks independent of where clips start and end.",
   "B": "Soloing is unrelated to range selection.",
   "C": "Adding a bus is done in the Fairlight menu.",
   "D": "Export is on the Deliver page."},
  "Range Selection (R) selects by time across tracks; Edit Selection (A) selects whole clips.")

q(2, "Edit Selection Mode (shortcut A) lets you:",
  ["Select and move whole clips", "Only draw automation", "Record ADR", "Set the loudness target"],
  "A",
  {"A": "Correct: A is the standard arrow/selection mode for grabbing and moving clips.",
   "B": "Automation drawing is a separate mode.",
   "C": "ADR uses the ADR panel.",
   "D": "Loudness targets are set in project/monitor settings."},
  "A = Edit Selection (move whole clips); R = Range Selection (select a time span).")

q(2, "To make two overlapping dialogue takes blend smoothly you create a:",
  ["Crossfade", "Bus", "Marker", "Submix"], "A",
  {"A": "Correct: a crossfade fades one clip out while the next fades in, smoothing the join.",
   "B": "A bus is for routing/summing.",
   "C": "A marker is a reference flag.",
   "D": "A submix groups tracks but doesn't blend two clips."},
  "Crossfades blend overlapping clips so transitions between takes are seamless.")

q(2, "Linking a stereo or grouped set of dialogue clips so they move together is done by:",
  ["Muting them", "Grouping / linking the clips", "Soloing them", "Normalising them"], "B",
  {"A": "Muting silences monitoring; it doesn't lock clips together.",
   "B": "Correct: linking/grouping keeps related clips locked so edits stay in sync.",
   "C": "Soloing affects monitoring only.",
   "D": "Normalising changes level, not linkage."},
  "Link/group related clips so trims and moves keep them in sync.")

q(2, "When trimming dialogue, snapping (the magnet) helps you:",
  ["Automatically lower the volume", "Align edits precisely to playhead, markers and clip edges",
   "Convert mono to stereo", "Add noise reduction"], "B",
  {"A": "Snapping doesn't change level.",
   "B": "Correct: snapping locks your edit point to nearby references for accurate alignment.",
   "C": "Snapping doesn't change channel format.",
   "D": "Snapping is unrelated to repair."},
  "Snapping aligns edits to playhead/markers/edges; toggle it off for free placement.")

q(2, "The waveform shown on a dialogue clip represents:",
  ["The colour of the clip", "The amplitude (level) of the audio over time",
   "The pan position", "The bus assignment"], "B",
  {"A": "Clip colour is a labelling choice.",
   "B": "Correct: the waveform's height shows amplitude/level through the clip.",
   "C": "Pan is set in the mixer, not shown as the waveform.",
   "D": "Bus assignment is routing, not the waveform."},
  "Waveform height = amplitude; reading it lets you spot loud peaks and quiet passages.")

q(2, "To hear only the dialogue while editing out a noisy section, you would:",
  ["Solo the dialogue track(s)", "Delete the Main bus", "Render the project", "Open the Color page"],
  "A",
  {"A": "Correct: soloing the dialogue isolates it so you can focus on the edit.",
   "B": "Deleting the Main bus would break output.",
   "C": "Rendering is for delivery.",
   "D": "The Color page is unrelated."},
  "Solo to isolate the part you're working on without deleting or muting permanently.")

q(2, "Nudging a selected clip frame-by-frame for tight sync is typically done with:",
  ["The comma/period (or arrow) keys", "The pan knob", "The fader", "The EQ"], "A",
  {"A": "Correct: nudge keys move the selection a frame (or sub-frame) at a time for fine sync.",
   "B": "Pan changes position in the field, not timing.",
   "C": "The fader changes level.",
   "D": "EQ changes tone."},
  "Nudge keys give frame-accurate clip moves — essential for lip-sync alignment.")

q(2, "A 'spot' (placing a clip at an exact timecode) is most useful when you need to:",
  ["Randomise placement", "Land a sound or line at a precise frame", "Mute a bus", "Add a fade"], "B",
  {"A": "Spotting is precise, the opposite of random.",
   "B": "Correct: spotting drops a clip at an exact timecode for frame-accurate placement.",
   "C": "Muting is unrelated.",
   "D": "Fades are separate."},
  "Spotting places audio at an exact timecode — precise sync for lines and effects.")

q(2, "Disabling a clip (rather than deleting it) is useful because it:",
  ["Permanently removes the audio", "Silences it while keeping it in place for later",
   "Exports it", "Converts it to a marker"], "B",
  {"A": "Disabling is reversible — nothing is removed.",
   "B": "Correct: a disabled clip stays on the track, silent, ready to re-enable.",
   "C": "Disabling doesn't export.",
   "D": "It doesn't become a marker."},
  "Disable to silence a clip non-destructively while keeping it for later.")

# ───────────────────────── MODULE 3 · Sound Design & FX Editing (14) ─────────────────────────
q(3, "The built-in browser for searching, previewing and dragging in sound effects is the:",
  ["Sound Library", "Index", "ADR panel", "Deliver queue"], "A",
  {"A": "Correct: the Sound Library searches, auditions and places sound effects.",
   "B": "The Index lists tracks/markers.",
   "C": "ADR is for dialogue replacement.",
   "D": "The Deliver queue is for renders."},
  "The Sound Library browses, previews and drags in SFX; you can mount your own folders too.")

q(3, "A 'spotting list' built with markers is used to:",
  ["Note where sound effects and design elements are needed", "Set the loudness target",
   "Store grades", "Choose a codec"], "A",
  {"A": "Correct: markers create a spotting list flagging every place a sound is needed.",
   "B": "Loudness targets are set elsewhere.",
   "C": "Grades belong to Color.",
   "D": "Codecs are a Deliver choice."},
  "Markers form a spotting list — your map of every sound effect and design cue to add.")

q(3, "Which shortcut adds a marker at the playhead?",
  ["M", "B", "S", "F"], "A",
  {"A": "Correct: M drops a marker at the playhead.",
   "B": "B is split/blade.",
   "C": "S is solo.",
   "D": "F is not the marker shortcut here."},
  "M adds a marker; double-click it to add a name/note for your spotting list.")

q(3, "Hard effects (footsteps, door slams, gunshots) are best placed on:",
  ["The dialogue tracks", "Dedicated SFX tracks separate from dialogue",
   "The Main bus directly", "A muted track"], "B",
  {"A": "Mixing them onto dialogue makes balancing impossible.",
   "B": "Correct: keep hard FX on their own tracks so you can level and route them as a group.",
   "C": "You place clips on tracks, not directly on a bus.",
   "D": "A muted track wouldn't be heard."},
  "Separate SFX onto their own tracks (hard FX, design, ambience) for independent control.")

q(3, "Layering several sounds to build one richer effect (e.g. a whoosh) is called:",
  ["Normalising", "Sound design layering", "Bouncing", "Patching"], "B",
  {"A": "Normalising changes level only.",
   "B": "Correct: layering combines multiple elements into a single designed sound.",
   "C": "Bouncing renders tracks down.",
   "D": "Patching is input/output routing."},
  "Layering stacks elements (low end, body, transient, tail) into one designed effect.")

q(3, "Ambience / atmosphere tracks (room tone, traffic, birds) are used to:",
  ["Establish a believable continuous environment under the scene", "Replace dialogue",
   "Set the project frame rate", "Create the loudness meter"], "A",
  {"A": "Correct: ambience beds create a consistent sense of place beneath the scene.",
   "B": "Ambience supports, not replaces, dialogue.",
   "C": "Frame rate is a project setting.",
   "D": "Meters aren't made from ambience."},
  "Ambience beds give a scene a continuous, believable environment.")

q(3, "Routing all your SFX tracks to a single bus lets you:",
  ["Control the whole effects layer with one fader", "Delete the dialogue",
   "Change the sample rate", "Export faster"], "A",
  {"A": "Correct: a shared SFX bus means one fader rides the entire effects layer.",
   "B": "It doesn't delete dialogue.",
   "C": "Bussing doesn't change sample rate.",
   "D": "It isn't an export speed feature."},
  "Send a group of tracks to a sub/bus so one fader controls the whole layer.")

q(3, "To audition a sound effect before committing it, you:",
  ["Render the timeline", "Preview/audition it in the Sound Library", "Delete the track", "Open Deliver"],
  "B",
  {"A": "Rendering is for final export.",
   "B": "Correct: the Sound Library lets you preview before dragging the clip in.",
   "C": "Deleting a track is unrelated.",
   "D": "Deliver is for export."},
  "Audition in the Sound Library first, then drag in the keeper.")

q(3, "Colour-coding tracks (dialogue, Foley, ambience, SFX) primarily helps with:",
  ["Loudness", "Fast visual organisation of a busy session", "Sample rate", "Pitch"], "B",
  {"A": "Colour doesn't change loudness.",
   "B": "Correct: colours make a dense, multi-layer session easy to read at a glance.",
   "C": "Colour doesn't affect sample rate.",
   "D": "Colour doesn't change pitch."},
  "Track colours keep complex sessions readable — group by sound type.")

q(3, "Foley refers to:",
  ["Automatic dialogue replacement", "Custom-performed everyday sounds (footsteps, cloth, props) recorded to picture",
   "A loudness standard", "A type of bus"], "B",
  {"A": "That describes ADR, not Foley.",
   "B": "Correct: Foley is performed sound — footsteps, movement, props — synced to picture.",
   "C": "It isn't a loudness standard.",
   "D": "It isn't a bus type."},
  "Foley = performed everyday sounds recorded in sync with picture to add realism.")

q(3, "Adjusting the level of a single sound effect without affecting others on the track is done with:",
  ["Clip gain on that clip", "The Main fader", "The monitor level", "The loudness target"], "A",
  {"A": "Correct: clip gain rides one clip's level independently.",
   "B": "The Main fader moves the whole mix.",
   "C": "Monitor level only changes what you hear, not the mix.",
   "D": "Loudness target is a delivery setting."},
  "Use clip gain for per-effect level; the fader for the whole track.")

q(3, "A 'sweetener' in sound design is:",
  ["A subtle added layer that enhances an existing sound", "A loudness preset",
   "A type of marker", "A delivery codec"], "A",
  {"A": "Correct: a sweetener is a small extra layer that reinforces or polishes a sound.",
   "B": "It isn't a loudness preset.",
   "C": "It isn't a marker.",
   "D": "It isn't a codec."},
  "Sweeteners are subtle reinforcing layers that make a sound feel bigger or cleaner.")

q(3, "Mounting your own folder of sound effects into the Sound Library lets you:",
  ["Search and drag from your personal SFX collection inside Fairlight",
   "Change the project resolution", "Disable dialogue", "Add a Main bus"], "A",
  {"A": "Correct: you can point the Sound Library at your own libraries to browse them in-app.",
   "B": "It doesn't affect resolution.",
   "C": "It doesn't touch dialogue.",
   "D": "It isn't bus creation."},
  "Add your own folders to the Sound Library so your whole SFX collection is searchable in Fairlight.")

q(3, "Naming markers in your spotting list is valuable because it:",
  ["Increases the bit depth", "Documents exactly what sound each cue needs",
   "Solos the track", "Renders the project"], "B",
  {"A": "Marker names don't change bit depth.",
   "B": "Correct: named markers tell you (and collaborators) precisely what each cue requires.",
   "C": "Naming doesn't solo.",
   "D": "Naming doesn't render."},
  "Named markers turn a spotting pass into a clear, actionable to-do list.")

# ───────────────────────── MODULE 4 · Recording VO & ADR (12) ─────────────────────────
q(4, "Before recording a voiceover onto a track, you must first:",
  ["Render the timeline", "Record-enable (arm) the track and set its input",
   "Delete the Main bus", "Open the Color page"], "B",
  {"A": "Rendering is for export, not recording.",
   "B": "Correct: arm the track and assign an input source before you can record to it.",
   "C": "Deleting the bus would break monitoring/output.",
   "D": "Color is unrelated."},
  "To record: arm (record-enable) the track and patch an input to it.")

q(4, "Patch Input/Output in Fairlight is used to:",
  ["Route hardware/audio inputs to tracks and tracks to outputs", "Change the grade",
   "Set the loudness", "Add markers"], "A",
  {"A": "Correct: the Patch Input/Output panel connects physical/source inputs to tracks and routes outputs.",
   "B": "Grading is on Color.",
   "C": "Loudness is set elsewhere.",
   "D": "Markers use M."},
  "Patch Input/Output is the routing matrix: get your mic input to the armed track.")

q(4, "ADR stands for:",
  ["Audio Data Recording", "Automated Dialogue Replacement", "Ambient Dynamic Range",
   "Adaptive Direct Routing"], "B",
  {"A": "Not a real term here.",
   "B": "Correct: ADR is Automated Dialogue Replacement — re-recording lines in sync with picture.",
   "C": "Not a real term here.",
   "D": "Not a real term here."},
  "ADR = Automated Dialogue Replacement: re-recording dialogue to picture to replace bad production audio.")

q(4, "The Fairlight ADR panel provides:",
  ["A cue list, record takes, and beeps/visual cues to guide the performer",
   "A colour grading toolset", "A delivery codec list", "A node graph"], "A",
  {"A": "Correct: the ADR panel manages cues, take recording and performer guide cues (beeps/streamers).",
   "B": "Grading is on Color.",
   "C": "Codecs are on Deliver.",
   "D": "Node graphs are Fusion/Color."},
  "The ADR panel runs the whole loop: cue list, guide beeps, take recording and selection.")

q(4, "Why monitor with headphones (not speakers) when recording a voiceover live to picture?",
  ["To raise the sample rate", "To prevent the speaker output bleeding back into the mic",
   "To change the codec", "To add reverb automatically"], "B",
  {"A": "Headphones don't change sample rate.",
   "B": "Correct: headphones stop playback from leaking into the live microphone (feedback/bleed).",
   "C": "Headphones don't change codecs.",
   "D": "They don't add reverb."},
  "Use headphones while recording so monitor audio doesn't bleed into the mic.")

q(4, "Recording multiple takes of the same ADR line lets you:",
  ["Reduce the bit depth", "Choose the best performance afterwards", "Skip editing", "Export faster"],
  "B",
  {"A": "Takes don't change bit depth.",
   "B": "Correct: several takes give you options to pick the strongest performance.",
   "C": "You still edit/comp the takes.",
   "D": "Takes don't speed export."},
  "Record several takes, then comp/choose the best — standard ADR and VO practice.")

q(4, "Setting input levels before recording aims to:",
  ["Peak as close to 0 dBFS as possible", "Capture a healthy level with headroom (peaks well below 0 dBFS)",
   "Record in red the whole time", "Mute the input"], "B",
  {"A": "Peaking at 0 dBFS risks clipping on louder moments.",
   "B": "Correct: aim for a strong but safe level leaving headroom so peaks never clip.",
   "C": "Recording in the red is clipping — bad.",
   "D": "Muting the input records nothing."},
  "Set levels for a healthy signal with headroom; clipped digital recordings can't be fixed.")

q(4, "A 'guide track' during ADR is:",
  ["The original production dialogue played to the performer for timing reference",
   "The Main bus", "The loudness meter", "A colour preset"], "A",
  {"A": "Correct: the guide track is the original line the actor listens to so the new take matches timing.",
   "B": "It isn't the Main bus.",
   "C": "It isn't a meter.",
   "D": "It isn't a colour preset."},
  "The guide track lets the performer match the original line's rhythm and sync.")

q(4, "Three visual beeps/streamer cues before an ADR take exist to:",
  ["Trigger the render", "Count the performer in so they start exactly on cue",
   "Set the codec", "Add a fade"], "B",
  {"A": "They don't trigger renders.",
   "B": "Correct: the count-in cues the actor to begin precisely in sync.",
   "C": "They don't set codecs.",
   "D": "They don't add fades."},
  "ADR count-in cues (beeps/streamers) give the performer a precise start point.")

q(4, "After recording, the new voiceover clip appears:",
  ["On the Deliver page only", "On the armed track in the timeline, ready to edit",
   "In the Color gallery", "As a marker"], "B",
  {"A": "It isn't confined to Deliver.",
   "B": "Correct: the recording lands on the armed track as a normal clip you can edit.",
   "C": "It doesn't go to the gallery.",
   "D": "It isn't a marker."},
  "Recorded audio becomes a normal timeline clip on the armed track.")

q(4, "Loop recording in ADR repeatedly plays a section so you can:",
  ["Render in a loop", "Record take after take of the same line without stopping",
   "Change the bus format", "Solo the Main"], "B",
  {"A": "It isn't about rendering.",
   "B": "Correct: loop recording cycles the cue so the performer can lay down repeated takes quickly.",
   "C": "It doesn't change bus format.",
   "D": "It doesn't solo the Main."},
  "Loop recording cycles a cue to capture multiple takes efficiently.")

q(4, "Record-enabling a track is indicated by which control on the track header?",
  ["The pan knob", "A record (R/arm) button that lights up", "The fade handle", "The marker flag"],
  "B",
  {"A": "Pan positions sound; it doesn't arm recording.",
   "B": "Correct: the arm/record-enable button lights to show the track will capture incoming audio.",
   "C": "Fade handles are on clips.",
   "D": "Markers are timeline flags."},
  "The lit arm/record button shows which track will capture the incoming signal.")

# ───────────────────────── MODULE 5 · Mixing (16) ─────────────────────────
q(5, "Panning a mono dialogue track to the centre means the sound:",
  ["Comes only from the left", "Sits equally in left and right (the centre image)",
   "Is muted", "Is doubled in volume"], "B",
  {"A": "Hard-left would be panned fully left.",
   "B": "Correct: centre pan places the sound equally in both speakers — standard for lead dialogue.",
   "C": "Centre pan isn't mute.",
   "D": "Panning doesn't double volume."},
  "Lead dialogue usually sits centre; pan effects/music wider to create space.")

q(5, "The fader on a channel strip controls the track's:",
  ["Pan position", "Overall output level", "EQ curve", "Bus format"], "B",
  {"A": "Pan is a separate control.",
   "B": "Correct: the fader sets the track's overall level into its bus.",
   "C": "EQ is its own section.",
   "D": "Bus format is a routing property."},
  "The fader = track level; it's your primary balancing control in the mix.")

q(5, "EQ (equalisation) is used to:",
  ["Shift timing", "Boost or cut specific frequency ranges to shape tone",
   "Change the pan", "Set the sample rate"], "B",
  {"A": "EQ doesn't move clips in time.",
   "B": "Correct: EQ raises or lowers chosen frequency bands to shape the sound's tone.",
   "C": "Pan is separate.",
   "D": "EQ doesn't set sample rate."},
  "EQ shapes tone by boosting/cutting frequency bands — e.g. trimming low rumble from dialogue.")

q(5, "A high-pass filter on a dialogue track is commonly used to:",
  ["Remove low-frequency rumble and handling noise", "Add bass", "Increase loudness to target",
   "Create reverb"], "A",
  {"A": "Correct: a high-pass lets highs through and cuts lows, removing rumble/handling noise.",
   "B": "It cuts bass, not adds it.",
   "C": "It isn't a loudness tool.",
   "D": "It doesn't create reverb."},
  "High-pass (low-cut) clears sub-bass rumble that clutters dialogue.")

q(5, "A compressor's main job is to:",
  ["Reduce the dynamic range by taming loud peaks", "Add echo",
   "Change pitch", "Create markers"], "A",
  {"A": "Correct: a compressor reduces the gap between loud and quiet, evening out level.",
   "B": "Echo is a delay/reverb effect.",
   "C": "Pitch is a different processor.",
   "D": "It doesn't make markers."},
  "Compression evens out dynamics — controls peaks so dialogue sits at a consistent level.")

q(5, "On a compressor, the 'threshold' sets:",
  ["The level above which compression starts acting", "The output sample rate",
   "The pan position", "The fade length"], "A",
  {"A": "Correct: signal above the threshold gets compressed; below it passes untouched.",
   "B": "Threshold isn't sample rate.",
   "C": "It isn't pan.",
   "D": "It isn't a fade."},
  "Threshold = the level where the compressor kicks in; ratio sets how hard it squeezes.")

q(5, "A limiter differs from a compressor by:",
  ["Boosting bass only", "Acting as a hard ceiling that stops peaks exceeding a set level",
   "Changing the frame rate", "Only working on buses"], "B",
  {"A": "A limiter isn't a bass tool.",
   "B": "Correct: a limiter is essentially a high-ratio compressor that prevents any peak passing the ceiling.",
   "C": "It doesn't change frame rate.",
   "D": "Limiters work on tracks and buses."},
  "A limiter is a brick-wall ceiling — nothing exceeds the set output level (protects against clipping).")

q(5, "A noise gate is used to:",
  ["Silence a track below a threshold (cutting hiss/bleed between phrases)",
   "Add reverb", "Raise loudness", "Pan the track"], "A",
  {"A": "Correct: a gate mutes signal that falls below the threshold, cleaning up gaps between words.",
   "B": "Gates don't add reverb.",
   "C": "Gates don't set loudness.",
   "D": "Gates don't pan."},
  "A gate closes on quiet passages, removing low-level noise between dialogue.")

q(5, "A bus in Fairlight is best described as:",
  ["A single clip", "A destination that sums/combines multiple tracks for shared processing or output",
   "A marker", "A keyboard shortcut"], "B",
  {"A": "A clip is a single segment of audio.",
   "B": "Correct: a bus sums signals from multiple tracks so you can process or route them together.",
   "C": "A marker is a reference flag.",
   "D": "A bus isn't a shortcut."},
  "Buses sum and route groups of tracks — sub-mixes, the Main, and aux sends.")

q(5, "The default master output bus that everything feeds into is the:",
  ["Aux 1", "Main 1", "Solo bus", "Sound Library"], "B",
  {"A": "Aux buses are for sends like reverb.",
   "B": "Correct: Main 1 is the default master bus carrying your final mix.",
   "C": "There's no 'solo bus' as the master.",
   "D": "The Sound Library is unrelated."},
  "Main 1 is the master bus — your final stereo (or surround) mix output.")

q(5, "An Aux bus (send) is commonly used to:",
  ["Feed several tracks into one shared reverb or effect", "Replace the dialogue",
   "Set the project frame rate", "Disable a track"], "A",
  {"A": "Correct: aux sends route tracks to a shared effect like reverb, returning to the mix.",
   "B": "It doesn't replace dialogue.",
   "C": "It isn't a frame-rate control.",
   "D": "It isn't a disable function."},
  "Aux sends share one effect (e.g. reverb) across many tracks for a cohesive space.")

q(5, "Automation in the mix lets you:",
  ["Record fader, pan and plugin moves so they replay automatically over time",
   "Change the codec", "Add markers only", "Re-link media"], "A",
  {"A": "Correct: automation captures parameter moves (level, pan, etc.) that replay on playback.",
   "B": "It isn't a codec setting.",
   "C": "It's not limited to markers.",
   "D": "It isn't media relinking."},
  "Automation records and replays mix moves over time — rides on dialogue, fades on music.")

q(5, "Which automation mode writes moves only while you actively touch a control, then returns to the existing value?",
  ["Touch", "Write (always)", "Off", "Trim only"], "A",
  {"A": "Correct: Touch writes while you hold the control and reverts when you let go.",
   "B": "Write writes constantly while running, overwriting existing automation.",
   "C": "Off disables automation writing.",
   "D": "'Trim only' isn't the matching mode here."},
  "Touch writes while held then releases; Latch keeps the last value; Write overwrites continuously.")

q(5, "Gain staging means:",
  ["Setting healthy levels at each stage so nothing clips or gets too quiet",
   "Choosing a codec", "Adding markers", "Colour-coding tracks"], "A",
  {"A": "Correct: gain staging keeps levels sensible from clip → track → bus → Main.",
   "B": "Codecs are a delivery choice.",
   "C": "Markers are references.",
   "D": "Colour-coding is organisation."},
  "Good gain staging keeps a clean signal path with headroom from input to Main.")

q(5, "Track EQ versus Clip EQ: Track EQ applies to:",
  ["Only one clip", "Everything on that whole track", "Only the Main bus", "Only markers"], "B",
  {"A": "That describes Clip EQ.",
   "B": "Correct: Track EQ processes the entire track's output.",
   "C": "Track EQ isn't limited to the Main.",
   "D": "EQ doesn't apply to markers."},
  "Clip EQ fixes one clip; Track EQ shapes the whole track; bus EQ shapes a group.")

q(5, "The Control Room / monitor level in the Mixer affects:",
  ["The recorded mix level", "Only how loud you hear playback, not the actual mix",
   "The codec", "The marker colour"], "B",
  {"A": "It does not change the mix that gets exported.",
   "B": "Correct: monitor level changes your listening volume only — it's not part of the mix.",
   "C": "It isn't a codec control.",
   "D": "It isn't marker colour."},
  "Monitor/Control-Room level changes what you hear, never the actual mixed output.")

# ───────────────────────── MODULE 6 · Repairing & Restoring (14) ─────────────────────────
q(6, "The collection of audio plugins bundled with Fairlight is called:",
  ["Fairlight FX", "ResolveFX", "OpenFX only", "Color FX"], "A",
  {"A": "Correct: Fairlight FX is the bundled set of audio plugins (repair, dynamics, reverb, etc.).",
   "B": "ResolveFX are video effects.",
   "C": "OpenFX is a plugin standard, not the Fairlight bundle name.",
   "D": "There's no 'Color FX' audio bundle."},
  "Fairlight FX = the bundled audio plugins: repair, dynamics, modulation, reverb and more.")

q(6, "Which Fairlight FX plugin removes a steady electrical hum (e.g. 50/60 Hz mains buzz)?",
  ["De-Hummer", "Chorus", "Reverb", "Pitch"], "A",
  {"A": "Correct: the De-Hummer targets mains hum and its harmonics.",
   "B": "Chorus is a modulation effect.",
   "C": "Reverb adds space.",
   "D": "Pitch shifts pitch."},
  "De-Hummer kills 50/60 Hz mains hum and harmonics — common with location power/lighting.")

q(6, "Harsh 'sss' sounds on a sibilant voice are best tamed with the:",
  ["De-Esser", "De-Hummer", "Gate", "Flanger"], "A",
  {"A": "Correct: a De-Esser specifically attenuates sibilant 'ess' frequencies.",
   "B": "De-Hummer targets hum, not sibilance.",
   "C": "A gate mutes quiet passages, not sibilance.",
   "D": "Flanger is a modulation effect."},
  "De-Esser tames sibilance ('s', 'sh', 't') without dulling the whole voice.")

q(6, "The Noise Reduction plugin works most effectively when you:",
  ["Guess settings blindly", "Capture a noise profile from a section of pure background noise",
   "Mute the track", "Raise the loudness target"], "B",
  {"A": "Blind guessing gives poor, artefact-heavy results.",
   "B": "Correct: learning a profile from isolated noise lets it subtract that signature accurately.",
   "C": "Muting removes the audio entirely.",
   "D": "Loudness targets are unrelated to learning noise."},
  "Teach Noise Reduction the noise (a clean noise-only sample), then it subtracts that profile.")

q(6, "Over-applying noise reduction typically produces:",
  ["Perfectly clean audio every time", "Watery/robotic artefacts and a hollow-sounding voice",
   "Higher sample rate", "More markers"], "B",
  {"A": "Too much almost always damages the audio.",
   "B": "Correct: pushing it too far creates underwater/metallic artefacts and thins the voice.",
   "C": "It doesn't change sample rate.",
   "D": "It doesn't add markers."},
  "Use the least noise reduction that works — too much leaves watery, artefact-ridden dialogue.")

q(6, "A short clicking/crackle from a faulty connection is best fixed with:",
  ["De-Crackle / De-Click type repair", "Reverb", "Chorus", "Pan"], "A",
  {"A": "Correct: de-crackle/de-click repair removes short transient clicks and crackle.",
   "B": "Reverb adds space, not repair.",
   "C": "Chorus is modulation.",
   "D": "Pan is positioning."},
  "De-Click/De-Crackle removes short transient pops and crackle from dialogue.")

q(6, "Applying a Fairlight FX plugin to a single clip versus a whole track means:",
  ["There is no difference", "A clip insert processes only that clip; a track insert processes the whole track",
   "Clip effects export but track effects don't", "Track effects only work on the Main"], "B",
  {"A": "There's a real, important difference.",
   "B": "Correct: place an effect on a clip to fix one clip, or on the track to process everything on it.",
   "C": "Both export normally.",
   "D": "Track effects aren't limited to the Main."},
  "Insert a plugin on a clip to repair one clip, or on the track to process all of it.")

q(6, "Sample-level (zoom right in) editing is useful for repair because it lets you:",
  ["Change the codec", "Pinpoint and remove a single click or pop precisely",
   "Add a bus", "Set loudness"], "B",
  {"A": "It's unrelated to codecs.",
   "B": "Correct: zooming to sample level lets you surgically find and fix a single glitch.",
   "C": "It isn't bus creation.",
   "D": "It isn't loudness setting."},
  "Zoom to sample level to hunt down and surgically remove individual clicks/pops.")

q(6, "The Voice Isolation / dialogue-cleanup feature (in recent Resolve versions) uses AI to:",
  ["Add reverb", "Separate spoken dialogue from background noise", "Change the grade", "Render faster"],
  "B",
  {"A": "It isn't a reverb.",
   "B": "Correct: AI Voice Isolation pulls clean dialogue out from noisy backgrounds.",
   "C": "It doesn't grade.",
   "D": "It isn't a render-speed tool."},
  "Voice Isolation (AI) extracts dialogue from noisy location audio — powerful for untreated rooms.")

q(6, "Why repair before you mix (rather than after)?",
  ["Mixing first is always faster", "A clean source lets EQ, compression and levels work predictably",
   "Repair only works on the Main bus", "It changes the frame rate"], "B",
  {"A": "Order matters more than raw speed here.",
   "B": "Correct: fixing noise/clicks first means downstream processing isn't amplifying problems.",
   "C": "Repair isn't Main-only.",
   "D": "It doesn't change frame rate."},
  "Repair first: clean dialogue makes every later EQ/compression/level decision predictable.")

q(6, "Room tone is also a repair tool because it can:",
  ["Patch a gap left after deleting a noise or word", "Increase bit depth",
   "Replace the Main bus", "Set the codec"], "A",
  {"A": "Correct: dropping matching room tone into a gap hides the edit where audio was removed.",
   "B": "It doesn't change bit depth.",
   "C": "It isn't a bus.",
   "D": "It isn't a codec."},
  "Fill repaired gaps with matching room tone so the patch is inaudible.")

q(6, "A 'noise floor' refers to:",
  ["The loudest peak", "The constant low-level background noise present in a recording",
   "The bus output", "A marker colour"], "B",
  {"A": "That's the peak, not the floor.",
   "B": "Correct: the noise floor is the steady background level beneath the wanted signal.",
   "C": "It isn't a bus.",
   "D": "It isn't a marker."},
  "The noise floor is the constant background level; good repair lowers it without harming the voice.")

q(6, "The Dialogue Processor / Dialogue plugin in Fairlight FX bundles tools to:",
  ["Grade colour", "Clean, level and shape dialogue (e.g. de-noise, EQ, leveling) in one place",
   "Render the timeline", "Create markers"], "B",
  {"A": "It isn't a colour tool.",
   "B": "Correct: it combines common dialogue-cleanup stages into a single plugin.",
   "C": "It doesn't render.",
   "D": "It doesn't make markers."},
  "The Dialogue Processor combines several dialogue-cleanup stages into one convenient plugin.")

q(6, "If a recording is already clipped/distorted at the source, the realistic outcome is:",
  ["It can always be fully restored", "Distortion is hard or impossible to remove — prevention at recording is key",
   "Noise Reduction fixes it instantly", "Increasing loudness fixes it"], "B",
  {"A": "Clipping destroys information that can't be perfectly recovered.",
   "B": "Correct: clipped audio loses data permanently; capture clean levels in the first place.",
   "C": "Noise Reduction targets noise, not clipping.",
   "D": "More loudness makes clipping worse."},
  "Clipping is destructive and largely unfixable — get levels right at the source.")

# ───────────────────────── MODULE 7 · Delivery & Mastering (12) ─────────────────────────
q(7, "Loudness for delivery is measured in:",
  ["dBFS peaks only", "LUFS (Loudness Units Full Scale)", "Hertz", "Pixels"], "B",
  {"A": "Peak dBFS doesn't reflect perceived loudness over time.",
   "B": "Correct: LUFS measures integrated perceived loudness, the standard for delivery targets.",
   "C": "Hertz is frequency.",
   "D": "Pixels are image, not audio."},
  "LUFS measures perceived loudness over time — the unit every delivery spec uses.")

q(7, "The EBU R128 broadcast loudness target is approximately:",
  ["-9 LUFS", "-14 LUFS", "-23 LUFS", "0 LUFS"], "C",
  {"A": "-9 LUFS is far too hot for broadcast.",
   "B": "-14 LUFS is a streaming/online target, not EBU R128 broadcast.",
   "C": "Correct: EBU R128 broadcast is -23 LUFS integrated (US ATSC A/85 is -24 LKFS).",
   "D": "0 LUFS is not a delivery target."},
  "Broadcast: EBU R128 = -23 LUFS; ATSC A/85 (US) = -24 LKFS.")

q(7, "Most online/streaming platforms (YouTube, social) normalise toward roughly:",
  ["-23 LUFS", "-14 LUFS", "-3 LUFS", "+6 LUFS"], "B",
  {"A": "-23 LUFS is broadcast, quieter than streaming.",
   "B": "Correct: streaming/social typically sit around -14 LUFS (some platforms -13 to -16).",
   "C": "-3 LUFS would be extremely loud and distorted.",
   "D": "Positive LUFS isn't a valid loudness target."},
  "Online/social target ≈ -14 LUFS; mixing far hotter just gets turned down by the platform.")

q(7, "True Peak for delivery is usually capped at:",
  ["0 dBTP", "-1 dBTP (or lower)", "+3 dBTP", "-23 dBTP"], "B",
  {"A": "0 dBTP risks inter-sample peaks clipping after encoding.",
   "B": "Correct: -1 dBTP is the common ceiling to avoid clipping after lossy encoding.",
   "C": "Positive true peak clips.",
   "D": "-23 is a loudness figure, not a true-peak ceiling."},
  "Cap True Peak around -1 dBTP so codec encoding doesn't push peaks into clipping.")

q(7, "Audio Normalization on a clip/timeline in Fairlight can target either:",
  ["Only pan", "Peak level or a loudness (LUFS) standard such as EBU R128",
   "Only frame rate", "Only colour"], "B",
  {"A": "Normalization isn't a pan tool.",
   "B": "Correct: you can normalise to a peak level or to a loudness standard/target.",
   "C": "It doesn't set frame rate.",
   "D": "It isn't colour."},
  "Audio Normalization offers peak or loudness (e.g. R128) modes to hit a target automatically.")

q(7, "The loudness meter in Fairlight shows Integrated, Short-term and Momentary loudness. 'Integrated' means:",
  ["The single loudest sample", "The average loudness over the whole programme",
   "The pan position", "The codec"], "B",
  {"A": "That's a peak, not integrated loudness.",
   "B": "Correct: integrated loudness is the overall average across the entire programme — what specs target.",
   "C": "It isn't pan.",
   "D": "It isn't a codec."},
  "Integrated LUFS = whole-programme average; that's the number delivery specs reference.")

q(7, "Where do you set the final audio codec, sample rate and bit depth for export?",
  ["The Color page", "The Deliver page's render settings (Audio tab)",
   "The Sound Library", "The Index"], "B",
  {"A": "Color is for grading.",
   "B": "Correct: the Deliver page render settings include an Audio tab for codec, sample rate and bit depth.",
   "C": "The Sound Library browses SFX.",
   "D": "The Index lists tracks/markers."},
  "Final audio export settings live in the Deliver page's render Audio tab.")

q(7, "Before final delivery, soloing/checking the Main bus meter helps confirm:",
  ["The grade is correct", "The mix isn't clipping and sits at the right loudness",
   "The frame rate", "The marker names"], "B",
  {"A": "The Main bus meter is about audio, not grade.",
   "B": "Correct: watching the Main meter verifies no clipping and the correct loudness before export.",
   "C": "Frame rate is a project setting.",
   "D": "Marker names are unrelated."},
  "Check the Main bus meter pre-export: no clipping, correct loudness target met.")

q(7, "For a single talking-head clip exported to several platforms, the most efficient loudness approach is to:",
  ["Re-mix from scratch for each platform", "Master to a sensible target (≈ -14 LUFS) with -1 dBTP and let platforms normalise",
   "Always master to 0 dBFS", "Skip loudness entirely"], "B",
  {"A": "Re-mixing each time is wasteful.",
   "B": "Correct: a clean master near -14 LUFS / -1 dBTP travels well across social platforms.",
   "C": "0 dBFS invites clipping.",
   "D": "Ignoring loudness produces inconsistent results."},
  "One well-mastered file (≈ -14 LUFS, -1 dBTP) serves most social platforms cleanly.")

q(7, "A 'stem' or sub-mix export (separate dialogue/music/effects buses) is valuable because it:",
  ["Reduces the sample rate", "Lets a client or broadcaster re-balance or re-version later",
   "Changes the grade", "Adds markers"], "B",
  {"A": "Stems don't lower sample rate.",
   "B": "Correct: separated D/M/E stems allow re-balancing, dubbing or re-versioning without a full re-mix.",
   "C": "Stems don't grade.",
   "D": "Stems aren't markers."},
  "Delivering D/M/E stems lets clients re-version, localise or re-balance without remixing.")

q(7, "When delivering for international dubbing, the most important stem to keep separate is:",
  ["The dialogue", "The colour grade", "The markers", "The thumbnail"], "A",
  {"A": "Correct: isolating dialogue lets it be replaced with a translated track (M&E stays intact).",
   "B": "Grade is a video matter.",
   "C": "Markers aren't stems.",
   "D": "Thumbnails are unrelated."},
  "Keep dialogue separate so an M&E (music & effects) mix can host translated dialogue.")

q(7, "The standard deliverable sample rate / bit depth for most professional video masters is:",
  ["48 kHz / 24-bit (or higher)", "8 kHz / 8-bit", "22 kHz / 16-bit mono only", "96 kHz / 4-bit"],
  "A",
  {"A": "Correct: 48 kHz, 24-bit is the professional video-audio master standard.",
   "B": "8 kHz/8-bit is telephone-grade, not professional.",
   "C": "22 kHz/16-bit mono is sub-standard for delivery.",
   "D": "4-bit is not a real professional depth."},
  "Professional video masters: 48 kHz, 24-bit audio.")

QUESTIONS = Q
assert len(QUESTIONS) == 100, f"Exam 1 has {len(QUESTIONS)} questions, expected 100"
