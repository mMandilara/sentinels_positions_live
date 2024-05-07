from flask import Flask, render_template
import json
import plotly.graph_objects as go

app = Flask(__name__)

# Function to read satellite data from JSON files
def read_satellite_data_from_json(identifiers):
    satellite_data = []
    for identifier in identifiers:
        filename = f"satellite_data_{identifier}.json"
        with open(filename, 'r') as file:
            data = json.load(file)
            longitude, latitude = data
            satellite_data.append((longitude, latitude, identifier))
    return satellite_data

@app.route('/')
def index():
    sats = ['S2A', 'S2B']
    colors = ['blue', 'red']

    # Create figure
    fig = go.Figure()

    # Update satellite positions
    def update_satellite_positions():
        updated_satellite_data = read_satellite_data_from_json(sats)
        updated_longitudes, updated_latitudes, _ = zip(*updated_satellite_data)
        for idx, (longitude, latitude) in enumerate(zip(updated_longitudes, updated_latitudes)):
            if idx < len(fig.data):
                fig.data[idx].update(lon=[longitude], lat=[latitude])
            else:
                fig.add_trace(go.Scattergeo(lon=[longitude], lat=[latitude], mode='markers',
                                             marker=dict(size=10, color=colors[idx]),
                                             hovertext=f"<br>Longitude: {longitude}<br>Latitude: {latitude}",
                                             name=sats[idx]))

        # Add long and lat lines
        for lon in range(-180, 180, 10):
            fig.add_trace(go.Scattergeo(lon=[lon]*181, lat=list(range(-90, 91)), mode='lines', line=dict(color='rgba(0,0,0,0.2)', width=1), showlegend=False))
        for lat in range(-90, 91, 10):
            fig.add_trace(go.Scattergeo(lon=list(range(-180, 181)), lat=[lat]*361, mode='lines', line=dict(color='rgba(0,0,0,0.2)', width=1), showlegend=False))

    # Add country borders
    fig.update_geos(
        showcountries=True, countrycolor="Black"
    )
    # Update layout
    fig.update_geos(projection_type="natural earth", showcoastlines=True)
    fig.update_layout(showlegend=True, width=1400, height=600)
    # Update satellite positions
    update_satellite_positions()
    # Plotly figure to HTML
    plot_html = fig.to_html(include_plotlyjs='cdn', full_html=False)

    return render_template('index.html', plot=plot_html, refresh_interval=10000)


if __name__ == '__main__':
    app.run(debug=True)
