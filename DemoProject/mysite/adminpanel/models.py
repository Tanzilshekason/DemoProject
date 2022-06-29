from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import truncatechars
from django.utils.safestring import mark_safe

# Create your models here.

class User_info(models.Model):
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
        verbose_name = 'user_info'
        verbose_name_plural = 'user_info'


class User_wish_list(models.Model):
    user_id = models.ForeignKey(User_info, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=100)

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = 'user_wish_list'
        verbose_name_plural = 'user_wish_list'


class User_address(models.Model):
    user_id = models.ForeignKey(User_info, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    zipcode = models.CharField(max_length=45)

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name = 'user_address'
        verbose_name_plural = 'user_address'


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


class Coupons_used(models.Model):
    user_id = models.IntegerField()
    order_id = models.IntegerField()
    created_date = models.DateField()
    coupon_id = models.ForeignKey(Coupon, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'coupon_used'
        verbose_name_plural = 'coupon_used'


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


class Contact_us(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45,unique=True)
    contact_no = models.CharField(max_length=45)
    message = models.TextField()
    note_adm = models.TextField()
    created_by = models.IntegerField()
    created_date = models.DateField()
    modify_by = models.IntegerField()
    modify_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact_us'
        verbose_name_plural = 'contact_us'


class Banners(models.Model):
    banner_path = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    images = models.ImageField()

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


class Email_template(models.Model):
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
        verbose_name = 'email_template'
        verbose_name_plural = 'email_template'

class Category(models.Model):
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

class Sub_Category(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'sub_category'
        verbose_name_plural = 'sub_category'

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brand'


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=False,default='')
    sub_category = models.ForeignKey(Sub_Category,on_delete=models.CASCADE,null=False,default='')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,)
    sku = models.CharField(max_length=45)
    shor_description = models.CharField(max_length=100)
    long_description = models.TextField()
    price = models.FloatField()
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




class Product_category(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'product_category'
        verbose_name_plural = 'product_category'


class Product_images(models.Model):
    image_name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created_by = models.IntegerField()
    created_date = models.DateField()
    modify_by = models.IntegerField()
    modify_date = models.DateField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_image = models.ImageField()

    def __str__(self):
        return self.image_name

    class Meta:
        verbose_name = 'Product_images'
        verbose_name_plural = 'Product_images'

    @property
    def short_description(self):
        return truncatechars(self.description, 20)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.product_image.url))

    admin_photo.short_description = 'Product_image'
    admin_photo.allow_tags = True


class Order_details(models.Model):
    order_id = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    amount = models.FloatField()

    class Meta:
        verbose_name = 'order_details'
        verbose_name_plural = 'order_details'


class Payment_gateway(models.Model):
    name = models.CharField(max_length=45)
    created_by = models.IntegerField()
    created_date = models.DateField()
    modify_by = models.IntegerField()
    modify_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'payment_gateway'
        verbose_name_plural = 'payment_gateway'


class User_order(models.Model):
    user_id = models.ForeignKey(User_info, on_delete=models.CASCADE)
    shipping_method = models.IntegerField()
    AWB_No = models.CharField(max_length=100)
    payment_gateway_id = models.ForeignKey(Payment_gateway, on_delete=models.CASCADE)
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
        verbose_name = 'user_order'
        verbose_name_plural = 'user_order'



class Product_attributes(models.Model):
    name = models.CharField(max_length=45)
    created_by = models.IntegerField()
    created_date = models.DateField()
    modified_by = models.IntegerField()
    modified_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product_attributes'
        verbose_name_plural = 'product_attributes'



class Product_attribute_value(models.Model):
    product_attribute = models.ForeignKey(Product_attributes, on_delete=models.CASCADE)
    attribute_value = models.CharField(max_length=45)
    created_by = models.IntegerField()
    created_date = models.DateField()
    modified_by = models.IntegerField()
    modified_date = models.DateField()

    def __str__(self):
        return self.attribute_value

    class Meta:
        verbose_name = 'product_attribute_value'
        verbose_name_plural = 'product_attribute_value'



class Product_attribute_assoc(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_attribute_id = models.ForeignKey(Product_attributes, on_delete=models.CASCADE)
    product_attribute_value_id = models.IntegerField()

    class Meta:
        verbose_name = 'product_attribute_assoc'
        verbose_name_plural = 'product_attribute_assoc'

# Model for USER
class User(AbstractUser):
    is_admin = models.BooleanField('Is admin',default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_manager = models.BooleanField('Is manager', default=False)


# Model for CRUD operations
class Manage_user(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100,unique=True)
    address = models.TextField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name

class User_login(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User_login'
        verbose_name_plural = 'User_login'

class User_register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User_register'
        verbose_name_plural = 'User_register'



