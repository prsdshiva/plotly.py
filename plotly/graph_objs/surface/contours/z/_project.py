from plotly.basedatatypes import BaseTraceHierarchyType


class Project(BaseTraceHierarchyType):

    # x
    # -
    @property
    def x(self):
        """
        Determines whether or not these contour lines are projected on
        the x plane. If `highlight` is set to *true* (the default), the
        projected lines are shown on hover. If `show` is set to *true*,
        the projected lines are shown in permanence.
    
        The 'x' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
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
        Determines whether or not these contour lines are projected on
        the y plane. If `highlight` is set to *true* (the default), the
        projected lines are shown on hover. If `show` is set to *true*,
        the projected lines are shown in permanence.
    
        The 'y' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['y']

    @y.setter
    def y(self, val):
        self['y'] = val

    # z
    # -
    @property
    def z(self):
        """
        Determines whether or not these contour lines are projected on
        the z plane. If `highlight` is set to *true* (the default), the
        projected lines are shown on hover. If `show` is set to *true*,
        the projected lines are shown in permanence.
    
        The 'z' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['z']

    @z.setter
    def z(self, val):
        self['z'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'surface.contours.z'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        x
            Determines whether or not these contour lines are
            projected on the x plane. If `highlight` is set to
            *true* (the default), the projected lines are shown on
            hover. If `show` is set to *true*, the projected lines
            are shown in permanence.
        y
            Determines whether or not these contour lines are
            projected on the y plane. If `highlight` is set to
            *true* (the default), the projected lines are shown on
            hover. If `show` is set to *true*, the projected lines
            are shown in permanence.
        z
            Determines whether or not these contour lines are
            projected on the z plane. If `highlight` is set to
            *true* (the default), the projected lines are shown on
            hover. If `show` is set to *true*, the projected lines
            are shown in permanence.
        """

    def __init__(self, arg=None, x=None, y=None, z=None, **kwargs):
        """
        Construct a new Project object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.surface.contours.z.Project
        x
            Determines whether or not these contour lines are
            projected on the x plane. If `highlight` is set to
            *true* (the default), the projected lines are shown on
            hover. If `show` is set to *true*, the projected lines
            are shown in permanence.
        y
            Determines whether or not these contour lines are
            projected on the y plane. If `highlight` is set to
            *true* (the default), the projected lines are shown on
            hover. If `show` is set to *true*, the projected lines
            are shown in permanence.
        z
            Determines whether or not these contour lines are
            projected on the z plane. If `highlight` is set to
            *true* (the default), the projected lines are shown on
            hover. If `show` is set to *true*, the projected lines
            are shown in permanence.

        Returns
        -------
        Project
        """
        super(Project, self).__init__('project')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif not isinstance(arg, dict):
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.surface.contours.z.Project 
constructor must be a dict or 
an instance of plotly.graph_objs.surface.contours.z.Project"""
            )

        # Import validators
        # -----------------
        from plotly.validators.surface.contours.z import (project as v_project)

        # Initialize validators
        # ---------------------
        self._validators['x'] = v_project.XValidator()
        self._validators['y'] = v_project.YValidator()
        self._validators['z'] = v_project.ZValidator()

        # Populate data dict with properties
        # ----------------------------------
        v = arg.pop('x', None)
        self.x = x or v
        v = arg.pop('y', None)
        self.y = y or v
        v = arg.pop('z', None)
        self.z = z or v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))