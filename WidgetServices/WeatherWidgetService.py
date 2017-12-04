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
            forecast_obj['img_src'] = self.__determine_img_src(forecast.text());
            forecast_obj['text'] = forecast.text();
            forecast_obj['date'] = forecast.date();
            forecast_obj['high'] = self.__f_to_c(self.__str_to_long(forecast.high()));
            forecast_obj['low'] = self.__f_to_c(self.__str_to_long(forecast.low()));
            forecast_array.append(forecast_obj);
            
        return forecast_array;
    
    def __determine_img_src(self, weather_category):
        img_src = '';
        
        if weather_category == 'Sunny':
            img_src = 'partial_cloudy';
        elif weather_category == 'Partly Cloudy':
            img_src = 'partial_cloudy';
        elif weather_category == 'Mostly Cloudy':
            img_src = 'partial_cloudy';
        elif weather_category == 'Showers':
            img_src = 'showers'
        elif weather_category == 'Breezy':
            img_src = 'cloudy';       
        elif weather_category == 'Light Rain':
            img_src = 'showers';
        else:
            img_src = 'partial_cloudy';
        
        img_src = img_src + '.png'
        return img_src;
    
    def __str_to_long(self, str):
        return long(float(str));
    
    def __f_to_c(self, temp):
        return ((temp - 32) * 5/9);
        
if __name__ == "__main__":
    print 'HI THERE'
    weatherWidgetService = WeatherWidgetService();
    print weatherWidgetService.get_forecast_by_region('toronto');