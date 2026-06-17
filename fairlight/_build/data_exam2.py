# -*- coding: utf-8 -*-
"""
Fairlight Certification — EXAM 2: Workflow & Decision Making.
100 scenario-based questions. Each has a real-world setup and tests reasoning
about the best workflow — weighted toward this studio's work: talking-head
interviews, commercials, corporate, untreated location sound, social delivery.
"""

Q = []


def q(module_num, scenario, stem, options, correct, explanations, principle):
    Q.append({
        "module_num": module_num,
        "scenario": scenario,
        "stem": stem,
        "options": options,
        "correct": correct,
        "explanations": explanations,
        "principle": principle,
    })


# ───────────────────────── MODULE 1 · Workflow foundations (12) ─────────────────────────
q(1, "You've finished the picture edit of a corporate interview on the Edit page and now need to clean and balance the audio.",
  "What is the correct way to move into audio work?",
  ["Export the audio, open a new project, and re-import it",
   "Switch to the Fairlight page — it's the same timeline, ready to work",
   "Re-edit everything on the Cut page first",
   "Render the video before touching audio"], "B",
  {"A": "Unnecessary — Fairlight already has the live timeline; round-tripping wastes time and risks sync errors.",
   "B": "Correct: Fairlight and Edit share one timeline, so you just switch pages and start.",
   "C": "Re-editing on the Cut page doesn't help the audio work.",
   "D": "No render is needed to access audio in Fairlight."},
  "Fairlight is a view of the same timeline — switch pages, no export/import.")

q(1, "A client interview was recorded with a lav mic and a boom mic simultaneously on two channels.",
  "How should you set up the Fairlight session?",
  ["Bounce both mics into one mono clip immediately",
   "Put each mic on its own track so you can choose/blend and process them separately",
   "Delete one mic at random", "Pan one mic hard left and forget about it"], "B",
  {"A": "Flattening removes your ability to pick the better mic per moment.",
   "B": "Correct: separate tracks let you choose the best mic, blend, and process each independently.",
   "C": "Deleting blindly throws away your safety/quality option.",
   "D": "Hard-panning a mic isn't a cleanup strategy and breaks the centre image."},
  "Keep each mic on its own track — choose and process the best source per moment.")

q(1, "You open a noisy location interview and the meters are bouncing into the red on the loudest words.",
  "What does the red indicate and what's the first move?",
  ["It's fine; red means good level", "Clipping — bring the clip gain/level down so peaks stay below 0 dBFS",
   "It means the track is muted; un-mute it", "It's the loudness target being met"], "B",
  {"A": "Red is a warning, not a good sign.",
   "B": "Correct: red = clipping at 0 dBFS; reduce level so peaks have headroom.",
   "C": "Red isn't a mute indicator.",
   "D": "Red peaks aren't the loudness target."},
  "Red meters = clipping; pull level down to restore headroom before doing anything else.")

q(1, "Three interviews shot on different days arrive at noticeably different volumes.",
  "What's the most efficient first step toward a consistent edit?",
  ["Mix purely by ear with no reference", "Rough-balance each clip's gain so they sit at a similar level before fine mixing",
   "Normalise to 0 dBFS peak", "Add reverb to match them"], "B",
  {"A": "Working with no reference makes consistency slow and error-prone.",
   "B": "Correct: rough clip-gain balancing first gives a level playing field for the detailed mix.",
   "C": "Peak-normalising to 0 dBFS invites clipping and ignores perceived loudness.",
   "D": "Reverb changes space, not level consistency."},
  "Rough-balance clip levels first, then refine — get clips in the same ballpark early.")

q(1, "You'll be doing many similar talking-head edits and want a repeatable starting point.",
  "Which approach best supports consistency across projects?",
  ["Rebuild routing and processing from scratch every time",
   "Save a template/preset with your track layout, buses and common processing",
   "Never use buses", "Mix each one at a random loudness"], "B",
  {"A": "Rebuilding each time is slow and inconsistent.",
   "B": "Correct: a saved template/preset standardises layout, routing and processing across jobs.",
   "C": "Buses are exactly what makes group control repeatable.",
   "D": "Random loudness defeats consistency."},
  "Standardise with templates/presets so every talking-head job starts from the same clean base.")

q(1, "Your timeline has dialogue, music and sound effects all jumbled across unlabelled tracks.",
  "What organisational step pays off most before mixing?",
  ["Leave it — organisation doesn't matter", "Group sound types onto labelled, colour-coded tracks (dialogue / music / SFX)",
   "Convert everything to mono", "Delete the music"], "B",
  {"A": "Disorganisation slows every later decision.",
   "B": "Correct: grouping and colour-coding by type makes the mix fast and legible.",
   "C": "Forcing mono can harm stereo elements like music.",
   "D": "Deleting music may remove needed content."},
  "Organise by sound type with labels and colours before mixing — speed and clarity.")

q(1, "A junior asks why you don't just 'fix it all with one master EQ on the timeline.'",
  "What's the best reasoning to give?",
  ["One master EQ is always best", "Different sources need different treatment; process per clip/track, then use the bus for shared polish",
   "EQ should never be used", "Only the Color page can fix audio"], "B",
  {"A": "A single master EQ can't address per-source problems.",
   "B": "Correct: fix problems at the clip/track level, reserve the bus for cohesive, shared polish.",
   "C": "EQ is essential, not forbidden.",
   "D": "Color doesn't process audio."},
  "Treat problems where they live (clip/track); use buses for shared, global polish.")

q(1, "You want to hear just the boom mic on one line without permanently changing the session.",
  "Best approach?",
  ["Delete every other track", "Solo the boom track temporarily", "Export the timeline",
   "Mute the Main bus"], "B",
  {"A": "Deleting tracks is destructive and unnecessary.",
   "B": "Correct: solo isolates monitoring without altering the session.",
   "C": "Exporting doesn't help you audition.",
   "D": "Muting the Main silences everything."},
  "Solo for non-destructive isolation while auditioning.")

q(1, "An interview clip looks fine but you can barely see its waveform at the current zoom.",
  "What helps you edit breaths and clicks accurately?",
  ["Open the Deliver page", "Zoom in horizontally (and vertically) to see waveform detail",
   "Add a bus", "Change the codec"], "B",
  {"A": "Deliver is for export.",
   "B": "Correct: zooming reveals the detail needed to edit breaths, clicks and tight cuts.",
   "C": "Buses are routing, not viewing.",
   "D": "Codecs are export settings."},
  "Zoom in to edit accurately — you can't trim what you can't see.")

q(1, "You need to drop a sound effect at exactly 00:01:23:10 to hit an on-screen action.",
  "What's the precise method?",
  ["Drag it roughly and hope", "Position the playhead/spot the clip to the exact timecode",
   "Normalise the clip", "Solo the Main"], "B",
  {"A": "Eyeballing won't reliably hit a single frame.",
   "B": "Correct: spotting to an exact timecode lands the effect on the right frame.",
   "C": "Normalising changes level, not timing.",
   "D": "Soloing doesn't place clips."},
  "Spot to timecode for frame-accurate placement against picture.")

q(1, "Your client review happens on laptop speakers, but you mixed on good headphones.",
  "What's the wise final check?",
  ["Skip checking other systems", "Also audition the mix on small/laptop speakers and phone to confirm it translates",
   "Only trust the headphones", "Master to 0 dBFS to be safe"], "B",
  {"A": "Skipping translation checks risks a mix that fails on the client's device.",
   "B": "Correct: check on consumer playback (laptop/phone) so dialogue stays clear everywhere.",
   "C": "One system can mislead you.",
   "D": "0 dBFS mastering invites clipping."},
  "Check the mix on the devices your audience actually uses — translation matters.")

q(1, "You realise mid-project the timeline sample rate doesn't match your recordings.",
  "Why does this matter for audio?",
  ["It doesn't matter at all", "Mismatched sample rates can cause pitch/sync issues; keep the project at the standard 48 kHz",
   "It changes the grade", "It only affects markers"], "B",
  {"A": "Sample-rate handling absolutely matters.",
   "B": "Correct: mismatches risk pitch/speed/sync problems; standardise on 48 kHz for video.",
   "C": "Sample rate isn't a grade setting.",
   "D": "It affects audio, not just markers."},
  "Keep projects at 48 kHz; sample-rate mismatches cause pitch and sync trouble.")

# ───────────────────────── MODULE 2 · Dialogue editing decisions (16) ─────────────────────────
q(2, "Between two interview sentences there's an ugly chair creak you removed, leaving silence that 'thuds' against the room sound.",
  "Best fix?",
  ["Leave the digital silence", "Fill the gap with matching room tone so the background stays continuous",
   "Add reverb over the gap", "Boost the gap's gain"], "B",
  {"A": "Sudden digital silence is jarring against the recorded ambience.",
   "B": "Correct: matching room tone bridges the gap so the cut is inaudible.",
   "C": "Reverb won't replace missing ambience naturally.",
   "D": "Boosting silence just raises noise."},
  "Patch removed sections with matching room tone so ambience never drops out.")

q(2, "Cutting tightly between two takes produces a faint click at the join.",
  "What removes it cleanly?",
  ["Add a short crossfade or fades at the edit", "Increase the loudness target",
   "Pan the clip", "Change the codec"], "A",
  {"A": "Correct: small fades/crossfade at the edit smooth the waveform discontinuity that clicks.",
   "B": "Loudness targets don't fix edit clicks.",
   "C": "Pan doesn't address the click.",
   "D": "Codec is unrelated to the edit."},
  "Edit-point clicks come from cutting on a non-zero sample — fades/crossfades fix them.")

q(2, "An interviewee's answer is great but they start with a long 'ummm.'",
  "Cleanest way to remove it while keeping natural flow?",
  ["Delete the whole answer", "Trim out the 'umm', then close the gap and smooth with room tone/fades",
   "Mute the entire track", "Add reverb to hide it"], "B",
  {"A": "Deleting the whole answer loses the content.",
   "B": "Correct: surgically trim the filler, close the gap, and smooth so it sounds natural.",
   "C": "Muting the track removes everything.",
   "D": "Reverb won't remove the word."},
  "Trim fillers surgically, then close and smooth the gap for natural pacing.")

q(2, "You have a single lav recording where the subject turns their head, causing level to drop on some words.",
  "Most appropriate first tool?",
  ["Clip gain (or volume keyframes) to lift the quiet words", "A noise gate",
   "Reverb", "Pitch shift"], "A",
  {"A": "Correct: ride clip gain / draw volume keyframes to even out the level changes.",
   "B": "A gate would cut quiet words entirely, making it worse.",
   "C": "Reverb doesn't fix level dips.",
   "D": "Pitch shift is irrelevant."},
  "Use clip gain / volume automation to even out level swings before compression.")

q(2, "Two people talk over each other on separate mics, and you only want one voice in a section.",
  "Best approach?",
  ["Delete both tracks", "Cut/trim or disable the unwanted voice's clip in that section",
   "Solo the Main bus", "Add a marker and move on"], "B",
  {"A": "Deleting both removes the wanted voice too.",
   "B": "Correct: trim or disable the unwanted clip in that span so only the chosen voice remains.",
   "C": "Soloing the Main doesn't remove the overlap.",
   "D": "A marker alone doesn't fix the overlap."},
  "Separate mics let you cut/disable the unwanted voice without harming the other.")

q(2, "After tightening an interview, the pacing feels rushed because you removed every breath.",
  "What's the professional view on breaths?",
  ["Always remove all breaths", "Keep natural breaths (or reduce, not eliminate) so speech sounds human",
   "Replace breaths with silence", "Add reverb to breaths"], "B",
  {"A": "Stripping all breaths makes speech robotic.",
   "B": "Correct: keep or gently lower breaths so dialogue stays natural and well-paced.",
   "C": "Hard silence where breaths were sounds unnatural.",
   "D": "Reverb on breaths is not the fix."},
  "Don't strip every breath — natural breathing keeps dialogue human; tame only the distracting ones.")

q(2, "A clip's edit needs to land precisely on a video cut for sync.",
  "What two features best support frame accuracy?",
  ["Snapping plus nudge keys", "Reverb plus chorus", "Solo plus mute", "Pan plus EQ"], "A",
  {"A": "Correct: snapping locks to references and nudge keys fine-tune frame by frame.",
   "B": "Those are creative effects, not sync tools.",
   "C": "Solo/mute affect monitoring, not placement.",
   "D": "Pan/EQ shape sound, not timing."},
  "Snapping + nudge keys give fast, frame-accurate dialogue sync.")

q(2, "You want the same EQ fix applied to every clip from one noisy lav across the timeline.",
  "Most efficient placement?",
  ["Put the EQ on the track that holds those clips", "Add EQ to each clip one by one forever",
   "Put EQ on the Color page", "Skip EQ"], "A",
  {"A": "Correct: track EQ processes all clips on that track at once — efficient and consistent.",
   "B": "Per-clip EQ is fine for one-offs but tedious for a whole track.",
   "C": "Color can't EQ audio.",
   "D": "Skipping leaves the problem."},
  "Apply a shared fix at track level; reserve clip-level processing for one-off problems.")

q(2, "A particular take has a unique pop that no other clip has.",
  "Where should the repair go?",
  ["On the whole track", "On just that clip (clip-level), so other clips are untouched",
   "On the Main bus", "On an Aux send"], "B",
  {"A": "Track-level would needlessly process clean clips.",
   "B": "Correct: a one-off problem gets a clip-level fix.",
   "C": "The Main bus affects the entire mix.",
   "D": "An aux send is for shared effects like reverb."},
  "Match the scope of the fix to the scope of the problem — one clip, clip-level.")

q(2, "You're comparing two takes of the same line to choose the better-sounding one.",
  "Quickest reliable method?",
  ["Render both and listen in another app", "Stack them on linked tracks and solo each to A/B compare",
   "Delete one immediately", "Judge by the waveform colour"], "B",
  {"A": "Round-tripping to another app is slow.",
   "B": "Correct: solo each in turn to A/B them directly in the session.",
   "C": "Deleting before comparing is risky.",
   "D": "Waveform colour tells you nothing about quality."},
  "A/B takes by soloing each in place — fast, reversible comparison.")

q(2, "A sentence is perfect except one mumbled word that's also fine in a different take.",
  "Best dialogue-editing move?",
  ["Re-shoot the interview", "Edit in the clearer word from the other take, matching level and tone",
   "Add reverb to hide the mumble", "Mute the whole sentence"], "B",
  {"A": "A re-shoot is wildly disproportionate.",
   "B": "Correct: splice the better word in and match level/EQ so the join is seamless.",
   "C": "Reverb won't clarify a mumble.",
   "D": "Muting removes the sentence."},
  "Comp the best words across takes, matching level and tone for an invisible edit.")

q(2, "Your dialogue track has consistent, even level now and you're ready for tone shaping.",
  "Correct order of operations?",
  ["EQ and compress first, then fix level", "Edit/level/clean first, then EQ and compression",
   "Master to LUFS before editing", "Add music before cleaning dialogue"], "B",
  {"A": "Processing before leveling makes the processors chase a moving target.",
   "B": "Correct: get clean, edited, evenly-leveled dialogue first, then shape with EQ/compression.",
   "C": "Mastering loudness comes at the end, not before editing.",
   "D": "Music comes after dialogue is solid."},
  "Order: edit → clean → level → EQ/compress → mix → master.")

q(2, "Linked picture-and-audio clips keep shifting out of sync when you trim audio.",
  "What likely prevents accidental drift?",
  ["Turning off all snapping forever", "Keeping linked clips grouped/linked so they move together, and using snapping",
   "Deleting the video track", "Randomly nudging until it lines up"], "B",
  {"A": "Disabling snapping entirely makes accurate alignment harder.",
   "B": "Correct: link/group clips and use snapping so audio and picture stay locked.",
   "C": "Deleting video isn't a sync fix.",
   "D": "Random nudging is not a method."},
  "Group/link related clips and use snapping to protect sync while editing.")

q(2, "An interview answer is usable but contains a phone notification 'ding' over a word.",
  "Most realistic clean fix?",
  ["Cut to the same word from another take or repair the spot, then patch with room tone",
   "Leave the ding in", "Add music to cover it", "Lower the whole interview's volume"], "A",
  {"A": "Correct: replace the affected word from another take or repair it, then blend with room tone.",
   "B": "Leaving an obvious ding looks unprofessional.",
   "C": "Music-as-coverup is a crude last resort, not a clean fix.",
   "D": "Lowering the whole interview doesn't remove the ding."},
  "Replace or repair the spot, then patch ambience — don't just bury problems under music.")

q(2, "You're handed a 40-minute interview to cut to 3 minutes for social.",
  "Which Fairlight habit keeps the audio edit clean at speed?",
  ["Cut anywhere and ignore joins", "Cut on natural pauses, add small fades, and keep room tone continuous",
   "Remove all room tone", "Compress first, edit later"], "B",
  {"A": "Careless joins create clicks and jarring jumps.",
   "B": "Correct: cut at pauses, fade edits, maintain ambience — fast and clean.",
   "C": "Removing room tone makes cuts obvious.",
   "D": "Editing after compression fights the processor."},
  "Cut on pauses, fade joins, keep ambience continuous — clean fast edits.")

q(2, "A clip plays back fine but you accidentally left it disabled and exported silence in that spot.",
  "What's the lesson for your workflow?",
  ["Disabled clips export their audio anyway", "Disabled clips are silent on export — check enable states before delivery",
   "Disabling is the same as soloing", "Disabling changes the codec"], "B",
  {"A": "Disabled clips don't play, so they export silent.",
   "B": "Correct: verify clips are enabled (not just present) before final export.",
   "C": "Disable and solo are unrelated.",
   "D": "Disable doesn't touch codecs."},
  "Disabled clips export as silence — sweep enable states before delivery.")

# ───────────────────────── MODULE 3 · Sound design decisions (14) ─────────────────────────
q(3, "You're scoring a 30-second product advert and need to map where every sound hit should land.",
  "Best first step?",
  ["Start dropping effects randomly", "Do a spotting pass with named markers at each needed sound",
   "Master the loudness first", "Export a draft immediately"], "B",
  {"A": "Random placement wastes time and misses beats.",
   "B": "Correct: a marker-based spotting list maps every cue before you build.",
   "C": "Loudness comes at the end.",
   "D": "Exporting before designing is premature."},
  "Spot first with named markers — plan the sound before placing it.")

q(3, "Your advert needs an impactful 'whoosh-to-impact' transition that no single library file nails.",
  "Best design approach?",
  ["Use one file and turn it up loud", "Layer multiple elements (whoosh, low boom, transient) into one designed hit",
   "Add reverb to dialogue instead", "Skip the transition"], "B",
  {"A": "One thin file rarely has the needed weight.",
   "B": "Correct: layering elements builds a fuller, custom-designed transition.",
   "C": "Reverb on dialogue is unrelated.",
   "D": "Skipping abandons the creative goal."},
  "Design big moments by layering complementary elements into one cohesive sound.")

q(3, "A corporate video cuts between an office and a street, but both feel 'dead' and disconnected.",
  "What grounds each location?",
  ["Nothing — silence is fine", "Add appropriate ambience beds (office room tone, street atmos) under each scene",
   "More dialogue compression", "A louder music track only"], "B",
  {"A": "Dead silence feels unnatural and unfinished.",
   "B": "Correct: ambience beds give each location a believable, continuous sense of place.",
   "C": "Compression won't create environment.",
   "D": "Music alone doesn't replace location atmosphere."},
  "Ambience beds establish place and make cuts between locations feel grounded.")

q(3, "You've added 20 sound effects across 8 tracks and riding each one is slow.",
  "How do you regain quick control of the whole effects layer?",
  ["Route all SFX tracks to one SFX sub-bus and ride that fader", "Delete half the effects",
   "Put effects on the dialogue track", "Master to -23 LUFS now"], "A",
  {"A": "Correct: a shared SFX sub-bus lets one fader control the entire effects layer.",
   "B": "Deleting effects sacrifices the design.",
   "C": "Mixing SFX onto dialogue removes independent control.",
   "D": "Mastering loudness isn't the issue here."},
  "Bus a group to one fader for instant control over a whole layer.")

q(3, "An advert's music is fighting the voiceover for attention.",
  "Cleanest way to keep the VO clear without manually dipping music everywhere?",
  ["Delete the music", "Use level automation (or side-chain ducking) so music dips under the VO",
   "Pan the VO hard left", "Raise the whole mix to 0 dBFS"], "B",
  {"A": "Deleting music abandons the creative bed.",
   "B": "Correct: automate music level (or duck it) under the VO so speech stays intelligible.",
   "C": "Hard-panning VO breaks the centre image.",
   "D": "Pushing to 0 dBFS clips."},
  "Duck/automate music under voiceover — keep speech intelligible without losing the bed.")

q(3, "You want consistent footsteps for a walking shot but the production audio has none usable.",
  "What discipline provides custom, sync-accurate steps?",
  ["ADR", "Foley — performed footsteps recorded to picture", "Noise reduction", "Loudness normalisation"],
  "B",
  {"A": "ADR replaces dialogue, not footsteps.",
   "B": "Correct: Foley is performed everyday sound (footsteps) recorded in sync to picture.",
   "C": "Noise reduction removes noise; it doesn't create steps.",
   "D": "Normalisation is a loudness tool."},
  "Foley creates custom, sync-accurate performed sounds like footsteps and cloth.")

q(3, "Your busy session is hard to read: dialogue, music, Foley and SFX all look the same.",
  "Fastest way to make it navigable?",
  ["Colour-code tracks by sound type and label them", "Mute everything",
   "Convert all tracks to mono", "Render and re-import"], "A",
  {"A": "Correct: colour-coding and labelling by type makes a dense session instantly legible.",
   "B": "Muting hides problems, doesn't organise them.",
   "C": "Forcing mono can damage stereo elements.",
   "D": "Re-importing doesn't organise tracks."},
  "Colour and label by sound type so a complex session is readable at a glance.")

q(3, "You found the perfect impact sound but it's slightly too quiet compared to neighbouring effects.",
  "Best level fix for that single effect?",
  ["Raise the Main fader", "Raise that clip's clip gain", "Add reverb", "Re-record the dialogue"], "B",
  {"A": "The Main fader moves the entire mix.",
   "B": "Correct: clip gain adjusts that one effect's level without touching anything else.",
   "C": "Reverb changes space, not level.",
   "D": "Dialogue re-recording is irrelevant."},
  "Per-effect level = clip gain; whole-layer level = the sub-bus fader.")

q(3, "A client wants the same brand 'sonic logo' sting placed identically at the end of 12 adverts.",
  "Most reliable way to keep it consistent?",
  ["Re-design it each time", "Save the sting as an asset/preset and spot it to the same point in each timeline",
   "Eyeball the placement", "Use a different sound each time"], "B",
  {"A": "Re-designing risks inconsistency.",
   "B": "Correct: reuse the saved asset and spot it to a precise point for identical results.",
   "C": "Eyeballing breaks consistency.",
   "D": "Varying the sound defeats branding."},
  "Reuse saved branded assets and spot them precisely for consistent identity.")

q(3, "An ambience bed loops audibly because it's too short for the scene.",
  "Cleanest way to extend it without an obvious seam?",
  ["Let the loop click repeatedly", "Crossfade overlapping copies (or use a longer take) so the loop point is hidden",
   "Mute it", "Add a marker"], "B",
  {"A": "An audible loop click is distracting.",
   "B": "Correct: crossfade overlapping copies to disguise the loop seam.",
   "C": "Muting removes the bed entirely.",
   "D": "A marker doesn't extend audio."},
  "Crossfade overlapping copies to hide loop seams in ambience beds.")

q(3, "You're auditioning effects for a UI 'tap' sound in a tech advert.",
  "Most efficient workflow inside Fairlight?",
  ["Import dozens of files to the timeline to hear them", "Preview candidates in the Sound Library, then drag in the keeper",
   "Render each to test", "Guess by filename"], "B",
  {"A": "Importing everything clutters the timeline.",
   "B": "Correct: audition in the Sound Library, then place only the winner.",
   "C": "Rendering to test is slow.",
   "D": "Filenames don't tell you how it sounds."},
  "Audition in the Sound Library; commit only the chosen sound to the timeline.")

q(3, "A scene's tension needs to build subtly under the dialogue without being noticed as 'music.'",
  "What design element suits this?",
  ["A loud melodic theme", "A low, evolving drone/atmos layer that rises gradually",
   "A bright UI beep", "Footsteps"], "B",
  {"A": "An overt theme draws attention to itself.",
   "B": "Correct: a subtle rising drone builds tension beneath dialogue unobtrusively.",
   "C": "A UI beep doesn't build tension.",
   "D": "Footsteps don't create mood."},
  "Drones/atmos layers build mood subtly under dialogue — felt more than heard.")

q(3, "You add a sweetener layer to an impact but now it's harsh on small speakers.",
  "Reasonable mix decision?",
  ["Leave it harsh", "EQ the sweetener to tame harsh highs, or lower its level so it supports rather than dominates",
   "Delete the entire impact", "Master louder to hide it"], "B",
  {"A": "Harshness will annoy viewers on phones/laptops.",
   "B": "Correct: shape the sweetener with EQ/level so it reinforces without harshness.",
   "C": "Deleting the impact overcorrects.",
   "D": "Louder mastering worsens harshness."},
  "Sweeteners should support, not dominate — EQ/level them to sit under the main sound.")

q(3, "Reviewing your advert, the SFX feel disconnected from the picture timing.",
  "What likely improves the 'hit' feeling?",
  ["Random placement", "Spot effects precisely to the on-screen action frames (and add transient layers for impact)",
   "Lower the sample rate", "Remove all ambience"], "B",
  {"A": "Random placement is the cause, not the cure.",
   "B": "Correct: tight sync to action frames (plus transient layering) makes hits land.",
   "C": "Sample rate doesn't affect sync feel.",
   "D": "Removing ambience won't fix SFX timing."},
  "Sync effects tightly to action and add transients so hits feel connected to picture.")

# ───────────────────────── MODULE 4 · Recording/ADR decisions (12) ─────────────────────────
q(4, "A client wants to add a voiceover narration to a finished corporate video, recorded at your desk.",
  "Correct Fairlight setup to record it?",
  ["Render the video first", "Add a track, patch the mic input to it, arm/record-enable it, set a safe level, then record",
   "Record on the Color page", "Use the Main bus as the input"], "B",
  {"A": "No render needed to record narration.",
   "B": "Correct: create a track, patch input, arm it, set a healthy level with headroom, then record.",
   "C": "Color can't record audio.",
   "D": "The Main bus is an output, not an input source."},
  "Record VO: new track → patch input → arm → set safe level → record.")

q(4, "Production dialogue on one line is unusable due to a passing siren, but the performance is needed.",
  "What's the standard professional remedy?",
  ["Leave the siren in", "Re-record the line with ADR, matching sync to the original guide track",
   "Boost the siren", "Delete the scene"], "B",
  {"A": "An unusable line stays unusable.",
   "B": "Correct: ADR re-records the line in sync to replace the ruined production audio.",
   "C": "Boosting the siren is the opposite of helpful.",
   "D": "Deleting the scene is disproportionate."},
  "When production audio is unsalvageable, ADR re-records the line to picture.")

q(4, "During a live VO record you monitor on studio speakers and the recording has a hollow doubled sound.",
  "Likely cause and fix?",
  ["The codec; change it", "Speaker bleed into the mic; monitor on headphones instead",
   "Too few markers; add some", "The grade; fix on Color"], "B",
  {"A": "Codec isn't causing acoustic bleed.",
   "B": "Correct: speakers leak into the mic; use headphones to prevent bleed/feedback.",
   "C": "Markers are unrelated.",
   "D": "Grade is unrelated to audio bleed."},
  "Monitor on headphones when recording live to picture to avoid speaker bleed.")

q(4, "You record three VO takes of a key line.",
  "Best practice after recording?",
  ["Keep only the first take always", "Audition all takes and comp/select the best (or best parts)",
   "Delete all but the loudest", "Export immediately without listening"], "B",
  {"A": "First isn't automatically best.",
   "B": "Correct: review all takes and choose/comp the strongest performance.",
   "C": "Loudest isn't best.",
   "D": "Exporting unheard risks shipping a weak take."},
  "Capture options, then audition and comp the best take(s).")

q(4, "An ADR performer keeps starting slightly late.",
  "Which ADR feature most directly helps their timing?",
  ["The loudness meter", "The count-in beeps/streamers and the guide track",
   "The Color wheels", "The Deliver queue"], "B",
  {"A": "The loudness meter doesn't cue performance.",
   "B": "Correct: count-in cues and the guide track let the performer start exactly on time.",
   "C": "Color wheels are unrelated.",
   "D": "The Deliver queue is for export."},
  "ADR count-in cues + guide track lock the performer to the original timing.")

q(4, "Setting record level, your loudest test words peak right at 0 dBFS.",
  "What should you do before the real take?",
  ["Record as-is", "Lower the input gain to leave headroom so peaks sit safely below 0 dBFS",
   "Raise the input to clip", "Mute the input"], "B",
  {"A": "Peaking at 0 dBFS risks clipping on louder delivery.",
   "B": "Correct: back off the input so there's headroom for unexpected loud moments.",
   "C": "Clipping ruins the recording.",
   "D": "Muting records nothing."},
  "Leave recording headroom — peaks should land well under 0 dBFS.")

q(4, "You need the new ADR line to sit believably in the scene's space.",
  "Which step helps it match the original?",
  ["Master to -14 LUFS only", "Match level/EQ and add matching room tone/reverb so it blends with the scene",
   "Pan it hard right", "Leave it bone dry in a reverberant scene"], "B",
  {"A": "Loudness mastering doesn't make ADR sit in the room.",
   "B": "Correct: match tone, level and space (room tone/reverb) so ADR blends with production sound.",
   "C": "Hard-panning dialogue breaks the image.",
   "D": "Dry ADR in a live room sounds pasted-on."},
  "Blend ADR by matching level, EQ and the scene's acoustic space.")

q(4, "Recording a long narration, you want to retry flubbed sentences without stopping the session.",
  "Which approach fits?",
  ["Loop/punch recording over the flubbed section", "Re-open the project each time",
   "Render after every sentence", "Use the Cut page"], "A",
  {"A": "Correct: loop/punch recording lets you re-take a section in place efficiently.",
   "B": "Re-opening the project each time is absurdly slow.",
   "C": "Rendering per sentence wastes time.",
   "D": "The Cut page isn't for VO capture."},
  "Punch/loop record to retake sections without rebuilding the session.")

q(4, "Your narration track records, but you hear nothing on playback though the meter moved while recording.",
  "Most likely cause?",
  ["The audio wasn't captured at all", "The track is still in input/record-monitor mode or the clip is muted/disabled — check monitoring and enable state",
   "The sample rate is too high", "The Color page is open"], "B",
  {"A": "The meter moving means signal was captured.",
   "B": "Correct: check track monitoring mode and that the clip is enabled/un-muted.",
   "C": "Sample rate wouldn't silence playback like this.",
   "D": "The Color page being open is irrelevant."},
  "If it recorded but won't play, check monitoring mode and clip enable/mute state.")

q(4, "A client provides a script and wants pickup lines recorded to match an existing VO's tone.",
  "What reference helps you match performance and level?",
  ["Ignore the original VO", "Play the original VO as reference and match mic distance, level and tone",
   "Master to 0 dBFS", "Record in a different room with no reference"], "B",
  {"A": "Ignoring the reference guarantees a mismatch.",
   "B": "Correct: reference the original and match mic technique, level and tone for continuity.",
   "C": "0 dBFS mastering doesn't address matching.",
   "D": "No reference makes matching guesswork."},
  "Match pickups to the original by referencing its tone, level and mic technique.")

q(4, "You're about to record but several other tracks are also record-enabled by accident.",
  "Why fix this first?",
  ["It speeds up export", "You could overwrite/record onto unintended tracks — arm only the target track",
   "It changes loudness", "It affects the grade"], "B",
  {"A": "Arming isn't an export-speed matter.",
   "B": "Correct: only the intended track should be armed to avoid recording onto the wrong tracks.",
   "C": "Arming doesn't set loudness.",
   "D": "It's unrelated to grade."},
  "Arm only the target track — stray record-enables risk recording onto the wrong track.")

q(4, "After ADR, the replaced line is clean but noticeably 'too clean' versus the noisy scene around it.",
  "Best blend decision?",
  ["Leave it pristine", "Add a touch of the scene's room tone/ambience under the ADR so it matches the surrounding texture",
   "Add heavy reverb everywhere", "Lower the whole mix"], "B",
  {"A": "A pristine line stands out against a textured scene.",
   "B": "Correct: lay matching room tone/ambience under the ADR to match the scene's noise floor.",
   "C": "Heavy reverb everywhere overcorrects.",
   "D": "Lowering the whole mix doesn't fix the mismatch."},
  "Match ADR's cleanliness to the scene by adding the scene's own ambience underneath.")

# ───────────────────────── MODULE 5 · Mixing decisions (16) ─────────────────────────
q(5, "In a talking-head edit, the dialogue is centred but the background music is also dead-centre and crowding it.",
  "Best mix decision for clarity?",
  ["Pan the dialogue hard left", "Keep dialogue centred and widen/pan the music outward to make space",
   "Mute the dialogue", "Raise both to 0 dBFS"], "B",
  {"A": "Hard-panning lead dialogue breaks the natural centre image.",
   "B": "Correct: keep dialogue centred and spread music wider so the voice has its own space.",
   "C": "Muting dialogue defeats the purpose.",
   "D": "Pushing both to 0 dBFS clips and doesn't create space."},
  "Keep dialogue centred; widen music/effects to carve space around the voice.")

q(5, "Dialogue level swings between a loud and a soft speaker even after clip-gain balancing.",
  "Which processor most directly evens the remaining dynamics?",
  ["A compressor on the dialogue", "A reverb", "A chorus", "A high-pass only"], "A",
  {"A": "Correct: compression reduces the loud/soft gap for a consistent dialogue level.",
   "B": "Reverb adds space, not consistency.",
   "C": "Chorus is a modulation effect.",
   "D": "A high-pass shapes lows, not dynamics."},
  "Compression evens dialogue dynamics after you've done coarse clip-gain balancing.")

q(5, "Lavalier dialogue has a low rumbling sound from clothing and air conditioning.",
  "First EQ move?",
  ["Boost the lows", "High-pass (low-cut) to remove sub-bass rumble below the voice",
   "Boost 10 kHz heavily", "Add reverb"], "B",
  {"A": "Boosting lows worsens rumble.",
   "B": "Correct: a high-pass clears rumble below the voice's useful range.",
   "C": "A big high boost adds harshness, not rumble removal.",
   "D": "Reverb doesn't remove rumble."},
  "High-pass dialogue to clear rumble below the voice — a near-universal first EQ.")

q(5, "You want a vocal-forward, polished sound but compressing each of 8 dialogue tracks separately is inconsistent.",
  "More efficient routing?",
  ["Compress the Main bus only and hope", "Route dialogue to a dialogue sub-bus and apply shared compression/EQ there",
   "Delete tracks until it's even", "Add aux reverb to fix level"], "B",
  {"A": "Main-bus-only processing also affects music/SFX.",
   "B": "Correct: a dialogue sub-bus lets you process all dialogue cohesively in one place.",
   "C": "Deleting tracks loses content.",
   "D": "Reverb doesn't fix level."},
  "Group dialogue to a sub-bus for cohesive, shared processing without touching music/SFX.")

q(5, "Your mix sounds great loud but the dialogue disappears at low volume on a phone.",
  "What's the likely issue and fix?",
  ["Dialogue is too loud; lower it", "Dialogue sits too low relative to music/SFX; raise dialogue or duck the bed so speech leads",
   "The codec is wrong", "Add more reverb to dialogue"], "B",
  {"A": "Lowering dialogue makes it worse.",
   "B": "Correct: dialogue must lead the mix; raise it or duck music/SFX so speech stays clear at low volume.",
   "C": "Codec doesn't cause this balance issue.",
   "D": "Reverb reduces intelligibility."},
  "Dialogue must lead — if it vanishes quietly, raise it or duck the bed.")

q(5, "You want music to automatically drop whenever the presenter speaks, then return.",
  "Which Fairlight technique achieves this cleanly?",
  ["Manual clip deletion", "Level automation on the music (or side-chain ducking from the dialogue)",
   "Solo the music", "Pan automation only"], "B",
  {"A": "Manual deletion is crude and not dynamic.",
   "B": "Correct: automate the music level (or side-chain duck it from dialogue) for clean dips.",
   "C": "Soloing won't duck under speech.",
   "D": "Pan won't reduce level under speech."},
  "Duck music under speech with level automation or side-chain ducking.")

q(5, "You're riding the dialogue fader live to even out a tricky section and want only those moves recorded.",
  "Which automation mode is most appropriate?",
  ["Touch", "Off", "Read-only", "No automation"], "A",
  {"A": "Correct: Touch writes only while you hold the fader, then returns to existing automation.",
   "B": "Off won't record your moves.",
   "C": "Read-only plays back but doesn't record.",
   "D": "Disabling automation records nothing."},
  "Touch mode records moves only while you hold the control — ideal for targeted rides.")

q(5, "A reverb is needed on several dialogue clips to place them in a hall, but inserting it on each is wasteful.",
  "Best routing?",
  ["Insert reverb on every clip", "Send the relevant tracks to an Aux bus with one reverb, returning to the mix",
   "Put reverb on the Main bus", "Use clip gain"], "B",
  {"A": "Per-clip reverb wastes resources and is inconsistent.",
   "B": "Correct: an aux send shares one reverb across tracks for a consistent space.",
   "C": "Main-bus reverb would wash the entire mix, including dry elements.",
   "D": "Clip gain is level, not reverb."},
  "Share one reverb via an aux send for a consistent, efficient space.")

q(5, "Your final Main bus occasionally ticks into the red on loud SFX hits.",
  "Safest protective step before delivery?",
  ["Ignore it", "Place a limiter on the Main bus set to a safe ceiling (e.g. -1 dBTP) and/or lower levels",
   "Boost everything", "Add reverb"], "B",
  {"A": "Ignoring clipping risks distorted delivery.",
   "B": "Correct: a Main-bus limiter at a safe ceiling catches stray peaks; also re-check levels.",
   "C": "Boosting worsens clipping.",
   "D": "Reverb doesn't prevent clipping."},
  "A Main-bus limiter at a safe ceiling protects against stray clipping peaks.")

q(5, "Two dialogue tracks sound thin alone but boxy together.",
  "What mixing concept explains the boxiness and a fix?",
  ["Frequency build-up; gently cut shared low-mid frequencies on one or both", "Pan; centre them harder",
   "Sample rate; raise it", "Markers; add more"], "A",
  {"A": "Correct: overlapping low-mid energy stacks up (build-up); EQ-cutting the shared range clears it.",
   "B": "Panning won't fix spectral build-up of centred dialogue.",
   "C": "Sample rate is unrelated.",
   "D": "Markers don't affect tone."},
  "Stacked sources build up low-mids; carve overlapping frequencies to clear 'boxy' mixes.")

q(5, "You need consistent loudness across a 6-video corporate series.",
  "Best mixing target discipline?",
  ["Mix each by ear with no target", "Mix every video to the same loudness target (e.g. ≈ -14 LUFS) and check on the loudness meter",
   "Master each at a random level", "Always hit 0 dBFS"], "B",
  {"A": "By-ear with no target yields inconsistent loudness.",
   "B": "Correct: a shared LUFS target plus meter checks makes the series consistent.",
   "C": "Random levels break consistency.",
   "D": "0 dBFS is a clipping ceiling, not a loudness target."},
  "Mix a series to one LUFS target and verify on the loudness meter for consistency.")

q(5, "Your compressor on dialogue is 'pumping' — the background noise rises and falls audibly.",
  "Likely cause and remedy?",
  ["Too gentle; compress harder", "Too aggressive on noisy audio; clean/repair first, then use gentler compression",
   "Wrong codec", "Too few markers"], "B",
  {"A": "Harder compression worsens pumping.",
   "B": "Correct: heavy compression on noisy dialogue pumps the noise; repair first, compress gently.",
   "C": "Codec doesn't cause pumping.",
   "D": "Markers are unrelated."},
  "Repair noise before compressing — heavy compression on noisy audio pumps the noise floor.")

q(5, "A presenter's sibilance ('sss') got harsher after you brightened the dialogue with EQ.",
  "Best follow-up?",
  ["Remove all high frequencies", "Add a de-esser after the brightening EQ to tame the sibilance",
   "Add reverb", "Lower the loudness target"], "B",
  {"A": "Killing all highs dulls the whole voice.",
   "B": "Correct: a de-esser specifically tames the sibilance your brightening exaggerated.",
   "C": "Reverb doesn't address sibilance.",
   "D": "Loudness targets are unrelated."},
  "Brightening can exaggerate 'ess' sounds — follow with a de-esser, not a broad high cut.")

q(5, "You want the viewer to feel a subtle stereo bed but keep the spoken word rock-solid and clear.",
  "Sound placement strategy?",
  ["Spread dialogue wide, keep music centred", "Keep dialogue centred and mono-solid; place music/ambience in the stereo field",
   "Pan everything hard left", "Make everything mono"], "B",
  {"A": "Wide dialogue smears the voice and risks mono-fold issues.",
   "B": "Correct: anchored, centred dialogue + a wider music/ambience bed keeps speech clear and the mix immersive.",
   "C": "Hard-left everything destroys the balance.",
   "D": "All-mono loses the stereo bed you want."},
  "Anchor dialogue centre/mono-solid; use the stereo field for music and ambience.")

q(5, "Mid-mix you realise monitor volume is very low and you keep pushing faders up to compensate.",
  "Why is this risky?",
  ["It isn't risky", "You may over-boost the actual mix; set a sensible monitor level and mix to the meters/target, not to a quiet room",
   "It changes the codec", "It edits the grade"], "B",
  {"A": "It is a real risk to your levels.",
   "B": "Correct: a too-quiet monitor tempts you to over-push the mix; fix monitor level and trust the meters.",
   "C": "Monitor level doesn't change codecs.",
   "D": "It doesn't touch the grade."},
  "Don't let a quiet monitor inflate your mix — set monitoring sensibly and trust the meters.")

q(5, "A bus you created isn't outputting to the Main, so part of your mix is missing on export.",
  "What's the diagnostic step?",
  ["Re-record everything", "Check the bus routing/assignment so every sub-bus feeds the Main output",
   "Lower the loudness target", "Add markers"], "B",
  {"A": "Re-recording doesn't fix routing.",
   "B": "Correct: verify each sub-bus is assigned to the Main so nothing is dropped on export.",
   "C": "Loudness targets don't fix routing.",
   "D": "Markers are unrelated."},
  "If a layer goes missing on export, check that its bus is routed to the Main.")

# ───────────────────────── MODULE 6 · Repair decisions (16) ─────────────────────────
q(6, "A talking-head was shot in an untreated room with constant air-conditioning hiss behind the voice.",
  "Best repair workflow?",
  ["Just turn the volume down", "Capture a noise profile from a voice-free moment and apply Noise Reduction (conservatively)",
   "Add reverb to mask it", "Boost the highs"], "B",
  {"A": "Lowering volume reduces the voice too and doesn't remove hiss.",
   "B": "Correct: learn the AC-noise profile from a clean section, then reduce it carefully.",
   "C": "Reverb adds to the problem.",
   "D": "Boosting highs makes hiss worse."},
  "Learn the noise from a clean sample, then apply conservative Noise Reduction.")

q(6, "After applying strong noise reduction, the presenter's voice sounds 'underwater' and metallic.",
  "What went wrong and the fix?",
  ["Not enough reduction; push harder", "Too much reduction created artefacts; back it off to the least amount that still works",
   "Wrong codec; change it", "Too few markers"], "B",
  {"A": "More reduction worsens artefacts.",
   "B": "Correct: dial back to the minimum effective amount to avoid watery artefacts.",
   "C": "Codec isn't the cause.",
   "D": "Markers are irrelevant."},
  "Use the least noise reduction that works — over-processing makes voices watery and metallic.")

q(6, "Location power caused a steady 50 Hz hum under an entire interview.",
  "Most targeted tool?",
  ["De-Esser", "De-Hummer", "Reverb", "Chorus"], "B",
  {"A": "A de-esser targets sibilance, not hum.",
   "B": "Correct: the De-Hummer removes mains hum and its harmonics specifically.",
   "C": "Reverb adds space.",
   "D": "Chorus is a modulation effect."},
  "De-Hummer removes mains hum (50/60 Hz) and harmonics — the right tool for electrical buzz.")

q(6, "A single clip has one loud click from a cable knock; the rest is clean.",
  "Most efficient repair scope?",
  ["Apply de-click to the whole track", "Zoom in and de-click / repair just that spot on that clip",
   "Apply repair to the Main bus", "Noise-reduce the entire timeline"], "B",
  {"A": "Whole-track repair needlessly processes clean audio.",
   "B": "Correct: target the single click at clip/sample level — minimal, precise repair.",
   "C": "Main-bus repair over-processes everything.",
   "D": "Timeline-wide reduction is overkill for one click."},
  "Match repair scope to the problem — one click gets a surgical, local fix.")

q(6, "You must decide the order: the dialogue is noisy, uneven and a bit dull.",
  "Best processing order?",
  ["Compress, then EQ, then de-noise", "De-noise/repair, then EQ, then compress/level",
   "EQ, then de-noise, then nothing", "Master loudness first"], "B",
  {"A": "Compressing noisy audio first pumps the noise.",
   "B": "Correct: clean first, then shape tone, then control dynamics/level.",
   "C": "Skipping dynamics leaves it uneven.",
   "D": "Loudness mastering belongs at the end."},
  "Repair → EQ → dynamics → level → master: clean the source before shaping it.")

q(6, "A recording is audibly clipped/distorted on the loudest words at the source.",
  "Realistic expectation?",
  ["Noise reduction will fully restore it", "Clipping is largely unrecoverable — salvage what you can, or re-record/ADR; prevent it next time",
   "Raising loudness fixes it", "A de-esser fixes it"], "B",
  {"A": "Noise reduction doesn't rebuild clipped data.",
   "B": "Correct: clipped audio is permanently damaged; mitigate, ADR if needed, and capture clean levels in future.",
   "C": "More loudness worsens clipping.",
   "D": "A de-esser targets sibilance, not clipping."},
  "Clipping destroys data — it's largely unfixable; prevention and ADR are the real answers.")

q(6, "An interview shot in a hard, echoey room sounds reverberant and distant.",
  "Which modern Fairlight capability most helps recover clear dialogue?",
  ["Add more reverb", "AI Voice Isolation / dialogue separation to pull the voice out of the room",
   "A noise gate alone", "Pitch shift"], "B",
  {"A": "Adding reverb worsens the problem.",
   "B": "Correct: AI Voice Isolation separates dialogue from a difficult room/background.",
   "C": "A gate only cuts gaps, not the reverberant character within speech.",
   "D": "Pitch shift is irrelevant."},
  "AI Voice Isolation extracts dialogue from noisy/reverberant rooms you couldn't treat on the day.")

q(6, "You de-noised a clip well, but the quiet gaps now sound unnaturally dead compared to the live room.",
  "Best finishing touch?",
  ["Leave the dead gaps", "Lay a low bed of matching room tone so the silence feels natural",
   "Add a loud ambience", "Boost the noise back"], "B",
  {"A": "Dead gaps reveal the processing.",
   "B": "Correct: a subtle room-tone bed restores a natural, continuous background.",
   "C": "A loud ambience would distract.",
   "D": "Re-adding noise undoes the repair."},
  "After heavy de-noising, lay subtle room tone so cleaned gaps feel natural.")

q(6, "Two lav mics on two people both pick up each other faintly (bleed), muddying the mix.",
  "Sensible cleanup approach?",
  ["Delete one mic", "Gate/automate each track so it's only open when its speaker talks, reducing the other's bleed",
   "Add reverb", "Master louder"], "B",
  {"A": "Deleting a mic loses a needed source.",
   "B": "Correct: gating/automation opens each mic only for its speaker, cutting cross-bleed.",
   "C": "Reverb worsens muddiness.",
   "D": "Louder mastering amplifies bleed."},
  "Gate/automate each mic to open only for its own speaker — reduces cross-bleed.")

q(6, "A clip has both broadband hiss and a separate sibilance problem.",
  "How should you treat them?",
  ["One plugin fixes both", "Use Noise Reduction for the hiss and a separate De-Esser for the sibilance",
   "Ignore the hiss", "Only gate it"], "B",
  {"A": "Distinct problems need distinct tools.",
   "B": "Correct: noise reduction for broadband hiss, de-esser for sibilant peaks — different tools.",
   "C": "Ignoring hiss leaves it audible.",
   "D": "A gate won't remove hiss within speech."},
  "Match each problem to its specific repair tool — hiss vs sibilance need different plugins.")

q(6, "You're tempted to fix a noisy interview entirely on the Main bus to save time.",
  "Why is per-track/clip repair usually better?",
  ["It isn't; Main-bus is best", "Each source has different noise; treating them individually avoids harming clean elements",
   "Main-bus repair changes frame rate", "Repair only works on the Main"], "B",
  {"A": "Main-bus repair is a blunt instrument here.",
   "B": "Correct: noise differs per source; targeted repair avoids degrading clean material.",
   "C": "Repair doesn't change frame rate.",
   "D": "Repair works at clip/track/bus levels."},
  "Repair where the problem lives; blanket Main-bus repair harms clean elements too.")

q(6, "A new noisy interview lands on your desk and you're tempted to start stacking repair plugins straight away.",
  "What's the smartest diagnostic habit before any repair?",
  ["Apply plugins immediately", "Listen and identify each specific problem (hum, hiss, clicks, reverb) before choosing tools",
   "Master to LUFS first", "Render a draft"], "B",
  {"A": "Blindly stacking plugins causes artefacts.",
   "B": "Correct: diagnose the specific issues first, then pick the matching tool for each.",
   "C": "Loudness mastering is last, not first.",
   "D": "A draft render doesn't diagnose problems."},
  "Diagnose first — identify each specific defect, then apply the matching repair.")

q(6, "A clip sounds fine on your monitors but the client says it has a high-pitched whine you can't hear.",
  "Useful Fairlight aid to find it?",
  ["The loudness meter", "The frequency analyser / spectrogram to see and locate the whine, then notch/repair it",
   "The Color scopes", "The marker list"], "B",
  {"A": "The loudness meter shows level, not a specific tone.",
   "B": "Correct: a frequency analyser/spectrogram reveals the offending tone so you can notch it out.",
   "C": "Color scopes are for picture.",
   "D": "Markers don't reveal frequencies."},
  "Use a frequency analyser/spectrogram to see tones you might miss, then notch them.")

q(6, "Your noise-reduced dialogue is clean but now slightly dull and lifeless.",
  "Reasonable repair-to-mix transition?",
  ["Re-add noise", "Gently restore presence with EQ (a small high-mid lift) after repair",
   "Add heavy reverb", "Lower the loudness"], "B",
  {"A": "Re-adding noise undoes the work.",
   "B": "Correct: a gentle high-mid EQ lift restores clarity/presence lost to aggressive cleanup.",
   "C": "Heavy reverb muddies it.",
   "D": "Loudness doesn't restore presence."},
  "Cleanup can dull dialogue — restore presence with gentle EQ afterward.")

q(6, "An entire shoot day's audio has the same hum and hiss signature.",
  "Efficient repair strategy?",
  ["Repair each clip from scratch individually", "Build a repair chain on the track (or save a preset) and apply it across the matching clips",
   "Only fix the first clip", "Avoid repair entirely"], "B",
  {"A": "From-scratch per clip is needlessly slow when the problem is identical.",
   "B": "Correct: a track-level chain or saved preset applies the same fix consistently across matching clips.",
   "C": "Fixing one clip leaves the rest noisy.",
   "D": "Skipping repair ships the noise."},
  "When the defect is consistent, reuse a repair chain/preset across all matching clips.")

q(6, "You want to confirm a repair actually improved things, not just changed them.",
  "Best verification habit?",
  ["Trust it blindly", "A/B bypass the repair (and check on different speakers/headphones) to confirm real improvement",
   "Only look at the waveform", "Master louder to decide"], "B",
  {"A": "Blind trust ships artefacts.",
   "B": "Correct: bypass-compare and audition on multiple systems to confirm the fix genuinely helps.",
   "C": "Waveforms don't reveal artefacts you must hear.",
   "D": "Loudness isn't a quality test."},
  "Always A/B bypass repairs and check on multiple systems — confirm improvement, not just change.")

# ───────────────────────── MODULE 7 · Delivery decisions (14) ─────────────────────────
q(7, "A client wants the same corporate video delivered for broadcast and for their YouTube channel.",
  "How should you handle loudness?",
  ["One file for both at any level", "Deliver a broadcast version (≈ -23/-24 LUFS) and a separate online version (≈ -14 LUFS)",
   "Master both to 0 dBFS", "Ignore loudness specs"], "B",
  {"A": "Broadcast and online have different loudness norms.",
   "B": "Correct: meet each platform's spec — ≈ -23/-24 LUFS broadcast, ≈ -14 LUFS online.",
   "C": "0 dBFS isn't a loudness spec and risks clipping.",
   "D": "Ignoring specs gets content rejected or auto-adjusted."},
  "Master to each platform's loudness spec — broadcast and online differ.")

q(7, "Your social videos sometimes sound quieter than competitors' after upload.",
  "Most likely reason and fix?",
  ["The codec; change it", "You mixed too conservatively; mix to ≈ -14 LUFS with -1 dBTP so the platform doesn't turn you down disproportionately",
   "Add reverb", "Lower the dialogue"], "B",
  {"A": "Codec isn't the loudness cause here.",
   "B": "Correct: target the platform's loudness (≈ -14 LUFS, -1 dBTP) so normalisation treats you fairly.",
   "C": "Reverb doesn't set loudness.",
   "D": "Lowering dialogue makes it quieter still."},
  "Hit the platform's loudness target (≈ -14 LUFS) so normalisation doesn't leave you quiet.")

q(7, "Before exporting, you check the Main bus and the integrated loudness reads -19 LUFS but the target is -14 LUFS.",
  "Best action?",
  ["Export anyway", "Raise the overall level (carefully, watching true peak) to reach ≈ -14 LUFS, or use loudness normalisation",
   "Lower it further", "Change the frame rate"], "B",
  {"A": "Exporting under-target ships a too-quiet file.",
   "B": "Correct: bring level up to target while keeping true peak safe (≤ -1 dBTP), or normalise to the spec.",
   "C": "Going quieter moves away from target.",
   "D": "Frame rate is unrelated to loudness."},
  "Bring integrated loudness to target while protecting true peak; normalisation can automate it.")

q(7, "A broadcaster requires separate dialogue, music and effects stems for the same programme.",
  "How do you produce them?",
  ["Export one stereo mix only", "Route D/M/E to separate buses and export each bus as its own stem",
   "Delete the music", "Render the Color page"], "B",
  {"A": "A single mix can't be re-balanced/localised.",
   "B": "Correct: separate D/M/E buses let you export discrete stems for re-versioning and dubbing.",
   "C": "Deleting music breaks the deliverable.",
   "D": "Color rendering isn't audio stems."},
  "Bus by D/M/E and export each as a stem for re-balancing, localisation and compliance.")

q(7, "The client may later translate the video into other languages.",
  "Which delivery protects that option?",
  ["A flattened final mix only", "An M&E (music & effects) stem with dialogue kept separate",
   "A louder master", "A different codec"], "B",
  {"A": "A flattened mix can't have dialogue swapped.",
   "B": "Correct: deliver M&E plus separate dialogue so translated dialogue can drop in over the M&E.",
   "C": "Loudness doesn't enable translation.",
   "D": "Codec choice doesn't enable dubbing."},
  "Keep dialogue separate and provide M&E so the piece can be dubbed into other languages.")

q(7, "On the Deliver page you're setting the audio export for a standard video master.",
  "Most appropriate audio settings?",
  ["8 kHz / 8-bit", "48 kHz / 24-bit, with the codec your delivery spec requires",
   "Whatever is default, unchecked", "96 kHz / 4-bit"], "B",
  {"A": "Telephone-grade is unacceptable for video.",
   "B": "Correct: 48 kHz / 24-bit is the professional standard; pick the spec's codec.",
   "C": "Blindly accepting defaults can mismatch the spec.",
   "D": "4-bit isn't a real professional depth."},
  "Deliver 48 kHz / 24-bit and the codec your spec demands — verify, don't assume.")

q(7, "After export you spot that one sub-bus wasn't routed to the Main, so the SFX layer is missing.",
  "What habit prevents this?",
  ["Never check routing", "Verify all bus assignments feed the Main and listen to the full mix before exporting",
   "Master louder", "Add markers"], "B",
  {"A": "Skipping checks is exactly how this happens.",
   "B": "Correct: confirm routing and do a final full-mix listen before delivering.",
   "C": "Loudness doesn't fix routing.",
   "D": "Markers don't verify routing."},
  "Pre-export checklist: confirm bus routing to Main and listen to the whole mix.")

q(7, "A vertical social cut and a horizontal web cut share the same audio mix.",
  "Most efficient audio approach?",
  ["Re-mix from scratch for each", "Reuse the same mastered audio if the edit/timing matches; only adjust if the cuts differ",
   "Master each at a random level", "Strip the audio entirely"], "B",
  {"A": "Re-mixing identical audio is wasteful.",
   "B": "Correct: if timing matches, reuse the mastered audio; only re-touch where the edits differ.",
   "C": "Random levels break consistency.",
   "D": "Stripping audio defeats the deliverable."},
  "Reuse a good master across versions when timing matches — re-touch only where edits differ.")

q(7, "Your delivery spec says max True Peak -1 dBTP, but your master hits -0.2 dBTP after the limiter.",
  "Correct response?",
  ["Ship it; close enough", "Lower the ceiling/level so true peaks stay at or below -1 dBTP",
   "Raise it to 0 dBTP", "Change the sample rate"], "B",
  {"A": "Exceeding the spec can get the file flagged or clip after encoding.",
   "B": "Correct: bring true peak to ≤ -1 dBTP to meet spec and survive lossy encoding.",
   "C": "0 dBTP is worse, not better.",
   "D": "Sample rate doesn't fix true peak."},
  "Respect the true-peak ceiling exactly — set the limiter so peaks stay ≤ spec (e.g. -1 dBTP).")

q(7, "A client asks for a 'clean' version with no music for their own re-edits.",
  "How do you provide it?",
  ["Send only the full mix", "Export a dialogue (and optionally effects) stem without the music bus",
   "Delete the project", "Render a still"], "B",
  {"A": "The full mix has music baked in.",
   "B": "Correct: export the relevant stems excluding music so they can re-edit freely.",
   "C": "Deleting the project is absurd.",
   "D": "A still isn't audio."},
  "Provide stems (e.g. dialogue/effects without music) when clients need clean re-edit material.")

q(7, "You delivered a file and the client reports the dialogue is hard to hear on their TV.",
  "Most likely mix issue to revisit?",
  ["The grade", "Dialogue level/intelligibility relative to music/effects — raise/duck and re-check loudness",
   "The thumbnail", "The frame rate"], "B",
  {"A": "The grade is picture, not audio clarity.",
   "B": "Correct: revisit the dialogue-to-bed balance and intelligibility, then re-verify loudness.",
   "C": "Thumbnails are unrelated.",
   "D": "Frame rate doesn't drive intelligibility."},
  "Intelligibility complaints point to the dialogue-vs-bed balance — fix and re-check loudness.")

q(7, "Final quality check before sending a master to a client.",
  "Which audio QC step matters most?",
  ["Only watch the video muted", "Listen end-to-end for clicks/dropouts/clipping and confirm loudness/true-peak meet spec",
   "Trust the meters without listening", "Skip QC to save time"], "B",
  {"A": "Muted review skips the audio entirely.",
   "B": "Correct: a full listen plus a loudness/true-peak check catches problems before the client does.",
   "C": "Meters alone miss audible glitches.",
   "D": "Skipping QC risks shipping faults."},
  "QC by listening fully and verifying loudness/true-peak against the spec before delivery.")

q(7, "A podcast-style talking-head will be distributed as audio too.",
  "Sensible loudness target for the audio-led platform?",
  ["-23 LUFS broadcast", "Around -16 LUFS (common podcast/spoken-word target), -1 dBTP",
   "0 dBFS", "+3 LUFS"], "B",
  {"A": "-23 LUFS is broadcast video, quieter than podcast norms.",
   "B": "Correct: spoken-word/podcast platforms commonly target around -16 LUFS with safe true peak.",
   "C": "0 dBFS is a clipping ceiling.",
   "D": "Positive LUFS isn't valid."},
  "Spoken-word/podcast audio commonly targets ≈ -16 LUFS, -1 dBTP.")

q(7, "You need to hand off a project so another editor can finish the mix.",
  "Best practice for a clean handoff?",
  ["Send only the exported MP4", "Keep tracks organised/labelled, buses logical, and deliver the project (and media) so they can continue",
   "Flatten everything to one track", "Delete the buses first"], "B",
  {"A": "An MP4 can't be re-mixed.",
   "B": "Correct: an organised, labelled session with logical routing lets another editor pick it up cleanly.",
   "C": "Flattening destroys their flexibility.",
   "D": "Deleting buses breaks the routing."},
  "Hand off organised, labelled sessions with intact routing — not a flattened export.")

QUESTIONS = Q
assert len(QUESTIONS) == 100, f"Exam 2 has {len(QUESTIONS)} questions, expected 100"
