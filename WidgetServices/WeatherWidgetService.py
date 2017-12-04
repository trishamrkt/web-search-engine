from weather import Weather
 
class WeatherWidgetService():
    
    def __init__(self):
        self.__weather = Weather();
        
    def get_forecast_by_region(self, region):
        """ 
        Forecast object: 
        { text: '', 
          date: '',
          high: '',
          low: ''
        }
        """
        forecast_array = [];
        
        location = self.__weather.lookup_by_location(region);
        forecasts = location.forecast();
        
        for forecast in forecasts:
            forecast_obj = {};
            forecast_obj['text'] = forecast.text();
            forecast_obj['date'] = forecast.date();
            forecast_obj['high'] = forecast.high();
            forecast_obj['low'] = forecast.low();
        
        print forecast_array;
        return forecast_array;
    
if __name__ == "__main__":
    weatherWidgetService = WeatherWidgetService();
    weatherWidgetService.get_forecast_by_region('toronto');