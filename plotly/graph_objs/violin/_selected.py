from plotly.basedatatypes import BaseTraceHierarchyType


class Selected(BaseTraceHierarchyType):

    # marker
    # ------
    @property
    def marker(self):
        """
        The 'marker' property is an instance of Marker
        that may be specified as:
          - An instance of plotly.graph_objs.violin.selected.Marker
          - A dict of string/value properties that will be passed
            to the Marker constructor
    
            Supported dict properties:
                
                color
                    Sets the marker color of selected points.
                opacity
                    Sets the marker opacity of selected points.
                size
                    Sets the marker size of selected points.

        Returns
        -------
        plotly.graph_objs.violin.selected.Marker
        """
        return self['marker']

    @marker.setter
    def marker(self, val):
        self['marker'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'violin'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        marker
            plotly.graph_objs.violin.selected.Marker instance or
            dict with compatible properties
        """

    def __init__(self, arg=None, marker=None, **kwargs):
        """
        Construct a new Selected object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.violin.Selected
        marker
            plotly.graph_objs.violin.selected.Marker instance or
            dict with compatible properties

        Returns
        -------
        Selected
        """
        super(Selected, self).__init__('selected')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif not isinstance(arg, dict):
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.violin.Selected 
constructor must be a dict or 
an instance of plotly.graph_objs.violin.Selected"""
            )

        # Import validators
        # -----------------
        from plotly.validators.violin import (selected as v_selected)

        # Initialize validators
        # ---------------------
        self._validators['marker'] = v_selected.MarkerValidator()

        # Populate data dict with properties
        # ----------------------------------
        v = arg.pop('marker', None)
        self.marker = marker or v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))