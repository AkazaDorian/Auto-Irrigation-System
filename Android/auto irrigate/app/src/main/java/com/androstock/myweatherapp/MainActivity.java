package com.androstock.myweatherapp;

import android.Manifest;
import android.content.Context;
import android.content.pm.PackageManager;
import android.graphics.Typeface;
import android.location.Location;
import android.location.LocationManager;
import android.os.Bundle;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.text.Html;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    static final int REQUEST_LOCATION = 1;
    LocationManager locationManager;




    TextView cityField, detailsField, currentTemperatureField, humidity_field, pressure_field, weatherIcon, updatedField, mytv;

    Typeface weatherFont, myfont;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getSupportActionBar().hide();
        setContentView(R.layout.activity_main);



        // Getting the location from device and storing it as latitude and longitude to be sent to Openweather
        LocationManager lm = (LocationManager)getSystemService(Context.LOCATION_SERVICE);
        try {
            if (ContextCompat.checkSelfPermission(getApplicationContext(), android.Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED ) {
                ActivityCompat.requestPermissions(this, new String[]{android.Manifest.permission.ACCESS_FINE_LOCATION}, 101);
            }
        } catch (Exception e){
            e.printStackTrace();
        }
        locationManager = (LocationManager)getSystemService(Context.LOCATION_SERVICE);


        Location location = lm.getLastKnownLocation(LocationManager.GPS_PROVIDER);



        double longitude = (location.getLongitude());
        double latitude = (location.getLatitude());
        String longi = String.valueOf(longitude);
        String lati = String.valueOf(latitude);







        // Labelling thr textfields with their proper names
        weatherFont = Typeface.createFromAsset(getApplicationContext().getAssets(), "fonts/weathericons-regular-webfont.ttf");

        cityField = (TextView)findViewById(R.id.city_field);
        updatedField = (TextView)findViewById(R.id.updated_field);
        detailsField = (TextView)findViewById(R.id.details_field);
        currentTemperatureField = (TextView)findViewById(R.id.current_temperature_field);
        humidity_field = (TextView)findViewById(R.id.humidity_field);
        pressure_field = (TextView)findViewById(R.id.pressure_field);
        weatherIcon = (TextView)findViewById(R.id.weather_icon);
        weatherIcon.setTypeface(weatherFont);


        Function.placeIdTask asyncTask =new Function.placeIdTask(new Function.AsyncResponse() {
            public void processFinish(String weather_city, String weather_description, String weather_temperature, String weather_humidity, String weather_pressure, String weather_updatedOn, String weather_iconText, String sun_rise) {

                cityField.setText(weather_city);
                updatedField.setText("\nLast updated: " + weather_updatedOn);
                detailsField.setText(weather_description);
                currentTemperatureField.setText(weather_temperature + "C");
                humidity_field.setText("Humidity: "+weather_humidity);
                pressure_field.setText("Pressure: "+weather_pressure);
                weatherIcon.setText(Html.fromHtml(weather_iconText));

            }
        });

        asyncTask.execute(lati, longi); //  asyncTask.execute("Latitude", "Longitude")



    }




}
