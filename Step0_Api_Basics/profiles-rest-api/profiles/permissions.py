from rest_framework import permissions


class UpdateProfile(permissions.BasePermission):
    """ Allow users to edit their own profile """

    # Function will be called every time when a request is made to the API we assigned our permission to this Function 
    # return Boolean values based on the authenticated user has the permissions to do the change they are doing now 
    # 
    def has_object_permission(self, request, view, obj) :
        """ Check user is editing their own Profile """

        # if the user is trying to perform a SAFE_MTHODS LIKE GET , Then No Problem , they are allowed to do that
        if request.method in permissions.SAFE_METHODS:
            return True

        # whether the object they are trying to update matches their authenticated user profile 
        # ( that user profile is added to the authentication of the request )
        # When you authenticate a request in DRF , it will assign the authenticated user profile to the request itself 

        return obj.id == request.user.id 



# Allow users to update theirs own Profile 

class UpdateOwnStatus(permissions.BasePermission):
    """ Allow users to update their own status """

    def has_object_permission(self, request, view, obj):
        """ make suer user edits its their own Status """

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id 