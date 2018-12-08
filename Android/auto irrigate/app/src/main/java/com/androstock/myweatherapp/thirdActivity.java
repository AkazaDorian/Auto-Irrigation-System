package com.androstock.myweatherapp;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Toast;

import com.squareup.picasso.Picasso;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;



public class thirdActivity extends AppCompatActivity{



    private ImageView imageView;
    EditText editTextAddress, editTextPort;
    String url;


    @Override
    protected void onCreate(Bundle savedInstanceState)
    {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_third);

        imageView= findViewById(R.id.imageView);//text = (TextView) findViewById(R.id.textView01);
        editTextAddress =  findViewById(R.id.photoAdd);
        editTextPort =  findViewById(R.id.photoPort);
    }

    public void onButtonClick(View v){
        Intent myIntent = new Intent(getBaseContext(),  SecondActivity.class);
        startActivity(myIntent);
    }

    public void onViewButton (View v) throws IOException {
        new Thread() {

            @Override
            public void run() {
                try {
                    // start sending data as long as click CONNECT button
                    sendData3( editTextAddress.getText().toString(), Integer.parseInt(editTextPort.getText().toString()));
                        url = getData();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }.start();
        while(url == null);

        Picasso.get().load(url).into(imageView);
        Toast.makeText(getApplicationContext(),"Image received", Toast.LENGTH_SHORT).show();
        url = null;
    }


    private void sendData3(String ipAddress, int portNum)  throws IOException {

        sendImageReq(ipAddress , portNum);

    }

        private void sendImageReq(String ipAddress, int portNum) throws IOException {

        InetAddress host = InetAddress.getByName( ipAddress ) ;
        DatagramSocket socket = new DatagramSocket();

        String TempMessage;
        TempMessage = "i";

        byte[] TempData = TempMessage.getBytes();
        DatagramPacket TempPacket = new DatagramPacket(TempData, TempData.length, host, portNum);
        socket.send(TempPacket);
        socket.close();
    }

    public   String getData() throws IOException {
        int server_port = 10000;
        String sensorText;
        DatagramSocket socket = new DatagramSocket(server_port);

        while (true){
            byte[] backData = new byte[1500];
            DatagramPacket BackPacket = new DatagramPacket(backData, backData.length);

            try{
                socket.receive(BackPacket);
                sensorText = new String (BackPacket.getData()).trim();
                socket.close();
                return sensorText;
            }catch (IOException e){
                e.printStackTrace();
            }
        }
    }



}
