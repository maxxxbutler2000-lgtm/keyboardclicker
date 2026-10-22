# Keydrift Keyboard Clicker

A keyboard ASMR clicker with 38 illustrated keyboards, saved progress, ten levels per board, late-game rainbow waves, and a hidden developer panel.

## Play

Open the GitHub Pages link shown under this repository's Deployments or Settings → Pages. Tap **Enter the scrapyard** once to enable audio. Click, type, or choose Hover to earn coins.

Type `secretpanel` anywhere on the page for developer controls.

## Files

- `index.html`: ready-to-play website, with all keyboard images and audio embedded so it works at the GitHub Pages project URL.
- `editable-source.zip`: the full editable HTML, CSS, JavaScript, images, audio, and source credits.
- `build.py`: rebuilds the single-file website using Python 3; no dependencies required.

To edit: unzip `editable-source.zip` into this folder to create `source/`, change the files there, then run `python3 build.py`. Preview with `python3 -m http.server 8000`.

## Publishing

GitHub Pages is configured to deploy the `main` branch from `/ (root)`.

## Credits

Case illustrations were generated with OpenAI imagegen. Cherry MX Blue and NK Cream recordings are from Mechvibes (NK Cream originally by Ryan). Honey samples are from LuSrackhall's KeyTone honey ASMR pack, disclosed by its creator as AI-assisted audio. Full links are included in the game's footer and `source/assets/SOURCES.txt`.
