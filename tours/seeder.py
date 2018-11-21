from django.utils.text import slugify
from faker import Faker
from tours.models import Tour
from orders.models import Order
from reviews.models import Review
from coupons.models import Coupon
import random


fake = Faker()


def generate_tour():
    title = fake.sentence()
    url = slugify(title)
    tour = Tour(title=title, url=url)
    tour.save()


def generate_order():
    all_tours = Tour.objects.all()
    random_tour = random.choice(all_tours)
    email = fake.profile()['mail']
    booking_reference = fake.word().upper()
    event_day = fake.date_this_year()
    people = random.randint(1, 10)
    status = random.choice(['c', 'p', 'o'])
    order = Order(
        tour=random_tour,
        email=email,
        booking_reference=booking_reference,
        event_day=event_day,
        people=people,
        status=status
    )
    order.save()


def generate_review():
    all_tours = Tour.objects.all()
    random_tour = random.choice(all_tours)
    rating = random.randint(1, 5)
    comment = fake.sentence()
    review = Review(
        tour=random_tour,
        rating=rating,
        comment=comment
    )
    review.save()


def generate_coupon():
    all_orders = Order.objects.all()
    random_order = random.choice(all_orders)
    code = fake.word().upper()
    discount = random.randint(0, 10) * 10
    coupon = Coupon(
        order=random_order,
        code=code,
        discount=discount
    )
    coupon.save()


def seed_data():
    for _ in range(2):
        generate_tour()
    for _ in range(2):
        generate_order()
    for _ in range(2):
        generate_review()
    for _ in range(2):
        generate_coupon()
        