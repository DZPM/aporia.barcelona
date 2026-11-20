# aporia.barcelona

The website of Aporia Barcelona, a regular meetup in Barcelona. Organised by Ubaldo Hervás, Rubén Orta, and David Arcos.

Live at <https://aporia.barcelona>. A static site built with [Pelican](https://getpelican.com/) and served by GitHub Pages.

## Work on the site

You need [uv](https://docs.astral.sh/uv/) and `make`.

```sh
make setup    # once: create .venv with the toolchain that uv.lock pins
make serve    # build and serve at http://127.0.0.1:8002
make publish  # build with the production settings, as CI does
make lint     # ruff, and actionlint if you have it
```

The content is Markdown in `content/`, in Spanish:

- `content/pages/index.md`: the text of the home page. The home page then lists the events and the people.
- `content/eventos/NN-slug.md`: one file per event, at `/eventos/NN-slug/` (docs/adr/0002).
- `content/personas/<slug>.md`: one file per person, organiser or guest, shown inside the home page (docs/adr/0003). Photos go in `content/images/personas/`.

The HTML is in `theme/templates/`, the stylesheet in `theme/static/css/style.css`, and the icons in `content/extra/`. Every page has the tags that X, LinkedIn, and WhatsApp read for a link preview (`theme/templates/_share.html`); an event uses its title, `Tema`, and `Summary`. The preview image is `content/extra/og.png`, made from `tools/og-card.html`.

## Add an event

Create `content/eventos/NN-slug.md`, with the next number and a short slug:

```markdown
Title: Aporia #NN: the title of the meetup
Slug: NN-slug
Date: 2026-11-26 19:00
Hora: 19:00
Tema: the topic
Foto: images/eventos/NN-slug.webp
Enlaces: Ubaldo, linkedin, https://www.linkedin.com/posts/...
    Ubaldo, x, https://x.com/...
Summary: One sentence; search engines show it.

The question of the meetup, in one paragraph.
```

`Slug` is the file name without `.md`. `Tema` goes in the title of the event page, after the number. `Enlaces` lists posts about the meetup, one per line as "who, network, URL" (the network is `linkedin`, `x`, `bluesky`, or `github`, the keys of `PERSONA_LINKS` in `pelicanconf.py`; the next lines start with four spaces). They show at the end of the page under "Enlaces", each with its icon and a text such as "Ubaldo en LinkedIn". Leave the field out when there is none. There is no place field: the place is private, and only the guests get it. `Date` is the day and time of the meetup. After the meetup, add what was said, without the names of attendees unless they agree. Look at it with `make serve` before you push: a push to `main` publishes it.

## Publish a meetup photo

The original photo of a meetup is never published, and never enters this repository: the repository is public, and git keeps every file it has ever had. Only a pixelated version is published, made with one treatment for the whole image (no region is treated apart).

1. Keep the original outside the repository (David keeps them in `~/Pictures/Aporia Barcelona/`).
2. Make the published version:

    ```sh
    make photo ORIGINAL="/path/to/original.jpg" OUT=content/images/eventos/NN-slug.webp
    ```

    It runs `tools/pixelate_photo.py`, with Pillow from the `photo` dependency group. The script refuses an original inside the repository, and writes no metadata.
3. Look at the result at the width of the page (`make serve`). The rule: common traits may show (a bald head, glasses, curly hair), but nobody is recognisable at a glance.
4. Put it in the event, after the first line of the recap, with the size the script prints:

    ```markdown
    ![Ocho personas alrededor de una mesa con bebidas, en una foto pixelada]({static}/images/eventos/NN-slug.webp){: .pixelada width="1200" height="672" }
    ```

    The `pixelada` class keeps the blocks hard when the browser scales the image.
5. Set `Foto: images/eventos/NN-slug.webp` in the event: the home page shows it in the event's card, next to the title and the date. An event with no photo gets an empty frame.

### Defaults

| Setting | Default | What it does |
|---|---|---|
| `BLUR` (`--blur`) | `6` | Gaussian blur in px, on the whole photo scaled to 1600 px wide, before the pixelation |
| `COLS` (`--cols`) | `100` | Blocks across: 16 px blocks at 1600 px, a grid of 100 x 56 for a 16:9 photo |
| Output | 12 px per block | 1200 x 672 for a 16:9 photo, lossless WebP, about 17 KB: it can be shared as it is |

These are the settings of Aporia #01 (2026-11-20). A later photo can use others (`make photo ... BLUR=10`, or `COLS=80` for larger blocks); say which in the commit message. More blur or fewer columns hide more.

## Add a person

Create `content/personas/<slug>.md`:

```markdown
Title: Name Surname
Rol: organizador
Orden: 1
Foto: images/personas/<slug>.jpg
Web:
LinkedIn:
X:
Bluesky:
GitHub:

One or two sentences about the person.
```

`Rol` is `organizador` or `invitado`. Leave a link empty to hide it. `Orden` sorts each group (docs/adr/0003).

## Publish

A push to `main` is a release: the workflow in `.github/workflows/deploy.yml` builds the site and deploys it to GitHub Pages. A pull request is built and checked, and never deploys. To see a change before it is live, use `make serve` or open a pull request.

## Documentation

- [`AGENTS.md`](AGENTS.md): the rules for coding agents (and for people).
- [`docs/edge.md`](docs/edge.md): what serves the site and is not in this repository (the domain, the DNS, the GitHub Pages settings).
- [`docs/adr/`](docs/adr/): the decisions.

## Licence

The code is under the GPL-3.0 ([`LICENSE`](LICENSE)). The text and the images of the site are under CC BY-SA 4.0 ([`LICENSE-CONTENT`](LICENSE-CONTENT)), except the photos of the people in `content/images/personas/`: they belong to each person, and are here with their permission.
