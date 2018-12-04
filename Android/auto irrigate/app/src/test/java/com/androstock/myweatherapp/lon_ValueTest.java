package com.androstock.myweatherapp;
import org.junit.Test;
import java.net.URL;
import static org.junit.Assert.*;

public class lon_ValueTest {
    @Test
    public void lon_isCorrect() throws Exception {
        Function function = new Function();
        String OPEN_WEATHER_MAP_URL =
                "http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&units=metric";

        double right_longitude = -75.69812;
        double right_latitude = 45.41117;
        String right_longi = String.valueOf(right_longitude);
        String right_lati = String.valueOf(right_latitude);
        //JSONObject rightData = Function.getWeatherJSON( right_lati, right_longi);
        URL right_url = new URL(String.format(OPEN_WEATHER_MAP_URL, right_lati, right_longi));



        double longitude = -190.69812;                            //wrong input
        double latitude = 45.41117;
        String longi = String.valueOf(longitude);
        String lati = String.valueOf(latitude);
        ///JSONObject data = function.getWeatherJSON(lati, longi);
        URL url = new URL(String.format(OPEN_WEATHER_MAP_URL, lati, longi));


        assertEquals("The longitude input is not in the range (180, -180)",  right_url,url);
    }
}