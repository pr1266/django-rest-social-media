from rest_framework import permissions

#! inja permission hamoono mizarim:

#? kolan update o delete baraye yek post faghat ba method haye
#? mojaz va user e owner e khode post
#* method e post ham nadarim inja:

class PostCustomPermission(permissions.BasePermission):

    safe_methods = ['GET', 'PUT', 'DELETE']

    message = 'you dont have permission to delete or update post of other users'
    
    def has_permission(self, request, view):

        return request.method in self.safe_methods

    def has_object_permission(self, request, view, obj):
        
        return request.user == obj.user

#! hala inja baraye like:
#? age user owner e post bashe mitoone RUD anjam bede
#? age owner e like ham bashe mitoone inkaro bokone
#* ama bazam method e POST nadarim

class LikeCustomPermission(permissions.BasePermission):

    safe_methods = ['GET', 'PUT', 'DELETE']

    def has_permission(self, request, view):

        return request.method in self.safe_methods

    def has_object_permission(self, request, view, obj):
        
        if request.user == obj.user:
            return True
        
        return request.user == obj.post.user
        