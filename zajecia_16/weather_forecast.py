from weather_forecast_file_handler import FileHandler


file_handler = FileHandler("weather_data.json")

szczecin_info = file_handler["Szczecin", "2025-06-18"]
print(szczecin_info)
file_handler["Poznań", "2025-06-18"] = "Pada"

file_handler.write_to_file()

my_generator = file_handler.items()

for weather in my_generator:
    print(weather)


for city, weather_info in file_handler:
    print(f"{city} - {weather_info}")