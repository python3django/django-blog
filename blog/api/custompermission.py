from rest_framework import permissions 
 
 
class IsCurrentUserAuthorOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an 'author' attribute.
    """     
    def has_object_permission(self, request, view, obj): 
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS: 
            # The method is a safe method 
            return True 
        else: 
            # The method isn't a safe method 
            # Only owners (author) are granted permissions for unsafe methods 
            return obj.author == request.user 


class IsAdminUserOrReadOnly(permissions.BasePermission): 
    def has_object_permission(self, request, view, obj): 
        if request.method in permissions.SAFE_METHODS: 
            # The method is a safe method 
            return True
        elif request.user.is_staff: 
            return True
