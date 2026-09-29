# Snowmoon: Zipcoin (fan anime)

An AI-made anime version of the scenes where **zipcoin** is used in *Snowmoon*, the novel by Vitalik Buterin.

**Episode 1: Chapter 6, "The salad".** Gladias's payment is declined, he takes out a private reputation-backed loan of 2773 zipcoins, and pays 10.5 zc + 1.1 zc tax. https://x.com/Zipcoin_eth/status/2104713009398780412

> This is a fan project. It is **not affiliated with or endorsed by Vitalik Buterin**.
> Source novel: https://vitalik.eth.limo/snowmoon/

---

## Why this repo exists

Snowmoon is released under the **GPL v3**. The author's note says:

> "you are free to go turn it into a movie or a vibe-coded anime or whatever, but if you do that, you are required to open-source the pipeline (AI prompts, scripts, task-specific harness, etc) and other non-commodity materials that you used to make it so that other people can build on top of your work."

This repo is that pipeline. Everything here is released under **GPL v3** (see `LICENSE`), so you can reuse and remix it, as long as you share your own pipeline too.

---

## What's in here

```
prompts/
  01_character_sheets.md          prompts for Gladias, Febric, the robot, the restaurant, the logo
  02_keyframes.md                 every still-image prompt, shot by shot, plus the fixes used
  03_seedance_motion.md           every animation prompt, settings and negative prompts
  04_dialogue_voices_sound_edit.md  script, voice settings, sound effects, edit order
images/
  character-sheets/               the locked character and location references
  keyframes/                      first frames for each shot
assets/
  logo/                           zipcoin logo (flat anime version and transparent PNGs)
  cards/                          payment cards (declined / loan request / received / success)
  endframes/                      keyframes with cards added, used as Seedance last frames
scripts/
  make_cards.py                   builds the payment card PNGs from the logo
  make_endframes.py               composites the cards onto the keyframes, turns the ring red for shot 7
audio/                            (voice lines go here)
LICENSE                           GPL v3
```

## The pipeline

1. **Character sheets:** ChatGPT image generation and Grok
2. **Keyframes (still images for each shot):** Grok, with the character sheets attached as references
3. **Payment cards and end frames:** Python (Pillow) scripts in `scripts/`
4. **Animation:** Seedance 2.0, first frame plus reference sheet, and a last frame for the payment shots. 16:9, 5 s, no audio
5. **Voices:** ElevenLabs text to speech
6. **Sound effects and music:** Pixabay / CapCut library
7. **Edit:** CapCut

The tools themselves are off-the-shelf and not included. Everything specific to this project is included.

### Rebuild the cards and end frames
```bash
pip install pillow numpy
cd scripts
python3 make_cards.py
python3 make_endframes.py
```

## Faithful to the book vs. creative choices

**From the book (chapter 6):**
- the restaurant, robot waiter, water and salad, four diners
- all of Febric's and Gladias's dialogue, word for word
- "Payment declined. Not enough funds."
- the reputation-backed loan: teaching assistant, positive review from the professor and 5 students, nullifier 0x18f4...60c5, 2773 zipcoins
- the payment: 10.5 zc base, 1.1 zc tax, 11.6 zc total

**Creative choices:**
- character faces, hair and clothes (the book only describes the robes, neck bands and watches)
- the robot design
- the zipcoin logo (the book doesn't describe one)
- the floating card style
- the robot handing Febric the tea (the book says "a waiter")
- fingertips tapping the circle (the book says he taps his watch)
- the whispered line to Emerald and the "Thank you" (not quoted in the book)
- the weather

## Credits
- Story, characters and world: *Snowmoon* by Vitalik Buterin (GPL v3)
- Adaptation, prompts and edit: [@zipcoin_eth](https://x.com/zipcoin_eth)
