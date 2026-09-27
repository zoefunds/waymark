# Integration

1. Register a capability with a stable key and version.
2. Read `get_definition_hash()` and pin it in the consumer configuration.
3. Call `route(request_id, request)` once.
4. After finalization, call `get_route(request_id)` and require `status == FINAL` and the expected definition hash.

Never consume an unknown route, silently accept a changed catalog, or treat a failed consensus transaction as a negative route.
