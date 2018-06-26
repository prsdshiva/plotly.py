from plotly.basedatatypes import BaseLayoutHierarchyType


class Domain(BaseLayoutHierarchyType):

    # x
    # -
    @property
    def x(self):
        """
        Sets the horizontal domain of this grid subplot (in plot
        fraction). The first and last cells end exactly at the domain
        edges, with no grout around the edges.
    
        The 'x' property is an info array that may be specified as a
        list or tuple of 2 elements where:
    
    (0) The 'x[0]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
    (1) The 'x[1]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        list
        """
        return self['x']

    @x.setter
    def x(self, val):
        self['x'] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the vertical domain of this grid subplot (in plot
        fraction). The first and last cells end exactly at the domain
        edges, with no grout around the edges.
    
        The 'y' property is an info array that may be specified as a
        list or tuple of 2 elements where:
    
    (0) The 'y[0]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
    (1) The 'y[1]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        list
        """
        return self['y']

    @y.setter
    def y(self, val):
        self['y'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout.grid'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        x
            Sets the horizontal domain of this grid subplot (in
            plot fraction). The first and last cells end exactly at
            the domain edges, with no grout around the edges.
        y
            Sets the vertical domain of this grid subplot (in plot
            fraction). The first and last cells end exactly at the
            domain edges, with no grout around the edges.
        """

    def __init__(self, arg=None, x=None, y=None, **kwargs):
        """
        Construct a new Domain object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.grid.Domain
        x
            Sets the horizontal domain of this grid subplot (in
            plot fraction). The first and last cells end exactly at
            the domain edges, with no grout around the edges.
        y
            Sets the vertical domain of this grid subplot (in plot
            fraction). The first and last cells end exactly at the
            domain edges, with no grout around the edges.

        Returns
        -------
        Domain
        """
        super(Domain, self).__init__('domain')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif not isinstance(arg, dict):
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.grid.Domain 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.grid.Domain"""
            )

        # Import validators
        # -----------------
        from plotly.validators.layout.grid import (domain as v_domain)

        # Initialize validators
        # ---------------------
        self._validators['x'] = v_domain.XValidator()
        self._validators['y'] = v_domain.YValidator()

        # Populate data dict with properties
        # ----------------------------------
        v = arg.pop('x', None)
        self.x = x or v
        v = arg.pop('y', None)
        self.y = y or v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))