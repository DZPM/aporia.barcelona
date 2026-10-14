# AGENTS.md

For coding agents. The [`README.md`](README.md) explains how the site works: the `make` targets, and what a push to `main` does (it is a release). Read it first, then:

- [`docs/adr/`](docs/adr/): the decisions. A change that goes against one needs a new ADR, not a quiet exception.
- [`docs/edge.md`](docs/edge.md): what lives outside the repository. A change in the DNS or in the GitHub Pages settings goes into it, in the same commit as its reason.

## Before you call a change done

- Run `make publish` and `make lint`. CI fails on any Pelican warning.
- Do not push to `main` to see a change: that publishes it. Use `make serve`, or open a pull request.

## Do not

- Add the name, photo, or contact of an attendee without their permission. The attendee list never enters the repository: it is public.
- Add a dependency, a service, or a third-party script without a reason in the commit message. The stack stays small on purpose (ADR 0001).
- Translate the content: the site is in Spanish. Code, comments, docs, ADRs, and commit messages are in English.
