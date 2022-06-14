from django.contrib import admin
from .models import User_info, User_wish_list,User_address, Coupon,Coupons_used,Cms
from .models import Configuration, Contact_us, Banners,Email_template,Category
from .models import Product,Product_category,Product_images,Order_details,Payment_gateway
from .models import User_order,Product_attributes,Product_attribute_value,Product_attribute_assoc
from .models import User
from .models import Manage_user

admin.site.site_header = 'ADMINPANEL ADMIN'
admin.site.site_title = 'ADMINPANEL ADMIN PORTAL'
admin.site.index_title = 'WELCOME TO ADMINPANEL ADMIN PORTAL'

admin.site.register(User)

class User_infoAdminSite(admin.ModelAdmin):
    model = User_info
    fields = ['firstname','lastname','email','password','status','created_date','fb_token',
              'twitter_token','google_token','registration_method']
    list_display = ('firstname','lastname','email','password','status','created_date','fb_token',
                    'twitter_token','google_token','registration_method')


admin.site.register(User_info,User_infoAdminSite)

class User_wish_listAdminSite(admin.ModelAdmin):
    model = User_wish_list
    fields = ['user_id','product_id']
    list_display = ('user_id','product_id')


admin.site.register(User_wish_list,User_wish_listAdminSite)

class User_addressAdminSite(admin.ModelAdmin):
    model = User_address
    fields = ['user_id','address1','address2','city','state','country','zipcode']
    list_display = ('user_id','address1','address2','city','state','country','zipcode')


admin.site.register(User_address,User_addressAdminSite)

class CouponAdminSite(admin.ModelAdmin):
    model = Coupon
    fields = ['code','percent_off','created_by','created_date','modify_by','modify_date','no_of_uses']
    list_display = ('code','percent_off','created_by','created_date','modify_by','modify_date','no_of_uses')


admin.site.register(Coupon,CouponAdminSite)

class Coupon_usedAdminSite(admin.ModelAdmin):
    model = Coupons_used
    fields = ['user_id','order_id','created_date','coupon_id']
    list_display = ('user_id','order_id','created_date','coupon_id')


admin.site.register(Coupons_used,Coupon_usedAdminSite)

class CmsAdminSite(admin.ModelAdmin):
    model = Cms
    fields = ['title','content','meta_title','meta_description','meta_keywords','created_by','created_date',
              'modify_by','modify_date']
    list_display = ('title','content','meta_title','meta_description','meta_keywords','created_by','created_date',
                    'modify_by','modify_date')


admin.site.register(Cms,CmsAdminSite)

class ConfigurationAdminSite(admin.ModelAdmin):
    model = Configuration
    fields = ['conf_key','conf_value','created_by','created_date','modify_by','modify_date','status']
    list_display = ('conf_key','conf_value','created_by','created_date','modify_by','modify_date','status')


admin.site.register(Configuration,ConfigurationAdminSite)

class Contact_usAdminSite(admin.ModelAdmin):
    model = Contact_us
    fields = ['name','email','contact_no','message','note_adm','created_by',
              'created_date','modify_by','modify_date']
    list_display = ('name','email','contact_no','message','note_adm','created_by',
                    'created_date','modify_by','modify_date')


admin.site.register(Contact_us,Contact_usAdminSite)


class BannersAdminSite(admin.ModelAdmin):
    model = Banners
    fields = ['banner_path','status','images','admin_photo']
    list_display = ('banner_path','status','images','admin_photo')
    readonly_fields = ('status','admin_photo')


admin.site.register(Banners,BannersAdminSite)


class Email_templateAdminSite(admin.ModelAdmin):
    model = Email_template
    fields = ['title','subject','content','created_by','created_date','modify_by','modify_date']
    list_display = ('title','subject','content','created_by','created_date','modify_by','modify_date')


admin.site.register(Email_template,Email_templateAdminSite)


class CategoryAdminSite(admin.ModelAdmin):
    model = Category
    fields = ['name','parent_id','created_by','created_date','modify_by','modify_date','status']
    list_display = ('name','parent_id','created_by','created_date','modify_by','modify_date','status')


admin.site.register(Category,CategoryAdminSite)


class ProductAdminSite(admin.ModelAdmin):
    model = Product
    fields = ['name','sku','short_description','long_description','price','special_price','special_price_from',
              'special_price_to','status','quantity','meta_title','meta_description','meta_keywords',
              'status1','created_by','created_date','modify_by','modify_date','is_featured']
    list_display = ('name','sku','short_description','long_description','price','special_price','special_price_from',
                    'special_price_to','status','quantity','meta_title','meta_description','meta_keywords',
                    'status1','created_by','created_date','modify_by','modify_date','is_featured')


admin.site.register(Product,ProductAdminSite)

class Product_CategoryAdminSite(admin.ModelAdmin):
    model = Product_category
    fields = ['product_id','category_id']
    list_display = ('product_id','category_id')


admin.site.register(Product_category,Product_CategoryAdminSite)

class Product_imagesAdminSite(admin.ModelAdmin):
    model = Product_images
    fields = ['image_name','status','created_by','created_date',
              'modify_by','modify_date','product_id','product_image','admin_photo']
    list_display = ('image_name','status','created_by','created_date',
                    'modify_by','modify_date','product_id','product_image','admin_photo')
    readonly_fields = ('status','admin_photo')


admin.site.register(Product_images,Product_imagesAdminSite)


class Order_detailsAdminSite(admin.ModelAdmin):
    model = Order_details
    fields = ['order_id','product_id','quantity','amount']
    list_display = ('order_id','product_id','quantity','amount')


admin.site.register(Order_details,Order_detailsAdminSite)

class Payment_gatewayAdminSite(admin.ModelAdmin):
    model = Payment_gateway
    fields = ['name','created_by','created_date','modify_by','modify_date']
    list_display = ('name','created_by','created_date','modify_by','modify_date')


admin.site.register(Payment_gateway,Payment_gatewayAdminSite)

class User_orderAdminSite(admin.ModelAdmin):
    model = User_order
    fields = ['user_id','shipping_method','AWB_No','payment_gateway_id','transaction_id',
              'created_date','status','grand_total','shipping_charges','coupon_id','billing_address1',
              'billing_address2','billing_city','billing_state','billing_country','billing_zipcode',
              'shipping_address1','shipping_address2','shipping_city','shipping_state','shipping_country',
              'shipping_zipcode']
    list_display = ('user_id','shipping_method','AWB_No','payment_gateway_id','transaction_id',
                    'created_date','status','grand_total','shipping_charges','coupon_id','billing_address1',
                    'billing_address2','billing_city','billing_state','billing_country','billing_zipcode',
                    'shipping_address1','shipping_address2','shipping_city','shipping_state','shipping_country',
                    'shipping_zipcode')


admin.site.register(User_order,User_orderAdminSite)


class Product_attributesAdminSite(admin.ModelAdmin):
    model = Product_attributes
    fields = ['name','created_by','created_date','modified_by','modified_date']
    list_display = ('name','created_by','created_date','modified_by','modified_date')


admin.site.register(Product_attributes,Product_attributesAdminSite)

class Product_attribute_valueAdminSite(admin.ModelAdmin):
    model = Product_attribute_value
    fields = ['product_attribute','attribute_value','created_by','created_date','modified_by','modified_date']
    list_display = ('product_attribute','attribute_value','created_by','created_date','modified_by','modified_date')


admin.site.register(Product_attribute_value,Product_attribute_valueAdminSite)

class Product_attribute_assocAdminSite(admin.ModelAdmin):
    model = Product_attribute_assoc
    fields = ['product_id','product_attribute_id','product_attribute_value_id']
    list_display = ('product_id','product_attribute_id','product_attribute_value_id')


admin.site.register(Product_attribute_assoc,Product_attribute_assocAdminSite)

class Manage_userAdminSite(admin.ModelAdmin):
    model = Manage_user
    fields = ['name','email','address','phone']
    list_display = ('name','email','address','phone')


admin.site.register(Manage_user,Manage_userAdminSite)



