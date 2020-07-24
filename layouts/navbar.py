import dash_bootstrap_components as dbc


navbar = dbc.NavbarSimple(
   children=[
      dbc.NavItem(dbc.NavLink("Home", href="/dash/")),
      dbc.DropdownMenu(
         nav=True,
         in_navbar=True,
         label="Menu",
         children=[
            dbc.DropdownMenuItem("Historical data", header=True),
            dbc.DropdownMenuItem("Temperature", href="/dash/hist/temp"),
            dbc.DropdownMenuItem("Pressure", href="/dash/hist/pres"),
            dbc.DropdownMenuItem("Humidity", href="/dash/hist/humi"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Help",  href="/dash/help"),
                  ],
              ),
            ],
   brand="WeatherApp",
   brand_href="/dash/",
   sticky="top",
   color="dark",
   dark=True,
)
