# aporia.barcelona

The website of Aporia Barcelona, a regular meetup: 8 to 12 people around a table, talking about AI and the future. Organised by David Arcos, Ubaldo Hervás, and Rubén.

Live at <https://aporia.barcelona>. A static site built with [Pelican](https://getpelican.com/) and served by GitHub Pages.

## Work on the site

You need [uv](https://docs.astral.sh/uv/) and `make`.

```sh
make setup    # once: create .venv with the toolchain that uv.lock pins
make serve    # build and serve at http://127.0.0.1:8000
make publish  # build with the production settings, as CI does
make lint     # ruff, and actionlint if you have it
```

The content is Markdown in `content/`: pages in `content/pages/`, one file per event in `content/eventos/` (from milestone 2). The HTML is in `theme/templates/`.

## Publish

A push to `main` is a release: the workflow in `.github/workflows/deploy.yml` builds the site and deploys it to GitHub Pages. A pull request is built and checked, and never deploys. To see a change before it is live, use `make serve` or open a pull request.

## Documentation

- [`AGENTS.md`](AGENTS.md): the rules for coding agents (and for people).
- [`docs/edge.md`](docs/edge.md): what serves the site and is not in this repository (the domain, the DNS, the GitHub Pages settings).
- [`docs/adr/`](docs/adr/): the decisions.

## Licence

The code is under the GPL-3.0 ([`LICENSE`](LICENSE)). The text and the images of the site are under CC BY-SA 4.0 ([`LICENSE-CONTENT`](LICENSE-CONTENT)).
