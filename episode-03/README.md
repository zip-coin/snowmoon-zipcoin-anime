# Episode 3 — Chapter 16: "Straight out of a life savings wallet?"

Gladias and Febric finish eating. Febric teases him about the declined payment from episode 1, so Gladias decides to test his social recovery wallet. The test is buying one bottle of Hydrafill for **5.5 zipcoins**. Febric confirms the request on his watch, Seila sends Gladias a security question, and the watch shows **3 of 4 signatures**.

---

## Dialogue (word for word from Snowmoon, chapter 16)

Short version, as recorded. Lines are cut down but not reworded or reordered.

1. **Febric:** "Did you remember to take out your zipcoins this time?"
2. **Gladias:** "Hey, I may make lots of mistakes, but I don't make the same mistake twice"
3. **Febric:** "Buy a Hydrafill bottle?"
4. **Gladias:** "Buy a Hydrafill bottle? Straight out of a life savings wallet?" … "Okay fine ... let me start the operation."
5. Febric's watch: "Wallet 0x8f62... social recovery mode transaction request", Hydrafill, 5.5 zipcoins. He taps Confirm.
6. Seila's question on Gladias's watch: "What was the most unusual thing I did on the evening the kids came back from Vil and Daia's?"
7. **Gladias** (whispering into his neck band): "You unplugged the screen in the restaurant when it was showing Lord Ephelion's speech."
8. Gladias's watch: 3 signatures done, 1 still needed.
9. **Febric:** "I'm obviously not gonna ask who that was, or who else you need to confirm it. But good luck!"

## Shots and audio

| Shot | Picture | Audio |
|---|---|---|
| 1 | Wide: both at the table, Helisport copter race on TV | Febric, line 1 |
| 2 | Gladias close-up | Gladias, line 2 |
| 4 | Febric, thumb at the Hydrafill poster | Febric, line 3 |
| 2 | Gladias close-up (reused) | Gladias, line 4 |
| 5 → 6 | Febric's watch: request → Confirmed | buzz, tap |
| 7 | Gladias's watch: Seila's question (hold 3 s) | buzz |
| 8 | Gladias whispering | Gladias, line 7 |
| 9 | Cross-fade to 3 of 4 signatures (CapCut only) | buzz + 3 soft chimes |
| 3 | Febric pointing | Febric, line 9 |

## Keyframes

`images/keyframes/` has the six stills (made in Grok with the Gladias and Febric sheets from episode 1 attached):
KF1 wide with the copter race on TV · KF2 Gladias · KF3 Febric pointing · KF4 Febric at the poster · KF5 Febric's watch (blank) · KF6 Gladias's watch (blank).

The watch screens and the poster label are **not** made by the AI. `scripts/make_screens.py` draws them and fits them to each watch's angle:

```bash
cd episode-03/scripts
python3 make_screens.py
```

Output goes to `assets/screens/`.

## Seedance (16:9 · 5 s · audio off)

Same method as episode 1: keyframe as the first frame, character sheet as the reference, and a last frame when a screen changes.

**Shot 8 (Gladias whispering):**
```
Anime close-up, clean cel-shaded style, soft daylight. Gladias, a man with short dark brown hair, a dark purple robe with the hood down and a black band around his neck, tilts his chin down slightly and whispers into the black band around his neck.
His lips clearly open and close the whole time in small, steady talking movements, like whispering a short sentence. He blinks slowly.
His head stays still and upright. He does not tilt or turn his head.
Static camera. No audio. Keep his face, hair, robe, neck band and the anime art style exactly the same.
```
Negative: `head tilt, head turning, closed mouth, still lips, style change, realistic, 3D render, face changing, extra fingers, extra hands, blurry, warping, camera movement`

**Shot 9:** no Seedance. In CapCut, cross-fade `ep3_gladias_question.jpg` into `ep3_gladias_signatures.jpg` (0.5 s), add a slow zoom and three soft chimes, one per tick. Doing it this way means no credits and no warped text.

## Faithful vs creative

**From the book (ch. 16):** every line of dialogue, the Hydrafill test purchase, 5.5 zipcoins, "Wallet 0x8f62... social recovery mode transaction request", Febric tapping Confirm, Seila's security question and Gladias's answer, whispering through the neck band, three signatures done with one to go.

**Creative:**
- the Helisport race on the TV
- the Hydrafill poster on the wall
- the watch screen designs and the zipcoin logo
- the "3 of 4" tick layout (the book says "Three signatures done... One to go")
- "Recovery check / from Seila" as the screen heading (the book's message starts "Security question:")
- the lines are shortened

## Files
```
images/keyframes/   KF1–KF6
assets/screens/     watch screens + poster (used as keyframes / last frames)
scripts/            make_screens.py
audio/              (voice lines go here)
```
