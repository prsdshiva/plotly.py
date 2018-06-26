from plotly.basedatatypes import BaseLayoutHierarchyType


class Rangeselector(BaseLayoutHierarchyType):

    # activecolor
    # -----------
    @property
    def activecolor(self):
        """
        Sets the background color of the active range selector button.
    
        The 'activecolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen

        Returns
        -------
        str
        """
        return self['activecolor']

    @activecolor.setter
    def activecolor(self, val):
        self['activecolor'] = val

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Sets the background color of the range selector buttons.
    
        The 'bgcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen

        Returns
        -------
        str
        """
        return self['bgcolor']

    @bgcolor.setter
    def bgcolor(self, val):
        self['bgcolor'] = val

    # bordercolor
    # -----------
    @property
    def bordercolor(self):
        """
        Sets the color of the border enclosing the range selector.
    
        The 'bordercolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen

        Returns
        -------
        str
        """
        return self['bordercolor']

    @bordercolor.setter
    def bordercolor(self, val):
        self['bordercolor'] = val

    # borderwidth
    # -----------
    @property
    def borderwidth(self):
        """
        Sets the width (in px) of the border enclosing the range
        selector.
    
        The 'borderwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['borderwidth']

    @borderwidth.setter
    def borderwidth(self, val):
        self['borderwidth'] = val

    # buttons
    # -------
    @property
    def buttons(self):
        """
        Sets the specifications for each buttons. By default, a range
        selector comes with no buttons.
    
        The 'buttons' property is a tuple of instances of
        Button that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.xaxis.rangeselector.Button
          - A list or tuple of dicts of string/value properties that
            will be passed to the Button constructor
    
            Supported dict properties:
                
                count
                    Sets the number of steps to take to update the
                    range. Use with `step` to specify the update
                    interval.
                label
                    Sets the text label to appear on the button.
                step
                    The unit of measurement that the `count` value
                    will set the range by.
                stepmode
                    Sets the range update mode. If *backward*, the
                    range update shifts the start of range back
                    *count* times *step* milliseconds. If *todate*,
                    the range update shifts the start of range back
                    to the first timestamp from *count* times
                    *step* milliseconds back. For example, with
                    `step` set to *year* and `count` set to *1* the
                    range update shifts the start of the range back
                    to January 01 of the current year. Month and
                    year *todate* are currently available only for
                    the built-in (Gregorian) calendar.

        Returns
        -------
        tuple[plotly.graph_objs.layout.xaxis.rangeselector.Button]
        """
        return self['buttons']

    @buttons.setter
    def buttons(self, val):
        self['buttons'] = val

    # font
    # ----
    @property
    def font(self):
        """
        Sets the font of the range selector button text.
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.layout.xaxis.rangeselector.Font
          - A dict of string/value properties that will be passed
            to the Font constructor
    
            Supported dict properties:
                
                color
    
                family
                    HTML font family - the typeface that will be
                    applied by the web browser. The web browser
                    will only be able to apply a font if it is
                    available on the system which it operates.
                    Provide multiple font families, separated by
                    commas, to indicate the preference in which to
                    apply fonts if they aren't available on the
                    system. The plotly service (at https://plot.ly
                    or on-premise) generates images on a server,
                    where only a select number of fonts are
                    installed and supported. These include *Arial*,
                    *Balto*, *Courier New*, *Droid Sans*,, *Droid
                    Serif*, *Droid Sans Mono*, *Gravitas One*, *Old
                    Standard TT*, *Open Sans*, *Overpass*, *PT Sans
                    Narrow*, *Raleway*, *Times New Roman*.
                size

        Returns
        -------
        plotly.graph_objs.layout.xaxis.rangeselector.Font
        """
        return self['font']

    @font.setter
    def font(self, val):
        self['font'] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not this range selector is visible. Note
        that range selectors are only available for x axes of `type`
        set to or auto-typed to *date*.
    
        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['visible']

    @visible.setter
    def visible(self, val):
        self['visible'] = val

    # x
    # -
    @property
    def x(self):
        """
        Sets the x position (in normalized coordinates) of the range
        selector.
    
        The 'x' property is a number and may be specified as:
          - An int or float in the interval [-2, 3]

        Returns
        -------
        int|float
        """
        return self['x']

    @x.setter
    def x(self, val):
        self['x'] = val

    # xanchor
    # -------
    @property
    def xanchor(self):
        """
        Sets the range selector's horizontal position anchor. This
        anchor binds the `x` position to the *left*, *center* or
        *right* of the range selector.
    
        The 'xanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'left', 'center', 'right']

        Returns
        -------
        Any
        """
        return self['xanchor']

    @xanchor.setter
    def xanchor(self, val):
        self['xanchor'] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the y position (in normalized coordinates) of the range
        selector.
    
        The 'y' property is a number and may be specified as:
          - An int or float in the interval [-2, 3]

        Returns
        -------
        int|float
        """
        return self['y']

    @y.setter
    def y(self, val):
        self['y'] = val

    # yanchor
    # -------
    @property
    def yanchor(self):
        """
        Sets the range selector's vertical position anchor This anchor
        binds the `y` position to the *top*, *middle* or *bottom* of
        the range selector.
    
        The 'yanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'top', 'middle', 'bottom']

        Returns
        -------
        Any
        """
        return self['yanchor']

    @yanchor.setter
    def yanchor(self, val):
        self['yanchor'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout.xaxis'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        activecolor
            Sets the background color of the active range selector
            button.
        bgcolor
            Sets the background color of the range selector
            buttons.
        bordercolor
            Sets the color of the border enclosing the range
            selector.
        borderwidth
            Sets the width (in px) of the border enclosing the
            range selector.
        buttons
            Sets the specifications for each buttons. By default, a
            range selector comes with no buttons.
        font
            Sets the font of the range selector button text.
        visible
            Determines whether or not this range selector is
            visible. Note that range selectors are only available
            for x axes of `type` set to or auto-typed to *date*.
        x
            Sets the x position (in normalized coordinates) of the
            range selector.
        xanchor
            Sets the range selector's horizontal position anchor.
            This anchor binds the `x` position to the *left*,
            *center* or *right* of the range selector.
        y
            Sets the y position (in normalized coordinates) of the
            range selector.
        yanchor
            Sets the range selector's vertical position anchor This
            anchor binds the `y` position to the *top*, *middle* or
            *bottom* of the range selector.
        """

    def __init__(
        self,
        arg=None,
        activecolor=None,
        bgcolor=None,
        bordercolor=None,
        borderwidth=None,
        buttons=None,
        font=None,
        visible=None,
        x=None,
        xanchor=None,
        y=None,
        yanchor=None,
        **kwargs
    ):
        """
        Construct a new Rangeselector object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.layout.xaxis.Rangeselector
        activecolor
            Sets the background color of the active range selector
            button.
        bgcolor
            Sets the background color of the range selector
            buttons.
        bordercolor
            Sets the color of the border enclosing the range
            selector.
        borderwidth
            Sets the width (in px) of the border enclosing the
            range selector.
        buttons
            Sets the specifications for each buttons. By default, a
            range selector comes with no buttons.
        font
            Sets the font of the range selector button text.
        visible
            Determines whether or not this range selector is
            visible. Note that range selectors are only available
            for x axes of `type` set to or auto-typed to *date*.
        x
            Sets the x position (in normalized coordinates) of the
            range selector.
        xanchor
            Sets the range selector's horizontal position anchor.
            This anchor binds the `x` position to the *left*,
            *center* or *right* of the range selector.
        y
            Sets the y position (in normalized coordinates) of the
            range selector.
        yanchor
            Sets the range selector's vertical position anchor This
            anchor binds the `y` position to the *top*, *middle* or
            *bottom* of the range selector.

        Returns
        -------
        Rangeselector
        """
        super(Rangeselector, self).__init__('rangeselector')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif not isinstance(arg, dict):
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.xaxis.Rangeselector 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.xaxis.Rangeselector"""
            )

        # Import validators
        # -----------------
        from plotly.validators.layout.xaxis import (
            rangeselector as v_rangeselector
        )

        # Initialize validators
        # ---------------------
        self._validators['activecolor'
                        ] = v_rangeselector.ActivecolorValidator()
        self._validators['bgcolor'] = v_rangeselector.BgcolorValidator()
        self._validators['bordercolor'
                        ] = v_rangeselector.BordercolorValidator()
        self._validators['borderwidth'
                        ] = v_rangeselector.BorderwidthValidator()
        self._validators['buttons'] = v_rangeselector.ButtonsValidator()
        self._validators['font'] = v_rangeselector.FontValidator()
        self._validators['visible'] = v_rangeselector.VisibleValidator()
        self._validators['x'] = v_rangeselector.XValidator()
        self._validators['xanchor'] = v_rangeselector.XanchorValidator()
        self._validators['y'] = v_rangeselector.YValidator()
        self._validators['yanchor'] = v_rangeselector.YanchorValidator()

        # Populate data dict with properties
        # ----------------------------------
        v = arg.pop('activecolor', None)
        self.activecolor = activecolor or v
        v = arg.pop('bgcolor', None)
        self.bgcolor = bgcolor or v
        v = arg.pop('bordercolor', None)
        self.bordercolor = bordercolor or v
        v = arg.pop('borderwidth', None)
        self.borderwidth = borderwidth or v
        v = arg.pop('buttons', None)
        self.buttons = buttons or v
        v = arg.pop('font', None)
        self.font = font or v
        v = arg.pop('visible', None)
        self.visible = visible or v
        v = arg.pop('x', None)
        self.x = x or v
        v = arg.pop('xanchor', None)
        self.xanchor = xanchor or v
        v = arg.pop('y', None)
        self.y = y or v
        v = arg.pop('yanchor', None)
        self.yanchor = yanchor or v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))