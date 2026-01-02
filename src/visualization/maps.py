# Map Visualization Utilities
import folium

def create_country_map(data, lat_col, lon_col, value_col):
    """Create a map visualization for countries."""
    m = folium.Map()
    for _, row in data.iterrows():
        folium.CircleMarker(
            location=[row[lat_col], row[lon_col]],
            radius=5,
            popup=f"{value_col}: {row[value_col]}",
            color='blue'
        ).add_to(m)
    return m