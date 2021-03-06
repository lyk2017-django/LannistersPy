from django.db import models
import uuid
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser
from django.contrib.staticfiles.templatetags.staticfiles import static


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True)
    price = models.FloatField(blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="uploaded")
    product_home = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=False)

    class Meta:
        get_latest_by = "name"
        unique_together = ("name", "brand")

    def __str__(self):
        return "{name}".format(name=self.name)

    def get_image_url(self):
        if not self.image:
            return static("img/itugnu.png")
        else:
            return self.image.url


def uuid_generator8():
    code = uuid.uuid4().hex
    return code[:8]


def uuid_generator16():
    code = uuid.uuid4().hex
    return code[:16]


class UserCard(models.Model):
    card_number = models.CharField(max_length=16, default=uuid_generator16, unique=True)
    balance = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "{card_number}".format(card_number=self.card_number[0:4]+"-"+self.card_number[4:8]+"-"+self.card_number[8:12]+"-"+self.card_number[12:16])


class PrepaidCard(models.Model):
    barcode = models.CharField(max_length=8, default=uuid_generator8, unique=True)
    value = models.PositiveIntegerField()
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return "{barcode}".format(barcode=self.barcode)


class Vendor(models.Model):
    location = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True, upload_to="uploaded")
    address = models.CharField(max_length=150, null=True)

    def __str__(self):
        return "{location}".format(location=self.location)

    def get_image_url(self):
        if not self.image:
            return static("img/itugnu.png")
        else:
            return self.image.url


class Inventory(models.Model):
    vendor = models.ForeignKey(Vendor)
    product = models.ForeignKey(Product)
    count = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("product", "vendor")

    def __str__(self):
        return "{vendor} -> {product} #{count}".format(vendor=self.vendor, product=self.product, count=self.count)


@receiver(pre_save, sender=Product)
def generate_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        if hasattr(sender, "name"):
            instance.slug = slugify(instance.name)
        else:
            raise AttributeError("Name field is required for slug.")
    return instance


class ExtendedUser(AbstractUser):
    card = models.OneToOneField(UserCard, null=True)


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    product = models.ForeignKey(Product)
    author = models.ForeignKey(ExtendedUser, blank=False, null=True)

    def __str__(self):
        return "{message}".format(message=self.message)


class Transaction(models.Model):
    prepaid_card = models.ForeignKey(PrepaidCard)
    user_card = models.ForeignKey(UserCard)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = "date"

    def __str__(self):
        return "{prepaid} -> {user}".format(prepaid=self.prepaid_card, user=self.user_card)
