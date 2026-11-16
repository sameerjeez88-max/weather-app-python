import requests

def get_weather(city):
    try:
        # wttr.in ek free service hai, isme API key ki zaroorat nahi
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Data nikalna
            current = data['current_condition'][0]
            temp = current['temp_C']
            description = current['weatherDesc'][0]['value']
            humidity = current['humidity']
            wind_speed = current['windspeedKmph']
            
            print(f"\n📍 Weather in {city.title()}:")
            print(f"🌡️ Temperature: {temp}°C")
            print(f"☁️ Condition: {description}")
            print(f"💧 Humidity: {humidity}%")
            print(f"💨 Wind Speed: {wind_speed} km/h\n")
        else:
            print(f"\n❌ Error: Could not fetch weather for '{city}'. Please check the spelling.\n")

    except Exception as e:
        print(f"\n❌ An error occurred: {e}\n")

def main():
    print("🌤️ Welcome to the Python Weather App!")
    print("Type 'exit' to quit.\n")
    
    while True:
        city = input("Enter city name: ").strip()
        
        if city.lower() == 'exit':
            print("Goodbye! 👋")
            break
            
        if city:
            get_weather(city)

if __name__ == "__main__":
    main()