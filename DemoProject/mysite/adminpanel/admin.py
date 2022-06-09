from django.contrib import admin
from .models import User_info, User_wish_list,User_address, Coupon,Coupons_used,Cms
from .models import Configuration, Contact_us, Banners,Email_template,Category
from .models import Product,Product_category,Product_images,Order_details,Payment_gateway
from .models import User_order,Product_attributes,Product_attribute_value,Product_attribute_assoc
from .models import User
from .models import Manage_user


admin.site.register(User_info)
admin.site.register(User_wish_list)
admin.site.register(User_address)
admin.site.register(Coupon)
admin.site.register(Coupons_used)
admin.site.register(Cms)
admin.site.register(Configuration)
admin.site.register(Contact_us)
admin.site.register(Banners)
admin.site.register(Email_template)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Product_category)
admin.site.register(Product_images)
admin.site.register(Order_details)
admin.site.register(Payment_gateway)
admin.site.register(User_order)
admin.site.register(Product_attributes)
admin.site.register(Product_attribute_value)
admin.site.register(Product_attribute_assoc)

admin.site.register(User)
admin.site.register(Manage_user)

