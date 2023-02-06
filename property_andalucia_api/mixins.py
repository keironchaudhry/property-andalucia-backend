class CustomQuerysetFilter:
    # https://www.django-rest-framework.org/api-guide/filtering/
    def get_queryset(self):
        """ Reveals object queryset based on whether the defined user
        is the owner of the object or is anonymous """
        user = self.request.user
        if user.is_authenticated:
            queryset = self.model.objects.filter(
                owner=user
            )
        else:
            queryset = self.model.objects.none()
        return queryset
