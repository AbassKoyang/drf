from .permissions import isStaffEditorPermission
from rest_framework import permissions

class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, isStaffEditorPermission]