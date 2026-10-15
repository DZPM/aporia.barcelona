# 2. One page per event, at /eventos/NN-slug/

Date: 2026-10-15. Status: accepted.

## Context

Each meetup needs a stable address: to share before the meetup, and to keep what was said after it.

## Decision

- An Event is a Pelican article: one Markdown file, `content/eventos/NN-slug.md`, served at `/eventos/NN-slug/`. `NN` is the number of the meetup, with two digits (`01`, `02`), the same number as in its title ("Aporia #01").
- The `Date` of an Event is the day and time of the meetup, not the day the page was written. The home page lists the events by that date, newest first.
- No drafts in the repository: the repository is public, so an Event enters it when it is ready to publish. The template is in the README.

## Consequences

- The address never changes once published: do not rename the file or change the `Slug` of a published Event.
- No categories, tags, or authors: the site has one kind of content.
