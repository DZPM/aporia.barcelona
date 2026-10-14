# The edge: what lives outside the repository

Everything that serves the site and is not in this repository, written down so it can be checked and rebuilt. Kept current: a change here is a change to this file in the same commit as the reason. Decision behind it: docs/adr/0001.

## Registrar

| Item | Value |
|---|---|
| Registrar | Namecheap, account of David Arcos. Registered 2026-10-14 |
| Nameservers | Namecheap BasicDNS (`dns1.registrar-servers.com`, `dns2.registrar-servers.com`) |
| Auto renew, registrar lock | to confirm |
| Mail | none, decided 2026-10-14. The domain came with Namecheap email forwarding (MX `eforward1` to `eforward5.registrar-servers.com`, SPF TXT at `@`); those records go |

## DNS records at Namecheap

| Host | Type | Value |
|---|---|---|
| `@` | A | `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` |
| `@` | AAAA | `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153` |
| `www` | CNAME | `dzpm.github.io.` |
| `_github-pages-challenge-dzpm` | TXT | the value GitHub shows when the domain is added to the account's verified domains (account Settings, Pages). Keep it: with the domain verified, no other GitHub account can claim `aporia.barcelona` or a subdomain for its own Pages site |

Every record uses the TTL Namecheap calls Automatic. Nothing else. The parking records that Namecheap creates with a new domain are removed.

## GitHub Pages

- Repository `DZPM/aporia.barcelona`, public. Source: GitHub Actions, the workflow in `.github/workflows/deploy.yml`, from `main`.
- Custom domain `aporia.barcelona` (the apex is the canonical address; GitHub redirects `www` to it), set in the repository settings (Settings, Pages). The domain is verified for the account (`protected_domain_state: verified`, 2026-10-14). The certificate must cover `www` too: GitHub asks for it only if the `www` record exists when the custom domain is saved, so after a change to `www`, remove the custom domain and save it again. With a deploy from Actions, GitHub ignores a `CNAME` file, so the repository has none.
- Enforce HTTPS: on since 2026-10-14. The Let's Encrypt certificate covers `aporia.barcelona` and `www.aporia.barcelona` (first one expires 2027-01-12; GitHub renews it).

## Check

```sh
dig +short aporia.barcelona A
dig +short aporia.barcelona AAAA
dig +short www.aporia.barcelona CNAME
curl -sI http://aporia.barcelona/ | head -1        # 301 to https
curl -sI https://www.aporia.barcelona/ | head -1   # 301 to the apex
curl -s https://aporia.barcelona/ | grep -c "<h1>"
```
