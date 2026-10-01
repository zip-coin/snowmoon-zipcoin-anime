# Episode 4 — Chapter 19: "Four hundred zipcoins"

Gladias and Zei are having tea in a cafeteria inside a mountain pyramid. Zei's watch buzzes with a message from a food court he once ate at. Someone anonymous **burned 400 zipcoins** to send it, and payments in zipcoins are fully anonymized, so how did the courtyard know he ate there?

---

## Dialogue (word for word from Snowmoon, chapter 19, lightly trimmed)

1. *Zei's watch buzzes.* **Gladias:** "What is it?"
2. **Zei:** "A message from a courtyard where I ate in Sadzu Du once. This is really weird. It seems to be addressed directly to me."
3. **Gladias:** "How does the courtyard know you ate there? Payment is done in zipcoins, that's fully anonymized."
4. **Zei:** "Exactly. The courtyard seems to have sent it to all their guests from the past half year."
5. **Gladias:** "What does it say?"
6. **Zei:** "It's from the Beautiful Plants food court, on 2415 Len Su street, in Sadzu Du. 'An anonymous person burned four hundred zipcoins to send this message.' The message envelope says that the recipient 'is successful' and is 18 years old. I know nothing else."
7. **Gladias:** "That's a ... well-calibrated description."

## Shots and audio

| # | Clip | Voice | Sound |
|---|---|---|---|
| 1 | Shot 1 (KF1 wide) | line 1 | watch buzz, cafeteria ambience |
| 2 | Shot 2 (KF2 Zei) | line 2 | |
| 3 | Shot 3 (KF3 Gladias) | line 3 | |
| 4 | Shot 2 reused | line 4 | |
| 5 | Shot 5 (KF4 → message card) | line 5 | hologram whoosh |
| 6 | Shot 6 (KF2 Zei, looped) | line 6 | |
| 7 | Shot 7 (KF3 Gladias) | line 7 | |

Ambience 15–20%, calm mysterious music 10–15%, all Seedance audio muted. Export at 1080p, 30fps.

---

## Reference prompts

**Zei sheet** (attach the Gladias sheet from episode 1 for style):
```
Match the art style, line weight and colouring of the attached image. Anime character reference sheet on a plain white background. Zei: an 18-year-old young man, slim, short neat black hair, sharp curious eyes, simple dark green zip jacket over a light grey top, black smart watch on his left wrist. Front, side and back views standing, plus one seated at a table holding a tea cup. Clean cel-shaded anime, soft muted colours. No text, no background.
```

**Cafeteria:**
```
Anime background art, no people. A large cafeteria built inside a mountain pyramid: sloped stone walls meeting high above, warm lighting, long wooden tables. On the walls, huge screens act as fake windows showing a sunny mountain valley. Calm, quiet, slightly futuristic. Wide shot, eye level. Clean cel-shaded anime, soft muted colours. No text.
```

## Keyframe prompts (16:9)

**KF1 (wide)**: attach the Gladias sheet, Zei sheet and cafeteria
```
Use the attached images as references. Keep Gladias, Zei, the cafeteria and the art style exactly the same. Clean cel-shaded anime, warm soft lighting. 16:9 widescreen.

Wide shot, eye level. Gladias and Zei sit facing each other at a wooden table in the cafeteria, with empty plates and two tea cups between them. Gladias is on the LEFT side of the frame, facing RIGHT: short dark brown hair, long dark purple robe with the hood DOWN, black band around his neck. He looks at Zei with a curious expression. Zei is on the RIGHT side of the frame, facing LEFT: short black hair, dark green zip jacket, grey top. He has just lifted his left wrist and stares at his black smart watch with wide, surprised eyes. The watch screen is dark. Behind them, huge screens on the sloped stone walls show a sunny mountain valley like windows.

No other people. No text, no letters, no logos anywhere.
```

**KF2 (Zei)**: attach the Zei sheet and cafeteria
```
Use the attached images as references. Keep Zei's face, hair, outfit and the art style exactly the same. Keep the cafeteria's lighting and colours the same. Clean cel-shaded anime, warm soft lighting. 16:9 widescreen.

Medium close-up of Zei from the chest up, eye level, turned three-quarters towards the LEFT side of the frame, looking at someone just off-screen on the left. Mouth open mid-sentence, a puzzled frown, eyebrows slightly raised. He holds a white tea cup in his right hand near the table. Short black hair, dark green zip jacket, grey top, black smart watch on his left wrist.

Background softly blurred: sloped stone wall and a large screen showing a sunny mountain valley.

Only Zei in frame. No text, no letters, no logos anywhere.
```

**KF3 (Gladias)**: attach the Gladias sheet and cafeteria
```
Use the attached images as references. Keep Gladias's face, hair, robe, neck band and the art style exactly the same. Keep the cafeteria's lighting and colours the same. Clean cel-shaded anime, warm soft lighting. 16:9 widescreen.

Medium close-up of Gladias from the chest up, eye level, turned three-quarters towards the RIGHT side of the frame, looking at someone just off-screen on the right. Mouth open mid-sentence, eyebrows raised, a curious, thoughtful expression. Short dark brown hair, dark purple robe with the hood DOWN resting on his shoulders, black band around his neck clearly visible.

Background softly blurred: sloped stone wall and a large screen showing a sunny mountain valley.

Only Gladias in frame. No text, no letters, no logos anywhere.
```
Fix used (to make him look across the table, not up at the window):
```
Keep everything exactly the same: his face, hair, robe, neck band, expression and the background. Only change his pose: he is sitting at a wooden table, turned three-quarters towards the RIGHT side of the frame, looking straight across the table at someone sitting opposite him at the same eye level. His eyes look level to the right, not up. The edge of the wooden table is visible at the bottom of the frame.
```

**KF4 (the message)**: attach the Zei sheet and cafeteria
```
Use the attached images as references. Keep Zei's jacket sleeve, watch and the art style exactly the same. Clean cel-shaded anime, warm soft lighting. 16:9 widescreen.

Close-up, looking slightly down at a wooden cafeteria table. A young man's left forearm in a dark green jacket sleeve rests on the table, wearing a black smart watch with a softly glowing screen. A white tea cup sits nearby. Floating in the air just above the watch is one large flat, semi-transparent holographic card, facing the camera straight on, completely BLANK and EMPTY, with a soft glowing edge. The card is big and takes up the upper middle of the frame.

Only the arm, watch, tea cup and table are in frame, and no face. No text, no letters, no logos anywhere.
```

The text on the card is **not** AI-generated. `scripts/make_card.py` draws it and fits it to the card's angle:
```bash
cd episode-04/scripts
python3 make_card.py
```

## Seedance prompts (16:9 · 5s · audio off)

Negative for all:
```
style change, realistic, 3D render, face changing, different person, extra fingers, extra hands, extra people, warped text, scrambled letters, subtitles, blurry, warping, camera movement
```

**Shot 1**: first frame KF1, reference Gladias + Zei sheets
```
Anime scene, clean cel-shaded style, warm soft lighting, inside a stone pyramid cafeteria. Gladias, a man with short dark brown hair, a dark purple robe with the hood down and a black band around his neck, sits on the LEFT side of the wooden table. Zei, a young man with short black hair and a dark green zip jacket, sits opposite him on the RIGHT side. Zei looks down at the black smart watch on his left wrist and his eyes slowly widen in surprise. Gladias leans forward slightly and asks a short question, his mouth moving briefly. Steam rises gently from the tea cups. Both stay seated. Static camera. No audio. Keep both faces, outfits and the anime art style exactly the same.
```

**Shot 2** (also used for shot 4): first frame KF2, reference Zei sheet
```
Anime close-up, clean cel-shaded style, warm soft lighting. Zei, a young man with short black hair, a dark green zip jacket and a grey top, faces the LEFT side of the frame and talks with a puzzled frown. His mouth clearly opens and closes the whole time in natural talking movements. He holds a white tea cup without drinking from it, blinks naturally and raises his eyebrows slightly. Very small head movement only. Background mountains and stone wall stay still. Static camera. No audio. Keep his face, hair, outfit and the anime art style exactly the same.
```

**Shot 3**: first frame KF3, reference Gladias sheet
```
Anime close-up, clean cel-shaded style, warm soft lighting. Gladias, a man with short dark brown hair, a dark purple robe with the hood down and a black band around his neck, sits at a wooden table facing the RIGHT side of the frame and talks with a curious, confused expression. His mouth clearly opens and closes the whole time in natural talking movements. Eyebrows raised, natural blinks, one small tilt of the head. Very small head movement only. Background stays still. Static camera. No audio. Keep his face, hair, robe, neck band and the anime art style exactly the same.
```

**Shot 5**: first frame KF4 (blank card), last frame `assets/ep4_kf4_message.jpg`
```
Anime close-up, clean cel-shaded style, warm soft lighting. A young man's wrist with a black smart watch rests on a wooden table. A flat holographic card floats above the watch. The card flickers softly and glowing lines of text fade in across it, one line after another. The wrist and watch stay completely still. Static camera. No audio. Art style unchanged.
```

**Shot 6**: first frame KF2, reference Zei sheet (loop ×3 for the long line)
```
Anime close-up, clean cel-shaded style, warm soft lighting. Zei, a young man with short black hair, a dark green zip jacket and a grey top, faces the LEFT side of the frame and talks slowly and seriously, as if reading something strange out loud. His mouth clearly opens and closes the whole time in natural talking movements. He glances down once, then looks back up to the left. He slowly lowers the tea cup to the table. Very small head movement only. Static camera. No audio. Keep his face, hair, outfit and the anime art style exactly the same.
```

**Shot 7**: first frame KF3, reference Gladias sheet
```
Anime close-up, clean cel-shaded style, warm soft lighting. Gladias, a man with short dark brown hair, a dark purple robe with the hood down and a black band around his neck, sits at a wooden table facing the RIGHT side of the frame. He pauses, raises one eyebrow, then says a short sentence slowly with a dry, impressed half-smile. His mouth clearly opens and closes while he talks. Natural blinks. Very small head movement only. Static camera. No audio. Keep his face, hair, robe, neck band and the anime art style exactly the same.
```

## Voices (ElevenLabs)

**Zei** (new):
```
Young man, 18 years old, calm and intelligent, clear medium-low voice, speaks at a steady thoughtful pace, slightly serious, a little puzzled and curious. Light non-native accent, neutral and hard to place. Natural, not dramatic.
```
Stability about 50–55%, style 10–20%. Read line 6 slower.

**Gladias:** same voice as in episodes 1–3.

## Faithful vs creative

**From the book (ch. 19):** the cafeteria inside a mountain pyramid with screens as windows, tea after the meal, Zei's watch buzzing, all dialogue, "Payment is done in zipcoins, that's fully anonymized", the Beautiful Plants food court at 2415 Len Su street in Sadzu Du, 400 zipcoins burned to send the message, and the Dzegoban sender line "sa dzu du de len su 2415 de bun kai mo fan".

**Creative:**
- Zei's look and voice (the book doesn't describe him)
- the cafeteria design
- the holographic card and its layout (in the book the message is on his watch)
- the zipcoin logo
- the dialogue is lightly trimmed

## Files
```
images/references/   Zei sheet, cafeteria
images/keyframes/    KF1–KF4
assets/              ep4_kf4_message.jpg (shot 5 last frame)
scripts/             make_card.py
audio/               (voice lines go here)
```
