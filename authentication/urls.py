from django.urls import path, include
from .views import CustomUserView, LoginView, LogoutView, MembersView, ProfilePictureView, SignUpView, UpdateProfileView, UserProfileView, upload_photo

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("user", CustomUserView)
router.register("user-profile", UserProfileView)

urlpatterns = [
    path("", include(router.urls)),
    # Auth views
    path('auth/login/',
         LoginView.as_view(), name='auth_login'),

     path('auth/singup/',
         SignUpView.as_view(), name='auth_login'),

    path('auth/logout/',
         LogoutView.as_view(), name='auth_logout'),

    path('profile/upload_photo', upload_photo, name="upload_photo"),
    path('profile/update', UpdateProfileView.as_view(), name="update_profile"),
    path('profile-pic/<int:id>', ProfilePictureView.as_view(), name="my_photo"),
    path('members/all', MembersView.as_view({'get': 'list'}), name="members")
]