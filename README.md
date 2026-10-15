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

The HTML is in `theme/templates/`, the stylesheet in `theme/static/css/style.css`, and the icons in `content/extra/`.

## Add an event

Create `content/eventos/NN-slug.md`, with the next number and a short slug:

```markdown
Title: Aporia #NN: the title of the meetup
Slug: NN-slug
Date: 2026-11-26 19:00
Hora: 19:00
Lugar: the place
Summary: One sentence; search engines show it.

The question of the meetup, in one paragraph.
```

`Slug` is the file name without `.md`. `Date` is the day and time of the meetup. After the meetup, add what was said, without the names of attendees unless they agree. Look at it with `make serve` before you push: a push to `main` publishes it.

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
