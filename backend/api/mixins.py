from .permissions import IsStaffEditorPermission
from rest_framework import permissions


class StaffEditorPermissionMixins:
    permissions_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
