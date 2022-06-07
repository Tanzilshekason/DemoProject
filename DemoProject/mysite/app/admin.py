from django.contrib import admin
from .models import user_info, user_wish_list,user_address, coupon,coupons_used,cms
from .models import configuration, contact_us, banners,email_template,category
from .models import product,product_category,product_images,order_details,payment_gateway
from .models import user_order,product_attributes,product_attribute_value,product_attribute_assoc
from .models import User


admin.site.register(user_info)
admin.site.register(user_wish_list)
admin.site.register(user_address)
admin.site.register(coupon)
admin.site.register(coupons_used)
admin.site.register(cms)
admin.site.register(configuration)
admin.site.register(contact_us)
admin.site.register(banners)
admin.site.register(email_template)
admin.site.register(category)
admin.site.register(product)
admin.site.register(product_category)
admin.site.register(product_images)
admin.site.register(order_details)
admin.site.register(payment_gateway)
admin.site.register(user_order)
admin.site.register(product_attributes)
admin.site.register(product_attribute_value)
admin.site.register(product_attribute_assoc)

admin.site.register(User)


