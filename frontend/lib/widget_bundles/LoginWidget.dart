import 'package:flutter/material.dart';
import 'package:frontend/pages/HomePage.dart';
import 'package:frontend/widgets/FancyButton.dart';
import 'package:frontend/widgets/FancyHeader.dart';
import 'package:frontend/widgets/FancyTextField.dart';

class LoginWidget extends StatefulWidget {
  final VoidCallback onSwitchToRegister;

  const LoginWidget({super.key, required this.onSwitchToRegister});

  @override
  State<LoginWidget> createState() => _LoginWidgetState();
}

class _LoginWidgetState extends State<LoginWidget> {
  final emailController = TextEditingController();
  final passwordController = TextEditingController();
  final usernameController = TextEditingController();
  bool confirm = false;
  bool _isLoading = false;


<<<<<<< HEAD
    try {
      final response = await http.post(
        url,
        headers: {
          'Content-Type': 'application/json',
          'Authorization': "Api-Key ho4f2fm2.WYyNAfuaYikL9QvUycDIz41FD1G18zEc",
        },
        body: jsonEncode({'email': email, 'username': username, 'password': password}),
      );

      if (response.statusCode == 200 || response.statusCode == 201) {
        // Success! You might want to save a token here
        
        return true;
      } else {
        print("Error is ${response.body}");
        return false;
      }
    } catch (e) {
      print("Error occured ${e}");
      return false;
    }
  }
=======
>>>>>>> 22cc8ba (Refind the UI)

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
                color: const Color.fromARGB(99, 188, 188, 188),
                blurRadius: .2,
                offset: Offset(1, 1),
                spreadRadius: 1.0,
              ),
            ],
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              SizedBox(height: MediaQuery.of(context).size.height * 0.06),
              FancyHeader(userText: 'Login', textSize: 60),
              SizedBox(height: MediaQuery.of(context).size.height * 0.03),
              Container(
                padding: EdgeInsets.all(8),
                width: MediaQuery.of(context).size.width * responsiveWidth,
                height: MediaQuery.of(context).size.height * 0.06,
                child: FancyTextField(
                  hint: 'Enter username',
                  label: 'Username',
                  controller: usernameController,
                ),
              ),

              Container(
                padding: EdgeInsets.all(8),
                width: MediaQuery.of(context).size.width * responsiveWidth,
                height:
                    MediaQuery.of(context).size.height *
                    0.06, // gets the size of the web browse
                child: FancyTextField(
                  hint: 'Enter email',
                  label: 'Email',
                  controller: emailController,
                  obscureText: false,
                ),
              ),

              Container(
                padding: EdgeInsets.all(8),
                width: MediaQuery.of(context).size.width * responsiveWidth,
                height:
                    MediaQuery.of(context).size.height *
                    0.06, // gets the size of the web browse
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
                          widget.onSwitchToRegister();
                        });
                      },
                    ),
                  ],
                ),
              ),

              SizedBox(height: MediaQuery.of(context).size.height * 0.01),
              _isLoading
                  ? CircularProgressIndicator()
                  : FancyButton(
                      function: () async {
                        setState(() => _isLoading = true);

                        print("HELLO");

                        if (confirm) {
                          Navigator.pushReplacement(
                            context,
                            MaterialPageRoute(builder: (_) => HomePage(username: 'placeholder',cesPoints:  1)),
                          );
                        }
                      },
                      text: 'Login',
                      buttonColor: Colors.green,
                    ),
            ],
          ),
        ),
      ),
    );
  }
}
