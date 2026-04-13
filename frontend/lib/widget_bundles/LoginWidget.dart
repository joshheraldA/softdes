import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:frontend/firebase/FbAuth.dart';
import 'package:frontend/pages/HomePage.dart';
import 'package:frontend/widgets/FancyButton.dart';
import 'package:frontend/widgets/FancyHeader.dart';
import 'package:frontend/widgets/FancyTextField.dart';
import 'package:http/http.dart' as http;

class RegisterWidget extends StatefulWidget {
  final VoidCallback onSwitchToLogin;

  const RegisterWidget({super.key, required this.onSwitchToLogin});

  @override
  State<RegisterWidget> createState() => _RegisterWidgetState();
}

class _RegisterWidgetState extends State<RegisterWidget> {

  Future<Map<String, dynamic>?> login(String email, String password) async {
    String? user_id = await login_acc(email, password);

    final url = Uri.parse('http://127.0.0.1:8000/api/v2/signed-in/');

    try {
      final response = await http.post(
        url,
        headers: {
          'Content-Type': 'application/json',
          'Authorization': "Api-Key nwwYC7dT.hkq3lSJLTMKnUVPUufOvSNaw8ksBrjQw",
        },
        body: jsonEncode({'id': user_id}),
      );

      if (response.statusCode == 200 || response.statusCode == 201) {
        final data = jsonDecode(response.body);
        return data;
      } else {
        print("Error is ${response.body}");
        return null;
      }
    } catch (e) {
      print("Error occured ${e}");
      return null;
    }
  }
  final emailController = TextEditingController();
  final passwordController = TextEditingController();
  @override
  Widget build(BuildContext context) {
    final double responsiveWidth = 0.25;

    return Center(
      child: SizedBox(
        width: MediaQuery.of(context).size.width * 0.5,
        height: MediaQuery.of(context).size.height * 0.6,
        child: Container(
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(20),
            color: const Color.fromARGB(255, 255, 255, 255),
            boxShadow: [
              BoxShadow(
                color: const Color.fromARGB(96, 62, 62, 62),
                blurRadius: .2,
                offset: Offset(0, 2),
                spreadRadius: 1.0,
              ),
            ],
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              SizedBox(height: MediaQuery.of(context).size.height * 0.07),
              FancyHeader(userText: 'Sign in', textSize: 60),
              SizedBox(height: MediaQuery.of(context).size.height * 0.05),
              Container(
                padding: EdgeInsets.all(8),
                width: MediaQuery.of(context).size.width * responsiveWidth,
                height: MediaQuery.of(context).size.height * 0.06,
                child: FancyTextField(
                  hint: 'Enter email',
                  label: 'Email',
                  controller: emailController,
                ),
              ),
              Container(
                padding: EdgeInsets.all(8),
                width: MediaQuery.of(context).size.width * responsiveWidth,
                height: MediaQuery.of(context).size.height * 0.06,
                child: FancyTextField(
                  hint: 'Enter Password',
                  label: 'Password',
                  controller: passwordController,
                  obscureText: true,
                ),
              ),

              Container(
                width: MediaQuery.of(context).size.width * (responsiveWidth - 0.02),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      'Forgot your password?',
                      style: TextStyle(
                        color: const Color.fromARGB(255, 147, 147, 147),
                      ),
                    ),
                    TextButton(
                      child: Text(
                        'Create an account',
                        style: TextStyle(
                          color: const Color.fromARGB(255, 147, 147, 147),
                        ),
                      ),
                      onPressed: () {
                        setState(() {
                          widget.onSwitchToLogin();
                        });
                      },
                    ),
                  ],
                ),
              ),
              FancyButton(
                function: () async {
                  Map<String,dynamic>? login_acc = await login(
                    emailController.text,
                    passwordController.text,
                  );
                  emailController.clear();
                  passwordController.clear();
                  final userData = login_acc?['data'];
                  if (login_acc!=null) {
                    print(login_acc);
                    Navigator.pushReplacement(
                      context,
                      MaterialPageRoute(builder: (_) => HomePage(username: userData['username'], cesPoints:userData['cesPoints'] ,)),
                    );
                  }
                },
                text: 'Sign in',
                buttonColor: Colors.green,
              ),
            ],
          ),
        ),
      ),
    );
  }
}