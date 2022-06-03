from django.db import models

# Create your models here.
class user(models.Model):
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    fb_token = models.CharField(max_length=100)
    twitter_token = models.CharField(max_length=100)
    google_token = models.CharField(max_length=100)
    registration_method = models.BooleanField(default=False)


def __str__(self):
    return self.title

class user_wish_list(models.Model):
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=100)

def __str__(self):
    return self.title

class user_address(models.Model):
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    zipcode = models.CharField(max_length=45)

def __str__(self):
    return self.title

class coupon(models.Model):
    code = models.CharField(max_length=45)
    percent_off = models.FloatField()
    created_by = models.IntegerField()
    created_date = models.DateTimeField()
    modify_by = models.IntegerField()
    modify_date = models.DateTimeField()
    no_of_uses = models.IntegerField()

def __str__(self):
    return self.title

class coupons_used(models.Model):
    user_id = models.IntegerField()
    order_id = models.IntegerField()
    created_date = models.DateField()
    coupon_id = models.ForeignKey(coupon, on_delete=models.CASCADE)

def __str__(self):
    return self.title

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

class configuration(models.Model):
    conf_key = models.CharField(max_length=45)
    conf_value = models.CharField(max_length=100)
    created_by = models.IntegerField()
    created_date = models.DateField()
    modify_by = models.IntegerField()
    modify_date = models.DateField()
    status = models.BooleanField(default=False)

def __str__(self):
    return self.title

class coupons_used(models.Model):
    user_id = models.IntegerField()
    order_id = models.IntegerField()
    created_date = models.DateField()
    coupon_id = models.ForeignKey(coupon, on_delete=models.CASCADE)

def __str__(self):
    return self.title

class contact_us(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    contact_no = models.CharField(max_length=45)
    message = models.TextField()
    note_adm = models.TextField()
    created_by = models.IntegerField()
    created_date = models.DateField()
    modify_by = models.IntegerField()
    modify_date = models.DateField()

def __str__(self):
    return self.title

class banners(models.Model):
    banner_path = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    images = models.ImageField()

def __str__(self):
    return self.title

class email_template(models.Model):
    title = models.CharField(max_length=45)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    created_by = models.IntegerField()
    created_date = models.DateField()
    modify_by = models.IntegerField()
    modify_date = models.DateField()

def __str__(self):
    return self.title

class category(models.Model):
    name = models.CharField(max_length=100)
    parent_id = models.IntegerField()
    created_by = models.IntegerField()
    created_date = models.DateField()
    modify_by = models.IntegerField()
    modify_date = models.DateField()
    status = models.BooleanField(default=False)

def __str__(self):
    return self.title

class product(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=45)
    short_description = models.CharField(max_length=100)
    long_description = models.TextField()
    price = models.FloatField()
    special_price = models.FloatField()
    special_price_from = models.DateField()
    special_price_to = models.DateField()
    status = models.IntegerField()
    quantity = models.IntegerField()
    meta_title = models.CharField(max_length=45)
    meta_description = models.TextField()
    meta_keywords = models.TextField()
    status1 = models.IntegerField()
    created_by = models.IntegerField()
    created_date = models.DateField()
    modify_by = models.IntegerField()
    modify_date = models.DateField()
    is_featured = models.BooleanField(default=False)

def __str__(self):
    return self.title

class product_category(models.Model):
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    category_id = models.ForeignKey(category, on_delete=models.CASCADE)

def __str__(self):
    return self.title

class product_images(models.Model):
    image_name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    created_by = models.IntegerField()
    created_date = models.DateField()
    modify_by = models.IntegerField()
    modify_date = models.DateField()
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    product_image = models.ImageField()

def __str__(self):
    return self.title

class order_details(models.Model):
    order_id = models.IntegerField()
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    amount = models.FloatField()

def __str__(self):
    return self.title

class payment_gateway(models.Model):
    name = models.CharField(max_length=45)
    created_by = models.IntegerField()
    created_date = models.DateField()
    modify_by = models.IntegerField()
    modify_date = models.DateField()

def __str__(self):
    return self.title

class user_order(models.Model):
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    shipping_method = models.IntegerField()
    AWB_No = models.CharField(max_length=100)
    payment_gateway_id = models.ForeignKey(payment_gateway, on_delete=models.CASCADE)
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
        return self.title

class product_attributes(models.Model):
    name = models.CharField(max_length=45)
    created_by = models.IntegerField()
    created_date = models.DateField()
    modified_by = models.IntegerField()
    modified_date = models.DateField()

def __str__(self):
    return self.title

class product_attribute_value(models.Model):
    product_attribute = models.ForeignKey(product_attributes, on_delete=models.CASCADE)
    attribute_value = models.CharField(max_length=45)
    created_by = models.IntegerField()
    created_date = models.DateField()
    modified_by = models.IntegerField()
    modified_date = models.DateField()

    def __str__(self):
        return self.title

class product_attribute_assoc(models.Model):
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    product_attribute_id = models.ForeignKey(product_attributes, on_delete=models.CASCADE)
    product_attribute_value_id = models.IntegerField()

    def __str__(self):
        return self.title

