from django.contrib import admin
from .models import userinfo, userwishlist,useraddress, coupon,couponsused,cms
from .models import configuration, contactus, banners,emailtemplate,categorys,subcategory,brands
from .models import products,productcategory,productimages,orderdetails,paymentgateway
from .models import userorder,productattributes,productattributevalue,productattributeassoc
from .models import user
from .models import manageuser,userlogin,userregister,filterprices,images

admin.site.site_header = 'ADMINPANEL ADMIN'
admin.site.site_title = 'ADMINPANEL ADMIN PORTAL'
admin.site.index_title = 'WELCOME TO ADMINPANEL ADMIN PORTAL'

admin.site.register(user)

class userinfoAdminSite(admin.ModelAdmin):
    model = userinfo
    fields = ['firstname','lastname','email','password','status','created_date','fb_token',
              'twitter_token','google_token','registration_method']
    list_display = ('firstname','lastname','email','password','status','created_date','fb_token',
                    'twitter_token','google_token','registration_method')


admin.site.register(userinfo,userinfoAdminSite)

class userwishlistAdminSite(admin.ModelAdmin):
    model = userwishlist
    fields = ['user_id','product_id']
    list_display = ('user_id','product_id')


admin.site.register(userwishlist,userwishlistAdminSite)

class useraddressAdminSite(admin.ModelAdmin):
    model = useraddress
    fields = ['user_id','address1','address2','city','state','country','zipcode']
    list_display = ('user_id','address1','address2','city','state','country','zipcode')


admin.site.register(useraddress,useraddressAdminSite)

class couponAdminSite(admin.ModelAdmin):
    model = coupon
    fields = ['code','percent_off','created_by','created_date','modify_by','modify_date','no_of_uses']
    list_display = ('code','percent_off','created_by','created_date','modify_by','modify_date','no_of_uses')


admin.site.register(coupon,couponAdminSite)

class couponsusedAdminSite(admin.ModelAdmin):
    model = couponsused
    fields = ['user_id','order_id','created_date','coupon_id']
    list_display = ('user_id','order_id','created_date','coupon_id')


admin.site.register(couponsused,couponsusedAdminSite)

class cmsAdminSite(admin.ModelAdmin):
    model = cms
    fields = ['title','content','meta_title','meta_description','meta_keywords','created_by','created_date',
              'modify_by','modify_date']
    list_display = ('title','content','meta_title','meta_description','meta_keywords','created_by','created_date',
                    'modify_by','modify_date')


admin.site.register(cms,cmsAdminSite)

class configurationAdminSite(admin.ModelAdmin):
    model = configuration
    fields = ['conf_key','conf_value','created_by','created_date','modify_by','modify_date','status']
    list_display = ('conf_key','conf_value','created_by','created_date','modify_by','modify_date','status')


admin.site.register(configuration,configurationAdminSite)

class contactusAdminSite(admin.ModelAdmin):
    model = contactus
    fields = ['name','email','subject','message']
    list_display = ('name','email','subject','message')


admin.site.register(contactus,contactusAdminSite)


class bannersAdminSite(admin.ModelAdmin):
    model = banners
    fields = ['banner_path','status','images','admin_photo']
    list_display = ('banner_path','status','images','admin_photo')
    readonly_fields = ('status','admin_photo')


admin.site.register(banners,bannersAdminSite)


class emailtemplateAdminSite(admin.ModelAdmin):
    model = emailtemplate
    fields = ['title','subject','content','created_by','created_date','modify_by','modify_date']
    list_display = ('title','subject','content','created_by','created_date','modify_by','modify_date')


admin.site.register(emailtemplate,emailtemplateAdminSite)


class categorysAdminSite(admin.ModelAdmin):
    model = categorys
    fields = ['name','parent_id','created_by','created_date','modify_by','modify_date','status']
    list_display = ('name','parent_id','created_by','created_date','modify_by','modify_date','status')


admin.site.register(categorys,categorysAdminSite)


class brandsAdminSite(admin.ModelAdmin):
    model = brands
    fields = ['name']


admin.site.register(brands,brandsAdminSite)


class subcategoryAdminSite(admin.ModelAdmin):
    model = subcategory
    fields = ['name','category']
    list_display = ('name','category')


admin.site.register(subcategory,subcategoryAdminSite)


class imagesTublerinline(admin.TabularInline):
    model = images
    fields = ['image','products','admin_photo']
    list_display = ('image','products','admin_photo')
    readonly_fields = ('products','admin_photo')


admin.site.register(images)


class productsInlineAdmin(admin.ModelAdmin):
    inlines = [imagesTublerinline]
    fields = ['category','sub_category','brand','name','sku','shor_description','long_description','price',
              'special_price','special_price_from','special_price_to','status','quantity','meta_title',
              'meta_description','meta_keywords','status1','created_by','created_date','modify_by','modify_date',
              'is_featured','image','admin_photo','Availability','filter_price']
    list_display = ('category','sub_category','brand','name','sku','shor_description','long_description','price',
                    'special_price','special_price_from','special_price_to','status','quantity','meta_title',
                    'meta_description','meta_keywords','status1','created_by','created_date','modify_by','modify_date',
                    'is_featured','image','admin_photo','Availability','filter_price')
    readonly_fields = ('status','admin_photo')


admin.site.register(products,productsInlineAdmin)

class productcategoryAdminSite(admin.ModelAdmin):
    model = productcategory
    fields = ['product_id','category_id']
    list_display = ('product_id','category_id')


admin.site.register(productcategory,productcategoryAdminSite)

class productimagesAdminSite(admin.ModelAdmin):
    model = productimages
    fields = ['image_name','status','created_by','created_date',
              'modify_by','modify_date','product_id','product_image','admin_photo']
    list_display = ('image_name','status','created_by','created_date',
                    'modify_by','modify_date','product_id','product_image','admin_photo')
    readonly_fields = ('status','admin_photo')


admin.site.register(productimages,productimagesAdminSite)


class orderdetailsAdminSite(admin.ModelAdmin):
    model = orderdetails
    fields = ['order_id','product_id','quantity','amount']
    list_display = ('order_id','product_id','quantity','amount')


admin.site.register(orderdetails,orderdetailsAdminSite)

class paymentgatewayAdminSite(admin.ModelAdmin):
    model = paymentgateway
    fields = ['name','created_by','created_date','modify_by','modify_date']
    list_display = ('name','created_by','created_date','modify_by','modify_date')


admin.site.register(paymentgateway,paymentgatewayAdminSite)

class userorderAdminSite(admin.ModelAdmin):
    model = userorder
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


admin.site.register(userorder,userorderAdminSite)


class productattributesAdminSite(admin.ModelAdmin):
    model = productattributes
    fields = ['name','created_by','created_date','modified_by','modified_date']
    list_display = ('name','created_by','created_date','modified_by','modified_date')


admin.site.register(productattributes,productattributesAdminSite)

class productattributevalueAdminSite(admin.ModelAdmin):
    model = productattributevalue
    fields = ['product_attribute','attribute_value','created_by','created_date','modified_by','modified_date']
    list_display = ('product_attribute','attribute_value','created_by','created_date','modified_by','modified_date')


admin.site.register(productattributevalue,productattributevalueAdminSite)

class productattributeassocAdminSite(admin.ModelAdmin):
    model = productattributeassoc
    fields = ['product_id','product_attribute_id','product_attribute_value_id']
    list_display = ('product_id','product_attribute_id','product_attribute_value_id')


admin.site.register(productattributeassoc,productattributeassocAdminSite)

class manageuserAdminSite(admin.ModelAdmin):
    model = manageuser
    fields = ['name','email','address','phone']
    list_display = ('name','email','address','phone')


admin.site.register(manageuser,manageuserAdminSite)

class userloginAdminSite(admin.ModelAdmin):
    model = userlogin
    fields = ['name','email']
    list_display = ('name','email')


admin.site.register(userlogin,userloginAdminSite)

class userregisterAdminSite(admin.ModelAdmin):
    model = userregister
    fields = ['name','email','password']
    list_display = ('name','email','password')


admin.site.register(userregister,userregisterAdminSite)

admin.site.register(filterprices)




