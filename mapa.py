import folium
tiles='http://www.google.cn/maps/vt?lyrs=s@1...{x}&y={y}&z={z}'
atributos= ''
m= folium.Map(location=[8.09306, -76.7283], zoom_start=5, tiles=tiles, attr=atributos)
m
folium.Marker([8.094805, -76.740871], tooltip='Playa').add_to(m)
folium.Marker([8.093493, -76.715773], tooltip='Alcaldia').add_to(m)
folium.Marker([8.091604, -76.731516], tooltip='Plaza de mercado').add_to(m)
folium.Marker([8.081818, -76.722781], tooltip='Puerto').add_to(m)
m