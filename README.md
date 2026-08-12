# Simple Commerce Backend

Educational Django + Django REST Framework project for learning basic backend concepts: models, serializers, viewsets, JWT auth, and a simple e-commerce flow (catalog, cart, and checkout).

## Stack

- Python 3.12+
- Django 6
- Django REST Framework
- SimpleJWT (authentication)
- Pillow (image uploads)
- SQLite (default database)
- [uv](https://docs.astral.sh/uv/) for dependency management

## Project structure

| App | Purpose |
| --- | --- |
| `shop` | Member registration/login and shop banners |
| `catalog` | Categories and products |
| `sale` | Cart, cart items, and order/payment submission |
| `simple_commerce_backend` | Project settings and root URL config |

## API overview

Base URL (local): `http://127.0.0.1:8000`

| Method | Endpoint | Description |
| --- | --- | --- |
| `POST` | `/api/shop/register/` | Register a member |
| `POST` | `/api/shop/login/` | Login and obtain JWT tokens |
| `GET` | `/api/shop/banner/` | List banners |
| `GET` | `/api/catalog/product/` | List products (paginated) |
| `GET` | `/api/catalog/product/{id}/` | Product detail |
| `POST` | `/api/sale/add-cart-item/` | Add item to cart (auth required) |
| `GET` | `/api/sale/cart-detail/` | View current cart (auth required) |
| `POST` | `/api/sale/submit-payment/` | Submit payment / create order (auth required) |
| — | `/api/admin/` | Django admin |

Protected endpoints expect:

```http
Authorization: Bearer <access_token>
```

## Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) installed
- Python 3.12 or newer (uv can install it for you)

## Install dependencies with uv

From the project root:

```bash
# Create a virtual environment and install dependencies from pyproject.toml / uv.lock
uv sync
```

This creates `.venv` and installs:

- Django
- djangorestframework
- djangorestframework-simplejwt
- Pillow

To add a new package later:

```bash
uv add <package-name>
```

## Run the project

1. Apply migrations:

```bash
uv run python manage.py migrate
```

2. (Optional) Create an admin user for `/api/admin/`:

```bash
uv run python manage.py createsuperuser
```

3. Start the development server:

```bash
uv run python manage.py runserver
```

The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Learning notes

This project is intentionally small so you can focus on:

- Splitting domain logic across Django apps (`shop`, `catalog`, `sale`)
- Serializers and generic API views / viewsets
- JWT authentication with SimpleJWT
- One-to-one and foreign-key relationships (Member ↔ User, Cart ↔ CartItem, Order ↔ OrderItem)
- File uploads (product images, payment slips, banners)

Not intended for production use as-is (debug mode, long-lived JWT settings, and insecure defaults are fine for learning only).
