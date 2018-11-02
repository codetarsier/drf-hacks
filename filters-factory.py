from django_filters import Filter


class ListFilter(Filter):
    """
        List django filter to query for multiple values
        eg usage:-
            id = ListFilter(name='id', lookup_expr='in')
    """

    def filter(self, qs, value):
        if not value:
            return qs

        self.lookup_type = 'in'
        values = value.split(',')
        return super(ListFilter, self).filter(qs, values)
