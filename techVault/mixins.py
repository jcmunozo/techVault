"""Shared access-control mixins."""


class OwnerQuerysetMixin:
    """Limit a view's queryset to objects owned by the current user.

    Applied to list/detail/update/delete views so a user can only see or act
    on their own records. A non-owner requesting someone else's object gets a
    404 instead of being able to read, edit or delete it.
    """

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
