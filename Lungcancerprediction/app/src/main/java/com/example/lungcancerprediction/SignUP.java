package com.example.lungcancerprediction;

import androidx.appcompat.app.AppCompatActivity;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class SignUP extends AppCompatActivity {

    EditText e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11;
    Button b1;
    SharedPreferences sh;
    String fname;
    String lname;
    String gender;
    String place;
    String post;
    String pin;
    String email;
    String phone;
    String username;
    String password;
    String cpassword;

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sign_up);

        e1=findViewById(R.id.editTextTextPersonName2);
        e2=findViewById(R.id.editTextTextPersonName3);
        e3=findViewById(R.id.editTextTextPersonName4);
        e4=findViewById(R.id.editTextTextPersonName7);
        e5=findViewById(R.id.editTextTextPersonName8);
        e6=findViewById(R.id.editTextTextPersonName9);
        e7=findViewById(R.id.editTextTextPersonName10);
        e8=findViewById(R.id.editTextTextPersonName11);
        e9=findViewById(R.id.editTextTextPersonName12);
        e10=findViewById(R.id.editTextTextPersonName13);
        e11=findViewById(R.id.editTextTextPersonName14);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                fname=e1.getText().toString();
                lname=e2.getText().toString();
                gender=e3.getText().toString();
                place=e4.getText().toString();
                post=e5.getText().toString();
                pin=e6.getText().toString();
                email=e7.getText().toString();
                phone=e8.getText().toString();
                username=e9.getText().toString();
                password=e10.getText().toString();
                cpassword=e11.getText().toString();
            }
        });


    }
}