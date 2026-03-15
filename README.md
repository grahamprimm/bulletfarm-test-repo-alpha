# bulletfarm-test-repo-alpha
Test repository for bulletfarm agent operator (alpha)

## API Documentation
## API Pagination

The API supports cursor-based pagination for endpoints that return lists of items. Use the following query parameters to paginate through the results:

- `page`: The page number to retrieve (default is 1).
- `per_page`: The number of items to return per page (default is 10).

### Example Request
```
GET /api/items?page=2&per_page=5
```
This request retrieves the second page of items, with 5 items per page.
