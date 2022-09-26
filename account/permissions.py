from rest_framework.permissions import IsAuthenticated
from account.models import Account

class IsVendor(IsAuthenticated):
    def has_permission(self, request, views):
        is_authenticated = super().has_permission(request, views)
        user = Account.objects.get(user=request.user)
        if not is_authenticated:
            return False

        return user.isVendor