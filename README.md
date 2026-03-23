# Fleet Data API

RESTful API built with FastAPI to manage and analyze fleet operation data.

## Features
- Create and retrieve trips
- Store data in PostgreSQL
- Calculate fleet metrics (total distance, idle distance)

## Tech Stack
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy

## Example

```json
{
  "truck_id": 1,
  "distance": 120,
  "productive": true
}
