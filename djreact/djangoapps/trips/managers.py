from datetime import datetime


class AvailableTripsManager(models.Manager):
    """
    Trip schedule safe queryset manager.
    """

    def get_queryset(self):
        """
        This method will only return the objects which have date_from defined
        in the future

        Usage:
            >>> TripSchedule.available.all()
        """
        return super(AvailableTripsManager).get_queryset().filter(
            date_from__gt=datetime.now()
        )