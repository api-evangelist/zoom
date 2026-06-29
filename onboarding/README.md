# Programmatic API Onboarding — Zoom

A single-file, zero-dependency Node.js (18+) CLI that reproduces SoundCloud's
`sc-api-auth.mjs` pattern for Zoom: register an application / obtain credentials
programmatically instead of clicking through a dashboard, so agents and developers
can onboard at the command line.

- Script: [`zoom-api-auth.mjs`](zoom-api-auth.mjs)
- Run `node zoom-api-auth.mjs --help` for usage and the required environment variables.
- Story / rationale: https://apievangelist.com/2026/08/31/zoom-server-to-server-oauth-is-headless/

Part of the API Evangelist "Programmatic API Onboarding for the Agentic Moment" series.
