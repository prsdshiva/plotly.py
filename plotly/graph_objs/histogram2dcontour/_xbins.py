from plotly.basedatatypes import BaseTraceHierarchyType


class XBins(BaseTraceHierarchyType):

    # end
    # ---
    @property
    def end(self):
        """
        Sets the end value for the x axis bins.
    
        The 'end' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['end']

    @end.setter
    def end(self, val):
        self['end'] = val

    # size
    # ----
    @property
    def size(self):
        """
        Sets the step in-between value each x axis bin.
    
        The 'size' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['size']

    @size.setter
    def size(self, val):
        self['size'] = val

    # start
    # -----
    @property
    def start(self):
        """
        Sets the starting value for the x axis bins.
    
        The 'start' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['start']

    @start.setter
    def start(self, val):
        self['start'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'histogram2dcontour'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        end
            Sets the end value for the x axis bins.
        size
            Sets the step in-between value each x axis bin.
        start
            Sets the starting value for the x axis bins.
        """

    def __init__(self, arg=None, end=None, size=None, start=None, **kwargs):
        """
        Construct a new XBins object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.histogram2dcontour.XBins
        end
            Sets the end value for the x axis bins.
        size
            Sets the step in-between value each x axis bin.
        start
            Sets the starting value for the x axis bins.

        Returns
        -------
        XBins
        """
        super(XBins, self).__init__('xbins')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif not isinstance(arg, dict):
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.histogram2dcontour.XBins 
constructor must be a dict or 
an instance of plotly.graph_objs.histogram2dcontour.XBins"""
            )

        # Import validators
        # -----------------
        from plotly.validators.histogram2dcontour import (xbins as v_xbins)

        # Initialize validators
        # ---------------------
        self._validators['end'] = v_xbins.EndValidator()
        self._validators['size'] = v_xbins.SizeValidator()
        self._validators['start'] = v_xbins.StartValidator()

        # Populate data dict with properties
        # ----------------------------------
        v = arg.pop('end', None)
        self.end = end or v
        v = arg.pop('size', None)
        self.size = size or v
        v = arg.pop('start', None)
        self.start = start or v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))