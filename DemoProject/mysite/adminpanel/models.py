from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import truncatechars
from django.utils.safestring import mark_safe
import datetime
# Create your models here.

class Userinfo(models.Model):
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)
    status = models.BooleanField(default=True)
    created_date = models.DateField()
    fb_token = models.CharField(max_length=100)
    twitter_token = models.CharField(max_length=100)
    google_token = models.CharField(max_length=100)
    registration_method = models.BooleanField(default=False)

    def __str__(self):
        return self.firstname

    class Meta:
        verbose_name = 'userinfo'
        verbose_name_plural = 'userinfo'


class UserWishList(models.Model):
    user_id = models.ForeignKey(Userinfo, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=100)

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = 'user wish list'
        verbose_name_plural = 'user wish list'


class UserAddress(models.Model):
    user_id = models.ForeignKey(Userinfo, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    zipcode = models.CharField(max_length=45)

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name = 'user Address'
        verbose_name_plural = 'user Address'


class Coupon(models.Model):
    code = models.CharField(max_length=45)
    percent_off = models.FloatField()
    created_by = models.IntegerField()
    created_date = models.DateField()
    modify_by = models.IntegerField()
    modify_date = models.DateField()
    no_of_uses = models.IntegerField()

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'coupon'
        verbose_name_plural = 'coupon'


class CouponsUsed(models.Model):
    user_id = models.IntegerField()
    order_id = models.IntegerField()
    created_date = models.DateField()
    coupon_id = models.ForeignKey(Coupon, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'coupon Used'
        verbose_name_plural = 'coupon Used'


class Cms(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    meta_title = models.TextField()
    meta_description = models.TextField()
    meta_keywords = models.TextField()
    created_by = models.IntegerField()
    created_date = models.DateField()
    modify_by = models.IntegerField()
    modify_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'cms'
        verbose_name_plural = 'cms'


class Configuration(models.Model):
    conf_key = models.CharField(max_length=45)
    conf_value = models.CharField(max_length=100)
    created_by = models.IntegerField()
    created_date = models.DateField()
    modify_by = models.IntegerField()
    modify_date = models.DateField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.conf_key

    class Meta:
        verbose_name = 'configuration'
        verbose_name_plural = 'configuration'


class Contactus(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45,unique=True)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    # contact_no = models.CharField(max_length=45)
    # note_adm = models.TextField()
    # created_by = models.IntegerField()
    # created_date = models.DateField()
    # modify_by = models.IntegerField()
    # modify_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contactus'
        verbose_name_plural = 'contactus'


class Banners(models.Model):
    banner_path = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    images = models.ImageField(upload_to='media')

    def __str__(self):
        return self.banner_path

    class Meta:
        verbose_name = 'banners'
        verbose_name_plural = 'banners'

    @property
    def short_description(self):
        return truncatechars(self.description, 20)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.images.url))
    admin_photo.short_description = 'Images'
    admin_photo.allow_tags = True


class EmailTemplate(models.Model):
    title = models.CharField(max_length=45)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    created_by = models.IntegerField()
    created_date = models.DateField()
    modify_by = models.IntegerField()
    modify_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'email template'
        verbose_name_plural = 'email template'

class Categorys(models.Model):
    name = models.CharField(max_length=100)
    parent_id = models.IntegerField()
    created_by = models.IntegerField()
    created_date = models.DateField()
    modify_by = models.IntegerField()
    modify_date = models.DateField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'category'

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Categorys,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategory'

class Brands(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'brands'
        verbose_name_plural = 'brands'


class FilterPrices(models.Model):
    FILTER_PRICE = (
        ('100 TO 199','100 TO 199'),
        ('200 TO 299','200 TO 299'),
        ('300 TO 399', '300 TO 399'),
        ('400 TO 499', '400 TO 499'),
        ('500 TO 600', '500 TO 600'),
    )
    price = models.CharField(choices=FILTER_PRICE,max_length=60)

    def __str__(self):
        return self.price

class Products(models.Model):
    Availability = (('In Stock','In Stock'),('Out Of Stock','Out Of Stock'))

    category = models.ForeignKey(Categorys,on_delete=models.CASCADE,null=False,default='')
    sub_category = models.ForeignKey(Subcategory,on_delete=models.CASCADE,null=False,default='')
    brand = models.ForeignKey(Brands,on_delete=models.CASCADE,null=False,default='')
    name = models.CharField(max_length=100,)
    sku = models.CharField(max_length=45)
    shor_description = models.CharField(max_length=100)
    long_description = models.TextField()
    price = models.CharField(max_length=10000)
    special_price = models.FloatField()
    special_price_from = models.DateField()
    special_price_to = models.DateField()
    status = models.BooleanField(default=True)
    quantity = models.IntegerField()
    meta_title = models.CharField(max_length=45)
    meta_description = models.TextField()
    meta_keywords = models.TextField()
    status1 = models.BooleanField(default=True)
    created_by = models.IntegerField()
    created_date = models.DateField()
    modify_by = models.IntegerField()
    modify_date = models.DateField()
    is_featured = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media/photos')
    filter_price = models.ForeignKey(FilterPrices,on_delete=models.CASCADE,null=False,default='')
    Availability = models.CharField(choices=Availability,null=True,max_length=100)



    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'product'

    @property
    def short_description(self):
        return truncatechars(self.short_description,20)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

    def __str__(self):
        return self.name

class Images(models.Model):
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey(Products,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'images'
        verbose_name_plural = 'images'

    @property
    def short_description(self):
        return truncatechars(self.short_description, 20)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    admin_photo.short_description = 'Images'
    admin_photo.allow_tags = True


class ProductCategory(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Categorys, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'product Category'
        verbose_name_plural = 'product Category'


class ProductImages(models.Model):
    image_name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created_by = models.IntegerField()
    created_date = models.DateField()
    modify_by = models.IntegerField()
    modify_date = models.DateField()
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to="media/photos/images")

    def __str__(self):
        return self.image_name

    class Meta:
        verbose_name = 'Product Images'
        verbose_name_plural = 'Product Images'

    @property
    def short_description(self):
        return truncatechars(self.description, 20)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.product_image.url))

    admin_photo.short_description = 'Product_image'
    admin_photo.allow_tags = True


class OrderDetails(models.Model):
    order_id = models.IntegerField()
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    amount = models.FloatField()

    class Meta:
        verbose_name = 'order Details'
        verbose_name_plural = 'order Details'


class PaymentGateway(models.Model):
    name = models.CharField(max_length=45)
    created_by = models.IntegerField()
    created_date = models.DateField()
    modify_by = models.IntegerField()
    modify_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'payment Gateway'
        verbose_name_plural = 'payment Gateway'


class UserOrder(models.Model):
    user_id = models.ForeignKey(Userinfo, on_delete=models.CASCADE)
    shipping_method = models.IntegerField()
    AWB_No = models.CharField(max_length=100)
    payment_gateway_id = models.ForeignKey(PaymentGateway, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    created_date = models.DateField()
    status = models.IntegerField()
    grand_total = models.FloatField()
    shipping_charges = models.FloatField()
    coupon_id = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    billing_address1 = models.CharField(max_length=100)
    billing_address2 = models.CharField(max_length=100)
    billing_city = models.CharField(max_length=45)
    billing_state = models.CharField(max_length=45)
    billing_country = models.CharField(max_length=45)
    billing_zipcode = models.CharField(max_length=45)
    shipping_address1 = models.CharField(max_length=100)
    shipping_address2 = models.CharField(max_length=100)
    shipping_city = models.CharField(max_length=45)
    shipping_state = models.CharField(max_length=45)
    shipping_country = models.CharField(max_length=45)
    shipping_zipcode = models.CharField(max_length=45)

    def __str__(self):
        return self.billing_address1

    class Meta:
        verbose_name = 'user Order'
        verbose_name_plural = 'user Order'



class ProductAttributes(models.Model):
    name = models.CharField(max_length=45)
    created_by = models.IntegerField()
    created_date = models.DateField()
    modified_by = models.IntegerField()
    modified_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product Attributes'
        verbose_name_plural = 'product Attributes'



class ProductAttributeValue(models.Model):
    product_attribute = models.ForeignKey(ProductAttributes, on_delete=models.CASCADE)
    attribute_value = models.CharField(max_length=45)
    created_by = models.IntegerField()
    created_date = models.DateField()
    modified_by = models.IntegerField()
    modified_date = models.DateField()

    def __str__(self):
        return self.attribute_value

    class Meta:
        verbose_name = 'product Attribute Value'
        verbose_name_plural = 'product Attribute Value'



class ProductAttributeAssoc(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    product_attribute_id = models.ForeignKey(ProductAttributes, on_delete=models.CASCADE)
    product_attribute_value_id = models.IntegerField()

    class Meta:
        verbose_name = 'product Attribute Assoc'
        verbose_name_plural = 'product Attribute Assoc'

# Model for USER
class User(AbstractUser):
    is_admin = models.BooleanField('Is admin',default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_manager = models.BooleanField('Is manager', default=False)


# Model for CRUD operations
class ManageUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100,unique=True)
    address = models.TextField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'manage User'
        verbose_name_plural = 'manage User'

class UserLogin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User Login'
        verbose_name_plural = 'User Login'

class UserRegister(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User Register'
        verbose_name_plural = 'User Register'


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postcode = models.IntegerField()
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    amount = models.CharField(max_length=1000)
    payment_id = models.CharField(max_length=300,null=True,blank=True)
    paid = models.BooleanField(default=False,null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Order'

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/photos')
    quantity = models.CharField(max_length=20)
    price = models.CharField(max_length=50)
    total = models.CharField(max_length=1000)

    @property
    def short_description(self):
        return truncatechars(self.short_description, 20)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

    def __str__(self):
        return self.order.user.username



