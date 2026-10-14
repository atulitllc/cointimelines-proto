# CryptoHistoryBook (prototype)
Static crypto history site. Planned domain cryptohistorybook.com (not bought). Served from GitHub Pages `/docs`.
- `fetch_prices.py`, `stitch.py`: fetch daily closes (Bitstamp, Coinbase Exchange, Binance public APIs) into `data/`.
- `content.py`, `articles.py`: events and articles with sources.
- `build.py`: builds `docs/`. `INDEXABLE = False` keeps every page noindex, robots disallow, no sitemap. `build-report.json` holds the per page thin-page gate.
