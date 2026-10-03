# Episode 5 — Chapter 20: "Fifty zipcoins"

Seila knocks on Lectoby's door. No answer. She knocks again. Then her watch buzzes: **"50 zipcoins have just been burned."** 🔥 Mov, waiting down the street, got impatient. The door opens, and the first thing Lectoby asks is why she burned them.

---

## Script (word for word from Snowmoon, chapter 20)

1. *Seila knocks. No response. She knocks again. Footsteps inside, not coming closer.*
2. *Her watch buzzes:* "50 zipcoins have just been burned.🔥"
3. *She knocks a third time. Footsteps come closer.*
4. **Lectoby** (behind the door): "What do you want?"
5. **Seila:** "Hi, I'm Seila. I'm the one that asked Balme and Telroy to send the message about the social media rubrics. I want to talk."
6. **Lectoby** (opens the door): "I'm Lectoby. I'm in the social media openness rubric. I'm sorry I didn't open the door. My wife is stuck in Northglade. I've been really upset today, I just don't want to talk to people."
7. **Seila:** "I understand. My kids are stuck in Northglade too."
8. **Lectoby:** "Why did you burn those zipcoins? You could have just asked Balme to tell me you're coming."
9. **Seila** (thinking): "Mov ... Why did he have to be so impatient?"
10. **Seila:** "I'm sorry, I'm just really desperate."

## Edit order

| # | Clip | Audio |
|---|---|---|
| 1 | Shot 1 – knock wide (KF1) | 2 knocks |
| 2 | Shot 2 – knock again (KF2) | knock, faint footsteps |
| 3 | Shot 3 – watch (KF3 → `assets/ep5_kf3_burned.jpg`) | buzz |
| 4 | Shot 4 – Mov (KF4) | silence |
| 5 | Shot 2 reused | 3rd knock, line 4 off-screen |
| 6 | Talk clip 1 – Seila (KF2) | line 5 |
| 7 | Talk clip 2 – Lectoby (KF5) | line 6, door creak |
| 8 | Talk clip 3 – Seila (KF2) | line 7 |
| 9 | Talk clip 4 – Lectoby (KF5) | line 8 |
| 10 | Shot 4 reused | line 9 as voice-over with light echo |
| 11 | `assets/clips/lectoby_listening.mp4` | line 10 off-screen |

10 AI clips in total: 4 silent + 4 lip-synced (lines 4, 9 and 10 need no lip sync).

---

## Reference prompt

**Seila sheet** (attach the Gladias sheet from episode 1 for style):
```
Match the art style, line weight and colouring of the attached image. Anime character reference sheet on a plain white background. Seila: a calm, determined woman in her late thirties, long dark wavy hair, soft brown eyes, simple grey knit cardigan over a dark top, long dark skirt, black smart watch on her left wrist. Front, side and back views standing, plus one close-up of her face looking worried. Clean cel-shaded anime, soft muted colours. No text, no background.
```
Mov uses the Keeper sheet from episode 2 (hood up, face hidden).

## Keyframe prompts (16:9)

Each starts with: *"Use the attached images as references. Keep the characters and art style exactly the same. Clean cel-shaded anime, soft late-afternoon light. 16:9 widescreen. No text, no letters, no logos anywhere."*

- **KF1 (Seila sheet + Keeper sheet):** Wide shot of a quiet residential street with trees and small modern family houses. In the foreground on the RIGHT, Seila stands at the front door of a house, her right hand raised mid-knock. Far in the background on the LEFT, under a tree by the street, a figure in a long dark purple privacy robe stands still with the hood UP and face covered, watching.
- **KF2 (Seila sheet):** Medium close-up of Seila from the chest up, standing at a closed wooden front door, turned three-quarters towards the RIGHT side of the frame, facing the door. Worried, impatient expression, lips pressed together. One hand raised near the door as if about to knock again.
- **KF3 (Seila sheet):** Close-up of a woman's left wrist in a grey knit cardigan sleeve, held up in front of a wooden front door. A black smart watch on her wrist, its screen facing the camera FLAT, completely BLANK and glowing white.
- **KF4 (Keeper sheet):** Medium-wide shot on a quiet tree-lined street. A figure in a long dark purple privacy robe stands under a tree with the hood UP and face covered, only a shadow where the face is. He has just lowered his left wrist from looking at his black smart watch. Still and calm, slightly suspicious.
- **KF5 (attach KF2 for style only):**
```
Use the attached image as a reference for the art style only: same anime line art, cel shading, colours and lighting. Do NOT copy the woman. Create a brand new anime character in exactly this style.

Japanese anime style, 2D cel-shaded illustration, clean black line art, flat colours with soft shading. NOT realistic, NOT a photo, NOT 3D.

Medium close-up, 16:9 widescreen. A tired anime man in his forties stands in an open front doorway, seen from outside. Messy dark hair, light stubble, sad red-rimmed eyes, plain wrinkled grey sweater. He holds the door half open with one hand and faces LEFT towards someone just outside, with a guarded, upset expression. A dim hallway behind him, soft late-afternoon light on his face.

No text, no letters, no logos anywhere.
```
(Without a style reference, Grok drew him realistic.)

The watch screen is **not** AI-generated: `scripts/make_watch.py` draws it onto KF3.

## Seedance prompts (16:9)

Negative for all:
```
style change, realistic, 3D render, photo, face changing, different person, face visible under hood, extra fingers, extra hands, extra people, warped text, scrambled letters, subtitles, blurry, warping, camera movement, out of sync lips
```

### Silent shots (5s, audio off)
**Shot 1** – @Image1 = KF1, + Seila sheet
```
@Image1 as the first frame. Anime scene, clean cel-shaded style, soft late-afternoon light, quiet residential street. Seila, a woman with long dark wavy hair, a grey knit cardigan and a long dark skirt, stands at the front door of a house on the RIGHT side of the frame. She raises her hand and knocks twice on the door, then lowers her hand and waits. Far in the background on the LEFT, a figure in a long dark purple robe with the hood up and face covered stands completely still on the pavement. Leaves sway gently in the trees. Static camera. No audio. Keep both characters and the anime art style exactly the same.
```
**Shot 2** – @Image1 = KF2, + Seila sheet
```
@Image1 as the first frame. Anime close-up, clean cel-shaded style, soft late-afternoon light. Seila, a woman with long dark wavy hair and a grey knit cardigan, stands at a wooden front door facing the RIGHT side of the frame. She knocks on the door again, then lowers her hand, sighs impatiently and glances at the door with a worried frown. Her lips stay closed. Very small head movement only. Her hair moves slightly. Static camera. No audio. Keep her face, hair, outfit and the anime art style exactly the same.
```
**Shot 3** – @Image1 = KF3, @Image2 = `assets/ep5_kf3_burned.jpg`
```
@Image1 as the first frame and @Image2 as the last frame. Anime close-up, clean cel-shaded style, soft light. A woman's wrist in a grey knit cardigan sleeve, held in front of a wooden door, wearing a black smart watch with a glowing white screen. The wrist stays completely still. The watch gives a tiny buzz shake, the screen flickers and a notification fades in. Static camera. No audio. Anime art style unchanged.
```
(Fallback with perfect text: `assets/clips/watch_burned.mp4`.)

**Shot 4** – @Image1 = KF4, + Keeper sheet
```
@Image1 as the first frame. Anime scene, clean cel-shaded style, soft late-afternoon light, tree-lined residential street. A figure in a long dark purple privacy robe with the hood up and the face completely hidden in black shadow stands in the middle of the street, looking at the black smart watch on his raised left wrist. He slowly lowers his wrist to his side, then tilts his hooded head very slightly to one side, completely calm. The face stays hidden in shadow the whole time. Leaves sway and dappled sunlight shifts on the road. Static camera. No audio. Anime art style unchanged.
```

### Lip-synced talking clips (audio ON, voice MP3 uploaded as @Audio1)
Trim silence from each voice file first; clip length = line length + ~1s (max 15s audio).

**Talk clip 1 – line 5** – @Image1 = KF2, @Image2 = Seila sheet, @Audio1 = line 5
```
@Image1 as the first frame. @Image2 is the character reference. Anime close-up, clean cel-shaded style, soft late-afternoon light. Seila, a woman with long dark wavy hair and a grey knit cardigan, stands at a wooden front door facing the RIGHT side of the frame and speaks the dialogue from @Audio1 to someone behind the door. Her lips move in perfect sync with @Audio1, matching every word. Polite, hopeful but slightly nervous delivery. She lowers her raised hand to her side as she starts talking. Natural blinks, very small head movement. Static camera. Keep her face, hair, outfit and the anime art style exactly the same.
```
**Talk clip 2 – line 6** – @Image1 = KF5, @Audio1 = line 6
```
@Image1 as the first frame. Anime close-up, clean cel-shaded style, dim hallway light. A tired man in his forties with messy black hair, stubble and a wrinkled grey sweater stands in an open doorway holding the door with one hand, facing slightly LEFT towards someone outside. He speaks the dialogue from @Audio1. His lips move in perfect sync with @Audio1, matching every word. Tired, sad, quiet delivery. Heavy slow blinks, eyes looking down when he mentions his wife, then back up. Very small head movement. Static camera. Keep his face, hair, sweater and the anime art style exactly the same.
```
**Talk clip 3 – line 7** – @Image1 = KF2, @Image2 = Seila sheet, @Audio1 = line 7
```
@Image1 as the first frame. @Image2 is the character reference. Anime close-up, clean cel-shaded style, soft late-afternoon light. Seila, a woman with long dark wavy hair and a grey knit cardigan, stands at a front door facing the RIGHT side of the frame and speaks the dialogue from @Audio1. Her lips move in perfect sync with @Audio1, matching every word. Soft, gentle, sad delivery. Her eyes soften and glisten slightly, a small understanding nod. Very small head movement. Static camera. Keep her face, hair, outfit and the anime art style exactly the same.
```
**Talk clip 4 – line 8** – @Image1 = KF5, @Audio1 = line 8
```
@Image1 as the first frame. Anime close-up, clean cel-shaded style, dim hallway light. The tired man with messy black hair, stubble and a grey sweater stands in the open doorway facing slightly LEFT and speaks the dialogue from @Audio1. His lips move in perfect sync with @Audio1, matching every word. Confused and slightly annoyed delivery, one eyebrow raised, head tilting a little. Natural blinks. Very small head movement. Static camera. Keep his face, hair, sweater and the anime art style exactly the same.
```

Line 10 is played off-screen over `assets/clips/lectoby_listening.mp4` (a slow camera drift on KF5 made by `scripts/make_motion_clips.py`) to save a generation.

## Voices (ElevenLabs)
- **Seila:** woman, late 30s, calm, warm and determined, slightly worried, soft clear voice, natural pace.
- **Lectoby:** man, 40s, tired, low and sad voice, speaks slowly, a little guarded.
- Line 9 is recorded as a quiet, annoyed thought; add light echo/reverb in CapCut.

## Faithful vs creative
**From the book (ch. 20):** the house, Seila knocking three times, the footsteps, "50 zipcoins have just been burned.🔥", Mov staying back, all dialogue, Seila's thought about Mov.

**Creative:**
- every character's look (the book doesn't describe them)
- Mov standing in the street and checking his watch (the book only says he "stayed back entirely"; Seila guesses it was him)
- the watch screen design and zipcoin logo
- Lectoby listening during the last line

## Files
```
images/references/   Seila sheet
images/keyframes/    KF1–KF5
assets/              ep5_kf3_burned.jpg (shot 3 last frame)
assets/clips/        watch_burned.mp4, lectoby_listening.mp4
scripts/             make_watch.py, make_motion_clips.py
audio/               (voice lines go here)
```
