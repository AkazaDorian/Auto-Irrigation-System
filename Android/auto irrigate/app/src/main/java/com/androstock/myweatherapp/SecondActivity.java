package com.androstock.myweatherapp;


import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.os.Handler;
import android.widget.TextView;
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;


public class SecondActivity extends AppCompatActivity {


    private Handler handler=null;

    TextView sensorTemp;
    EditText editTextAddress, editTextPort;
    Button buttonConnect, irrgateButton;
    String address;
    String sensorText, humiText;
    int count  = 0;
    int modeCount = 1;





    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);

        editTextAddress =  findViewById(R.id.address);
        editTextPort =  findViewById(R.id.host);
        buttonConnect =  findViewById(R.id.connectButt);
        sensorTemp = findViewById(R.id.SensorTemp);
        irrgateButton = findViewById(R.id.irrigateButt);
        handler=new Handler();

    }




    public void onClickButton2(View v) {
        Intent myIntent = new Intent(SecondActivity.this, MainActivity.class);
       startActivity(myIntent);
    }
    public void onClickButton3(View v) {
        startActivity(new Intent(SecondActivity.this, thirdActivity.class));
    }

    public void onIrriButton(View v){

        new Thread() {

            @Override
            public void run() {
                try {
                    // start sending data as long as click CONNECT button
                    sendIrri(editTextAddress.getText().toString(), Integer.parseInt(editTextPort.getText().toString()));

                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }.start();
        if(count == 1 || count%2 != 0){

            Toast.makeText(getApplicationContext(), "Irrigation Stopped", Toast.LENGTH_SHORT).show();
        }else {

            Toast.makeText(getApplicationContext(),"Irrigation Start", Toast.LENGTH_SHORT).show();
        }
    }
    private void sendIrri(String ipAddress, int portNum)  throws IOException {
        count+=1;
        if (count == 1 || count%2 != 0 ){
        InetAddress host = InetAddress.getByName( ipAddress ) ;



        DatagramSocket socket = new DatagramSocket();
        String IrriMessage;
        IrriMessage = "r";

        byte[] IrriData = IrriMessage.getBytes();
        DatagramPacket IrriPacket = new DatagramPacket(IrriData, IrriData.length, host, portNum);
        socket.send(IrriPacket);
        socket.close();

        }
        else{
            InetAddress host = InetAddress.getByName( ipAddress ) ;

            DatagramSocket socket = new DatagramSocket();
            String IrriMessage;
            IrriMessage = "s";

            byte[] IrriData = IrriMessage.getBytes();
            DatagramPacket IrriPacket = new DatagramPacket(IrriData, IrriData.length, host, portNum);
            socket.send(IrriPacket);
            socket.close();

        }
    }



    public void onModeButt(View v) throws IOException {
        new Thread() {

            @Override
            public void run() {
                try {
                    // start sending data as long as click CONNECT button
                    sendMode(editTextAddress.getText().toString(), Integer.parseInt(editTextPort.getText().toString()));


                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }.start();

        if(modeCount == 1 || modeCount %2 != 0){

            Toast.makeText(getApplicationContext(), "Auto Mode on", Toast.LENGTH_SHORT).show();
        }else {

            Toast.makeText(getApplicationContext(),"Auto Mode off", Toast.LENGTH_SHORT).show();
        }
    }



    private void sendMode(String ipAddress, int portNum)  throws IOException {

        modeCount+=1;
        if (modeCount%2 == 1 ) {
            InetAddress host = InetAddress.getByName(ipAddress);

            DatagramSocket socket = new DatagramSocket();
            String ModeMessage;
            ModeMessage = "u";

            byte[] ModeData = ModeMessage.getBytes();
            DatagramPacket ModePacket = new DatagramPacket(ModeData, ModeData.length, host, portNum);
            socket.send(ModePacket);
            socket.close();
        }else{
            InetAddress host = InetAddress.getByName(ipAddress);

            DatagramSocket socket = new DatagramSocket();
            String ModeMessage;
            ModeMessage = "a";

            byte[] ModeData = ModeMessage.getBytes();
            DatagramPacket ModePacket = new DatagramPacket(ModeData, ModeData.length, host, portNum);
            socket.send(ModePacket);
            socket.close();

        }

    }

    public void onConnectButton(View v) {

        new Thread() {
            @Override
            public void run() {
                try {
                    // start sending data as long as click CONNECT button
                    sendData1(editTextAddress.getText().toString(), Integer.parseInt(editTextPort.getText().toString()));
                    sensorText = getData();
                    handler.post(runnableUi);

                    sendData2(editTextAddress.getText().toString(), Integer.parseInt(editTextPort.getText().toString()));
                    humiText = getData();
                    handler.post(runnableUi);

                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }.start();
    }
    Runnable   runnableUi=new  Runnable() {
        @Override
        public void run() {
            sensorTemp.setText("temp is : "+ sensorText + "°C \nHumi is : " + humiText +" %");
        }
    };

    private void sendData1(String ipAddress, int portNum)  throws IOException {
            // define the variables
            InetAddress host = InetAddress.getByName( ipAddress ) ;

             // call the send and request functions using IP address and port number
            sendTempReq(host , portNum);

    }
    private void sendData2(String ipAddress, int portNum)  throws IOException {

        InetAddress host = InetAddress.getByName( ipAddress ) ;
        sendHumiReq(host, portNum);


    }
    private void sendTempReq(InetAddress ipAddress, int portNum) throws IOException {
        DatagramSocket socket = new DatagramSocket();

        String TempMessage;
        TempMessage = "t";

        byte[] TempData = TempMessage.getBytes();
        DatagramPacket TempPacket = new DatagramPacket(TempData, TempData.length, ipAddress, portNum);
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


    private void sendHumiReq(InetAddress ipAddress, int portNum) throws IOException {
        DatagramSocket HumiSocket = new DatagramSocket();

        String HumiMessage;
        HumiMessage = "h";

        byte[] Hdata = HumiMessage.getBytes();
        DatagramPacket HumiPacket = new DatagramPacket(Hdata, Hdata.length, ipAddress, portNum);
        HumiSocket.send(HumiPacket);

        HumiSocket.close() ;

    }

}




