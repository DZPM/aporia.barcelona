# AGENTS.md

For coding agents. The [`README.md`](README.md) explains how the site works: where each text lives, how to add an event or a person, the `make` targets, and what a push to `main` does (it is a release). Read it first, then:

- [`docs/adr/`](docs/adr/): the decisions. A change that goes against one needs a new ADR, not a quiet exception.
- [`docs/edge.md`](docs/edge.md): what lives outside the repository. A change in the DNS or in the GitHub Pages settings goes into it, in the same commit as its reason.

## Words

- **Event**: one meetup, and its page: a Markdown file in `content/eventos/` (docs/adr/0002). Its `Date` is the day of the meetup.
- **Person**: an organiser or a guest: a Markdown file in `content/personas/`, shown inside the home page and nowhere else (docs/adr/0003).

## Before you call a change done

- Run `make publish` and `make lint`. CI fails on any Pelican warning.
- Do not push to `main` to see a change: that publishes it. Use `make serve`, or open a pull request.

## Do not

- Add the name, photo, or contact of an attendee or a guest without their permission. The attendee list never enters the repository: it is public.
- Commit a draft: an Event or a Person enters the repository when it is ready to publish.
- Rename the file or change the `Slug` of a published Event: its address is shared.
- Add a dependency, a service, or a third-party script without a reason in the commit message. The stack stays small on purpose (ADR 0001).
- Translate the content: the site is in Spanish. Code, comments, docs, ADRs, and commit messages are in English.
