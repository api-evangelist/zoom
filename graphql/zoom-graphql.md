# Zoom GraphQL Schema

## Description

Zoom does not currently offer a native public GraphQL API. All programmatic access to Zoom's platform is provided through its REST APIs available at `https://api.zoom.us/v2`. This GraphQL schema is a conceptual representation derived from the Zoom REST API surface, covering the core object types and their relationships across meetings, webinars, users, recordings, chat, reporting, and telephony.

The schema is intended to assist developers in understanding the Zoom data model, generating typed clients, building schema-stitching gateways over the REST API, or prototyping GraphQL wrappers using tools such as GraphQL Mesh, Hasura, or StepZen.

## Endpoint

No public GraphQL endpoint exists. This schema is conceptual.

## Docs

- Developer Portal: https://developers.zoom.us/
- REST API Reference: https://developers.zoom.us/docs/api/
- Meeting API: https://developers.zoom.us/docs/api/rest/meeting/
- User API: https://developers.zoom.us/docs/api/rest/user/
- Account API: https://developers.zoom.us/docs/api/rest/account/
- Recording API: https://developers.zoom.us/docs/video-sdk/web/recording/
- Chat API: https://developers.zoom.us/docs/api/rest/chat-api/
- Webinar API: https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#tag/Webinars
- Phone API: https://developers.zoom.us/docs/api/phone/
- Reports API: https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#tag/Reports

## Note

This schema is **conceptual**. It was derived from Zoom's published REST API documentation and OpenAPI specifications. Type names, field names, and relationships follow conventions observed in the Zoom REST API response bodies. No official Zoom GraphQL endpoint backs this schema.
