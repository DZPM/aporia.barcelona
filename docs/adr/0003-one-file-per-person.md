# 3. One file per person, shown inside the home page

Date: 2026-10-15. Status: accepted.

## Context

The home page presents the organisers, and later the guests of each meetup. Each one has a name, a photo, a short text, and some links, and each one should be able to edit their own.

## Decision

- A Person is one Markdown file, `content/personas/<slug>.md`. The frontmatter holds `Title` (the name), `Rol` (`organizador` or `invitado`), `Orden`, `Foto`, and the links (`Web`, `LinkedIn`, `X`, `Bluesky`, `GitHub`). The body is the short text.
- A Person has no page of its own. The home page shows the organisers under "Sobre nosotros" and the guests under "Invitados", each group sorted by `Orden`, as cards: the photo, the name linked to `Web`, and the other links as icons under it.
- The photo is a file in `content/images/personas/`, square, 320 px (shown at 160); `Foto` is its path from `content/`, for example `images/personas/david-arcos.jpg`.

## Consequences

- To add, change, or remove a person is to edit one file; the templates do not change.
- `Orden` is compared as text: use one digit for the organisers and two digits from 10 for the guests, so that 10 does not come before 2.
- A guest gets a file only with their permission (AGENTS.md).
