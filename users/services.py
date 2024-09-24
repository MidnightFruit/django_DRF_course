from audioop import reverse

import stripe
from config.settings import STRIPE_KEY
from materials.models import Course


def create_price(price, product:stripe.Product):
    stripe.api_key = STRIPE_KEY
    return stripe.Price.create(
        currency="rub",
        unit_amount=price * 100,
        product=product.get("id"),
    )


def create_product(course: Course):
    stripe.api_key = STRIPE_KEY
    return stripe.Product.create(name=course.name)


def create_payment(price: stripe.Price):
    stripe.api_key = STRIPE_KEY
    return stripe.checkout.Session.create(
        success_url=reverse('materials:courses_list'),
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )