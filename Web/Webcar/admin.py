from django.contrib import admin

from Webcar.models import Users
from Webcar.models import Admins
from Webcar.models import ErrorType
from Webcar.models import Orders
from Webcar.models import ChargeError
from Webcar.models import Subs


admin.site.register(Users)
admin.site.register(Admins)
admin.site.register(ErrorType)
admin.site.register(Orders)
admin.site.register(ChargeError)
admin.site.register(Subs)