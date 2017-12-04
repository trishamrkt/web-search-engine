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
            forecast_obj['high'] = self.__f_to_c(self.__str_to_long(forecast.high()));
            forecast_obj['low'] = self.__f_to_c(self.__str_to_long(forecast.low()));
            forecast_array.append(forecast_obj);
            
        return forecast_array;
    
    def __str_to_long(self, str):
        return long(float(str));
    
    def __f_to_c(self, temp):
        return ((temp - 32) * 5/9);
        
if __name__ == "__main__":
    print 'HI THERE'
    weatherWidgetService = WeatherWidgetService();
    print weatherWidgetService.get_forecast_by_region('toronto');