# 1. Pelican on GitHub Pages, no CDN

Date: 2026-10-14. Status: accepted.

## Context

Aporia Barcelona needs a small public site: a home page and one page for each event. Three people edit it. Nobody wants to run a server.

## Decision

- A static site built with Pelican from Markdown, in a public repository on the personal account of David Arcos. Ubaldo and Rubén are collaborators with write access.
- GitHub Actions builds it and GitHub Pages serves it, at the apex `aporia.barcelona`, with HTTPS from GitHub (Let's Encrypt). GitHub redirects `www` to the apex.
- No CDN or proxy in front (no Cloudflare). The DNS stays at the registrar, Namecheap.

## Consequences

- No server, no hosting bill: the domain is the only cost.
- No edge rules: a redirect is a page in the site, and the response headers are the ones GitHub Pages sends.
- The repository is public because GitHub Pages on the free plan needs it. Nothing private goes into it (see AGENTS.md).
- A move to a GitHub organisation, if it comes, changes the Pages address in the `www` record and the domain verification (docs/edge.md).
