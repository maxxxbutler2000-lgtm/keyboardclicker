# Keydrift Keyboard Clicker

A keyboard ASMR clicker with 38 illustrated keyboards, ten levels per board, late-game rainbow waves, and cloud accounts.

## Play and accounts

[Open the hosted game with ChatGPT sign-in and database-backed saves](https://keydrift-asmr-mb.maxxxbutler2000.chatgpt.site/).

Sign in to save coins, unlocked keyboards, and levels across devices. Sign out in the Account menu. The first sign-in imports the current browser game; later sign-ins restore the cloud save. Conflicting saves let you choose which progress to keep. Access follows the hosted site's existing sharing settings.

GitHub Pages runs the static browser-only version. Its Cloud sign-in button opens the hosted game because Pages cannot run a server or database.

Tap **Enter the scrapyard** to enable audio, then click, type, or choose Hover. Type `secretpanel` anywhere for developer controls.

## Files and editing

- `index.html`: static game with all images and audio embedded.
- `editable-source.zip`: full frontend and account backend, schema, migrations, tests, and assets.
- `build.py`: rebuilds the static single-file game with Python 3.

Unzip `editable-source.zip` here to create `source/`, edit `source/public/`, then run `python3 build.py`. Preview with `python3 -m http.server 8000`. GitHub Pages deploys main from the repository root.

For the database-backed version, see `source/README.md`. It uses a Sites Worker with trusted ChatGPT identity headers and a D1 database. No passwords or credentials are stored in this repository. Applied database migrations must remain unchanged.

## Credits

Case illustrations were generated with OpenAI imagegen. Cherry MX Blue and NK Cream recordings are from Mechvibes (NK Cream originally by Ryan). Honey samples are from LuSrackhall's KeyTone honey ASMR pack, disclosed by its creator as AI-assisted audio. Links are in the game footer and `source/public/assets/SOURCES.txt`.
