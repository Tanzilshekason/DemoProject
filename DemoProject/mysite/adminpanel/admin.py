from django.contrib import admin
from .models import Userinfo, Userwishlist,Useraddress, Coupon,Couponsused,Cms
from .models import Configuration, Contactus, Banners,Emailtemplate,Categorys,Subcategory,Brands
from .models import Products,Productcategory,Productimages,Orderdetails,Paymentgateway
from .models import Userorder,Productattributes,Productattributevalue,Productattributeassoc
from .models import User
from .models import Manageuser,Userlogin,Userregister,Filterprices,Images

admin.site.site_header = 'ADMINPANEL ADMIN'
admin.site.site_title = 'ADMINPANEL ADMIN PORTAL'
admin.site.index_title = 'WELCOME TO ADMINPANEL ADMIN PORTAL'

admin.site.register(User)

class UserinfoAdminSite(admin.ModelAdmin):
    model = Userinfo
    fields = ['firstname','lastname','email','password','status','created_date','fb_token',
              'twitter_token','google_token','registration_method']
    list_display = ('firstname','lastname','email','password','status','created_date','fb_token',
                    'twitter_token','google_token','registration_method')


admin.site.register(Userinfo,UserinfoAdminSite)

class UserwishlistAdminSite(admin.ModelAdmin):
    model = Userwishlist
    fields = ['user_id','product_id']
    list_display = ('user_id','product_id')


admin.site.register(Userwishlist,UserwishlistAdminSite)

class UseraddressAdminSite(admin.ModelAdmin):
    model = Useraddress
    fields = ['user_id','address1','address2','city','state','country','zipcode']
    list_display = ('user_id','address1','address2','city','state','country','zipcode')


admin.site.register(Useraddress,UseraddressAdminSite)

class CouponAdminSite(admin.ModelAdmin):
    model = Coupon
    fields = ['code','percent_off','created_by','created_date','modify_by','modify_date','no_of_uses']
    list_display = ('code','percent_off','created_by','created_date','modify_by','modify_date','no_of_uses')


admin.site.register(Coupon,CouponAdminSite)

class CouponsusedAdminSite(admin.ModelAdmin):
    model = Couponsused
    fields = ['user_id','order_id','created_date','coupon_id']
    list_display = ('user_id','order_id','created_date','coupon_id')


admin.site.register(Couponsused,CouponsusedAdminSite)

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

class ContactusAdminSite(admin.ModelAdmin):
    model = Contactus
    fields = ['name','email','subject','message']
    list_display = ('name','email','subject','message')


admin.site.register(Contactus,ContactusAdminSite)


class BannersAdminSite(admin.ModelAdmin):
    model = Banners
    fields = ['banner_path','status','images','admin_photo']
    list_display = ('banner_path','status','images','admin_photo')
    readonly_fields = ('status','admin_photo')


admin.site.register(Banners,BannersAdminSite)


class EmailtemplateAdminSite(admin.ModelAdmin):
    model = Emailtemplate
    fields = ['title','subject','content','created_by','created_date','modify_by','modify_date']
    list_display = ('title','subject','content','created_by','created_date','modify_by','modify_date')


admin.site.register(Emailtemplate,EmailtemplateAdminSite)


class CategorysAdminSite(admin.ModelAdmin):
    model = Categorys
    fields = ['name','parent_id','created_by','created_date','modify_by','modify_date','status']
    list_display = ('name','parent_id','created_by','created_date','modify_by','modify_date','status')


admin.site.register(Categorys,CategorysAdminSite)


class BrandsAdminSite(admin.ModelAdmin):
    model = Brands
    fields = ['name']


admin.site.register(Brands,BrandsAdminSite)


class SubcategoryAdminSite(admin.ModelAdmin):
    model = Subcategory
    fields = ['name','category']
    list_display = ('name','category')


admin.site.register(Subcategory,SubcategoryAdminSite)


class ImagesTublerinline(admin.TabularInline):
    model = Images
    fields = ['image','product','admin_photo']
    list_display = ('image','product','admin_photo')
    readonly_fields = ('product','admin_photo')


admin.site.register(Images)


class ProductsInlineAdmin(admin.ModelAdmin):
    inlines = [ImagesTublerinline]
    fields = ['category','sub_category','brand','name','sku','shor_description','long_description','price',
              'special_price','special_price_from','special_price_to','status','quantity','meta_title',
              'meta_description','meta_keywords','status1','created_by','created_date','modify_by','modify_date',
              'is_featured','image','admin_photo','Availability','filter_price']
    list_display = ('category','sub_category','brand','name','sku','shor_description','long_description','price',
                    'special_price','special_price_from','special_price_to','status','quantity','meta_title',
                    'meta_description','meta_keywords','status1','created_by','created_date','modify_by','modify_date',
                    'is_featured','image','admin_photo','Availability','filter_price')
    readonly_fields = ('status','admin_photo')


admin.site.register(Products,ProductsInlineAdmin)

class ProductcategoryAdminSite(admin.ModelAdmin):
    model = Productcategory
    fields = ['product_id','category_id']
    list_display = ('product_id','category_id')


admin.site.register(Productcategory,ProductcategoryAdminSite)

class ProductimagesAdminSite(admin.ModelAdmin):
    model = Productimages
    fields = ['image_name','status','created_by','created_date',
              'modify_by','modify_date','product_id','product_image','admin_photo']
    list_display = ('image_name','status','created_by','created_date',
                    'modify_by','modify_date','product_id','product_image','admin_photo')
    readonly_fields = ('status','admin_photo')


admin.site.register(Productimages,ProductimagesAdminSite)


class OrderdetailsAdminSite(admin.ModelAdmin):
    model = Orderdetails
    fields = ['order_id','product_id','quantity','amount']
    list_display = ('order_id','product_id','quantity','amount')


admin.site.register(Orderdetails,OrderdetailsAdminSite)

class PaymentgatewayAdminSite(admin.ModelAdmin):
    model = Paymentgateway
    fields = ['name','created_by','created_date','modify_by','modify_date']
    list_display = ('name','created_by','created_date','modify_by','modify_date')


admin.site.register(Paymentgateway,PaymentgatewayAdminSite)

class UserorderAdminSite(admin.ModelAdmin):
    model = Userorder
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


admin.site.register(Userorder,UserorderAdminSite)


class ProductattributesAdminSite(admin.ModelAdmin):
    model = Productattributes
    fields = ['name','created_by','created_date','modified_by','modified_date']
    list_display = ('name','created_by','created_date','modified_by','modified_date')


admin.site.register(Productattributes,ProductattributesAdminSite)

class ProductattributevalueAdminSite(admin.ModelAdmin):
    model = Productattributevalue
    fields = ['product_attribute','attribute_value','created_by','created_date','modified_by','modified_date']
    list_display = ('product_attribute','attribute_value','created_by','created_date','modified_by','modified_date')


admin.site.register(Productattributevalue,ProductattributevalueAdminSite)

class ProductattributeassocAdminSite(admin.ModelAdmin):
    model = Productattributeassoc
    fields = ['product_id','product_attribute_id','product_attribute_value_id']
    list_display = ('product_id','product_attribute_id','product_attribute_value_id')


admin.site.register(Productattributeassoc,ProductattributeassocAdminSite)

class ManageuserAdminSite(admin.ModelAdmin):
    model = Manageuser
    fields = ['name','email','address','phone']
    list_display = ('name','email','address','phone')


admin.site.register(Manageuser,ManageuserAdminSite)

class UserloginAdminSite(admin.ModelAdmin):
    model = Userlogin
    fields = ['name','email']
    list_display = ('name','email')


admin.site.register(Userlogin,UserloginAdminSite)

class UserregisterAdminSite(admin.ModelAdmin):
    model = Userregister
    fields = ['name','email','password']
    list_display = ('name','email','password')


admin.site.register(Userregister,UserregisterAdminSite)

admin.site.register(Filterprices)




