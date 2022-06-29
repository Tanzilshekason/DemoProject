from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import truncatechars
from django.utils.safestring import mark_safe

# Create your models here.

class userinfo(models.Model):
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


class userwishlist(models.Model):
    user_id = models.ForeignKey(userinfo, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=100)

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = 'user wish list'
        verbose_name_plural = 'user wish list'


class useraddress(models.Model):
    user_id = models.ForeignKey(userinfo, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    zipcode = models.CharField(max_length=45)

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name = 'user address'
        verbose_name_plural = 'user address'


class coupon(models.Model):
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


class couponsused(models.Model):
    user_id = models.IntegerField()
    order_id = models.IntegerField()
    created_date = models.DateField()
    coupon_id = models.ForeignKey(coupon, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'couponused'
        verbose_name_plural = 'couponused'


class cms(models.Model):
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


class configuration(models.Model):
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


class contactus(models.Model):
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
        verbose_name = 'contactus'
        verbose_name_plural = 'contactus'


class banners(models.Model):
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


class emailtemplate(models.Model):
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

class categorys(models.Model):
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

class subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(categorys,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategory'

class brands(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'brands'
        verbose_name_plural = 'brands'


class products(models.Model):
    category = models.ForeignKey(categorys,on_delete=models.CASCADE,null=False,default='')
    sub_category = models.ForeignKey(subcategory,on_delete=models.CASCADE,null=False,default='')
    brand = models.ForeignKey(brands,on_delete=models.CASCADE,null=True)
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




class productcategory(models.Model):
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    category_id = models.ForeignKey(categorys, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'product category'
        verbose_name_plural = 'product category'


class productimages(models.Model):
    image_name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created_by = models.IntegerField()
    created_date = models.DateField()
    modify_by = models.IntegerField()
    modify_date = models.DateField()
    product_id = models.ForeignKey(products,on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to="media/photos/images")

    def __str__(self):
        return self.image_name

    class Meta:
        verbose_name = 'Product images'
        verbose_name_plural = 'Product images'

    @property
    def short_description(self):
        return truncatechars(self.description, 20)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.product_image.url))

    admin_photo.short_description = 'Product_image'
    admin_photo.allow_tags = True


class orderdetails(models.Model):
    order_id = models.IntegerField()
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    amount = models.FloatField()

    class Meta:
        verbose_name = 'order details'
        verbose_name_plural = 'order details'


class paymentgateway(models.Model):
    name = models.CharField(max_length=45)
    created_by = models.IntegerField()
    created_date = models.DateField()
    modify_by = models.IntegerField()
    modify_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'payment gateway'
        verbose_name_plural = 'payment gateway'


class userorder(models.Model):
    user_id = models.ForeignKey(userinfo, on_delete=models.CASCADE)
    shipping_method = models.IntegerField()
    AWB_No = models.CharField(max_length=100)
    payment_gateway_id = models.ForeignKey(paymentgateway, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    created_date = models.DateField()
    status = models.IntegerField()
    grand_total = models.FloatField()
    shipping_charges = models.FloatField()
    coupon_id = models.ForeignKey(coupon, on_delete=models.CASCADE)
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
        verbose_name = 'userorder'
        verbose_name_plural = 'userorder'



class productattributes(models.Model):
    name = models.CharField(max_length=45)
    created_by = models.IntegerField()
    created_date = models.DateField()
    modified_by = models.IntegerField()
    modified_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product attributes'
        verbose_name_plural = 'product attributes'



class productattributevalue(models.Model):
    product_attribute = models.ForeignKey(productattributes, on_delete=models.CASCADE)
    attribute_value = models.CharField(max_length=45)
    created_by = models.IntegerField()
    created_date = models.DateField()
    modified_by = models.IntegerField()
    modified_date = models.DateField()

    def __str__(self):
        return self.attribute_value

    class Meta:
        verbose_name = 'product attribute value'
        verbose_name_plural = 'product attribute value'



class productattributeassoc(models.Model):
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    product_attribute_id = models.ForeignKey(productattributes, on_delete=models.CASCADE)
    product_attribute_value_id = models.IntegerField()

    class Meta:
        verbose_name = 'product attribute assoc'
        verbose_name_plural = 'product attribute assoc'

# Model for USER
class user(AbstractUser):
    is_admin = models.BooleanField('Is admin',default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_manager = models.BooleanField('Is manager', default=False)


# Model for CRUD operations
class manageuser(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100,unique=True)
    address = models.TextField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'manage user'
        verbose_name_plural = 'manage user'

class userlogin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User login'
        verbose_name_plural = 'User login'

class userregister(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User register'
        verbose_name_plural = 'User register'



