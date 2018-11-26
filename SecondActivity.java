package com.androstock.myweatherapp;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

import android.os.AsyncTask;
import android.os.Bundle;
import android.app.Activity;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class SecondActivity extends AppCompatActivity {

    TextView sensorTemp,SensorHumidity;
    EditText editTextAddress, editTextPort;
    Button buttonConnect;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);

        editTextAddress =  findViewById(R.id.address);
        editTextPort =  findViewById(R.id.host);
        buttonConnect =  findViewById(R.id.connectButt);
        sensorTemp = findViewById(R.id.SensorTemp);
        SensorHumidity = findViewById(R.id.SensorHumidity);

    }


   public void onClickButton2(View v) {
        Intent myIntent = new Intent(getBaseContext(), MainActivity.class);
       startActivity(myIntent);
    }


    public void onConnetButton(View v) {
        new Thread() {
            @Override
            public void run() {
                try {
                    sendData(editTextAddress.getText().toString(), Integer.parseInt(editTextPort.getText().toString()));
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }.start();
                }
    private void sendData(String ipAddress, int portNum)  throws IOException {
        DatagramSocket socket = null;
        try
        {
            // Convert the arguments first, to ensure that they are valid
            InetAddress host = InetAddress.getByName( ipAddress ) ;
            int port         = portNum ;
            socket = new DatagramSocket() ;
            String Tmessage;
            String Hmessage;
            int PACKETSIZE = 100;


            //sent temp request
            Tmessage = "t";
            byte [] Tdata = Tmessage.getBytes() ;
            DatagramPacket Tpacket = new DatagramPacket( Tdata, Tdata.length, host, port ) ;
            socket.send( Tpacket ) ;

            //wait for temp
            int portIN = 10000 ;
            DatagramSocket TempBacksocket = new DatagramSocket( portIN ) ;
            for( ;; )
            {

            DatagramPacket TempBackpacket = new DatagramPacket( new byte[PACKETSIZE], PACKETSIZE ) ;
            TempBacksocket.receive( TempBackpacket ) ;
            sensorTemp.setText(new String(TempBackpacket.getData()).trim());
            break;

            }


            //sent humi request
            Hmessage = "h";
            byte [] Hdata = Hmessage.getBytes() ;
            DatagramPacket Hpacket = new DatagramPacket(Hdata, Hdata.length, host, port ) ;
            socket.send( Hpacket ) ;

            //wait for humi

        }catch( Exception e )
        {
            System.out.println( e ) ;
        }
        finally
        {
            if( socket != null )
                socket.close() ;
        }
    }




}

    //@Override
   // protected void onPostExecute(Void result) {
     //   textResponse.setText(response);
       // super.onPostExecute(result);



